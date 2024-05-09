from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from django.contrib import messages
import os


# Create your views here.
# api_url = "http://bmt-backend-env-1.eba-9vhdbybw.us-east-1.elasticbeanstalk.com"

# api_url = "http://127.0.0.1:8005/api"
api_url = os.environ['BACKEND_URL']
ticket_url = "https://9s287tuhy9.execute-api.us-east-1.amazonaws.com"
s3_image = "https://bmt-frontend-1.s3.amazonaws.com/cozy-restaurant-tables-ready-dinner-39875776.jpeg"
nutrition_url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"

# Get request to backend service to fetch all the restaurants
def index(request):
    try:
        headers = {'Accept': 'application/json'}
        response = requests.get(f"{api_url}/restr", headers=headers)
        response = response.json()

        paramas = {'restrs': response, 's3_image': s3_image}

        return render(request, 'bmtfe/index.html', paramas)
    except Exception as e:
        paramas = {"response": {"message": "Exceptions while connecting to backend API Server",
                   "error": e
                   }
                }
        return render(request, 'bmtfe/backenderror.html', paramas)

# Get request to backend service to fetch a single the restaurant through path parameter
def knowMore(request, restr_id):
    headers = {'Accept': 'application/json'}
    response = requests.get(f"{api_url}/restr/{restr_id}", headers=headers)
    response = response.json()

    paramas = {'restr': response, 's3_image': s3_image}
    return render(request, 'bmtfe/knowmore.html', paramas)

# Post request to thirdpart API for ticket creation. JSON body request
def supportTicket(request):
    if request.method=="POST":
        user_dict = {"title": request.POST['title'],
                    "content": request.POST['content'],
                    "category": request.POST['category'],
                    "status": "PENDING",
                    "user": "libin",
                    }
        # print(user_dict)
        url = f"{ticket_url}/dev/api/ticket/"
        response = requests.post(url, json=user_dict)
        response = response.json()
        messages.success(request, f"Your ticket for '{response['title']}' has been generated with the ticket id : {response['ticket_id']}.")
        return redirect('index')
    else:
        return HttpResponse('402 - Only POST method allowd')

## This funtionality is on hold
def foodReview(request):
    return render(request, 'bmtfe/foodreview.html')

def ownerPage(request, restr_id):
    # headers = {'Accept': 'application/json'}
    # response = requests.get(f"{api_url}/api/restr/{restr_id}", headers=headers)
    headers = {'Accept': 'application/json'}
    url = f"{api_url}/pending_booking/{restr_id}"
    response = requests.get(url, headers=headers)
    response = response.json()

    paramas = {'bookings': response}

    return render(request, 'bmtfe/owner.html', paramas)

def handleSignUp(request):

    if request.method=="POST":
        user_dict = {"username": request.POST['username'],
                    "email": request.POST['email'],
                    "first_name": request.POST['fname'],
                    "last_name": request.POST['lname'],
                    "phone_number": request.POST['pnumber'],
                    "password": request.POST['pass1']
                    }
    
        url = f"{api_url}/api/auth/create/user"
        response = requests.post(url, json=user_dict)

        response = response.json()
        response = response[1]
        response_username = response['Username']
        response_fullname = response['Full Name']
        messages.success(request, f"Hello {response_fullname}, your user id has been created as {response_username}")
        return redirect('index')

    # headers = {'Content-Type': 'application/json'}
    # headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    else:
        return HttpResponse('402 - Only POST method allowd')

def handleSignIn(request):

    if request.method == "POST":
        user_dict = f"username={request.POST['username']}&password={request.POST['pass']}"
        # data = "key1=value1&key2=value2"  

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = f'{api_url}/api/auth/token'
        response = requests.post(url, data=user_dict, headers=headers)
        response = response.json()
        # response = response[0]
        # response_token = response['token']
        # return HttpResponse(response['token'])
        messages.success(request, f"Hello {response.fullname}, your user id has been created as {response.username}")
        return redirect('index')
    else:
        return HttpResponse('402 - Only POST method allowd')
def handleSignOut(request):
    pass

# Post request for restaurant booking to backend service
def restrBooking(request, restr_id):
    if request.method == 'POST':
        user_dict = {"name": request.POST['name'],
                    "location": request.POST['location'],
                    "email_id": request.POST['email'],
                    "phone_number": request.POST['phone'],
                    "booking_date": request.POST['date'],
                    "booking_time": request.POST['time'],
                    "complete": False,
                    "restr_id": restr_id
                    }
        # data = "key1=value1&key2=value2"  

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = f"{api_url}/book"
        response = requests.post(url, json=user_dict)
        response = response.json()
        response = response[1]
        # response = response[0]
        # response_token = response['token']
        # return HttpResponse(response['token'])
        messages.success(request, f"Hello {response['name']}, your booking at {response['restr_name']} has been confirmed on {response['date']} at {response['time'] }.")
        return redirect('index')
    else:
        headers = {'Accept': 'application/json'}
        url = f"{api_url}/restr/{restr_id}"
        response = requests.get(url, headers=headers)
        response = response.json()

        paramas = {'restr': response}

        return render(request, 'bmtfe/booking.html', paramas)

# Put request to backend serivce to updated the booking with completion status
def bookingComplete(request, booking_id):
    complete =   { "complete": True }

    headers = {'Accept': 'application/json'}
    url = f"{api_url}/booking_complete/{booking_id}"
    response = requests.put(url, json=complete)
    response = response.json()
    response = response[1]
    
    messages.success(request, f"{response['response']} for the booking id {booking_id} ")

    return redirect('index')

# Delete request to backend service for deleting the booking 
def bookingDelete(request, booking_id):
    url = f"{api_url}/del_booking/{booking_id}"
    response = requests.delete(url)
    response = response.json()
    response = response[1]
    
    messages.success(request, f"{response['response'].title()} for the booking id {booking_id} ")

    return redirect('index')

# Used POST method to send GET request to thirdpart API for NUTRITION details 
# with quetyparameter. Which will render the response when the page request.
def handleNutrition(request):
    if request.method == 'POST':
        querystring = {"query":request.POST['search']}
        headers = {
            	"X-RapidAPI-Key": "93410e0c95msha42c20c9a112066p1d666fjsne829da26a6fd",
            	"X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
                }
        response = requests.request("GET", nutrition_url, headers=headers, params=querystring)
        response = response.json()
        
        paramas = {'nutritions': response}
    
        return render(request, 'bmtfe/nutrition.html', paramas)
    else:
        return render(request, 'bmtfe/nutrition.html')

from .forms import *
def formHandler(request):
    form = StudentForm
    mydict = {
        'form': form
    }
    form_dat = request.POST
    print(form_dat)
    return render(request, 'bmtfe/forms.html', context=mydict)