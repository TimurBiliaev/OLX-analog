from django.urls import path
from revelation.views import render_revelation, RenderAnswerForm, answer__message

urlpatterns = [
    path('revelation/<int:id>/"', render_revelation, name='revelation'),
    path('CreateAnswer/<int:id>/', RenderAnswerForm, name='revanswer'),
    path('ans_msg/<int:id>, ', answer__message, name='msg_answer')
]
