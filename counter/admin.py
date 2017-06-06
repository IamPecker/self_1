# coding=utf-8
from django.contrib import admin
from django.template.loader import get_template
from django.template import Context
from root.forms import RoomModelForm, RoomReserveModelForm
from models import RoomReserve, RoomCall, UserRoom

# Register your models here.
from root.models import RoomUseTime


class RoomReserveAdmin(admin.ModelAdmin):
    # change_list_template = 'change_list.html'
    list_display = ('room_number', 'name', 'type', 'current_use', 'reserve')
    # search_fields = ('is_use',)
    list_filter = ('type', 'current_use',)
    ordering = ('id',)

    change_form = RoomReserveModelForm
    # def has_add_permission(self, request):
    #     return False

    def get_form(self, request, obj=None, **kwargs):
        return self.change_form

    def reserve(self, obj):
        t = get_template('reserve_operation.html')
        return t.render(Context({
            'can_use': obj.current_use == 1
        }))

    reserve.short_description = u'预订'


class RoomCallAdmin(admin.ModelAdmin):
    list_display = ('room_number',  'call_time')

    def has_add_permission(self, request):
        return False


class UserRoomAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_phone', 'room_number', 'start_time', 'end_time', )

    def has_add_permission(self, request):
        return False


admin.site.register(RoomReserve, RoomReserveAdmin)
admin.site.register(RoomCall, RoomCallAdmin)
admin.site.register(UserRoom, UserRoomAdmin)
