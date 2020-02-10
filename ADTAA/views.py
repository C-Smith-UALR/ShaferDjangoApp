from django.shortcuts import render

from django.http import HttpResponse

UALRclasses = [
    {
        'title': 'Programming I',
        'courseNo': '1375',
        'meetingTime': '1630 - 1745',
        'disciplines': ['Programming - C++', 'Programming Languages']
    },
    {
        'title': 'Artificial Intelligence',
        'courseNo': '4383',
        'meetingTime': '1215 - 1330',
        'disciplines': ['Programming - Python', 'Artificial Intelligence']
    }
]

def assistant(request):
    context = {
        'UALRclasses': UALRclasses
    }
    return render(request, 'ADTAA/assistant.html', context)
    # return render(request, 'ADTAA/assistant.html', context, {'title': 'ADTAA'})
    # return HttpResponse('<h1>This is the ADTAA</h1>')
