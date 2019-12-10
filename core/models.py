from datetime import date
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Information(models.Model):
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=30)
    contact_no = PhoneNumberField()
    email = models.EmailField()
    dob = models.DateField(verbose_name='Date of birth')
    location = models.CharField(max_length=30)
    summary = models.TextField()
    facebook = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    banner_image = models.ImageField(
        upload_to='banner_image', null=True, blank=True)
    profile_image = models.ImageField(
        upload_to='profile_image', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.id = 1
        super(Information, self).save(*args, **kwargs)

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=40, null=True, blank=True)
    duration = models.CharField(max_length=9, null=True, blank=True)
    academy = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.degree


class Skill(models.Model):
    title = models.CharField(max_length=50)
    progress = IntegerRangeField(min_value=1, max_value=100)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    comments = models.TextField(null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='product_image')
    description = models.TextField()
    source_code_link = models.CharField(max_length=200, null=True, blank=True)
    live_link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(
        upload_to='service_image', null=True, blank=True)

    def __str__(self):
        return self.title


# class UserInfo(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     info = models.ForeignKey(Information, on_delete=models.CASCADE)
#     skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
#     projects = models.ForeignKey(Project, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username
