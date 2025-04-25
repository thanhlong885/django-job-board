from django.shortcuts import render, get_object_or_404, redirect
from .models import JobPosting
from .forms import ApplicationForm
# Create your views here.

def index(request):
    active_postings = JobPosting.objects.filter(is_active=True)
    context = {
        "job_postings": active_postings
    }
    return render(request, "job_board/index.html", context)

def job_detail(request, pk):
    posting = get_object_or_404(JobPosting, pk=pk, is_active=True)
    applications = posting.applications.all()
    
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.job = posting
            app.save()
            return redirect("job-detail", pk=pk)
    else:
        form = ApplicationForm()
            
    context = {
        "posting": posting,
        "form": form,
        "applications": applications
    }
    return render(request, "job_board/detail.html", context)