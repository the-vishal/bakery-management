from rest_framework import serializers
from .models import Ingredient, IngredientRatio, BakeryItem

class IngredientRatioSerializer(serializers.Serializer):
    class Meta:
        model = IngredientRatio
        fields = ('id','ingredient','quantity',)

class IngredientSerializer(serializers.Serializer):
    class Meta:
        model = Ingredient
        fields = ('id','name',)


class BakeryItemSerializer(serializers.Serializer):
    class Meta:
        model = BakeryItem
        fields = ('id','name','ingredients','cost_price','selling_price',)

    def get_ingredients(self, obj):
        print("--------here ---------------")
        qset = IngredientRatio.objects.filter(ingredient=obj)
        return [IngredientRatioSerializer(m).data for m in qset]
