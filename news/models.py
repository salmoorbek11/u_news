from django.utils import timezone
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def get_absolute_url(self):
        return "/post/%i/" % self.id

    def __str__(self) -> str:
        return self.title