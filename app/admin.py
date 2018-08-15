from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Book, Issue, Return

# Register your models here.

admin.site.site_header = 'Library Management System'
# admin.site.site_title = 'Library Management System'


class UserAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'first_name', 'last_name', 'depertment_name')
    list_filter = ('depertment_name', 'semester')
    search_fields = ('roll_number', 'first_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'remaining', 'category')
    list_filter = ('category', 'author_name')
    search_fields = ('name', 'author_name')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_id', 'issue_date', 'return_date', 'fine',)
    list_filter = ('issue_date',)
    search_fields = ('issue_id',)


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Return,)
admin.site.register(Issue, IssueAdmin)

admin.site.unregister(Group,)