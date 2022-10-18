from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from ordered_model.models import OrderedModel

User = get_user_model()


class Todo(OrderedModel):
    uid = models.CharField(_('UID'), max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    task = models.CharField(_('Task'), max_length=64)
    completed = models.BooleanField(_('Is completed'), default=False)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    order_with_respect_to = 'user'

    def __str__(self):
        return self.task
