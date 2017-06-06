#coding=utf-8
from django.contrib import admin

from root.forms import RoomModelForm, StaffModelForm
from root.models import Room, Staff, Order
from django.core.exceptions import PermissionDenied
# Register your models here.

def change_use(modeladmin, request, queryset):
    queryset.update(is_use = False)

change_use.short_description = '房间全部可用'


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'name', 'type', 'show_use')
    # search_fields = ('is_use',)
    list_filter = ('type',)
    # date_hierarchy = 'time_use'
    ordering = ('id',)
    actions = [change_use]
    change_form = RoomModelForm

    def get_form(self, request, obj=None, **kwargs):
        return self.change_form


class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_number', 'name', 'gender', 'age', 'status', 'join_time')
    # search_fields = ('is_use',)
    list_filter = ('staff_number',)
    # date_hierarchy = 'time_use'
    ordering = ('id',)
    actions = [change_use]
    change_form = StaffModelForm

    # def get_form(self, request, obj=None, **kwargs):
    #     return self.change_form

class OrderAdmin(admin.ModelAdmin):
    change_list_template =  'change_list.html'
    list_display = ('room_number', 'fee', 'finish_time')
    list_display_links = None
    # search_fields = ('is_use',)
    list_filter = ('finish_time',)
    # date_hierarchy = 'time_use'
    ordering = ('id',)
    actions = None

    # def has_add_permission(self, request):
    #     return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return PermissionDenied

    # def has_change_permission(self, request, obj=None):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False



admin.site.register(Room, RoomAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Order, OrderAdmin)