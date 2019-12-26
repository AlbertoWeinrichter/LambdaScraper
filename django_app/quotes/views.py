# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from quotes.tasks import topic_discovery


class StartSpider(APIView):
    permission_classes = ()

    @staticmethod
    def get(request):
        topic = request.query_params.get('topic', None)

        topic_discovery.delay(topic)

        return Response({"message": 'Harvesting quotes about "{topic}"'.format(topic=topic)})
