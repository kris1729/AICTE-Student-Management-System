from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Scheme, Course, College,State,Student


class AddSchemeForm(forms.ModelForm):
    id = forms.CharField(required=True,
                         widget=forms.widgets.NumberInput(attrs={'placeholder': 'Scheme ID', 'class': 'form-control'}),
                         label='')
    name = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'Scheme Name', 'class': 'form-control'}),
                           label='')

    class Meta:
        model = Scheme
        fields = ('id', 'name')


class AddCourseForm(forms.ModelForm):
    code = forms.CharField(required=True,
                           widget=forms.widgets.NumberInput(
                               attrs={'placeholder': 'Course Code', 'class': 'form-control'}),
                           label='')
    name = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'Course Name', 'class': 'form-control'}),
                           label='')
    duration = forms.CharField(required=True,
                                  widget=forms.widgets.NumberInput(
                                      attrs={'placeholder': 'Course Duration', 'class': 'form-control'}),
                                  label='')

    class Meta:
        model = Course
        fields = ('code', 'name', 'duration')

class AddCollegeForm(forms.ModelForm):
    name = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'College Name', 'class': 'form-control'}),
                           label='')
    code = forms.CharField(required=True,
                           widget=forms.widgets.NumberInput(
                               attrs={'placeholder': 'College Code', 'class': 'form-control'}),
                           label='')
    state = forms.ModelChoiceField(queryset=State.objects.all(), required=True,label='College State')

    city = forms.CharField(required=True,
                               widget=forms.widgets.TextInput(
                                   attrs={'placeholder': 'College city ', 'class': 'form-control'}),
                               label='')

    pincode = forms.CharField(required=True,
                           widget=forms.widgets.NumberInput(
                               attrs={'placeholder': 'College pincode', 'class': 'form-control'}),
                           label='')

    address = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'College address', 'class': 'form-control'}),
                           label='')
    phone = forms.CharField(required=True,
                           widget=forms.widgets.NumberInput(
                               attrs={'placeholder': 'College phone', 'class': 'form-control'}),
                           label='')

    class Meta:
        model = College
        fields = ('name', 'code', 'state', 'city', 'pincode', 'address', 'phone')


class AddStudentForm(forms.ModelForm):
    first_name = forms.CharField(required=True,
                                 widget=forms.widgets.TextInput(
                                     attrs={'placeholder': 'First Name', 'class': 'form-control', }),
                                 label='')
    last_name = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
                           label='')
    serial_no = forms.CharField(required=False,
                                widget=forms.widgets.NumberInput(
                                    attrs={'placeholder': 'Serial_no', 'class': 'form-control'}),
                                label='')

    admission_year = forms.CharField(required=True,
                          widget=forms.widgets.NumberInput(
                              attrs={'placeholder': 'Admission Year', 'class': 'form-control'}),
                          label='')
    date_of_birth = forms.DateField(required=True,
                          widget=forms.widgets.DateInput(
                              attrs={'placeholder': 'Date of Birth', 'class': 'form-control'}),
                          label='')
    aadhar_id = forms.CharField(required=True,
                               widget=forms.widgets.NumberInput(
                                   attrs={'placeholder': 'Aadhar ID ', 'class': 'form-control'}),
                               label='')
    scheme = forms.ModelChoiceField(queryset=Scheme.objects.all(), required=False ,label='Scheme', blank=True)

    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=True,label='Course')

    college = forms.ModelChoiceField(queryset=College.objects.all(), required=True, label='College')



    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'serial_no', 'admission_year', 'date_of_birth', 'aadhar_id', 'scheme', 'course' , 'college')


class SearchStudentForm(forms.ModelForm):
    first_name = forms.CharField(required=False,
                                 widget=forms.widgets.TextInput(
                                     attrs={'placeholder': 'First Name', 'class': 'form-control'}),
                                 label='')

    last_name = forms.CharField(required=False,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
                           label='')


    # admission_year = forms.ModelChoiceField(queryset=Student.admission_year.objects.all(), required=False,blank=True, label='Admission Year')

    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=False, label='Course')

    college = forms.ModelChoiceField(queryset=College.objects.all(), required=False, label='College')

    aadhar_id = forms.CharField(required=False,
                               widget=forms.widgets.NumberInput(
                                   attrs={'placeholder': 'Aadhar ID ', 'class': 'form-control'}),
                               label='')

    scheme = forms.ModelChoiceField(queryset=Scheme.objects.all(), required=False, label='Scheme')

    class Meta:
        model = Student
        fields = ('first_name', 'last_name','serial_no', 'course', 'college', 'aadhar_id')
