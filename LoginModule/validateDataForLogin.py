from django.template.context_processors import request
from django.shortcuts import render
from CardAgainstHumanatyWebbApp import dataBaseConnection


def userNameForm(request):
    userName = request.POST.get("userName")
    password = request.POST.get("passWord")
    
    if len(userName) > 0 and len(password) > 0:
        idFromDb = dataBaseConnection.getIdFromUserNameAndPass(userName, password)
    
        if idFromDb is  None:
            return render(request, 'loginModule/login.html')
        
        else:
            return render(request, 'mainRoomModule/mainRoom.html')
    
    else:
        return render(request, 'loginModule/login.html')
    
