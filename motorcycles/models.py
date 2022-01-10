from django.db import models
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Motorcycle(models.Model):
    id = models.AutoField(primary_key=True)
    motorcycle_name = models.CharField(max_length=200)
    motorcycle_brand = models.CharField(max_length=200)
    motorcycle_image = models.ImageField(upload_to='images', storage=gd_storage, blank=True, default=None)

    def __str__(self):
        return self.motorcycle_name
