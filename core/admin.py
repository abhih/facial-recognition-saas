from django.contrib import admin

from .models import User, Membership, Payment

admin.site.register(User)
admin.site.register(Membership)
admin.site.register(Payment)
