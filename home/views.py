from typing import List
from django.views import View
from django.shortcuts import render


class HomeView(View):
    def get(self, request):
        return render(request, 'home/main.html')
