from .models import TimeSheet, Holidays, User
from datetime import datetime

# https://calendar.nagsh.ir/تقویم-سال-99-در-یک-نگاه/
holidays = [
    {"date": "2020/07/31", "desc": "Ghorban"},
    {"date": "2020/8/08", "desc": "ghadir"},
    {"date": "2020/08/29", "desc": "tasoa"},
    {"date": "2020/08/30", "desc": "ashora"},
    {"date": "2020/10/08", "desc": "arbaeen"},
    {"date": "2020/10/25", "desc": "emamhasan"},
    {"date": "2020/10/08", "desc": "arbaeen"},
    {"date": "2020/11/03", "desc": "molod"},
    {"date": "2021/01/17", "desc": "Shahadat "},
    {"date": "2021/02/10", "desc": "22bahman"},
    {"date": "2021/01/17", "desc": "holiday_0"},
    {"date": "2021/02/10", "desc": "holiday_1"},
    {"date": "2021/03/20", "desc": "holiday_2"},
    {"date": "2021/03/21", "desc": "holiday_3"},
    {"date": "2021/03/22", "desc": "holiday_4"},
    {"date": "2021/03/23", "desc": "holiday_5"},
    {"date": "2021/03/24", "desc": "holiday_6"},
    {"date": "2021/03/29", "desc": "holiday_7"},
    {"date": "2021/05/04", "desc": "holiday_8"},
    {"date": "2021/06/05", "desc": "holiday_9"},
    {"date": "2021/06/06", "desc": "holiday_10"},
    {"date": "2021/07/21", "desc": "holiday_11"},
    {"date": "2021/08/18", "desc": "holiday_12"},
    {"date": "2021/09/27", "desc": "holiday_13"},
    {"date": "2021/10/05", "desc": "holiday_14"},
    {"date": "2021/10/24", "desc": "holiday_15"},
    {"date": "2022/02/15", "desc": "holiday_16"},
    {"date": "2022/03/01", "desc": "holiday_17"},
    {"date": "2022/03/20", "desc": "holiday_18"},
    {"date": "2022/03/21", "desc": "holiday_19"},
    {"date": "2022/03/22", "desc": "holiday_20"},
    {"date": "2022/03/23", "desc": "holiday_21"},
    {"date": "2022/04/02", "desc": "holiday_22"},
    {"date": "2022/05/02", "desc": "holiday_23"},
    {"date": "2022/05/03", "desc": "holiday_24"},
    {"date": "2022/06/04", "desc": "holiday_25"},
    {"date": "2022/06/05", "desc": "holiday_26"},
    {"date": "2022/07/09", "desc": "holiday_27"},
    {"date": "2022/07/17", "desc": "holiday_28"},
    {"date": "2022/08/07", "desc": "holiday_29"},
    {"date": "2022/08/08", "desc": "holiday_30"},
    {"date": "2022/09/24", "desc": "holiday_31"},
    {"date": "2022/09/26", "desc": "holiday_32"},
    {"date": "2022/10/04", "desc": "holiday_33"},
]
for holiday in holidays:
    h = Holidays(
        time=datetime.strptime(holiday["date"], "%Y/%m/%d"),
        descrtiption=holiday["desc"],
    )
    h.save()

start_date = datetime.strptime("2020/06/21", "%Y/%m/%d")
end_date = datetime.now()
end_date = datetime.strptime("2022/11/22", "%Y/%m/%d")
users = User.objects.all()
for user in users:
    TimeSheet.creat_user_timesheet(user, start_date, end_date)
