from django.shortcuts import render, redirect
import requests
from .models import Message

url = "http://localhost:8000" #Replace
# Create your views here.
def get(request):
    r = requests.get(url+"/api/")
    response = r.json()
    if response["status"] == True:
        context = { 'message' : response["message"] }
        return render(request, "get/index.html", context)


def post(request):
    context = { 'message': "This is the default message"}
    return render(request, "post/index.html", context)

def submit(request):

    print("Submit called")
    print(request.method)
    input = request.POST['value']
    print('input')
    # Add code to call api to hash value
    context = {'message': input}
    return render(request, "post/index.html", context)


def addMessage(request):
    pass

def storeMessage(request):

    # Add code to save message
    return redirect(addMessage)

def getMessage(request):
    # Add code to retrieve message with a given message_id
    return render(request, "messages/getMessage.html", context)
