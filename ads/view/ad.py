import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):
    @staticmethod
    def get(request):
        ads = Ad.objects.all()

        response = []
        for ad in ads:
            response.append(
                {
                    "id": ad.id,
                    "name": ad.name,
                    "author": ad.author,
                    "price": ad.price,
                    "description": ad.description,
                    "address": ad.address,
                    "is_published": ad.is_published,
                }
            )
        return JsonResponse(response, safe=False)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(**data)
        return JsonResponse({
            "id": new_ad.id,
            "name": new_ad.name,
            "author": new_ad.author,
            "price": new_ad.price,
            "description": new_ad.description,
            "address": new_ad.address,
            "is_published": new_ad.is_published,
        })


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()

        except:
            return JsonResponse({"error": "Not found"})
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        })