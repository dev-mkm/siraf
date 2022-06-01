from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError

def phonenumber(value):
    if len(value) != 11 or value.startswith("09"):
        raise ValidationError('Invalid Number')

def validate_image(image):
    file_size = image.file.size
    limit_mb = 5
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)

class file(models.Model):
    title = models.CharField(max_length=128),
    description = models.TextField(),
    address = models.TextField(),
    visitPhoneNumber = models.CharField(max_length=11 ,validators=[phonenumber]),
    city_name = models.CharField(max_length=128),
    status = models.BooleanField(),
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL),
    ownerPhoneNumber = models.CharField(max_length=11 ,validators=[phonenumber]),
    type = models.CharField(max_length=1, choices=(
        ('B', 'Buy'),
        ('S', 'Sell'),)),

class fileImage(models.Model):
    property = models.ForeignKey(file, related_name='virtualTour', on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to='images/', validators=[validate_image])