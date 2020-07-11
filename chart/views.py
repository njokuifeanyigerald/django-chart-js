from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import HomeModel
from poll.models import PollModel
class Home(TemplateView):
    queryset = HomeModel
    template_name ='home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = HomeModel.objects.all()
        return context


class LineChart(ListView):
    queryset=  PollModel
    template_name = "linechart.html"

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(**kwargs)
        context['polls'] = PollModel.objects.all()
        return context