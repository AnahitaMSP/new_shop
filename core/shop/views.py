from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DeleteView
from . models import ProductModel,ProductStatusType
# Create your views here.
class ShopProductGridView(ListView):
    template_name = "shop/product_grid.html"
    queryset=ProductModel.objects.filter(status=ProductStatusType.publish.value)
    paginate_by=9
    
    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        context["total_item"] = self.get_queryset().count()

        return context