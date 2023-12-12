from django.db import models


# Create your models here.
class Contacts(models.Model):
    contact_name = models.CharField(max_length = 100)
    contact_email = models.EmailField()
    contact_notes = models.TextField()
    created_time =  models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'app_cma'

    def __str__(self):
        return self.contact_name