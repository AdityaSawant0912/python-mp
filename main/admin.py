from django.contrib import admin
from .models import Tutorial
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    fields = ["tutorial_title", "tutorial_content", "tutorial_published"]
    
    fieldsets = (
        ("Title", {
            "fields": (
                "tutorial_title",
            ),
        }),
        ("Content", {
            "fields": ()
        })
    )
    

admin.site.register(Tutorial) 
