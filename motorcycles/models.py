from django.db import models

from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Motorcycles(models.Model):
    id = models.AutoField(primary_key=True)
    motorcycle_name = models.CharField(max_length=200)
    motorcycle_image = models.FileField(upload_to='images', storage=gd_storage)
