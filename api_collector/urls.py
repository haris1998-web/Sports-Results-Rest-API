from django.urls import path
from .views import GetApiDataView1, games_list


urlpatterns = [
    path('get-api-data1', GetApiDataView1.as_view(), name='get-api-data1'),
    path('matches/', games_list)
]
