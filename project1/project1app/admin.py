from django.contrib import admin
from project1app.models import Client,Owner,Restaurant,Review,Reservation,Contact
# Register your models here.

admin.site.register(Client)
admin.site.register(Owner)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Reservation)
admin.site.register(Contact)
