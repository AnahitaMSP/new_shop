from django.shortcuts import  redirect 
from django.urls import reverse_lazy
from django.views.generic import UpdateView,ListView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserType
from dashboard.permissions import HasAdminAccessPermission
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from dashboard.admin.forms import AdminPasswordChangeForm,AdminProfileEditForm
from accounts.models import Profile
from django.core.exceptions import FieldError
from django.contrib import messages
from shop.models import ProductModel,ProductStatusType , ProductCategoryModel
from dashboard.admin.forms import *


class AdminProductListView(LoginRequiredMixin,HasAdminAccessPermission,ListView):
    template_name = "dashboard/admin/products/product-list.html"
    paginate_by=10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size',self.paginate_by)
        
    def get_queryset(self):
        queryset=ProductModel.objects.all()
        if search_q:=self.request.GET.get('q'):
            queryset=queryset.filter(title__icontains=search_q)
        if category_id :=self.request.GET.get("category_id"):
            queryset = queryset.filter(category__id=category_id)
        if min_price:=self.request.GET.get("min_price"):
            queryset=queryset.filter(price__gte=min_price)
        if max_price:=self.request.GET.get("max_price"):
            queryset=queryset.filter(price__lte=max_price)
        if order_by:=self.request.GET.get("order_by"):
            try:
                queryset=queryset.order_by(order_by)
            except FieldError :
                pass
        return queryset

    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        context["total_item"] = self.get_queryset().count()
        context["categories"] = ProductCategoryModel.objects.all()
        self.request.session['fav_color'] = 'blue'


        return context

class AdminProductEdittView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    queryset = ProductModel.objects.all()
    template_name = "dashboard/admin/products/product-edit.html"
    form_class=ProductForm

    success_message='ویرایش محصول انجام شد'

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:product-edit",kwargs={'pk':self.get_object().pk})

class AdminProductDeleteView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin,DeleteView):
    success_message='محصول با موفقیت حذف شد'
    template_name = "dashboard/admin/products/product-delete.html"
    success_url=reverse_lazy("dashboard:admin:product-list")

    queryset = ProductModel.objects.all()

class AdminProductCreateView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, CreateView):
    queryset = ProductModel.objects.all()
    template_name = "dashboard/admin/products/product-create.html"
    form_class = ProductForm
    success_message = 'ایجاد محصول انجام شد'

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)  # Call super to save the form and set self.object
        return redirect(reverse_lazy("dashboard:admin:product-edit",kwargs={'pk':form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:product-edit", kwargs={'pk': self.object.pk})  # Use self.object



