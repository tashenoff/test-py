from django.contrib import admin
from .models import Bb
from .models import Rubric

class BbAdmin(admin.ModelAdmin):
    list_display = ('titles', 'content', 'price', 'rubric', 'published')
    list_display_links = ('titles', 'content')
    search_fields = ('titles', 'content',)

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric, RubricAdmin)