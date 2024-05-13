from django.urls import path
from . import views

urlpatterns=[
    path('create-job/',views.create_job,name='create-job'),
     path('manage-jobs/',views.manage_jobs,name='manage-jobs'),
     path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
      path('update_job/<int:job_id>/', views.update_job, name='update_job'),
     path('all_applicants/<int:job_id>/', views.all_applicants_view, name='all_applicants'),
    path('delete_applicant/<int:job_id>/<int:applicant_id>/', views.delete_applicant, name='delete_applicant'),


]