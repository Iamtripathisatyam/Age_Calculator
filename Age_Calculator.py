from dateutil.relativedelta import relativedelta
from datetime import datetime
from time import strptime
from plyer import notification
import os
valid=True
while valid:
 os.system("cls")

 date = datetime.now().strftime("%d/%m/%Y")
 bdate = input("Please Enter Your D.O.B(i.e dd/mm/yy): ")
 try:
     val=strptime(bdate,"%d/%m/%Y")
 except:
    notification.notify(title="Age Calculator Presented by: Satyam Tripathi",
                         message="\n\t\tAlert! This is Not The Right Format"
                         , app_icon="C:/Users/Dell/Downloads/err.ico", timeout=15)
    continue
    # raise IndexError("Hi This Alert is From Satyam's side So Please Give the Correct Input")
 in_date = bdate.split('/')
 date = date.split('/')
 in_date = [int(i) for i in in_date]
 date = [int(i) for i in date]
 newdate = []
 in_date[0], in_date[2] = in_date[2], in_date[0]
 date[0], date[2] = date[2], date[0]
 if in_date<=date:
   now=datetime.strptime(bdate,"%d/%m/%Y")
   notification.notify(title="Age Calculator Presented by: Satyam Tripathi ", message=f"\n\tYour Age: {relativedelta(datetime.now(),now).years} Years, "
   f" {relativedelta(datetime.now(),now).months} Months, "
   f"{relativedelta(datetime.now(),now).days} Days"
  , app_icon="C:/Users/Dell/Downloads/cal.ico", timeout=15)
 else:
     notification.notify(title="Age Calculator Presented by: Satyam Tripathi",
                         message=f"\n\t\tNope! This is {date[0]} And You Can't be in {in_date[0]}"
                         , app_icon="C:/Users/Dell/Downloads/err.ico", timeout=15)
