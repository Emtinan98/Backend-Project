from rest_framework_simplejwt import serializers
from rest_framework import serializers
from .models import *


class UserSerializerView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class ComicSerializerView(serializers.ModelSerializer):
    user = UserSerializerView()

    class Meta:
        model = Comic
        fields = '__all__'
        depth = 1


class ProfileSerializerView(serializers.ModelSerializer):
    user = UserSerializerView()

    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = '__all__'
