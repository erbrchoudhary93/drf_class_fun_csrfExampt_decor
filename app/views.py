from rest_framework.parsers import JSONParser
from .models import Student
from .serilizer import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


#function based view


@csrf_exempt
def student_api(request,id=0):
    if request.method=='GET':
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method =='POST':
        data= JSONParser().parse(request)  # convert into python data
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # msg ={"msg":"Data added successfully"}
            return JsonResponse (serializer.data,safe = False)
        return JsonResponse(serializer.errors,safe=False)
    

    if request.method  == 'PATCH':
        pythondata= JSONParser().parse(request)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serilizer= StudentSerializer(stu, data=pythondata,partial=True)  # partial update 
        if serilizer.is_valid():
            serilizer.save()
            res = {'msg': 'Data Updated'}
            return JsonResponse(serilizer.data,safe=False)
        return JsonResponse(serilizer.errors,safe=False)
        
    if request.method  == 'PUT':
        pythondata= JSONParser().parse(request)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serilizer= StudentSerializer(stu, data=pythondata)  # full data update
        if serilizer.is_valid():
            serilizer.save()
            res = {'msg': 'Data Updated'}
            return JsonResponse(serilizer.data,safe=False)
        return JsonResponse(serilizer.errors,safe=False)
    if request.method == 'DELETE':
        pythondata = JSONParser().parse(request)   
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()  
        res= {'msg':"Data Deleted !! "}
        return JsonResponse(res,safe=False)
            
            
        

#class based curd method
@method_decorator(csrf_exempt, name ='dispatch')
class StudentAPI(View):
    def get(self , request,*args,**kwargs):
        # pythondata= JSONParser().parse(request)
        # id=pythondata.get('id',None)
        # if id is not None:
        #     stu= Student.objects.get(id=id)
        #     serializer=StudentSerializer(stu)
        #     return JsonResponse(serializer.data,safe=False)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    def post(self , request,*args,**kwargs):
        pythondata= JSONParser().parse(request)  # convert into python data
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            # res={'msg':'Data Created'}
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.error_messages,safe=False)
    
    def patch(self , request,*args,**kwargs):
        pythondata= JSONParser().parse(request)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serilizer= StudentSerializer(stu, data=pythondata,partial=True)  # partial update 
        if serilizer.is_valid():
            serilizer.save()
            # res = {'msg': 'Data Updated'}
            return JsonResponse(serilizer.data,safe=False)
        return JsonResponse(serilizer.errors,safe=False)
    
    
    def put(self , request,*args,**kwargs):
        pythondata= JSONParser().parse(request)
        Id = pythondata.get('id')
        print(Id)
        stu = Student.objects.get(id=Id)
        serilizer= StudentSerializer(stu, data=pythondata)  # full data update
        if serilizer.is_valid():
            serilizer.save()
            # res = {'msg': 'Data Updated'}
            return JsonResponse(serilizer.data,safe=False)
        return JsonResponse(serilizer.errors,safe=False)
    
    
    def delete(self , request,*args,**kwargs):
        pythondata = JSONParser().parse(request)   
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()  
        res= {'msg':"Data Deleted !! "}
        return JsonResponse(res,safe=False)
        
        
      




        
            
            
        