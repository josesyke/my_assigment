from django.shortcuts import render
from django.views.generic import View
from .models import Student, CohortGroup, Student_Profile, Program
import pdb

# Create your views here.


def student(request):
   
    all_student = Student.objects.all()
    # pdb.set_trace()
   
    context = {
        
        'students': all_student
        
    }
    
    return render(request,'blog/indexmain.html', context=context)





