from django.shortcuts import render , redirect 
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserType


class DashboardHomeView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.type == UserType.customer.value:
                return redirect(reverse_lazy('dashboard:customer:home'))
            elif request.user.type == UserType.admin.value:
                return redirect(reverse_lazy('dashboard:admin:home'))

        return redirect(reverse_lazy('accounts:login'))
