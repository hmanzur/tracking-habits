from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    icon_name = 'accessibility'

    list_display = 'title', 'end_at', 'finished_at', 'get_status'

    search_fields = 'title', 'description'

    def get_status(self, habit):
        """ Get habit status with html icon """

        html = u'<i class="material-icons {}-text">{}</i>{}'
        current, icon, color, text = timezone.now(), 'assignment_turned_in', 'green', 'Success'

        if (not habit.finished_at and current > habit.end_at) or \
           (habit.finished_at and habit.finished_at > habit.end_at):

            icon, color, text = 'assignment_late', 'red', 'Failed'

        return format_html(html.format(color, icon, text))
    get_status.short_description = 'Status'
    get_status.allow_tags  = True
    
