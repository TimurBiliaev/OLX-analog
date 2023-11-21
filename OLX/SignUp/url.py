from django.urls import path
from SignUp.views import RenderSignIn, RenderRegestration, sign_out, PasswordRecovery


urlpatterns = [
    path('Sign_in/', RenderSignIn, name='sign_in'),
    path('Regestration/', RenderRegestration, name='regestration'),
    path('Logout/', sign_out, name='logout'),
    path('Recovery/', PasswordRecovery, name='Recovery'),
]