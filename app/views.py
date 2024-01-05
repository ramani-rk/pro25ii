from django.shortcuts import render

# Create your views here

from app.models import *

def create_friend(request):
    if request.method == 'POST':
        fname=request.POST['fn']
        fnum=request.POST['fnum']
        fmail=request.POST['fm']
        floc=request.POST['fl']

        fo=Friends.objects.get_or_create(fname=fname,fnum=fnum,fmail=fmail,floc=floc)[0]
        fo.save()

        ft=Friends.objects.all()
        d={'details' : ft}
        return render(request,'friend_details.html',d)

    return render (request,'create_friend.html')