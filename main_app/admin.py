from django.contrib import admin
from .models import Cat
from .models import People
from .models import Photo

# Register your models here.

admin.site.register(Cat)
admin.site.register(People)
admin.site.register(Photo)
