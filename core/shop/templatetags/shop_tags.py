from django import template
from shop.models import ProductModel,ProductStatusType

register =template.Library()

@register.inclusion_tag("includes/latest_products_main.html")
def show_latest_products():
    latest_products=ProductModel.objects.filter(status=ProductStatusType.publish.value).order_by("-created_date")[:8]
    return {"latest_products":latest_products}

@register.inclusion_tag("includes/similar_products.html")
def show_similar_products(product):
    product_categories = product.category.all()
    similar_products = ProductModel.objects.filter(
        status=ProductStatusType.publish.value,
        category__in=product_categories
    ).order_by("-created_date")[:4]

    # Debugging output
    # print(f"Product: {product.title}, Similar Products Count: {similar_products.count()}")

    return {"similar_products": similar_products}
