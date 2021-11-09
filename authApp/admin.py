#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.user import User
from .models.invoice import Invoice
from .models.product import Product
from .models.sale import Sale

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Sale)