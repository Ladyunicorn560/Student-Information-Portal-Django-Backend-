from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from ss_app.models import Student
from .forms import StudentForm 
from django.shortcuts import get_object_or_404

def default_page(request):
    return render(request, 'default_page.html')

def student_list(request):
    form = StudentForm()

    if request.method == 'POST':
        # Check if the form is submitted to display the student list
        if 'display_student_list' in request.POST:
            students = Student.objects.all().values()
            return render(request, 'display_student_list.html', {'students': students})

    return render(request, 'student_list.html', {'form': form})


def display_student_list(request):
    students = Student.objects.all().values()
    return render(request, 'student_list.html', {'students': students, 'display_student_list': True})
   
    

def add_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(
                fname=form.cleaned_data['fname'],
                lname=form.cleaned_data['lname'],
                rollno=form.cleaned_data['rollno'],
                department=form.cleaned_data['department'],
                course=form.cleaned_data.get('course')
            )
            return redirect('student_list')

    return render(request, 'add_student.html', {'form': form})

def delete_student_list(request):
    students = Student.objects.all().values()
    return render(request, 'delete_student_list.html', {'students': students})

def update_student_list(request):
    students = Student.objects.all().values()
    return render(request, 'update_student_list.html', {'students': students})

def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('student_list')

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'update_student_list.html', {'form': form, 'student': student})
