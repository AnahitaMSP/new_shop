from django.shortcuts import render , redirect 
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserType


class AdminDashboardHomeView(LoginRequiredMixin,TemplateView):
    template_name="dashboard/admin/home.html"

