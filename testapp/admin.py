from django.contrib import admin
from testapp.models import Q,Java
# Register your models here.

class QAdmin(admin.ModelAdmin):
    list_display=['Qta1','op1','op2','op3','op4']
admin.site.register(Q,QAdmin)

class JavaAdmin(admin.ModelAdmin):
    list_display=['Qta1','op1','op2','op3','op4']
admin.site.register(Java,JavaAdmin)

