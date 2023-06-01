from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Users

# Create your views here.
# login page
def login(req):
    if(req.method=="POST"):
        user = Users.objects.filter(name=req.POST['name'], passwd=req.POST["password"])
        if(len(user) != 0 ):
            req.session['name']=user[0].name
            return HttpResponseRedirect('/alltrainee')
    return render(req, 'trainee/login.html')

def logout(req):
    req.session.clear()
    return HttpResponse('logout')

# signin page
def signin(req):
    if(req.method == 'POST'):
        Users.objects.create(name=req.POST['name'], passwd=req.POST['password'])
        return HttpResponseRedirect('/alltrainee')
    return render(req, 'trainee/signin.html')
    
# allTrainee page
def allTrainee(req):
    # get all users from model
    users = Users.objects.all()
    return render(req, 'trainee/allTrainee.html', {'users': users})

# updateTrainee page
def updateTrainee(req, id):
    user = Users.objects.get(id=id)
    if(req.method == 'POST'):
        Users.objects.filter(id=id).update(name=req.POST['name'], passwd=req.POST['password'])
        return HttpResponseRedirect('/alltrainee')      
    return render(req, 'trainee/update.html', {'user': user})

# deleteTrainee page
def deleteTrainee(req, id):
    Users.objects.filter(id=id).delete()
    return HttpResponseRedirect('/alltrainee')