import glob

import face_recognition
from PIL import Image
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CustomUserEntity
from authentication.serializers import UserImageSerializer
from face_recognition_login import settings


class SignupView(APIView):
    http_method_names = ['post']
    permission_classes = [
        permissions.AllowAny
    ]
    renderer_classes = [
        JSONRenderer,
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        custom_user_entity = CustomUserEntity.objects.create(**{
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        })

        images = dict((request.data).lists())['image']
        serialization_failed = 0
        for image_elem in images:
            user_img_dict = {}
            user_img_dict['custom_user_entity_id'] = custom_user_entity.id
            user_img_dict['image'] = image_elem
            user_image_serializer = UserImageSerializer(data=user_img_dict)

            if user_image_serializer.is_valid():
                user_image_serializer.save()
            else:
                serialization_failed = 1

        if serialization_failed:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)


class LoginView(APIView):
    http_method_names = ['post']
    permission_classes = [
        permissions.AllowAny
    ]
    renderer_classes = [
        JSONRenderer,
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        person_image = dict((request.data).lists())['image'][0]
        image_list = [Image.open(item) for i in
                      [glob.glob('staticfiles/photo/*.%s' % ext) for ext in ["jpg", "jpeg", "gif", "png", "tga"]] for
                      item in i]
        for custom_user_image in image_list:
            a = face_recognition.load_image_file(custom_user_image.filename)
            custom_user_image_encoding = face_recognition.face_encodings(face_image=a)[0]
            person_image_encoding = face_recognition.face_encodings(face_image=person_image.name)[0]

            compare_result = face_recognition.compare_faces([custom_user_image_encoding], person_image_encoding)
        print(image_list)
