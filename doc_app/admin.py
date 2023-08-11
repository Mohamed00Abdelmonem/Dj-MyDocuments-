from django.contrib import admin
from .models import detail_subject, Subject, Section


admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(detail_subject)