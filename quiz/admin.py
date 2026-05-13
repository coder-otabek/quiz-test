from django.contrib import admin
from django.db import models
from .models import QuizData


@admin.register(QuizData)
class QuizDataAdmin(admin.ModelAdmin):
    list_display = ('title',)

    # Matn maydonini (TextField) admin panelda kattaroq ko'rsatish
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 25, 'cols': 120})},
    }

    # Bazada faqat bitta yozuv bo'lishini ta'minlash
    def has_add_permission(self, request):
        if QuizData.objects.count() >= 1:
            return False  # Bir marta yaratilgandan keyin "Add" tugmasi yo'qoladi
        return True