from rest_framework import serializers
from .models import Student
import json
from rest_framework.validators import UniqueValidator

class  StudentSerializer(serializers.Serializer):
    
    
    id=serializers.IntegerField(validators=[UniqueValidator(queryset=Student.objects.all())])
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
    def create(self,validated_data):   # create data
        return Student.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):  #update data
        # print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        # print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    
    # def validate_id(self, value):
           
    #     if  Student.objects.filter(id=value).exists():
    #         raise serializers.ValidationError("Id is Already Exists")
    #     return value
    
    # def validate_name(self, value):
    #     # I assumed that you will that the string value, is a JSON object.
    #     # name = json.loads(value).get('name', None)
    #     if  Student.objects.filter(name=value).exists():
    #         raise serializers.ValidationError("Name is Already Exists")
    # # You need to return the value in after validation.
    #     return value
    # def validate_roll(self, value):
    #     if  Student.objects.filter(roll=value).exists():
    #         raise serializers.ValidationError("Roll Number is Already Exists")
    #     return value
    
   