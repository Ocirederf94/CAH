from LoginModule import views, validateDataForRegister, validateDataForLogin
from django.urls.conf import path

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="login"),
    path('validateDataForRegister', validateDataForRegister.userNameForm, name="userNameForm"),
    path('validateDataForLogin', validateDataForLogin.userNameForm, name="userNameForm")

]