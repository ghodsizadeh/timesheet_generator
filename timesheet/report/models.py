from django.db import models
import random 
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    user_id = models.IntegerField()
    
    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    def __str__(self):
        return f'{self.user_id}'
class Holidays(models.Model):
    time = models.DateField(null=False,blank=False, )
    descrtiption = models.TextField()

class TimeSheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(null=False,blank=False)
    terminal_id = models.CharField(max_length=200,default= '0001 : 05')
    clas = models.CharField('class',max_length=200,default= 'User')
    mode = models.CharField(max_length=200,default= 'Access')
    types = models.CharField('type',max_length=200,default= 'User')
    result = models.CharField(max_length=200,default= 'Success')
    @property
    def name(self):
        return self.user.fullname
        
    property = models.IntegerField(default=1000)
    

    @classmethod
    def add_start_time(cls, user,date ):
        h_rand = random.randint(0,10)
        h = 8 if h_rand < 4 else 9
        if h== 8:
            m = random.randint(40,57)
        else:
            m = random.randint(1,38)
        s = random.randint(1,50)
        time=date.replace(hour=h, minute= m,second=s)
        time=make_aware(time)

        tmp = cls(user=user,time=time)
        tmp.save()
    @classmethod
    def add_end_time(cls, user,date ):
        h_rand = random.randint(0,10)
        if h_rand<3:
            h = 16
        elif h_rand<7:
            h = 17
        else:
            h = 18
        if h== 16:
            m = random.randint(40,57)
        else:
            m = random.randint(10,59)
        s = random.randint(1,50)
        time=date.replace(hour=h, minute= m,second=s)
        time=make_aware(time)
        tmp = cls(user=user,time=time)
        tmp.save()

    @classmethod
    def add_user_time(cls, user,date ):

         cls.add_start_time(user, date)
         cls.add_end_time(user, date)

    @classmethod
    def creat_user_timesheet(cls, user, start_date, end_date):
        next_day = timedelta(days=1)
        date = start_date
        while True:
            isholiday = Holidays.objects.filter(time=date)
            if date.weekday()  in [3,4] or isholiday:
                print(date, date.weekday(), end='\r')
                date += next_day
                continue

            TimeSheet.add_user_time(user =user, date=date)

            if date >= end_date:
                break
            date+= next_day
    @classmethod 
    def get_report(cls, user, start_date=None, end_date=None):
        query = cls.objects.filter(user=user)
        if start_date:
            query = query.filter(time__gt=start_date)
        if end_date:
            query = query.filter(time__lt=end_date)
        import pandas as pd 
        df = pd.DataFrame(query.all().values())
        df['Name'] = user.fullname

        df.columns = df.columns.str.capitalize()
        df['User_id'] = user.user_id

        rename={'Clas':'Class','Types':'Type'}
        df= df.rename(rename,axis=1)
        cols = ['Time','Terminal_id','User_id','Name','Class','Mode','Result','Property']
        df = df[cols]
        df.to_html(f'~/{user.fullname}.html')
        return df


    







