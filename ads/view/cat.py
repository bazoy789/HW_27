import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):
    @staticmethod
    def get(request):
        cats = Category.objects.all()

        response = []
        for cat in cats:
            response.append(
                {
                    "id": cat.id,
                    "name": cat.name
                }
            )
        return JsonResponse(response, safe=False)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        new_cats = Category.objects.create(**data)
        return JsonResponse({"id": new_cats.id, "name": new_cats.name})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            cats = self.get_object()
        except:
            return JsonResponse({"error": "Not found"})
        return JsonResponse({"id": cats.id, "name": cats.name})