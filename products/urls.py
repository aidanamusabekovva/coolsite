
from django.urls import path
from products import views

#from django.urls import path
# from products.views import index, about,count_age, find_name
    # path('index/<int:age>/',views.index),
    # path('category/', views.about),
    # path("count_age/<int:age>/", views.count_age),
    # path("find-name/<str:name>/", views.find_name),



from django.urls import path
from products import views

urlpatterns = [
    path("index/", views.index),
    path("about/", views.about),
    path("animal/", views.animal, name="animal"),
    path("animal/<str:animal_name>/", views.detail_animal),
    path("delete-animal/<int:animal_id>", views.delete_animal),
    path("delete-animal-by-name/<str:animal_name/", views.delete_animal_by_name),
    path('add-animal/', views.create_animal),
    path("edit-animal/<int:animal_id>", views.edit_animal)
]
# from django.urls import path
# from products import views
#
# urlpatterns = [
#     path("index/", views.index),
# ]
# index главная страница
# post delete

#
# urlpatterns1 = [
#     path("index/<int:user_id>/<str:name>/", views.index)
# ]