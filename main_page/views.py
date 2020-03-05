from django.shortcuts import render
from django.views import View
from .models import Feedback


class MainPage(View):
    def get(self, request):
        return render(request, 'main_page/index.html')

    def post(self, request):
        feedback = Feedback(
            name=request.POST['Name'],
            email=request.POST['Email'],
            phone=request.POST['Phone']
        )
        feedback.save()
        return render(request, 'main_page/index.html')

