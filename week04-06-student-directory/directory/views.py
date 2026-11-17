from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentEditForm, StudentFilterForm
from .models import Module, Student

def home(request):
    return render(request, "directory/home.html", {"students": Student.objects.all()[:8]})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, "directory/student_detail.html", {"student": student})

def module_list(request):
    return render(request, "directory/module_list.html", {"modules": Module.objects.prefetch_related("students")})

def student_list(request, page=1):
    students = Student.objects.all().prefetch_related("modules")
    filter_form = StudentFilterForm(request.GET)
    if filter_form.is_valid():
        first = filter_form.cleaned_data["first_name"]
        last = filter_form.cleaned_data["last_name"]
        module = filter_form.cleaned_data["module"]
        if first: students = students.filter(first_name__icontains=first)
        if last: students = students.filter(last_name__icontains=last)
        if module: students = students.filter(modules__code__icontains=module)
    paginator = Paginator(students.distinct(), 10)
    page_obj = paginator.get_page(page)
    query_string = request.GET.urlencode()
    return render(request, "directory/student_list.html", {"page_obj": page_obj, "filter_form": filter_form, "query_string": query_string})

def student_edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentEditForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("directory:student_detail", student_id=student.id)
    else:
        form = StudentEditForm(instance=student)
    return render(request, "directory/student_edit.html", {"form": form, "student": student})
