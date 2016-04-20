from django.contrib import admin
from .models import TalkList
from .models import Talk


# Register your models here.
admin.site.register(TalkList)
admin.site.register(Talk)