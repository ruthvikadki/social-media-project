from typing import Any

from django.views import generic
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import read_json_data, generate_count_analytics

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class AnalyticsView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:        
        context_data = super().get_context_data(**kwargs)
        context_data["analytics"] = generate_count_analytics()
        
        page = self.request.GET.get('page', 1)
        paginator = Paginator(read_json_data().get("posts"), 10)
        try:
            post_data = paginator.page(page)
        except PageNotAnInteger:
            post_data = paginator.page(1)
        except EmptyPage:
            post_data = paginator.page(paginator.num_pages)
        
        context_data["post_data"] = post_data        
        return context_data


class AnalyticsAPIView(View):
    def get(self, request, *args, **kwargs):
        analytics_data = generate_count_analytics()
        return JsonResponse(analytics_data)
