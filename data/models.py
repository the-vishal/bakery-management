from django.db import models
from django.core.validators import MaxValueValidator 

# Create your models here.
class Ingredient(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class BakeryItem(models.Model):
	name = models.CharField(max_length=200)
	ingredients = models.ManyToManyField(Ingredient, through='IngredientRatio')	
	cost_price = models.PositiveIntegerField()
	selling_price = models.PositiveIntegerField()

	def __str__(self):
		return self.name

class IngredientRatio(models.Model):
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
	bakeryitem = models.ForeignKey(BakeryItem, on_delete=models.CASCADE, null=True)
	quantity = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

	def __str__(self):
		return '{} : {}%'.format(self.ingredient.name, self.quantity)
	class Meta:
		db_table = "ingredient_bakeryitem_ingredients"