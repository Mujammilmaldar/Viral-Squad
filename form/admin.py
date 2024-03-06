from django.contrib import admin
from .models import TextData, DocumentData

class TextDataAdmin(admin.ModelAdmin):
    # Customize the display of TextData model in the admin interface
    list_display = ('name', 'dob', 'CollegeName', 'BranchOfStudy', 'email')
    list_filter = ('CollegeName', 'BranchOfStudy')
    search_fields = ('name', 'email')

class DocumentDataAdmin(admin.ModelAdmin):
    # Customize the display of DocumentData model in the admin interface
    list_display = ('text_data', 'photo', 'aadhar_card', 'achievement_file')
    list_filter = ('text_data',)
    search_fields = ('text_data__name', 'text_data__email')

# Register your models with the admin site
admin.site.register(TextData, TextDataAdmin)
admin.site.register(DocumentData, DocumentDataAdmin)
