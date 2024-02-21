from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CategoryList, CategoryDetail, SubCategoryList, SubCategoryDetail, ItemList, ItemDetail

# router = SimpleRouter()
# router.register(r'categories', CategoryList, basename='category')
# router.register(r'subcategories', SubCategoryList, basename='subcategory')
# router.register(r'items', ItemList, basename='item')

urlpatterns = [
    # path('', include(router.urls)),
    path('categories/', CategoryList.as_view(), name='category'),
    path('subcategories/', SubCategoryList.as_view(), name='subcategory'),
    path('items/', ItemList.as_view(), name='item'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('subcategories/<int:pk>/', SubCategoryDetail.as_view(), name='subcategory-detail'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]
