from django.urls import path
from SignUp.views import RenderSignIn
from Catalog.views import  Search__of__category


urlpatterns = [
    path('Sign_in/', RenderSignIn, name='sign_in'),
    path('Category/<int:id>', Search__of__category, name='category_s'),
]

