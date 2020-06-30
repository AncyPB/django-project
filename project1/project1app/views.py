from django.shortcuts import render
from project1app.models import Client,Owner,Restaurant,Review,Reservation,Contact
from project1app.form import NewUserForm,ReviewForm,ReserveForm
from django.http import HttpResponse
# Create your views here.
hotelname='none'
hotel_id='0'
def index(request):
    if(request.POST.get('submitt')):
        name=request.POST.get('search').upper()
        global hotelname
        hotelname=name
        restaurant_list = Restaurant.objects.order_by('hotelname')
        for value in restaurant_list:
            if (str(value.hotelname) == str(hotelname)):
                return view(request)
        my_dict={'value':'not found'}
        return render(request,'index.html',context=my_dict)
    if(request.POST.get('submit')):
        n_name=request.POST.get('name')
        n_phone=request.POST.get('phone')
        n_email=request.POST.get('email')
        n_message=request.POST.get('message')
        usr=Contact.objects.get_or_create(name=n_name,Email=n_email,phone=n_phone,message=n_message)[0]
        usr.save()
    return render(request,'index.html')

def signup(request):
    if(request.POST.get('submit')):
        n_name=request.POST.get('name')
        n_phone=request.POST.get('phone')
        n_email=request.POST.get('email')
        n_message=request.POST.get('password')
        usr=Clients.objects.get_or_create(name=n_name,Email=n_email,phone=n_phone,message=n_message)[0]
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        users=Client.objects.order_by('email')
        for value in users:
            if str(value.email)== str(email) and str(value.password) == str(password):
                return home(request)
        my_dict={'heading':'Wrong Email or Password'}
        return render(request,'login.html',context=my_dict)
    return render(request,'login.html')

def home(request):
    if(request.POST.get('submitt')):
        name=request.POST.get('search').upper()
        global hotelname
        hotelname=name
        restaurant_list = Restaurant.objects.order_by('hotelname')
        for value in restaurant_list:
            if (str(value.hotelname) == str(hotelname)):
                return view(request)
        my_dict={'value':'not found'}
        return render(request,'home.html',context=my_dict)
    if(request.POST.get('submit')):
        name=request.POST.get('submit')
        hotelname=name
        return view(request)
    restaurant_list = Restaurant.objects.order_by('hotelname')
    my_dict={'restaurant':restaurant_list}
    return render(request,'home.html',context=my_dict)

def view(request):
    global id
    restaurant_list = Restaurant.objects.order_by('hotelname')
    for value in restaurant_list:
        if (str(value.hotelname) == str(hotelname)):
            global hotel_id
            hotel_id=value.hotelname
            id=value.id
            my_dict = {'restaurant':value}
            return render(request,'view.html',context=my_dict)

def views(request):
    return viewreview(request)

def reserve(request):
    if(request.POST.get('submitt')):
        n_name=request.POST.get('name')
        n_phone=request.POST.get('phone')
        n_people=request.POST.get('npeople')
        n_date=request.POST.get('date')
        n_time=request.POST.get('time')
        n_message=request.POST.get('message')
        usr=Reservation.objects.get_or_create(hotelname=hotel_id,name=n_name,phone=n_phone,numberPeople=n_people ,date=n_date ,time=n_time ,message=n_message)[0]
        usr.save()
        return view(request)
    return render(request,'reserve.html')

def review(request):
    if(request.POST.get('submitt')):
        n_email=request.POST.get('email')
        n_food=request.POST.get('food')
        n_ambience=request.POST.get('ambience')
        n_hospitality=request.POST.get('hospitality')
        n_rating=request.POST.get('rating')
        n_review=request.POST.get('review')
        usr=Review.objects.get_or_create(hotelname=hotel_id,email=n_email,food=n_food,ambience=n_ambience ,hospitality=n_hospitality ,rating=n_rating ,review=n_review)[0]
        usr.save()
        return view(request)
    return render(request,'review.html')

def owner(response):
    global id
    restaurant_list = Restaurant.objects.order_by('hotelname')
    for value in restaurant_list:
        if (str(value.hotelname) == str(hotelname)):
            global hotel_id
            hotel_id=value.hotelname
            id=value.id
    reserve = Reservation.objects.filter(hotelname=str(id))
    my_dict = {'review':reserve}
    return render(response,'owner.html',context=my_dict)

def hotel(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        users=Owner.objects.order_by('email')
        for value in users:
            print(value.email,value.password)
            if str(value.email)== str(email) and str(value.password) == str(password):
                global hotelname
                hotelname=value.hotelname
                return owner(request)
        my_dict={'heading':'Wrong Email or Password'}
        return render(request,'hotel.html',context=my_dict)
    return render(request,'hotel.html')

def viewreview(response):
    restaurant_list = Review.objects.filter(hotelname=str(id))
    my_dict = {'review':restaurant_list}
    return render(response,'viewreview.html',context=my_dict)
