from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('domestic/', views.domestic, name='domestic'),
    path('booking/flight/', views.flight, name='flight'),
    path('booking/hotel/', views.hotel, name='hotel'),
    path('booking/train/', views.train, name='train'),
    path('international/', views.international, name='international'),
    path('cruise/', views.cruise, name='cruise'),
    path('traking/', views.traking, name='tracking'),
    path('camping/', views.camping, name='camping'),
    path('visainquiry/', views.visainquiry, name='visainquiry'),
    path('passportinquiry/', views.passportinquiry, name='passportinquiry'),
    path('domestic/package/', views.domesticpackage, name='dpackage'),
    path('international/package/', views.internationalpackage, name='ipackage'),
    path('cruise/package/', views.cruisepackage, name='cpackage'),
    path('tracking/package/', views.treckingpackage, name='tpackage'),
    path('camping/package/', views.campingpackage, name='cpackage'),

]
