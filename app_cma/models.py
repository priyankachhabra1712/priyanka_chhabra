from django.db import models

# Create your models here.
class Contacts(models.Model):
    contact_name = models.CharField(max_length = 50)
    contact_email = models.CharField(max_length = 50)
    contact_notes = models.CharField(max_length = 200)
    created_time = models.CharField(max_length=25)

    class Meta:
        app_label = 'app_cma'

    def __str__(self):
        return self.contact_name