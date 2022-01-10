from django.db import models

# #PASSO 
# from gdstorage.storage import GoogleDriveStorage

# gd_storage = GoogleDriveStorage()


class Motorcycle(models.Model):
    id = models.AutoField(primary_key=True)
    motorcycle_name = models.CharField(max_length=200)
    motorcycle_brand = models.CharField(max_length=200)
    motorcycle_image = models.ImageField(upload_to='images', blank=True, default=None)
    # # PASSO
    # storage=gd_storage

    def __str__(self):
        return self.motorcycle_name
