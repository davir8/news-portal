from django.db import models

class NoticeManager(models.Manager):
    # busca por titulo
    def search(self, query):
        return self.get_queryset().filter(title__icontains=query)

class Notice(models.Model):
    title = models.CharField('Título', max_length=300)
    objects = NoticeManager()