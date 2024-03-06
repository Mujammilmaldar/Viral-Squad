from django.db import models

class TextData(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    CollegeName = models.CharField(max_length=100)
    BranchOfStudy = models.CharField(max_length=100)
    yearofeducation = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    mobile2 = models.CharField(max_length=20, blank=True, null=True)
    insta = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    achievement=models.TextField(blank=True)
    statement1 = models.BooleanField(default=False)
    statement2 = models.BooleanField(default=False)
    statement3 = models.BooleanField(default=False)

class DocumentData(models.Model):
    text_data = models.OneToOneField(TextData, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos')
    aadhar_card = models.FileField(upload_to='documents')
    achievement_file = models.FileField(upload_to='documents')
