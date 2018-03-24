from django.template.context_processors import request
from django.shortcuts import render
from CardAgainstHumanatyWebbApp import dataBaseConnection


def userNameForm(request):
    userName = request.POST.get("userName")
    password = request.POST.get("passWord")
    
    if len(userName) > 0 and len(password) > 0:
        userFromDb = dataBaseConnection.getDatabaseUserName(userName)
        print(str(userFromDb))
        
        if userFromDb is None:
            dataBaseConnection.insertUserNameInDb(userName, password)
            return render(request, 'loginModule/login.html')
  
        else:
            return render(request, 'loginModule/register.html')   
            
    else:
        return render(request, 'loginModule/register.html')
    
