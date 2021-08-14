from django.db import models
from django.urls import reverse


class Books(models.Model):
    title = models.CharField(max_length=200)
    about = models.TextField(null=True)
    pages = models.IntegerField(null=True)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name_plural = "Books"
