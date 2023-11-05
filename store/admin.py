from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models.product import Products, Color, CMD
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class CMDResource(resources.ModelResource):
    class Meta:
        model = CMD
        fields = ('command',)

@admin.register(CMD)
class CMDAdmin(ImportExportModelAdmin):
    resource_class = CMDResource
    list_display = ('command', )

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', )

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)


# username = Tanushree, email = tanushree7252@gmail.com, password = 1234
