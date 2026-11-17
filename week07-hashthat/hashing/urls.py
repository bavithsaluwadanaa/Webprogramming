from django.urls import path
from . import views
app_name = "hashing"
urlpatterns = [path("", views.home, name="home"), path("hash/<str:digest>/", views.result, name="result"), path("quickhash/", views.quick_hash, name="quick_hash")]
