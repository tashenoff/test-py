# from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader
from bboard.models import Bb
from bboard.models import Rubric
from django.http import JsonResponse


def rubricsJson(request):
    rubrics = Rubric.objects.all()
    data = list(rubrics.values())
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)