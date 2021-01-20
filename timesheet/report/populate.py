from .models import TimeSheet, Holidays, User
from datetime import datetime
#https://calendar.nagsh.ir/تقویم-سال-99-در-یک-نگاه/
holidays = [{'date':'2020/07/31','desc':'Ghorban'},
{'date':'2020/8/08','desc':'ghadir'},
{'date':'2020/08/29','desc':'tasoa'},
{'date':'2020/08/30','desc':'ashora'},
{'date':'2020/10/08','desc':'arbaeen'},
{'date':'2020/10/25','desc':'emamhasan'},
{'date':'2020/10/08','desc':'arbaeen'},
{'date':'2020/11/03','desc':'molod'},
{'date':'2021/01/17','desc':'zahra'},
{'date':'2021/02/10','desc':'22bahman'},

]
for holiday in holidays:
    h = Holidays(time=datetime.strptime(holiday['date'],'%Y/%m/%d'),descrtiption=holiday['desc'])
    h.save()

start_date = datetime.strptime('2020/06/21','%Y/%m/%d') 
end_date = datetime.now()
users = User.objects.all()
for user in :
    TimeSheet.creat_user_timesheet(user, start_date, end_date)
