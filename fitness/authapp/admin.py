from django.contrib import admin
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment,Attendance

# Register your models here.

admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Enrollment)
admin.site.register(Attendance)

