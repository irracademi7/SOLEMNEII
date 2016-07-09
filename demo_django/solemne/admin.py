from __future__ import unicode_literals

from django.db import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','sort_order','status','created_at','updated_at')
    # list_filter = ('owner','active')
    # list_search = ('name',)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','sku','price','category','status','created_at','updated_at',)    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)