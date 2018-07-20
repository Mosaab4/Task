from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Campaign(models.Model):

    STATUS_CHOICES = (
        ('enabled','Enabled'),
        ('disabeld','Disabled')
    )

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='enabled')
    type = models.ForeignKey(Type, related_name='types', on_delete=models.CASCADE)
    stop_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name