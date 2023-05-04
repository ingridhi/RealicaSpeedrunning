from django.urls import path
from .views import goto_login, mainview, testview

urlpatterns = [
    path('', goto_login, name="goto_login"),
    path('home/', mainview, name="mainview"),
    path('test/', testview, name="testview"),
]
