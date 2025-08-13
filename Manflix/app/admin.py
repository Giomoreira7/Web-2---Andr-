from django.contrib import admin
from .models import *
 
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','category') #colocamos o que queremos que aparece de primeira mão no banco
    search_fields = ('title','category') # como vamo buscar os filmes
 
 
admin.site.register(Directors)
admin.site.register(Movies,MovieAdmin)
admin.site.register(Plans)