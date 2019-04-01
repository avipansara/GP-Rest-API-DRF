from django.urls import path, include
from api import views

urlpatterns = [

  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/
  # Method      : POST 
  # { "name"    : "Recipe 1", "user_id" : 1 }
  # Description : create a recipe
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/
  # Method      : GET 
  # Description : retrieve all recipes
  # <------------------------------------------------->
  path('recipes/', views.ListCreateRecipe.as_view(), name='recipe_list'),

  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1 <-- Recipe ID
  # Method      : GET 
  # Description : get individual recipe by their id
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1
  # Method      : PUT/PATCH 
  # { "name"    : "Recipe 2" }
  # Description : Edit recipe name
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1
  # Method      : DELETE 
  # Description : delete recipe
  # <------------------------------------------------->
  path('recipes/<int:pk>/', views.RetrieveUpdateDestroyRecipe.as_view(), name='recipe_detail'),

  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1/step/
  # Method      : POST 
  # {"step_text": "step_name" }
  # Description : create steps/ for recipe/1
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1/step/
  # Method      : GET
  # Description : retrieve all steps related to recipe/1
  # <------------------------------------------------->
  # Endpoint    : 127.0.0.1:8000/api/recipes/1/step/1
  # Method      : PUT/PATCH
  # Description : Update step/1 related to recipes/1/
  # <------------------------------------------------->
  # Endpoint    : 127.0.0.1:8000/api/recipes/1/step/1
  # Method      : DELETE
  # Description : DELETE step/1 related to recipes/1/
  # <------------------------------------------------->
  path('recipes/<int:pk>/step/', views.ListCreateStep.as_view(), name='step_list'),
  path('recipes/<int:recipe_id>/step/<int:pk>/', views.RetrieveUpdateDestroyStep.as_view(), name='step_detail'),

  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1/ingredient/
  # Method      : POST 
  # {"ingredient_text": "ingredient"}
  # Description : create ingredient/ for recipe/1
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1/ingredient/
  # Method      : GET
  # Description : retrieve all ingredients related to recipe/1
  # <------------------------------------------------->
  # Endpoint    : 127.0.0.1:8000/api/recipes/1/ingredient/1
  # Method      : PUT/PATCH
  # Description : Update ingredient/1 related to recipe/1/
  # <------------------------------------------------->
  # Endpoint    : 127.0.0.1:8000/api/recipes/1/ingredient/1
  # Method      : DELETE
  # Description : DELETE ingredient/1 related to recipe/1/
  # <------------------------------------------------->
  path('recipes/<int:pk>/ingredient/', views.ListCreateIngredient.as_view(), name='ingredient_list'),
  path('recipes/<int:recipe_id>/ingredient/<int:pk>/', views.RetrieveUpdateDestroyIngredient.as_view(), name='ingredient_detail'),
  
  
 # recipes belongs to the current user
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/user/1/
  # Method      : GET
  # Description : retrieve all Recipes belong to the current User
  # <------------------------------------------------->
  path('recipes/user/<int:pk>/', views.UserRecipeList.as_view(), name='user_list'),
]