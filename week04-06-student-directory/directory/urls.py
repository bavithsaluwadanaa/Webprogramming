from django.urls import path
from . import views

app_name = "directory"
urlpatterns = [path("", views.home, name="home"), path("students/", views.student_list, name="student_list"), path("students/page/<int:page>/", views.student_list, name="student_list_page"), path("students/<int:student_id>/", views.student_detail, name="student_detail"), path("students/<int:student_id>/edit/", views.student_edit, name="student_edit"), path("modules/", views.module_list, name="module_list")]
