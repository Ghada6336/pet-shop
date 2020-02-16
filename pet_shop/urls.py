"""pet_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from petshop import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.welcome ,name='hello-world'),
    path('petshop/list/',views.Petshop_list ,name='pet-list'),
    path('petshop/detail/<int:pet_id>/',views.Petshop_detail ,name='pet-detail'),

    path('petshop/create/',views.Petshop_create ,name='pet-create'),
    path('petshop/update/<int:pet_id>/',views.Petshop_update ,name='pet-update'),
    path('petshop/delete/<int:pet_id>/',views.Petshop_delete ,name='pet-delete'),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
