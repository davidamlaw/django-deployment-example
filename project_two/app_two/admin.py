from django.contrib import admin
from app_two.models import AccessRecord, Topic, WebPage, UserProfileInfo
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
# admin.site.register(User)
admin.site.register(UserProfileInfo)
