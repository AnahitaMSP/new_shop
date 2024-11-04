from django import template
from shop.models import ProductModel,ProductStatusType

register =template.Library()

@register.inclusion_tag("includes/latest_products_main.html")
def show_latest_products():
    latest_products=ProductModel.objects.filter(status=ProductStatusType.publish.value).order_by("-created_date")[:8]
    return {"latest_products":latest_products}