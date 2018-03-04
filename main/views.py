#Django Imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from . forms import LightForm
from . models import Light

#Paho MQTT Imports
import paho.mqtt.client as mqtt
import os, urllib.parse as urlparse
#MQTT CODE
def PublishMQTT(topic,message):
    mqttc = mqtt.Client()
    url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://aqfodyqs:qLUWLpXyQLqj@m14.cloudmqtt.com:15104')
    url = urlparse.urlparse(url_str)
    mqttc.username_pw_set(url.username, url.password)
    mqttc.connect(url.hostname, url.port)
    mqttc.publish(topic, message)
# Create your views here.
def index(request):
    return render(request, 'main/index.html',{'hi':'hi'})
from django.views import generic
from django.urls import reverse
from .models import Light

class IndexView(generic.ListView):
    context_object_name = 'light_list'
    template_name = 'main/index.html'
    def get_queryset(self):
        return Light.objects.all()

def LightView(request,pk):
    light = get_object_or_404(Light,pk=pk)
    if request.method == 'POST':
        #POST REQUEST
        form = LightForm(request.POST,instance = light)
        if form.is_valid():
            #enter data into DB
            PublishMQTT(light.name,light.state)
            form.save()
            return HttpResponseRedirect(reverse('main:LightView',kwargs={'pk':pk}))
    else:
        #GET REQUEST
        form = LightForm(instance=light)
    return render(request, 'main/light.html', {'form':form,'pk':pk})

class DeleteLight(generic.DeleteView):
    model = Light
    success_url = reverse_lazy('main:IndexView')
class CreateLight(generic.CreateView):
    model = Light
    success_url = reverse_lazy('main:IndexView')
    fields = ['name']
