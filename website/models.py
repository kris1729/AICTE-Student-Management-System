from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator





# Create your models here.
class State(models.Model):
    name = models.CharField('State Name',max_length=50)
    code = models.CharField('State Code', primary_key=True,  max_length=2, validators=[MinLengthValidator(2), MaxLengthValidator(2)])

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


def generate_code(state, code):
    # Your custom logic here
    y = str(State.objects.get(name=state).code) +str(code)
    return y

class College(models.Model):
    name = models.CharField('College Name', max_length=100)
    code = models.CharField('College Code', primary_key=True, max_length=5, validators=[MinLengthValidator(3), MaxLengthValidator(3)])
    state = models.ForeignKey(State, blank=False, null=False, on_delete=models.CASCADE)
    city = models.CharField('College City', max_length=100)
    pincode = models.CharField('College Pincode',max_length=6, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    address = models.CharField('College Address',max_length=200)
    phone = models.CharField('College Phone',max_length=10, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    created_at = models.DateTimeField('College Creation Date', auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def save(self, *args, **kwargs):
        self.code = generate_code(self.state, self.code)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField('Course Name', max_length=100)
    code = models.CharField('Course Code', primary_key=True,max_length=3, validators=[MinLengthValidator(3), MaxLengthValidator(3)])
    duration = models.IntegerField('Course Duration')
    created_at = models.DateTimeField('Course Creation Date', auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Scheme(models.Model):
    name = models.CharField('Scheme Name', null=False, blank=False, max_length=100)
    id = models.CharField('Scheme Id', primary_key=True,max_length=3, validators=[MinLengthValidator(3), MaxLengthValidator(3)])
    created_at = models.DateTimeField('Scheme Creation Date', auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


def generate_pk(admission_year, course, college, serial_no):
    # Your custom logic here
    y=str(College.objects.get(name=college).code)+str(admission_year)[-2:]+str(Course.objects.get(name=course).code)+str(serial_no)
    print(y)
    return y


class Student(models.Model):
    first_name = models.CharField('First Name',max_length=100)
    last_name = models.CharField('Last Name',max_length=100)
    serial_no = models.CharField('Serial No', max_length=3, validators=[MinLengthValidator(3), MaxLengthValidator(3)])
    uid = models.CharField('UID', primary_key=True, max_length=15, validators=[MinLengthValidator(13), MaxLengthValidator(13)], )
    admission_year = models.CharField('Admission Year', max_length=4, validators=[MinLengthValidator(4), MaxLengthValidator(4)])
    date_of_birth = models.DateField('Date of Birth', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Student Creation Date', auto_now_add=True)
    aadhar_id = models.CharField('Aadhar ID', max_length=15,validators=[MinLengthValidator(12), MaxLengthValidator(12)])
    scheme = models.ForeignKey(Scheme, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['aadhar_id']),
            models.Index(fields=['first_name', 'last_name']),
        ]

    def save(self, *args, **kwargs):
        self.uid = generate_pk(self.admission_year, self.course, self.college, self.serial_no)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
