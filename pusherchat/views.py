from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
pusher = Pusher(app_id=u'295876', key=u'4b34c484eeb9fe4f4142', secret=u'6b17e2a894fc39296783')



# Create your views here.
@login_required(login_url='/admin/login/')
def chat(request):
    return render(request,"chat.html");


@csrf_exempt
def broadcast(request):
    
    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done");