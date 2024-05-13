from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .form import JobForm,JobApplicationForm
from django.contrib import messages
from .models import Job,JobApplication
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def create_job(request):
    if request.user.is_recruiter:
        if request.method =='POST':
            form = JobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.save()
                messages.info(request,'New Job has been created')
                return redirect('dashboard')
            else:
                messages.warning(request,'Something went wrong')
                return redirect('create-job')
        else:
            form = JobForm()
            context = {'form':form}
            return render(request,'job/create_job.html',context)
    else:
        messages.warning(request,'permission Denied')
        return redirect('dashboard')
    
#--------------Update Job-------
def update_job(request, job_id):
    # Retrieve the job instance from the database
    job_instance = get_object_or_404(Job, job_id=job_id)

    if request.method == 'POST':
        # Update the job instance with the submitted data
        job_instance.title = request.POST.get('title')
        job_instance.salary = request.POST.get('salary')
        job_instance.experience = request.POST.get('experience')
        job_instance.location = request.POST.get('location')
        job_instance.skills = request.POST.get('skills')
        job_instance.requirements = request.POST.get('requirements')
        job_instance.responsibilities = request.POST.get('responsibilities')
        job_instance.qualifications = request.POST.get('qualifications')
        job_instance.is_available = request.POST.get('is_available') == 'on'  # Assuming it's a checkbox

        # Save the updated job instance
        job_instance.save()

        # Redirect to a success page or to the job detail page
        return redirect('manage-jobs')  # Assuming you have a URL named 'job_detail'
    else:
        # Render the update form with the existing job data
        return render(request, 'job/update_job.html', {'job': job_instance})
    

def apply_for_job(request, job_id=None):
    if job_id is not None:
        job = get_object_or_404(Job, pk=job_id)
    else:
        job = None

    if request.method == 'POST':
        # Check if the user has already applied for the job using email ID in session
        if request.session.get('applied_job_{}'.format(job_id), False):
            return HttpResponse('<h1>You have already applied for this job</h1>')

        form = JobApplicationForm(request.POST)
        if form.is_valid():
            try:
                job_application = form.save(commit=False)
                job_application.job = job

                # Set user to None for anonymous users
                job_application.user = None

                job_application.save()

                # Set a session variable to mark that the user has applied for this job
                request.session['applied_job_{}'.format(job_id)] = True

                return HttpResponse('<h1>Thanks for applying</h1>')
            except Exception as e:
                return HttpResponse('<h1>Internal Server Error: {}</h1>'.format(str(e)))
    else:
        form = JobApplicationForm()

    return render(request, 'website/applicant_form.html', {'form': form, 'job': job})




def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user)
    context = {'jobs':jobs}
    return render(request,'job/manage_jobs.html',context)


def all_applicants_view(request, job_id):
    job = Job.objects.get(pk=job_id)
    applicants = JobApplication.objects.filter(job=job)
    return render(request, 'job/all_applicants.html', {'applicants': applicants, 'job': job})


def delete_applicant(request,job_id, applicant_id):
    applicant = JobApplication.objects.get(pk=applicant_id)
    applicant.delete()
    return redirect('all_applicants',job_id=job_id)




