from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.conf import settings
from django.forms.models import model_to_dict
from .models import Ingredient, BakeryItem
from .serializers import IngredientSerializer, BakeryItemSerializer
from rest_framework import exceptions

# from django.db.models import Q

class IngredientManagerView(APIView):
	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)
	serializer_class = IngredientSerializer

	def get(self, request):
		igid = request.GET.get('id')
		ingredient = Ingredient.objects.get(id=igid)
		return Response(model_to_dict(ingredient))

	def put(self, request, format=None):
		payload = request.data
		name = payload.get('name')
		try:
			ig, already = Ingredient.objects.get_or_create(name=name)
			if not already:
				raise IngredientAlreadyAvailable
			else:
				ig.save()
				status = "success"
				message = "id:{}".format(ig.id)
				code = 200
				
		except Exception as ex:
			status = "failed"
			message = str(ex)
			code = 400
		return Response({"status":status, "message":message}, status=code)

class IngredientAlreadyAvailable(exceptions.APIException):
	default_detail = 'Ingredient Already Available'


class ItemManagerView(APIView):
	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)
	serializer_class = BakeryItemSerializer

	def get(self, request):
		item_id = request.GET.get('id')
		if item_id:
		else:
			item = BakeryItem.objects.get(id=item_id)
		resp = [
					{
						'id':i.id, 
						'name':i.name, 
						'quantity':i.quantity
					} for i in model_to_dict(item)
				]
		print(resp)
		return Response(resp)

	# def put(self, request, format=None):
	# 	payload = request.data
	# 	name = payload.get('name')
	# 	try:
	# 		ig, already = Ingredient.objects.get_or_create(name=name)
	# 		if not already:
	# 			raise IngredientAlreadyAvailable
	# 		else:
	# 			ig.save()
	# 			status = "success"
	# 			message = "id:{}".format(ig.id)
	# 			code = 200
				
	# 	except Exception as ex:
	# 		status = "failed"
	# 		message = str(ex)
	# 		code = 400
	# 	return Response({"status":status, "message":message}, status=code)

class OrderManagerView(APIView):
	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)
	serializer_class = BakeryItemSerializer

	def get(self, request):
		item_id = request.GET.get('id')
		item = BakeryItem.objects.get(id=item_id)
		resp = model_to_dict(item)
		print(resp)
		return Response(resp)