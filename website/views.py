from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import State, Scheme, Course, College, Student
from .forms import AddSchemeForm, AddCourseForm, AddCollegeForm, AddStudentForm, SearchStudentForm


# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.success(request, 'ERROR! Invalid Credential')
            return redirect('home')
    else:
        students = Student.objects.count()
        course = Course.objects.count()
        college = College.objects.count()
        scheme = Scheme.objects.count()
        state = State.objects.count()
        return render(request, 'home.html', {'students': students, 'course': course, 'college': college, 'scheme': scheme, 'state': state})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been Logged Out...')
    return redirect('home')


def student_page(request):
    if request.user.is_authenticated:
        return render(request, 'student_page.html', {})
    else:
        messages.success(request, 'Please log in first')
        return redirect('home')


def courses_page(request):
    course_records = Course.objects.all()
    if request.user.is_authenticated:
        return render(request, 'courses_page.html', {'course_records': course_records})
    else:
        messages.success(request, 'Please log in first')
        return redirect('home')


def courses_search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            search_by = request.POST.get('search_by')
            courses_search = request.POST.get('courses_search')
            if courses_search:
                if search_by == 'course_code':
                    result_search = Course.objects.filter(code__icontains=courses_search)
                    return render(request, 'courses_search.html', {'result_search': result_search})
                elif search_by == 'course_name':
                    # result_search = Course.objects.raw(f"SELECT * FROM website_course WHERE name ='{searched_for}' ")
                    result_search = Course.objects.filter(name__icontains=courses_search)
                    return render(request, 'courses_search.html', {'result_search': result_search})
                else:
                    messages.success(request, 'Please enter a valid scheme id')
                    return redirect('courses_page')
            else:
                messages.success(request, 'Please enter a valid scheme id')
                return redirect('courses_page')
        else:
            return redirect('courses_page')
    else:
        messages.success(request, 'You must be logged in ')
        return redirect('home')


def schemes_page(request):
    scheme_records = Scheme.objects.all()
    if request.user.is_authenticated:
        return render(request, 'schemes_page.html', {'scheme_records': scheme_records})
    else:
        messages.success(request, 'Please log in first')
        return redirect("home")


def schemes_search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            search_by = request.POST.get('search_by')
            scheme_search = request.POST.get('scheme_search')
            if scheme_search:
                if search_by == 'scheme_id':
                    result_search = Scheme.objects.filter(id__icontains=scheme_search)
                    return render(request, 'schemes_search.html', {'result_search': result_search})
                elif search_by == 'scheme_name':
                    # result_search = Course.objects.raw(f"SELECT * FROM website_course WHERE name ='{searched_for}' ")
                    result_search = Scheme.objects.filter(name__icontains=scheme_search)
                    return render(request, 'schemes_search.html', {'result_search': result_search})
                else:
                    messages.success(request, 'Please enter a valid scheme id')
                    return redirect('schemes_page')
            else:
                messages.success(request, 'Please enter a valid scheme id')
                return redirect('schemes_page')
        else:
            return redirect('schemes_page')
    else:
        messages.success(request, 'You must be logged in ')
        return redirect('home')


def state_page(request):
    state_records = State.objects.all()
    if request.user.is_authenticated:
        return render(request, 'state_page.html', {'state_records': state_records})
    else:
        messages.success(request, 'Please log in first')
        return redirect("home")


def college_page(request):
    college_records = College.objects.all()
    if request.user.is_authenticated:
        return render(request, 'college_page.html', {'college_records': college_records})
    else:
        messages.success(request, 'Please log in first')
        return redirect("home")


def add_college(request):
    form = AddCollegeForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'College Added')
                return redirect('college_page')
        return render(request, 'add_college.html', {'form': form})
    else:
        messages.success(request, 'You must be loggedin')
        return redirect('home')


def add_student(request):
    form = AddStudentForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            # admission_year = form.data['admission_year']
            # college_code = form.data['college']
            # course_code = form.data['course']
            # roll_number = form.data['uid']
            # uid = str(admission_year)[-2:] + str(college_code)+str(course_code)+str(roll_number)[-3:]
            # form.uid = uid
            # form1.data['uid']= uid
            if form.is_valid():
                form.save()
                messages.success(request, 'Student Added')
                return redirect('student_page')
        return render(request, 'add_student.html', {'form': form})
    else:
        messages.success(request, 'You must be loggedin')
        return redirect('home')


def add_scheme(request):
    form = AddSchemeForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Scheme Added')
                return redirect('schemes_page')
        return render(request, 'add_scheme.html', {'form': form})
    else:
        messages.success(request, 'You must be loggedin')
        return redirect('home')


def add_course(request):
    form = AddCourseForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Course Added')
                return redirect('courses_page')
        return render(request, 'add_course.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')


# def student_search(request):
#     form = SearchStudentForm(request.POST or None)
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             if form.is_valid():
#                 form.save()
#                 render(request, 'student_search.html', {'result_search': form})
#             return render(request, 'student_page.html', {'form': form})
#         return redirect('student_page')
#     else:
#         messages.success(request, 'You must be logged in')
#         return redirect('home')

# def student_page(request):
#     form = SearchStudentForm(request.POST or None)
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             if form.is_valid():
#                 return render(request, 'student_search.html', {'form': form})
#         return render(request, 'student_page.html', {'form': form})
#     else:
#         messages.success(request, 'You must be logged in')
#         return redirect('home')

def student_search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            search_by = request.POST.get('search_by')
            students_search = request.POST.get('student_search')
            if students_search:
                if search_by == 'students_aadhar':
                    result_search = Student.objects.filter(aadhar_id__icontains=students_search)
                    return render(request, 'student_search.html', {'result_search': result_search})
                elif search_by == 'students_uid':
                    # result_search = Course.objects.raw(f"SELECT * FROM website_course WHERE name ='{searched_for}' ")
                    result_search = Student.objects.filter(uid__icontains=students_search)
                    return render(request, 'student_search.html', {'result_search': result_search})
                else:
                    messages.success(request, 'Please enter a valid id')
                    return redirect('student_page')
            else:
                messages.success(request, 'Please enter a valid  id')
                return redirect('student_page')
        else:
            return render(request, 'student_page.html', {})
    else:
        messages.success(request, 'You must be logged in ')
        return redirect('home')


def student_page(request):
    if request.user.is_authenticated:
        return render(request, 'student_page.html', {})
    else:
        messages.success(request, 'You must be logged in ')
        return redirect('home')


def student_details(request, uid):
    uid = str(uid)
    uid = uid.strip()
    if request.user.is_authenticated:
        student = Student.objects.get(uid=uid)
        college = student.college
        course = student.course
        if student.scheme:
            scheme = Scheme.objects.get(name=student.scheme)
            return render(request, 'student_details.html',
                          {'student': student,'college': college,'course':course ,'scheme': scheme})
        else:
            return render(request, 'student_details.html', {'student': student, 'college': college, 'course': course})
    else:
        messages.success(request, 'You must be logged in ')
        return redirect(home)


# show colleges in state
def state_college(request, state_code):
    state = State.objects.get(code=state_code)
    colleges = state.college_set.all()
    return render(request, 'state_college.html', {'colleges': colleges, 'state': state})


# show students in college
def college_student(request, college_code):
    college = College.objects.get(code=college_code)
    students = college.student_set.all()
    return render(request, 'college_student.html', {'students': students, 'college': college})


def college_details(request, college_code):
    if request.user.is_authenticated:
        college = College.objects.get(code=college_code)
        return render(request, 'college_details.html', {'college': college})
    else:
        messages.success(request, 'You must be logged in ')
        return redirect(home)


def update_student(request, uid):
    if request.user.is_authenticated:
        current_record = Student.objects.get(uid=uid)
        form = AddStudentForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been updated')
            return redirect('home')
        return render(request, 'update_student.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')


def delete_student(request, uid):
    if request.user.is_authenticated:
        delete_it = Student.objects.get(uid=uid)
        delete_it.delete()
        messages.success(request, "Student Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be Logged in to do that")
        return redirect('home')


# def student_add(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':


def current_student(request):
    if request.user.is_authenticated:
        current_students = Student.objects.filter(admission_year__gte=datetime.now().year - 5)
        return render(request, 'current_student.html', {'current_students': current_students})
    else:
        messages.success(request, 'You must be logged in ')
        return redirect(home)


def old_student(request):
    if request.user.is_authenticated:
        old_students = Student.objects.filter(admission_year__lt=datetime.now().year - 5)
        return render(request, 'old_student.html', {'old_students': old_students})
    else:
        messages.success(request, 'You must be logged in ')
        return redirect(home)


def more_search_student(request):
    if request.user.is_authenticated:
        return render(request, 'more_search_student.html', {})
    else:
        messages.success(request, 'Please log in first')
        return redirect('home')



def base(request):
    return render(request, 'base.html', {})
