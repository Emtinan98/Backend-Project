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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_comic(request: Request):
    """ This endpoint for adding comics """
    if not request.user.is_authenticated or not request.user.has_perm('comics.add_comic'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)

    request.data["user"] = request.user.id

    new_comic = ComicSerializer(data=request.data)
    if new_comic.is_valid():
        new_comic.save()
        return Response({"Comic": new_comic.data})
    else:
        print(new_comic.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_comic(request: Request):
    """ This endpoint for List comics """
    comic = Comic.objects.all()

    responseData = {
        "msg": "list of Comic",
        "Comics": ComicSerializer(instance=comic, many=True).data
    }

    return Response(responseData)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_comic(request: Request, comic_id):
    """ This endpoint for update comics """
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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_comic(request: Request, comic_id):
    """ This endpoint for delete comics """
    comic = Comic.objects.get(id=comic_id)
    comic.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_feedback(request: Request, profile_id):
    """ This endpoint for adding feedback """
    print("adding feedback")
    if not request.user.is_authenticated or not request.user.has_perm('comics.add_feedback'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)

    request.data["user"] = request.user.id

    new_feedback = FeedbackSerializer(data=request.data)
    if new_feedback.is_valid():
        new_feedback.save()

        pro = Profile.objects.get(id=profile_id)
        pro.score = pro.score + 1
        pro.save()

        return Response({"Feedback": new_feedback.data})
    else:
        print(new_feedback.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_feedback(request: Request):
    """ This endpoint for list all feedback """
    feedback = Feedback.objects.all()

    dataResponse = {
        "msg": "List of All Feedback",
        "Feedback": FeedbackSerializer(instance=feedback, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_feedback(request: Request, feedback_id):
    """ This endpoint for update feedback """
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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_feedback(request: Request, feedback_id):
    """ This endpoint for delete feedback """
    feedback = Feedback.objects.get(id=feedback_id)
    feedback.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_profile(request: Request):
    """ This endpoint for adding profile """
    if not request.user.is_authenticated or not request.user.has_perm('comics.add_profile'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)

    request.data["user"] = request.user.id

    new_profile = ProfileSerializer(data=request.data)
    if new_profile.is_valid():
        new_profile.save()
        return Response({"Profile": new_profile.data})
    else:
        print(new_profile.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_profile(request: Request):
    """ This endpoint for list all profile """
    profile = Profile.objects.all()

    responseData = {
        "msg": " list of profile ",
        "Profile": ProfileSerializerView(instance=profile, many=True).data
    }
    return Response(responseData)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_profile(request: Request, profile_id):
    """ This endpoint for update profile """
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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_profile(request: Request, profile_id):
    """ This endpoint for delete profile """
    profile = Profile.objects.get(id=profile_id)
    profile.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['GET'])
def top10_comic(request: Request):
    """ This endpoint for list the top 10 comics by rating """
    top = Comic.objects.order_by('-rating')[:10]

    dataResponse = {
        "msg": "List of Top 10 Comics ",
        "TOP 10 COMICS : ": ComicSerializer(instance=top, many=True).data
    }
    return Response(dataResponse)


@api_view(['GET'])
def top10_reader(request: Request):
    """ This endpoint for list the top 10 reader by score """
    top = Profile.objects.order_by('-score')[:10]

    dataResponse = {
        "msg": "List of Top 10 Readers ",
        "TOP 10 Readers : ": ProfileSerializer(instance=top, many=True).data
    }
    return Response(dataResponse)


@api_view(['GET'])
def search_for_comic(request: Request):
    """ This endpoint for searching comics by title  """
    if request.method == 'GET':
        comic = Comic.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            search_s = Comic.objects.filter(title=title)
            search_comic = {
                "Comic": ComicSerializerView(instance=search_s, many=True).data
            }
            return Response(search_comic)
    return Response("non")


@api_view(['GET'])
def search_for_profile(request: Request):
    """ This endpoint for searching profile by name  """
    if request.method == 'GET':
        profile = Profile.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            search_s = Profile.objects.filter(name=name)
            search_profile = {
                "Profile": ProfileSerializerView(instance=search_s, many=True).data
            }
            return Response(search_profile)
    return Response("non")


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_favorite(request: Request):
    """ This endpoint for adding comics for yor favorite  """
    if not request.user.is_authenticated or not request.user.has_perm('comics.add_favorite'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)

    request.data["user"] = request.user.id

    new_fav = FavoriteSerializer(data=request.data)
    if new_fav.is_valid():
        new_fav.save()
        return Response({"Favorite": new_fav.data})
    else:
        print(new_fav.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_favorite(request: Request):
    """ This endpoint for list all your favorite comics  """
    favorite = Favorite.objects.all()

    responseData = {
        "msg": " Favorite : ",
        "Favorite": FavoriteSerializer(instance=favorite, many=True).data
    }
    return Response(responseData)
