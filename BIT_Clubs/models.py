from django.db import models
from django.conf import settings
from django.utils import timezone


class Club(models.Model):

    name = models.CharField(max_length=20)
    display_picture = models.ImageField(upload_to='')
    header_image = models.ImageField(upload_to='')
    about = models.TextField()

    def __str__(self):
        return self.name


class TeamMember(models.Model):

    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

    def __str__(self):
        return self.member_name
