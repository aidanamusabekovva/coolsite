from django.contrib import admin
from women.models import Women, Category


from django.contrib import admin
from women.models import Women, Category


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'age')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'bio')
    list_filter = ('nationality',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
