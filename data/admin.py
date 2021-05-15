from django.contrib import admin
from .models import Ingredient,IngredientRatio,BakeryItem

class IngredientRatioInline(admin.TabularInline):
    model = IngredientRatio
    extra = 2

class BakeryItemAdmin(admin.ModelAdmin):
	inlines = (IngredientRatioInline,)
	list_display = ('name', 'cost_price', 'selling_price')


admin.site.register(BakeryItem, BakeryItemAdmin)
admin.site.register(Ingredient)