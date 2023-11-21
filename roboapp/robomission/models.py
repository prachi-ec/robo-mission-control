from django.db import models
from datetime import datetime

STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('EXECUTING', 'Executing'),
        ('COMPLETED', 'Completed'),
    ]

class Mission(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'completed_at': self.completed_at.isoformat(),
        }

    def __str__(self):
        return self.name

    def set_completed(self):
        self.completed_at = datetime.now()
        self.save()
