from django.urls import path
from UserProfile.views import  RenderProfile, Delete_revelation, Edit_revelation, ShowOtherUserProfile, EditProfile, edit_data,change_password,delete_profile,RenderMessages, accept_answer, delete_answer


urlpatterns = [
    path('Profile/', RenderProfile, name='userprofile'),
    path('DelRev/<int:id>/', Delete_revelation, name='deleterevelation'),
    path('EditRev/<int:id>/', Edit_revelation, name='editrevelation'),
    path('User/<int:id>/', ShowOtherUserProfile, name='otheruser'),
    path('DataProfile/', EditProfile, name="dataprofile"),
    path('EditData/', edit_data, name="editdata"),
    path('ChangePassword/', change_password, name="editpassword"),
    path("DELETEPROFILE/", delete_profile, name="delprofile"),
    path('messages/', RenderMessages, name='msg'),
    path('accept_ans/<int:id>', accept_answer, name='aans'),
    path('del_answ/<int:id>', delete_answer, name='dans'),
]