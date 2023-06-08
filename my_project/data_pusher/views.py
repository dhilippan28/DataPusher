from django.shortcuts import render
from .models import AccountDetails, DestinationDetails
from .serializer import AccountDetailsSerializer, DestinationDetailsSerializer, AccountWithDestinationSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests, json, urllib.parse

def http_client(url, method, header, data):
    if method.lower() == "post" or "put":
        requests.get(url, data=json.dumps(data), headers=header)
    elif method.lower() == "get":
        params = urllib.parse.urlencode(data)
        requests.get(url +"?"+ params, headers=header)
    return True

class AccountListView(generics.ListCreateAPIView):
    queryset=AccountDetails.objects.all()
    serializer_class=AccountDetailsSerializer

class AccountDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=AccountDetails.objects.all()
    serializer_class=AccountDetailsSerializer

class DestinationListView(generics.ListCreateAPIView):
    queryset=DestinationDetails.objects.all()
    serializer_class=DestinationDetailsSerializer

class DestinationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=DestinationDetails.objects.all()
    serializer_class=DestinationDetailsSerializer

class AccountWithDestinationListView(generics.RetrieveAPIView):
    queryset=AccountDetails.objects.all()
    serializer_class=AccountWithDestinationSerializer

class IncomingData(APIView):
    def get(self, request):
         if request.content_type != "application/json":
              return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
         else:
              return Response("Method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def post(self, request):
        try:
            secret_token = request.headers.get("CL-X-Token")
            if secret_token:
                if request.content_type == "application/json":
                    account_data = AccountDetails.objects.filter(app_secret_code = secret_token)
                    if account_data:
                        destination_data=DestinationDetails.objects.filter(account_id=account_data[0])
                    else:
                        return Response("Secret-Token not found", status=status.HTTP_204_NO_CONTENT)
                    if destination_data:
                        data = json.loads(request.body)
                        for d in destination_data:
                            http_client(d.url, d.http_method, d.headers, data)
                        return Response("Data is pushed to respective destination urls Successfully",
                                        status=status.HTTP_200_OK)
                             
                    else:
                        return Response("No destination urls for this Account", status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Un Authenticated", status=status.HTTP_401_UNAUTHORIZED)
                
        except Exception as error:
            return Response(str(error),status=status.HTTP_500_INTERNAL_SERVER_ERROR)


