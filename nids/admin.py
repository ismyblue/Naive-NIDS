from django.contrib import admin
from nids.models import *


# Register your models here.
admin.site.register(Schema)
admin.site.register(Event)
admin.site.register(Signature)
admin.site.register(Sig_reference)
admin.site.register(Reference)
admin.site.register(Reference_system)
admin.site.register(Sig_class)
admin.site.register(Sensor)
admin.site.register(Iphdr)
admin.site.register(Tcphdr)
admin.site.register(Udphdr)
admin.site.register(Icmphdr)
admin.site.register(Opt)
admin.site.register(Data)
admin.site.register(Encoding)
admin.site.register(Detail)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(FullEvent)
