import bcrypt
from ..models import *
from collegeData.models import CollegeV1_0,StateV1_0
from django.db.models import Q
import datetime


def EncryptPassword(password,request):
    ''':
    :param password: contains the user password
    :param request: contains the paramenter sent by the user
    :return: encrypted password using bcrypt
    '''

    hashedPassword=""
    try:
        hashedPassword = bcrypt.hashpw(str(password), bcrypt.gensalt())
    except Exception as e:
        return 0
    return hashedPassword



def CheckIfUserExists(data,parameter,request):
    '''
    :param data: contains either Phone number or EmailId
    :param parameter: contains keyword "Phone" or "EmailId" to be check
    :param request: contains the parameter sent by the user
    :return: true if user is present else false
    '''
    try:

        if parameter == "Phone":
            try:
                userObj = Userv1_0.objects.get(Phone=data)
                return True
            except Exception as e:
                return False

        elif parameter == "EmailId":
            try:
                userObj = Userv1_0.objects.get(EmailId=data)
                return True
            except Exception as e:
                return False
        return True
    except Exception as e:
        return 0


def CreateUser(userObj,request):
    '''
    :param userObj: contains object of the user from User Model
    :param request: contains the parameter sent by the user
    :param FILES: contains image file if sent by the user
    :return: None
    '''

    try:
        print request
        if "Phone" in request:
            userObj.Phone=request['Phone']
        if "EmailId" in request:
            userObj.EmailId=request['EmailId']
        if "Name" in request:
            userObj.Name=request['Name']
        userObj.RegisterTime=datetime.datetime.now()
        userObj.Password=request['Password']
        userObj.save()
        if "College" in request:
            college = CollegeV1_0.objects.get(College=request['College'])
            userObj.CollegeId=college
        if "State" in request:
            state = StateV1_0.objects.get(StateName = request['State'])
            userObj.StateId = state

        userObj.save()
    except Exception as e:
        return 0
    return


def registerUser(self, request):
    '''

    :param self:
    :param request: contains parameter sent by the user
    :return: "1" if success else  "0" . "409" if user with that phone/Email present. "404-1" if Phone/EmailId not given.


    '''


    returnData = []
    if "Password" not in request:
        return "PASSWORD_NOT_PRESENT"


    try:
        # # Hash the password
        password = EncryptPassword(request['Password'], request)
        if password == 0:
            return "PASSWORD_ERROR"
        request['Password'] = EncryptPassword(request['Password'], request)


        # Check if user is already present
        if "Phone" in request:
            if CheckIfUserExists(request['Phone'], "Phone", request) == True:
                return "USER_EXIST_PHONE"
        elif "EmailId" in request:
            request['EmailId'] = request['EmailId'].lower()
            if CheckIfUserExists(request['EmailId'], "EmailId", request) == True:
                return "USER_EXIST_EMAIL"
        else:
            # EmailId or phone is not present in parameter
            return "EMAILID_PHONE_NOT_PRESENT"

        # Add userObj
        userObj = Userv1_0()
        user = CreateUser(userObj, request)
        if user ==0 :
            return "USER_CREATION_ERROR"

        returnData.append({"Uid":  userObj.Uid})
        return returnData



    except Exception as e:
        return "SERVER_ERROR"
