from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,unique=True,blank=False,validators=[validators.MaxLengthValidator(1)])
    def __str__(self):
        return self.topic_name
def validate_name(name):
    if not name.isalpha():
        raise ValidationError("{} is having characters other than alphabets".format(name))   
class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True,validators=[validate_name],blank=False)
    url=models.URLField(max_length=100,unique=True,blank=False)
    def __str__(self):
        return self.name
class AccessDetails(models.Model):
    webpage=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.datetime).split(" ")[0]
class ProfilePic(models.Model):
    name=models.CharField(max_length=100,unique=True,\
        validators=[validate_name],blank=False)
    image=models.ImageField(upload_to="%Y/%m/%d")

    def __str__(self):
        return self.name  