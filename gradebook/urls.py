from django.urls import path, include
from gradebook import views

urlpatterns=[
    path("", views.show_first_page, name="home"),
    # path("", include("django.contrib.auth.urls")),
    # path("signup/", views.SignUpView.as_view() ,name="signup"),
    path("login/", views.LogInView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("showgrades/", views.show_grades, name="show-grades"),
    path("addgrade/", views.GradeCreateView.as_view(), name="add-grade"),
    path("updategrade/<int:pk>/", views.GradeUpdateView.as_view(), name="update-grade"),
    path("deletegrade/<int:pk>", views.GradeDeleteView.as_view(), name="delete-grade"),
]