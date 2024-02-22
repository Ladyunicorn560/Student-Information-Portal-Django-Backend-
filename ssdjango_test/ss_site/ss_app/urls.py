# urls.py

from django.urls import path
from ss_app import views

urlpatterns = [
    path("", views.default_page, name="default_page"),
    path("student_list/", views.student_list, name="student_list"),
    path("add_student/", views.add_student, name="add_student"),
    path("update_student_list/", views.update_student_list, name="update_student_list"),
    path("delete_student_list/", views.delete_student_list, name="delete_student_list"),
    path("delete_student/<int:student_id>/", views.delete_student, name="delete_student"),
    path("update_student/<int:student_id>/", views.update_student, name="update_student"),
]
