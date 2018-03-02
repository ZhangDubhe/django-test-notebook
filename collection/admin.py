from django.contrib import admin

# Register your models here.
from .models import User, Question, Type, QuestionDetail, QuizLog


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User',             {'fields': ['user_name']}),
        ('User information', {'fields': ['user_email', 'user_password', 'is_admin'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'user_name', 'user_email', 'add_at', 'is_admin')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'create_at')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'question_type', 'add_at', 'update_at')


admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(QuestionDetail)
admin.site.register(QuizLog)