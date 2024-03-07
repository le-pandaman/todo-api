from django.contrib import admin

from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            None,
            {'fields': [
                'task',
                'is_done',
            ],
            }
        ),
    ]

    list_display = ['task', 'is_done',  'date', 'completed']

    list_filter = ['task', 'is_done', 'date']


admin.site.register(Todo, TodoAdmin)
