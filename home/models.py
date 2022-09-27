from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'title'], name='name of constraint')
        ]

    def __str__(self):
        return f'{self.title} - {self.user}'

    def get_absolute_url_update(self):
        return reverse('home:update_task', args=(self.id,))

    def get_absolute_url_delete(self):
        return reverse('home:delete_task', args=(self.id,))

    def get_absolute_url_detail(self):
        return reverse('home:detail_task', args=(self.id,))
