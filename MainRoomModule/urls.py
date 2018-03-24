from LoginModule import views
from django.urls.conf import path

urlpatterns = [
    path('', views.login, name="login"),
   ]