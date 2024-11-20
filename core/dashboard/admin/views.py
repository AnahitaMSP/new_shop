from django.shortcuts import render , redirect 
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserType
from dashboard.permissions import HasAdminAccessPermission
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from dashboard.admin.forms import AdminPasswordChangeForm

class AdminDashboardHomeView(LoginRequiredMixin,HasAdminAccessPermission,TemplateView):
    template_name="dashboard/admin/home.html"

class AdminSecurityEditView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin,auth_views.PasswordChangeView):
    template_name="dashboard/admin/profile/security-edit.html"
    form_class=AdminPasswordChangeForm
    success_url=reverse_lazy("dashboard:admin:security-edit")
    success_message="بروز رسانی پسوورد با موفقیت انجام شد"
