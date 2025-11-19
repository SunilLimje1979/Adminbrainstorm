from django.db import models

# Create your models here.

class TblUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_uid = models.CharField(max_length=255,null=True,blank=True)
    user_code = models.CharField(max_length=32,unique=True) #will be used for api to fetch details.
    user_firstname = models.CharField(max_length=255,null=True,blank=True)
    user_middlename = models.CharField(max_length=255,null=True,blank=True)
    user_lastname = models.CharField(max_length=255,null=True,blank=True)
    user_gender = models.IntegerField(null=True,blank=True) # 0=Female,1=Male,2=other
    user_mobileno = models.CharField(max_length=15,null=True,blank=True)
    user_contactnos = models.TextField(null=True,blank=True)#to store multiple contsct numbers if present .
    user_email = models.CharField(max_length=255,null=True,blank=True)
    user_address = models.TextField(null=True,blank=True)
    user_dob = models.DateField(null=True,blank=True)
    user_enrollment_date = models.DateField(null=True,blank=True)
    user_profilephoto = models.TextField(null=True,blank=True) #to add image link
    user_username = models.CharField(max_length=255,null=True,blank=True)
    user_password = models.CharField(max_length=255,null=True,blank=True)
    user_role =  models.IntegerField(null=True,blank=True) #0=Admin,1=Teacher,2=Student,3=SuperAdmin

    #############Bydefault fields####################
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_reason = models.CharField(max_length=100, blank=True, null=True)
   
    class Meta:
       db_table = 'TblUser'
       indexes = [
            models.Index(fields=['user_code']),
            models.Index(fields=['user_role']),
            models.Index(fields=['is_deleted']),
        ]


class TblSchool(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_uid = models.CharField(max_length=255,null=True,blank=True) # uid = SCH-number(SCH1)
    school_code = models.CharField(max_length=32,unique=True) #will be used for api to fetch details.
    school_name = models.CharField(max_length=500,null=True,blank=True)
    school_mobileno = models.CharField(max_length=15,null=True,blank=True)
    school_contactnos = models.TextField(null=True,blank=True)#to store multiple contact numbers if present .
    school_email = models.CharField(max_length=255,null=True,blank=True)
    school_website = models.CharField(max_length=500,null=True,blank=True)
    school_address = models.TextField(null=True,blank=True)
    school_pincode = models.CharField(max_length=10,null=True,blank=True)
    school_country_id = models.IntegerField(null=True,blank=True)
    school_state_id = models.IntegerField(null=True,blank=True)
    school_city_id = models.IntegerField(null=True,blank=True)
    school_profile_photo = models.TextField(null=True,blank=True) #image path link

    #############Bydefault fields####################
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_reason = models.CharField(max_length=100, blank=True, null=True)
   
    class Meta:
       db_table = 'TblSchool'

class TblGrade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    grade_uid = models.CharField(max_length=255,null=True,blank=True)
    grade_name = models.CharField(max_length=255,null=True,blank=True)
    school =  models.ForeignKey(TblSchool, on_delete=models.CASCADE, null=True, blank=True,related_name="TblGrade_school_id")

    #############Bydefault fields####################
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_reason = models.CharField(max_length=100, blank=True, null=True)
   
    class Meta:
       db_table = 'TblGrade'


class TblDivision(models.Model):
    division_id = models.AutoField(primary_key=True)
    division_uid = models.CharField(max_length=255,null=True,blank=True)
    division_name = models.CharField(max_length=255,null=True,blank=True)
    grade =  models.ForeignKey(TblGrade, on_delete=models.CASCADE, null=True, blank=True,related_name="TblDivision_grade_id")
    school =  models.ForeignKey(TblSchool, on_delete=models.CASCADE, null=True, blank=True,related_name="TblDivision_school_id")

    #############Bydefault fields####################
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_reason = models.CharField(max_length=100, blank=True, null=True)
   
    class Meta:
       db_table = 'TblDivision'



class TblStudentAcademics(models.Model):
    studentacademic_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TblUser, on_delete=models.CASCADE, null=True, blank=True,related_name="StudentAcademics_user_id")
    school =  models.ForeignKey(TblSchool, on_delete=models.CASCADE, null=True, blank=True,related_name="StudentAcademics_school_id")
    grade = models.ForeignKey(TblGrade, on_delete=models.CASCADE, null=True, blank=True,related_name="StudentAcademics_grade_id")
    division = models.ForeignKey(TblDivision, on_delete=models.CASCADE, null=True, blank=True,related_name="StudentAcademics_division_id")
    academic_year = models.CharField(max_length=255,null=True,blank=True)
    roll_no = models.CharField(max_length=50, null=True, blank=True)

    #############Bydefault fields####################
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_reason = models.CharField(max_length=100, blank=True, null=True)
   
    class Meta:
       db_table = 'TblStudentAcademics'

       indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['school']),
            models.Index(fields=['grade']),
            models.Index(fields=['division']),
            models.Index(fields=['academic_year']),
            models.Index(fields=['roll_no']),
            models.Index(fields=['is_deleted']),
        ]


class TblTeacherAcademics(models.Model):
    teacheracademic_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TblUser, on_delete=models.CASCADE, null=True, blank=True,related_name="teacherAcademics_user_id")
    school =  models.ForeignKey(TblSchool, on_delete=models.CASCADE, null=True, blank=True,related_name="teacherAcademics_school_id")
    grade = models.ForeignKey(TblGrade, on_delete=models.CASCADE, null=True, blank=True,related_name="teacherAcademics_grade_id")
    division = models.ForeignKey(TblDivision, on_delete=models.CASCADE, null=True, blank=True,related_name="teacherAcademics_division_id")
    academic_year = models.CharField(max_length=255,null=True,blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    teacher_type = models.IntegerField(default=1)  # 0 = Class Teacher 1 = Subject Teacher 2 = Coordinator 3 = Admin Staff


    #############Bydefault fields####################
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True, blank=True)
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_reason = models.CharField(max_length=100, blank=True, null=True)
   
    class Meta:
       db_table = 'TblTeacherAcademics'
       indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['school']),
            models.Index(fields=['grade']),
            models.Index(fields=['division']),
            models.Index(fields=['subject']),
            models.Index(fields=['academic_year']),
            models.Index(fields=['is_deleted']),
        ]