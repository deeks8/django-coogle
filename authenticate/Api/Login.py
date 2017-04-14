import bcrypt
from ..models import *
from collegeData.models import CollegeV1_0,StateV1_0
from django.db.models import Q
import datetime


def Login(self,request):
    '''

    :param self:
    :param request:
    :return:

    '''

    returnData=[]

    if "Password" not in request:
        return "PASSWORD_NOT_PRESENT"

    userPassword=request['Password']
    request['Password']="xxxx"

    try:
        userObj=""
        #Fetch the user object
        try:
            if "Email" in request:
                request['Email']=request['Email'].lower()
                userObj=Userv1_0.objects.get(EmailId=request['Email'])
            else :
                #EmailId or phone is not present in parameter
                return "EMAILID_PHONE_NOT_PRESENT"
        except Exception as e:
            print e
            return "USER_OBJECT_NOT_PRESENT"


        #Verify password
        if bcrypt.hashpw(str(userPassword), str(userObj.Password)) == str(userObj.Password):



            # If register time is not set for old users, then set it now.
            if userObj.RegisterTime is None:
                userObj.RegisterTime = datetime.datetime.now()
                userObj.save()
            returnData.append({"Login": "true"})

            return returnData
        else:
            return "WRONG_PASSWORD"

    except Exception as e:

        return "LOGIN_FUNCTION_FAILED"