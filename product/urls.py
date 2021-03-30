from django.urls import path
from product.views import product_list, dashboard, save_product, edit_product, delete_product

app_name = "product"

urlpatterns = [
    path("product-list/", product_list, name="product_list"),
    path("dashboard/", dashboard, name="dashboard"),
    path("save-product/", save_product, name="save_product"),
    path("edit-product/<int:id>/", edit_product, name="edit_product"),
    path("delete-product/<int:id>/", delete_product, name="delete_product"),
]

"""
    localhost:8000/service/
"""