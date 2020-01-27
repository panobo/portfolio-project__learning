from django.shortcuts import render


def job_home(request):
    return render(request, 'jobs/job_home.html')