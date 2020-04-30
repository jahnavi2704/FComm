from django.shortcuts import render
import paho.mqtt.client as mqttClient
import time
from .models import *
from django.http import HttpResponse


def topic(request):

    return  render(request,'message/courses.html')

def select_topic(request):
     a = Topic.objects.all()
     context = {'Topic': a}

     return render(request, 'message/index.html', context=context)

def topic_result(request):
    selected=request.POST['select']
    selected_prof = request.POST['select_professor']
    Topic.objects.create(topic=selected, name=selected_prof)
    a = Topic.objects.all()
    context = {'Topic': a,
    'name':selected_prof}
    return render(request,'message/index.html',context=context)







def sent_messages(request):
     a = Message.objects.all().order_by('userlogid')
     context = {'messages': a,
                 'Topic' : Topic}
     # return redirect('../')
     return render(request, 'message/display.html', context=context)

def result(request):
    print(request.POST)
    fullname = request.POST['fullname']
    global Topic
    A = fullname.split(',')
    for i in range(0, len(A)-1):
        B = A[i].split("}")
        Message.objects.create(fullname=B[1],topic=B[0])
    a = Topic.objects.all()
    context = {'Topic': a}
    return render(request,'message/index.html',context=context)

def main(request):
    a = Message.objects.all()
    n = request.POST['topic']
    print(n)
    context = {'selected_name':n,
    'messages':a}
    print(a[0].topic)
    return render(request, 'message/contact.html', context=context)
