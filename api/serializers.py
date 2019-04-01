from rest_framework import serializers
from api.models import Recipe, Step, Ingredient

class StepSerializer(serializers.ModelSerializer):
  class Meta:
    model = Step
    fields= ('id', 'recipe', 'step_text',)

    read_only_fields = ['recipe']

class IngredientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingredient
    fields= ('id', 'recipe', 'ingredient_text',)

    read_only_fields = ['recipe']

class RecipeSerializer(serializers.ModelSerializer):
  step = StepSerializer(many=True, read_only=True)
  ingredient = IngredientSerializer(many=True, read_only=True)

  class Meta:
    model = Recipe
    fields= ('id', 'user', 'name', 'step', 'ingredient',)
    
    read_only_fields = ['user']