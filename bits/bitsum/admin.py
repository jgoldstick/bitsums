from django.contrib import admin
from .models import BitSum


class BitSumAdmin(admin.ModelAdmin):
    pass
admin.site.register(BitSum, BitSumAdmin)
