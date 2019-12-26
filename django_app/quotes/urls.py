from django.conf.urls import url
from quotes.views import StartSpider

urlpatterns = [
    url(r'start_spider$', StartSpider.as_view()),
]