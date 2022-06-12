from django.urls import path
from . import views

app_name = "comics"

urlpatterns = [
    path("add_comic/", views.add_comic, name="add_comic"),
    path("all_comic/", views.list_comic, name="list_comic"),
    path("update_comic/<comic_id>/", views.update_comic, name="update_comic"),
    path("delete_comic/<comic_id>/", views.delete_comic, name="delete_comic"),
    path("add_feedback/<profile_id>/", views.add_feedback, name="add_feedback"),
    path("all_feedback/", views.list_feedback, name="list_feedback"),
    path("update_feedback/<feedback_id>/", views.update_feedback, name="update_feedback"),
    path("delete_feedback/<feedback_id>/", views.delete_feedback, name="delete_feedback"),
    path("add_profile/", views.add_profile, name="add_profile"),
    path("all_profile/", views.list_profile, name="list_profile"),
    path("update_profile/<profile_id>/", views.update_profile, name="update_profile"),
    path("delete_profile/<profile_id>/", views.delete_profile, name="delete_profile"),
  # path("score/", views.score, name="score"),  # not in postman
    path("follow/", views.follow, name="follow"),  # not in postman
    path("top10_comic/", views.top10_comic, name="top10_comic"),
    path("top10_reader/", views.top10_reader, name="top10_reader"),
    path("search_for_comic/", views.search_for_comic, name="search_for_comic"),
    path("search_for_profile/", views.search_for_profile, name="search_for_profile"),

]
