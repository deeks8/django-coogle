from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests
import responses
import json

from .models import *
from Api import ApiCollege,ApiState

class CollegeListV1_0(APIView):
    def post(self, request, format=None):
        '''
        :Author: Deeksha
        :param request: contains the parameter sent by the user
        :param format:
        :return:
        '''

        returnData = ApiCollege.post(self, request.data)
        if returnData == "RECORD_NOT_FOUND":
            return Response("400", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)


class StateListV1_0(APIView):
    def post(self, request, format=None):
        '''
        :Author: Deeksha
        :param request: contains the parameter sent by the user
        :param format:
        :return:
        '''

        returnData = ApiState.stateSearch(self, request.data)
        if returnData == "RECORD_NOT_FOUND":
            return Response("400", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)

class StateDetailV1_0(APIView):
    def post(self, request, format=None):
        '''
        :Author: Deeksha
        :param request: contains the parameter sent by the user
        :param format:
        :return:
        '''

        returnData = ApiState.stateDetail(self, request.data)
        if returnData == "RECORD_NOT_FOUND":
            return Response("400", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)


class StateIdListV1_0(APIView):
    def post(self, request, format=None):
        '''
        :Author: Deeksha
        :param request: contains the parameter sent by the user
        :param format:
        :return:
        '''

        returnData = ApiState.stateId(self, request.data)
        if returnData == "RECORD_NOT_FOUND":
            return Response("400", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)


class CollegeSearchV1_0(APIView):
    def post(self, request, format=None):
        '''
        :Author: Deeksha
        :param request: contains the parameter sent by the user
        :param format:
        :return:
        '''

        returnData = ApiCollege.collegeSearch(self, request.data)
        if returnData == "RECORD_NOT_FOUND":
            return Response("400", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
