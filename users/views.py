
from rest_framework.views import APIView
import json
from .PasswordManager import  password
from rest_framework.response import Response
from .models import usersDatabase,Expense
import time
from bson import ObjectId


class ExpenseRetrive(APIView):
    def get(self,request):
        data = json.loads(request.body.decode('utf-8'))
        Userid=data['userId']
        ans=Expense.objects.all().filter(Userid=Userid)
        print(len(ans))
        for i in ans:
            print(i)
        return Response({"a"})
        return Response({'Amount': ans.Amount, 'Remark': ans.Remark, 'Type': ans.Type, 'Category': ans.Category})
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        Expense.objects.create(
        Userid= data["Userid"],
        Amount= data["Amount"],
        Remark= data["Remark"],
        Type=data["Type"],
        Category= data["Category"]
    )
        return Response(data)


class GetProfile(APIView):
    # Path /users/profile/
    def get(self,request):
        data = request.GET
        w=(ObjectId(data['id']))
        ans = usersDatabase.objects.filter(_id=w).all()[0]
        print(ans.__dict__)
        return Response(
            {
                "Name":ans.Name,
                "Email":ans.Email,
                "DOB":ans.DOB,
                "Gender":ans.Gender
            }
        )
class AddRetrive(APIView):
    def get(self,request):


        data=dict(request.GET)
        data['email'] = request.query_params.get('email')
        data['password'] = request.query_params.get("password")
        ans = usersDatabase.objects.filter(Email=data['email']).first()
        salt = ans.salt
        hash = ans.hash

        if password.is_correct_password(bytes(salt),bytes(hash),data['password']):
            return Response({"isAuth": "True", "id": str(ans._id)})
        return Response({"isAuth": "False"})
    def post(self, request):
        data=json.loads(request.body.decode('utf-8'))
        salt, hash = password.hash_new_password(data['password'])
        dd,mm,yyyy=data['dob'].split("-")
        mm=time.strptime(mm, "%B").tm_mon
        data['dob']=yyyy+"-"+str(mm)+"-"+dd
        print(str(salt)  ,hash,salt[2:-1])
        '''if users_database.objects.filter(Email=data['email'])!=None:
            return Response({"message":"Email Already Exist"})
            '''
        usersDatabase.objects.create(
        Email= data['email'],
        Name= data['name'],
        DOB= data['dob'],
        Gender= data['gender'],
        salt= salt,
        hash= hash,
        )



        return Response({"message":"Sucessfully Created"})

# Create your views here.
