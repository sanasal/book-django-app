from django.contrib import admin
from .models import Mystry_and_Police, Sciences, Islam
from .models import Psychology, Programming ,Languages 
from .models import Add_Comment , Report_Issue

# Register your models here.

admin.site.register(Mystry_and_Police)
admin.site.register(Sciences)
admin.site.register(Languages)
admin.site.register(Programming)
admin.site.register(Islam)
admin.site.register(Psychology)
admin.site.register(Add_Comment)
admin.site.register(Report_Issue)