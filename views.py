from django.shortcuts import render, redirect
import requests
from .models import Message

base_url = "http://localhost:8000" #Replace
# Create your views here.

def get(request):
    r = requests.get(base_url + "/api/")
    response = r.json()
    if response["status"] == True:
        context = { 'message' : response["message"] }
        return render(request, "get/index.html", context)


def post(request):

    context = { 'message': "This is the default message"}
    return render(request, "post/index.html", context)

def submit(request):
    request_url = base_url + "/api/generate"
    # Add code to call api and fetch result, and display result instead of the input
    context = {'message': input}
    return render(request, "post/index.html", context)


def addMessage(request):
    pass

def storeMessage(request):

    # Add code to save message
    return redirect(addMessage)

def getMessage(request):
    # message = Message.objects.get(id=id)
    # Add code to retrieve message with a given message_id.
    # An example of how to retrieve a message with a given id is provided above
    return render(request, "messages/getMessage.html", context)
