from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mobile_num = models.CharField(max_length=15)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.email
# flight model
class FlightInquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    mobile = models.CharField(max_length=12)
    depart = models.DateField()
    r_date = models.DateField()
    from_city = models.CharField(max_length=20)
    to_city = models.CharField(max_length=20)
    adult = models.IntegerField()
    child = models.IntegerField()

    def __str__(self):
        return self.name

# hotel model
class HotelInquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    mobile = models.CharField(max_length=12)
    check_in = models.DateField()
    check_out = models.DateField()
    city = models.CharField(max_length=20)
    adult = models.IntegerField()
    child = models.IntegerField()

    def __str__(self):
        return self.name

# train model
class TrainInquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    mobile = models.CharField(max_length=12)
    depart = models.DateField()
    r_date = models.DateField()
    from_city = models.CharField(max_length=20)
    to_city = models.CharField(max_length=20)
    adult = models.IntegerField()
    child = models.IntegerField()

    def __str__(self):
        return self.name
# domestic model
class Domestic(models.Model):
    package_name = models.CharField(max_length=250)
    package_image = models.ImageField(upload_to='website/media')
    package_day = models.IntegerField(blank=True, null=True)
    package_night = models.IntegerField(blank=True, null=True)
    package_price = models.IntegerField(blank=True, null=True)
    package_category = models.CharField(max_length=60)
    package_itinerary = models.FileField(upload_to='website/itinerary', default='website/itinerary/newbalaji.pdf')

    def __str__(self):
        return self.package_name

class International_package(models.Model):
    package_name = models.CharField(max_length=250)
    package_image = models.ImageField(upload_to='website/media')
    package_day = models.IntegerField(blank=True, null=True)
    package_night = models.IntegerField(blank=True, null=True)
    package_price = models.IntegerField(blank=True, null=True)
    package_category = models.CharField(max_length=60)
    package_itinerary = models.FileField(upload_to='website/itinerary', default='website/itinerary/newbalaji.pdf')

    def __str__(self):
        return self.package_name

class Cruise(models.Model):
    package_name = models.CharField(max_length=250)
    package_image = models.ImageField(upload_to='website/media')
    package_day = models.IntegerField(blank=True, null=True)
    package_night = models.IntegerField(blank=True, null=True)
    package_price = models.IntegerField(blank=True, null=True)
    package_category = models.CharField(max_length=60)
    package_itinerary = models.FileField(upload_to='website/itinerary', default='website/itinerary/newbalaji.pdf')

    def __str__(self):
        return self.package_name

class Hotdeal(models.Model):
    package_name = models.CharField(max_length=250)
    package_image = models.ImageField(upload_to='website/media')
    package_day = models.IntegerField(blank=True, null=True)
    package_night = models.IntegerField(blank=True, null=True)
    package_price = models.IntegerField(blank=True, null=True)
    package_category = models.CharField(max_length=60)
    package_itinerary = models.FileField(upload_to='website/itinerary', default='website/itinerary/newbalaji.pdf')

    def __str__(self):
        return self.package_name

class Tracking(models.Model):
    package_name = models.CharField(max_length=250)
    package_image = models.ImageField(upload_to='website/media')
    package_day = models.IntegerField(blank=True, null=True)
    package_night = models.IntegerField(blank=True, null=True)
    package_price = models.IntegerField(blank=True, null=True)
    package_category = models.CharField(max_length=60)
    package_itinerary = models.FileField(upload_to='website/itinerary', default='website/itinerary/newbalaji.pdf')

    def __str__(self):
        return self.package_name

class Camping(models.Model):
    package_name = models.CharField(max_length=250)
    package_image = models.ImageField(upload_to='website/media')
    package_day = models.IntegerField(blank=True, null=True)
    package_night = models.IntegerField(blank=True, null=True)
    package_price = models.IntegerField(blank=True, null=True)
    package_category = models.CharField(max_length=60)
    package_itinerary = models.FileField(upload_to='website/itinerary', default='website/itinerary/newbalaji.pdf')

    def __str__(self):
        return self.package_name

class VisaInquiry(models.Model):
    visa_name = models.CharField(max_length=30)
    visa_mobile = models.IntegerField(blank=True, null=True)
    visa_email = models.EmailField(max_length=20)
    visa_course = models.CharField(max_length=60)
    visa_country = models.CharField(max_length=60)

    def __str__(self):
        return self.visa_name

class Passport(models.Model):
    p_name = models.CharField(max_length=60)
    p_mobile = models.IntegerField(blank=True, null=True)
    p_email = models.EmailField(max_length=20)

    def __str__(self):
        return self.p_name
