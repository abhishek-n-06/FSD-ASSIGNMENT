from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

class StudentListView(CreateView, ListView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_list.html'
    success_url = reverse_lazy('student-list')
    context_object_name = 'students'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student details added successfully!")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentForm()
        return context

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student details updated successfully!")
        return response

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Student details deleted successfully!")
        return super().delete(request, *args, **kwargs)

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'
