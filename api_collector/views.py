from rest_framework import generics, status, views
import requests
from rest_framework.response import Response
import time
from jsonmerge import merge
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def games_list(request):
    if request.method == 'GET':
        url = "https://www.balldontlie.io/api/v1/games?"
        second_url = 'https://api.football-data.org/v2/matches'
        headers = {'X-Auth-Token': '608e9a76518540178d4fdc98e550bacd'}

        if 'page' in request.GET:
            page = request.GET['page']
            url += "page="+page

        if 'per_page' in request.GET:
            per_page = request.GET['per_page']
            url += "&per_page="+per_page
            second_url += "?limit="+per_page

        if 'start_date' in request.GET:
            start_date = request.GET['start_date']
            url += "&start_date="+start_date
            second_url += "&dateFrom="+start_date

        if 'end_date' in request.GET:
            end_date = request.GET['end_date']
            url += "&end_date="+end_date
            second_url += "&dateTo="+end_date

        response = requests.get(url).json()
        second_response = requests.get(second_url, headers=headers).json()

        print(url)
        print(second_url)

        if "error" in second_response:
            second_response = {}

        if len(response['data']) == 0:
            response = {}
        else:
            response = {}

        if "errorCode" in second_response:
            second_response = {}

        return Response(merge(response, second_response))


class GetApiDataView1(generics.GenericAPIView):
    def get(self, request):
        MAX_RETRIES = 5
        if request.method == "GET":
                attempt_num = 0
                while attempt_num < MAX_RETRIES:
                    r = requests.get("https://www.balldontlie.io/api/v1/games/", timeout=10)
                    if r.status_code == 200:
                        data = r.json()
                        return Response(data, status=status.HTTP_200_OK)
                    else:
                        attempt_num += 1
                        time.sleep(5)
                return Response({"error": "Request failed"}, status=r.status_code)
        else:
            return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)

