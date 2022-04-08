from django.contrib import admin
from .models import Payment, Order, OrderProduct
# Register your models here.


class OrderEventInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'event', 'quantity', 'event_price', 'ordered')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'roll_number', 'date_of_birth', 'college', 'Department', 'year', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderEventInline]

class PaymentAdmin(admin.ModelAdmin):

    list_display = ('user','payment_id','amount_paid','status')

admin.site.register(Payment,PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
