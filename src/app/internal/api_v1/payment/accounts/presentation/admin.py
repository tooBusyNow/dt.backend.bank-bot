from django.contrib import admin

from app.internal.api_v1.payment.accounts.db.models import Account


@admin.register(Account)
class PaymentAccountAdmin(admin.ModelAdmin):
    pass
