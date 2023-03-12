from django.http import JsonResponse


def main_view(request):
    return JsonResponse({"status": "ok"})
