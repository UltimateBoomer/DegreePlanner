from django.http.response import JsonResponse

def listCourses(request):
    return JsonResponse({'courses': []})
