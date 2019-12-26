import json
import os

import boto3
from celery import shared_task
from celery.decorators import task
from quotes.models import Quote


@task(name="topic_discovery")
def topic_discovery(topic):
    client = boto3.client('lambda',
                          region_name=os.environ.get('AWS_REGION_NAME'),
                          aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
                          )

    response = client.invoke(
        FunctionName=os.environ.get('DISCOVERY_FUNCTION'),
        InvocationType='RequestResponse',
        Payload=bytes(json.dumps({"topic": topic}), encoding='utf8')
    )

    results = json.loads(response["Payload"]._raw_stream.data)
    for r in results:
        extract_detail.delay(r)


@shared_task
def extract_detail(url):
    client = boto3.client('lambda',
                          region_name=os.environ.get('AWS_REGION_NAME'),
                          aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
                          )

    response = client.invoke(
        FunctionName=os.environ.get('DETAIL_FUNCTION'),
        InvocationType='RequestResponse',
        Payload=bytes(json.dumps({"url": url}), encoding='utf8'),
    )

    results = json.loads(response["Payload"]._raw_stream.data)
    Quote.objects.create(
        content=results["content"],
        author=results["author"]
    )
