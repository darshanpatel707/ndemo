from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
# Create your views here.
def home(request):
    all_hotdeal = Hotdeal.objects.all()
    return render(request,'website/index.html', {'hotdeal': all_hotdeal})

def contact(request):
    if request.method == 'POST':
        name_c = request.POST.get('name')
        email_c = request.POST.get('email')
        mobile_c = request.POST.get('mobile')
        message_c= request.POST.get('message')

        query = Contact(name=name_c,email=email_c,mobile_num=mobile_c,message=message_c)
        query.save()
        return render(request,'website/thank.html')
    else:
        return render(request,'website/contact.html')

def booking(request):
    return render(request,'website/booking.html')

def domestic(request):
    all_domestic = Domestic.objects.all()
    return render(request, 'website/domestic.html', {'domestic': all_domestic})

def international(request):
    all_international = International_package.objects.all()
    return render(request, 'website/international.html', {'international': all_international})
def flight(request):
    if request.method == 'POST':
        name_f = request.POST.get('name').capitalize()
        email_f = request.POST.get('email')
        mobile_f = request.POST.get('mobile')
        depart_f = request.POST.get('d-date')
        return_f = request.POST.get('r-date')
        from_f = request.POST.get('from')
        to_f = request.POST.get('to')
        adult_f = request.POST.get('adult')
        child_f = request.POST.get('child')
        query = FlightInquiry(name=name_f,email=email_f,mobile=mobile_f,depart=depart_f,r_date=return_f,from_city=from_f,to_city=to_f,adult=adult_f,child=child_f)
        query.save()
        return render(request, 'website/thank.html', {'name': name_f})
    else:
        return render(request, 'website/flight.html')

def hotel(request):
    if request.method == 'POST':
        name_h = request.POST.get('name').capitalize()
        email_h = request.POST.get('email')
        mobile_h = request.POST.get('mobile')
        check_in = request.POST.get('in-date')
        check_out = request.POST.get('out-date')
        city_h = request.POST.get('city')
        adult_h = request.POST.get('adult')
        child_h = request.POST.get('child')
        query = HotelInquiry(name=name_h,email=email_h,mobile=mobile_h,check_in=check_in,check_out=check_out,city=city_h,adult=adult_h,child=child_h)
        query.save()
        return render(request, 'website/thank.html', {'name': name_h})
    else:
        return render(request, 'website/hotel.html')

# train
def train(request):
    if request.method == 'POST':
        name_f = request.POST.get('name').capitalize()
        email_f = request.POST.get('email')
        mobile_f = request.POST.get('mobile')
        depart_f = request.POST.get('d-date')
        return_f = request.POST.get('r-date')
        from_f = request.POST.get('from')
        to_f = request.POST.get('to')
        adult_f = request.POST.get('adult')
        child_f = request.POST.get('child')
        query = TrainInquiry(name=name_f,email=email_f,mobile=mobile_f,depart=depart_f,r_date=return_f,from_city=from_f,to_city=to_f,adult=adult_f,child=child_f)
        query.save()
        return render(request, 'website/thank.html', {'name': name_f})
    else:
        return render(request, 'website/train.html')
# cruise
def cruise(request):
    all_cruise = Cruise.objects.all()
    return render(request, 'website/cruise.html', {'cruise': all_cruise})

def hotdeal(request):
    all_hotdeal = Hotdeal.objects.all()
    return render(request, 'website/hotdeal.html', {'hotdeal': all_hotdeal})

def traking(request):
    all_tracking = Tracking.objects.all()
    return render(request, 'website/tracking.html', {'tracking': all_tracking})

def camping(request):
    all_camping = Camping.objects.all()
    return render(request, 'website/camping.html', {'camping': all_camping})

def visainquiry(request):
    if request.method == 'POST':
        name_v = request.POST.get('name').capitalize()
        mobile_v = request.POST.get('mobile')
        email_v = request.POST.get('email')
        course_v = request.POST.get('course')
        country_v = request.POST.get('country')
        query1 = VisaInquiry(visa_name=name_v, visa_mobile=mobile_v,visa_email=email_v,visa_course=course_v,visa_country=country_v)
        query1.save()
        return render(request, 'website/thank.html', {'name': name_v})
    else:
        return render(request, 'website/index.html')

def passportinquiry(request):
    if request.method == 'POST':
        name_p = request.POST.get('name').capitalize()
        mobile_p = request.POST.get('mobile')
        email_p = request.POST.get('email')
        query = Passport(p_name=name_p, p_mobile=mobile_p,p_email=email_p)
        query.save()
        return render(request, 'website/thank.html', {'name': name_p})
    else:
        return render(request, 'website/index.html')

def domesticpackage(request):
    if request.method == 'POST':
        package_id = request.POST.get('packageid')
        obj = Domestic.objects.get(id=package_id)
        context = {
            'image': obj.package_image,
            'title': obj.package_name,
            'day': obj.package_day,
            'night': obj.package_night,
            'price': obj.package_price,
            'itinerary': obj.package_itinerary
        }
        return render(request, 'website/dpackage.html', context)
    else:
        return render(request, 'website/domestic.html')

def internationalpackage(request):
    if request.method == 'POST':
        package_id = request.POST.get('packageid')
        obj =  International_package.objects.get(id=package_id)
        context = {
            'image': obj.package_image,
            'title': obj.package_name,
            'day': obj.package_day,
            'night': obj.package_night,
            'price': obj.package_price,
            'itinerary': obj.package_itinerary
        }
        return render(request, 'website/ipackage.html', context)
    else:
        return render(request, 'website/index.html')
def cruisepackage(request):
    if request.method == 'POST':
        package_id = request.POST.get('packageid')
        obj = Cruise.objects.get(id=package_id)
        context = {
            'image': obj.package_image,
            'title': obj.package_name,
            'day': obj.package_day,
            'night': obj.package_night,
            'price': obj.package_price,
            'itinerary': obj.package_itinerary
        }
        return render(request, 'website/dpackage.html', context)
    else:
        return render(request, 'website/index.html')

def treckingpackage(request):
    if request.method == 'POST':
        package_id = request.POST.get('packageid')
        obj = Tracking.objects.get(id=package_id)
        context = {
            'image': obj.package_image,
            'title': obj.package_name,
            'day': obj.package_day,
            'night': obj.package_night,
            'price': obj.package_price,
            'itinerary': obj.package_itinerary
        }
        return render(request, 'website/dpackage.html', context)
    else:
        return render(request, 'website/index.html')
def campingpackage(request):
    if request.method == 'POST':
        package_id = request.POST.get('packageid')
        obj = Camping.objects.get(id=package_id)
        context = {
            'image': obj.package_image,
            'title': obj.package_name,
            'day': obj.package_day,
            'night': obj.package_night,
            'price': obj.package_price,
            'itinerary': obj.package_itinerary
        }
        return render(request, 'website/dpackage.html', context)
    else:
        return render(request, 'website/index.html')
