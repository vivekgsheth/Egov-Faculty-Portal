from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Message
from details.models import Faculty


#Converts complex datatypes into python native datatypes so that they can easily be rendered in JSON or XML.It also provides deserialization.

class UserSerializer(serializers.ModelSerializer):
    #write_only = True will not disp pwd in GET request . It will only disp it in POST req.
    password = serializers.CharField(write_only=True)
    online = serializers.ReadOnlyField(source='userprofile.online')

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'online']


class MessageSerializer(serializers.ModelSerializer):
    #SlugRelatedField may be used to represent the target of the relationship using a field on the target
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']


class FacultySerializer(serializers.ModelSerializer):
    faculty_id = serializers.CharField()
    faculty_name = serializers.CharField()
    image = serializers.FileField()

    class Meta:
        model = Faculty
        fields = ['faculty_id', 'faculty_name', 'image']


# class TimelineSerializer(serializers.Serializer):
#     faculties = FacultySerializer(many=True)
#     users = UserSerializer(many=True)


