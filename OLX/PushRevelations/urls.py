from django.urls import path
from PushRevelations.views import RenderPushRev

urlpatterns = [
    path('PushRev', RenderPushRev, name='pushreveletaion'),
]

