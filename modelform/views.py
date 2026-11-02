from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Student_Data
from .form import StudentForm

# Create your views here.
def create_student(request):
    form=StudentForm()
    if request.method=='POST':
       form=StudentForm(request.POST)
       name=request.POST.get('name')
       age=int(request.POST.get('age'))
       email=request.POST.get('email')

       if form.is_valid():
            form.save()   
            return render(request,'studentdata/success.html')
            
    return render(request,'studentdata/student.html',{'form':form})

def studentList(request):
    
    stud=Student_Data.objects.all()
    return render(request,'studentdata/studentlist.html',{'student':stud})


def studentDetail(request,pk):
    
    stud=Student_Data.objects.get(pk=pk)

    return render(request,'studentdata/studentDetail.html',{'student':stud})



def studentedit(request,pk):
    stud=Student_Data.objects.get(pk=pk)
    if request.method=='POST':
       form=StudentForm(request.POST,instance=stud)
       if form.is_valid():
            form.save()   
            return redirect('getstudentdata')
    else:
        form=StudentForm(instance=stud)

    return render(request,'studentdata/student.html',{'form':form})

def studentdelete(request,pk):
    stud=Student_Data.objects.get(pk=pk)
    if request.method=='POST':
        stud.delete()
        return redirect('getstudentdata')

    return render(request,'studentdata/confirmdelete.html')
       
       
           
        

        
    return render(request,'studentdata/confirmdelete.html',{'form':form})


