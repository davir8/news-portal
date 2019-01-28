from django.db import models

class Notice(models.Model):
    title = models.CharField('Título', max_length=300)