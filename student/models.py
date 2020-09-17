from django.db import models

class Hostel_name(models.Model):
    h_name = models.CharField(max_length=200)


class HostelDetail(models.Model):
    name         = models.CharField(max_length=200)
    rooms        = models.IntegerField(default=0)
    capacity     = models.IntegerField(default=0)
    vacancy      = models.IntegerField(default=0)

    # class Meta:
    #      db_table = "hostelDetail"

class StudentDetaile(models.Model):
    h_id           =models.ForeignKey(HostelDetail, on_delete=models.CASCADE)
    student_name   =models.CharField(max_length=200)
    enroll_no      =models.CharField(max_length=100, unique=True)
    course         =models.CharField(max_length=200)
    dob            =models.CharField(max_length=100)
    add_yr         =models.CharField(max_length=100)
    dept_name      =models.CharField(max_length=200)
    email_id       =models.EmailField(max_length=200)
    phone_no       =models.IntegerField()
    gender         =models.CharField(max_length=13)
    hostel_name    =models.CharField(max_length=200)
    room_no        =models.IntegerField()
    mess_dev        =models.BooleanField(default=0)
    
    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s %s %s %S' % (self.student_name, self.enroll_no, self.course, self.course,
                          self.dob, self.add_yr, self.dept_name, self.email_id, self.phone_no,
                          self.gender, self.hostel_name, self.room_no)



class login(models.Model):
    user_name = models.CharField(max_length=100)
    lpassword = models.CharField(max_length=50)
    
#
# class Warden_login(models.Model):
#     # h_ids    = models.ForeignKey(Hostel_name, on_delete=models.CASCADE)
#     hos_name = models.CharField(max_length=200)
#     user     = models.CharField(max_length=100)
#     Wpassword= models.CharField(max_length=50)

    

    
    