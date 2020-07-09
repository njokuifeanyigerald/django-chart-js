from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HomeModel

class Home(TemplateView):
    queryset = HomeModel
    template_name ='home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = HomeModel.objects.all()
        return context
