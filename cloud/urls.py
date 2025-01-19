"""cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from storage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('userlogin/',views.userlogin, name="userlogin"),
    path('receiverlogin/',views.receiverlogin,name="receiverlogin"),
    path('data_uploader_register/',views.register1, name="register1"),
    path('data_Receiver_register/',views.register2, name="register2"),
    path('Data_uploader_signup/',views.signup1, name="signup1"),
    path('Data_receiver_signup/',views.signup2, name="signup2"),
    path('data_uploader_login/',views.login1, name="login1"),
    path('data_receiver_login/',views.login2, name="login2"),
    path('upload/<int:id>/',views.upload, name="upload"),
    path('request/<str:id1>/<int:id>/',views.request,name="request"),
    path('send_email/<str:name>/<int:id>/',views.send_email,name="send_email"),
    path('download/<int:id1>/',views.download, name="download"),
    path('back/<int:id>/',views.back, name="back"),
    
    #path('view/',views.view, name="view"),
    path('logout/',views.logout, name="logout"),
    #path('upload_file/',views.upload_file,name="upload_file"),
    path('main/',views.main, name="main"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)