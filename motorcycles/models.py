from django.db import models
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Motorcycle(models.Model):
    id = models.AutoField(primary_key=True)
    motorcycle_name = models.CharField(max_length=200)
    motorcycle_brand = models.CharField(max_length=200)

    def __str__(self):
        return self.motorcycle_name


class MotorcycleImage(models.Model):
    motorcycle_name = models.ForeignKey(Motorcycle, on_delete=models.DO_NOTHING, null=True)
    motorcycle_image = models.FileField(upload_to='images', storage=gd_storage)

    @property
    def get_image_url(self):
        if self.motorcycle_image and hasattr(self.motorcycle_image, 'url'):
            return self.motorcycle_image.url
        else:
            return "/static/images/no-image.png"
