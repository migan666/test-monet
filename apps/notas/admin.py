from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class AdminStudent(admin.ModelAdmin):
    list_display=("name","last_name")
    search_fields=("name",)

admin.site.register(Student,AdminStudent)

class AdminQuestion(admin.ModelAdmin):
    list_display=("test","name","answer_correct","points")
    search_fields=("name",)

admin.site.register(Question,AdminQuestion)

class AdminAnswer(admin.ModelAdmin):
    list_display=("user","question","name","is_correct","points")
    search_fields=("name",)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(Answer,AdminAnswer)

class AdminTest(admin.ModelAdmin):
    list_display=("name",)
    search_fields=("name",)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
admin.site.register(Test,AdminTest)

class UserAdmin(BaseUserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(id=request.user.id)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
