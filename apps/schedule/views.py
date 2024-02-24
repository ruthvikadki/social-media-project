from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import SchedulePost
from .forms import SchedulePostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class SchedulePostListView(LoginRequiredMixin, generic.ListView):
    template_name = 'pages/schedule-page.html'
    login_url = 'user:login'
    queryset = SchedulePost.objects.all()
    context_object_name = 'schedule_post'
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(username=self.request.user)

class SchedulePostCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = SchedulePostCreateForm
    template_name = 'pages/schedule-post-create.html'
    login_url = "user:login" 
    success_url = reverse_lazy("schedule:schedule_page")

    def form_valid(self, form):
        self.object=form.save(user=self.request.user)
        super().form_valid
        return HttpResponseRedirect(self.get_success_url())

class SchedulePostDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'pages/schedule-content-detail.html'
    login_url = "user:login"
    pk_url_kwarg = 'id'
    queryset = SchedulePost.objects.all()

    


