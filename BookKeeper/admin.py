from django.contrib import admin
from .models import Group, Bill, Person

admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Bill)
