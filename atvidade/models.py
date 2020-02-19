from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    materia = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descicao = models.TextField()
    data_de_envio = models.DateTimeField(default=timezone.now)
    data_de_entrega = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
