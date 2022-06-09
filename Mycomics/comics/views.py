from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *


# Create your views here.

# EDIT ALL permission

# ADMIN ONLY CHICK THE PERMISSION
@api_view(['POST'])
def add_comic(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('comic.add_comic'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)

        # request.data.update(user=request.user.id) # the same thing
    request.data["user"] = request.user.id  # the same as above CHICK

    new_comic = ComicSerializer(data=request.data)
    if new_comic.is_valid():
        new_comic.save()
        return Response({"Comic": new_comic.data})
    else:
        print(new_comic.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_comic(request: Request):
    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        comic = Comic.objects.filter(title__contains=search_phrase)
    else:
        comic = Comic.objects.order_by('-created_at').all()

    responseData = {
        "msg": "list of notes",
        "Comics": ComicSerializerView(instance=comic, many=True).data
    }

    return Response(responseData)


@api_view(['PUT'])
def update_comic(request: Request, comic_id):
    comic = Comic.objects.get(id=comic_id)

    updated_comic = ComicSerializer(instance=comic, data=request.data)
    if updated_comic.is_valid():
        updated_comic.save()
        responseData = {
            "msg": "updated Comic successfully"
        }

        return Response(responseData)
    else:
        print(updated_comic.errors)
        return Response({"msg": "cannot update comic !! "}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_comic(request: Request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    comic.delete()
    return Response({"msg": "Deleted Successfully"})


# READER & ADMIN CHICK THE PERMISSION
@api_view(['POST'])
def add_feedback(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('feedback.add_feedback'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)

        # request.data.update(user=request.user.id) # the same thing
    request.data["user"] = request.user.id  # the same as above

    new_feedback = FeedbackSerializer(data=request.data)
    if new_feedback.is_valid():
        new_feedback.save()
        return Response({"Feedback": new_feedback.data})
    else:
        print(new_feedback.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_feedback(request: Request):
    feedback = Feedback.objects.all()

    dataResponse = {
        "msg": "List of All Feedback",
        "Feedback": FeedbackSerializer(instance=feedback, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
def update_feedback(request: Request, feedback_id):
    feedback = Comic.objects.get(id=feedback_id)

    updated_feedback = ComicSerializer(instance=feedback, data=request.data)
    if updated_feedback.is_valid():
        updated_feedback.save()
        responseData = {
            "msg": "updated Feedback successfully"
        }

        return Response(responseData)
    else:
        print(updated_feedback.errors)
        return Response({"msg": "cannot update Feedback !! "}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_feedback(request: Request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    feedback.delete()
    return Response({"msg": "Deleted Successfully"})


# READER & ADMIN CHICK THE PERMISSION
@api_view(['POST'])
def add_profile(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('profile.add_profile'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)

        # request.data.update(user=request.user.id) # the same thing
    request.data["user"] = request.user.id  # the same as above

    new_profile = ProfileSerializer(data=request.data)
    if new_profile.is_valid():
        new_profile.save()
        return Response({"Profile": new_profile.data})
    else:
        print(new_profile.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_profile(request: Request):
    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        profile = Profile.objects.filter(name__contains=search_phrase)

    responseData = {
        "msg": " list of profile ",
        "Profile": ProfileSerializerView(instance=profile, many=True).data
    }
    return Response(responseData)


@api_view(['PUT'])
def update_profile(request: Request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    updated_profile = ComicSerializer(instance=profile, data=request.data)
    if updated_profile.is_valid():
        updated_profile.save()
        responseData = {
            "msg": "updated profile successfully"
        }

        return Response(responseData)
    else:
        print(updated_profile.errors)
        return Response({"msg": "cannot update Profile !! "}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_profile(request: Request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    profile.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['GET'])
def score(request: Request):
    pass


def follow(request: Request):
    pass


@api_view(['GET'])
def top10_comic(request: Request):
    top = Comic.objects.order_by('-rating')[:10]

    dataResponse = {
        "msg": "List of Top 10 Comics ",
        "TOP 10 COMICS : ": ComicSerializer(instance=top, many=True).data
    }
    return Response(dataResponse)


@api_view(['GET'])
def top10_reader(request: Request):
    top = Points.objects.order_by('-score')[:10]

    dataResponse = {
        "msg": "List of Top 10 Readers ",
        "TOP 10 Readers : ": PointsSerializer(instance=top, many=True).data
    }
    return Response(dataResponse)
