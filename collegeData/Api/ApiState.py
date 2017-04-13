from ..models import *



def post(self, request, format=None):

    '''
    Inserts a new row in the state model if the given state is not already present

    :return: state :
    '''

    try:
        state, created = StateV1_0.objects.get_or_create(
            StateName = request['State']
        )
        return state
    except Exception as e:
        return "RECORD_NOT_FOUND"  #bad request



def stateSearch(self, request, format=None):
    '''
    retrieve 10 state data given a cityname pattern

    :return:

    '''
    try:
        sendData = []
        tempArray = []
        queryset = StateV1_0.objects.filter(StateName__icontains=request['State'])
        if len(queryset) == 0:
                return "RECORD_NOT_FOUND"  # bad request, city not in request
        count = 1
        for item in queryset:
            if item.StateName not in tempArray:
                sendData.append({"State":item.StateName,"StateId":item.StateId})
                tempArray.append(item.StateName)
                count = count + 1
            if count > 10:
                break
        return sendData
    except Exception as e:
        return "RECORD_NOT_FOUND" #bad request, city not in request


def stateDetail(self, request, format=None):
    '''
    retrieve a state data
    :return:

    '''
    try:
        sendData = []
        queryset = StateV1_0.objects.get(StateName=request['State'])
        sendData.append({"State":queryset.StateName,"StateId":queryset.StateId})
        return sendData
    except Exception as e:
        return "RECORD_NOT_FOUND" #bad request)


def stateId(self, request, format=None):
    '''
    retrieve a state data
    :return:

    '''
    try:
        sendData = []
        queryset = StateV1_0.objects.get(StateId=request['State'])
        sendData.append({"State":queryset.StateName,"StateId":queryset.StateId})
        return sendData
    except Exception as e:
        return "RECORD_NOT_FOUND" #bad request)

def allStateList(self, request, format=None):
    '''
    retrieve a state data
    :return:

    '''
    try:
        if request["All"] == "True":
            sendData = []
            queryset = StateV1_0.objects.all()
            for item in queryset:
                sendData.append({"State":item.StateName,"StateId":item.StateId})
            return sendData
    except Exception as e:
        return "RECORD_NOT_FOUND" #bad request)

