from ..models import *
from . import ApiState
from django.db.models import Q


def post(self, request, format=None):

    '''
    Inserts a new row in the state model if the given state is not already present

    :return: state :
    '''

    try:
        sendData = []
        college, created = CollegeV1_0.objects.get_or_create(
            StateId = ApiState.post(self,request,format = None),
            College = request['College']

        )
        sendData.append({"CollegeId":college.CollegeId})
        return sendData
    except Exception as e:
        return "RECORD_NOT_FOUND"  #bad request



def collegeSearch(self, request, format=None):
    '''
    retrieve 10 colleges data given a college pattern

    :return:

    '''
    try:
        sendData = []
        queryset = CollegeV1_0.objects.filter(Q(College__icontains=request['College'])&(Q(StateId = request['StateId'])))
        if len(queryset) == 0:
                return "RECORD_NOT_FOUND"  # bad request
        count = 1
        for item in queryset:
                sendData.append({"College":item.College,"CollegeId":item.CollegeId,"State":item.StateId.StateName,"StateId":item.StateId.StateId})
                count = count + 1
                if count > 10:
                    break
        return sendData
    except Exception as e:
        return "RECORD_NOT_FOUND" #bad request