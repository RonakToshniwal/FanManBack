from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
import json
from .PasswordManager import  password
import pymongo


class AddRetrive(APIView):
    def post(self, request):
        data=json.loads(request.body.decode('utf-8'))
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Users"]
        mycol = mydb["user_database"]
        if len(list(mycol.find({"Email":data['email']})))!=0:
            return JsonResponse({"message":"Email Already Exist "})
        print(data)
        salt, hash = password.hash_new_password(data['password'])
        Mydict={
            "Email":data['email'],
            "Name": data['name'],
            "DOB":data['dob'],
            "Gender":data['gender'],
            "salt": salt,
            "hash": hash,
        }
        mycol.insert_one(Mydict)


        return JsonResponse({"message":"Sucessfully Created"})

# Create your views here.
