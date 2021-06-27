from rest_framework import generics, status, views
import requests
from rest_framework.response import Response
import time
from jsonmerge import merge
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def games_list(request):
    # Add the code here
    return Response({"Data": "The Data will be shown here"}, status=status.HTTP_200_OK)


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

