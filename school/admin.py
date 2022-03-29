from django.contrib import admin

from .models import Student, Teacher

class RelationshipInline(admin.TabularInline):
    model = Student.teacher.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        RelationshipInline,
    ]
    exclude = ('teacher',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        RelationshipInline,
    ]




