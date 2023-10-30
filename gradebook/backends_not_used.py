# #https://docs.djangoproject.com/en/4.2/topics/auth/customizing/

# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
# from .models import User
# from django.contrib.auth.hashers import make_password

# class GradebookUserBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(username=username)
#         except UserModel.DoesNotExist:
#             return None

#         if user.check_password(password):
#             return user

#         try:
#             gradebook_user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             return None

#         if gradebook_user.password == make_password(password):
#             return gradebook_user

#         return None