from django.db import models
from django.contrib.auth.models import User
from PushRevelations.models import Revelation

class RevelationAnswer(models.Model):
    revelation = models.ForeignKey(
        Revelation,
        on_delete=models.CASCADE,
    )

    description = models.TextField(max_length=200)

    user_client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='client_revelation_answers',
        )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='revelation_answers',
        )

    created = models.DateTimeField(auto_now_add=True)

