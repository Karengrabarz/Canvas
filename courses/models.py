from email.policy import default
from django.db import models

import uuid
from enum import Enum

class Course_status(models.TextChoices):
    NOT_STARTED = 'not started',
    IN_PROGRESS = 'in progress',
    FINISHED = 'finished'

class Course(models.Model):
    id = models.UUIDField(primary_key = True, editable=False, default = uuid.uuid4)
    name = models.CharField(max_length = 100, unique = True)
    status = models.CharField(
        max_length = 11,
        choices = Course_status.choices,
        default = Course_status.NOT_STARTED
    )
    start_date = models.DateField(max_length = 10)
    end_date = models.DateField(max_length = 10)
    instructor = models.ForeignKey('accounts.Account', on_delete = models.CASCADE, related_name = 'courses', null=True, default=None)