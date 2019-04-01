from rest_framework import generics
from rest_framework import serializers
from api.serializers import RecipeSerializer, StepSerializer, IngredientSerializer
from api.models import Recipe, Step, Ingredient
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

# GET Current User Recipes
class UserRecipeList(generics.ListAPIView):
  serializer_class = RecipeSerializer
  queryset = Recipe.objects.all()

  def get_queryset(self):
    try:
        user = User.objects.get(id=self.kwargs.get('pk'))
    except Exception as e:
        raise serializers.ValidationError({'error':'User is not found in the database'})

    return self.queryset.filter(user=user)

# Add Recipe
class ListCreateRecipe(generics.ListCreateAPIView):
  serializer_class = RecipeSerializer
  queryset = Recipe.objects.all()

  def perform_create(self, serializer):
    try:
      user = User.objects.get(id=self.request.data['user_id'])
      serializer.save(user=user)
    except Exception as e:
      raise serializers.ValidationError({'error':'User is not found in the database'})

# Update, Delete Recipe
class RetrieveUpdateDestroyRecipe(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = RecipeSerializer
  queryset = Recipe.objects.all()

# Add Steps
class ListCreateStep(generics.ListCreateAPIView):
  serializer_class = StepSerializer
  queryset = Step.objects.all()

  def get_queryset(self):
    return self.queryset.filter(recipe_id=self.kwargs.get('pk'))
    
  def perform_create(self, serializer):
    recipe = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))
    serializer.save(recipe=recipe)

# Update, Delete Step
class RetrieveUpdateDestroyStep(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = StepSerializer
  queryset = Step.objects.all()

  def get_queryset(self):
    return self.queryset.filter(recipe_id=self.kwargs.get('recipe_id'))

# Add Ingredients
class ListCreateIngredient(generics.ListCreateAPIView):
  serializer_class = IngredientSerializer
  queryset = Ingredient.objects.all()

  def get_queryset(self):
    return self.queryset.filter(recipe_id=self.kwargs.get('pk'))
  
  def perform_create(self, serializer):
    recipe = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))
    serializer.save(recipe=recipe)

# Update, Delete Ingredient
class RetrieveUpdateDestroyIngredient(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = IngredientSerializer
  queryset = Ingredient.objects.all()

  def get_queryset(self):
    return self.queryset.filter(recipe_id=self.kwargs.get('recipe_id'))