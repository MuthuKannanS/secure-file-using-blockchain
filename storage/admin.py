from django.contrib import admin

# Register your models here.
from storage.models import data_uploader,data_receiver,files,request_files

#class userAdmin(admin.ModelAdmin):
    #user = ['username','rollno','email','password','c_password']

admin.site.register(data_uploader)
admin.site.register(data_receiver)
admin.site.register(files)
admin.site.register(request_files)
