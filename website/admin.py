from django.contrib import admin
from .models import Post, Created, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'deleted']
    search_fields = list_display

    def get_queryset(self, request): # SOBRESCREVENDO
        #return Post.objects.all()# MOSTRA COM TODOS OS CAMPOS (ORIGINAL)
        return Post.objects.filter(deleted=True)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    search_fields = list_display

admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Created)
