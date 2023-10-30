from django.urls import path, include
from gradebook import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path("", views.show_first_page, name="home"),
    # path("", include("django.contrib.auth.urls")),
    # path("signup/", views.SignUpView.as_view() ,name="signup"),
    path("login/", views.LogInView.as_view(), name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    # path("showgrades/", views.show_grades, name="show-grades"),
    path("addgrade/", views.GradeCreateView.as_view(), name="add-grade"),
    path("updategrade/<int:pk>/", views.GradeUpdateView.as_view(), name="update-grade"),
    path("deletegrade/<int:pk>", views.GradeDeleteView.as_view(), name="delete-grade"),
    path("teacher_home/", views.teacher_home, name="teacher-page"),
    path("pupil_home/", views.pupil_home, name="pupil-page"),
]