from django.db import models

# Create your models here.
class data_uploader(models.Model):
    username = models.TextField(max_length=20)
    password = models.TextField(max_length=20)
    def __str__(self):
        return self.username
        
class data_receiver(models.Model):
    username = models.TextField(max_length=20)
    password = models.TextField(max_length=20)
    mail = models.TextField(max_length=20)
    def __str__(self):
        return self.username
        
class files(models.Model):
    username = models.TextField(max_length=20)
    key = models.TextField(max_length=20)
    filename = models.TextField(max_length=20)
    file = models.FileField(upload_to='store/')
    hash_value = models.TextField()
    date_time = models.DateTimeField()
    def __str__(self):
        return self.filename
        
class request_files(models.Model):
    uploader_name = models.TextField(max_length=20)
    filename = models.TextField(max_length=20)
    receiver_name = models.TextField(max_length=20)
    def __str__(self):
        return self.filename