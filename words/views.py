from django.shortcuts import render

from .models import Word

from django.views.generic import TemplateView, View


class SearchView(TemplateView):
    template_name = "search.html"

class WordView(View):

    def post(self, request, *args, **kwargs):
        search_for = request.POST.get("search")
        return render(request, 'list.html', {"words": Word.objects.filter(word__icontains=search_for.lower())})