from django.shortcuts import render,get_object_or_404
from Job.models import Job,JobApplication
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'website/home.html')


def job_listing(request):
    jobs = Job.objects.filter(is_available=True)
    context = {'jobs':jobs}
    return render(request,'website/job_listing.html',context)

#------------JOB-DETAILS-------

def job_details(request, pk):
    job = get_object_or_404(Job, pk=pk)
    applied = JobApplication.objects.filter(job=job, email=request.user).exists()
    context = {'job': job, 'applied': applied}
    return render(request, 'website/job_details.html', context)

