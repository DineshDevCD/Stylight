Database Mysql version - 8.0.12

The solution is based on Django rest framework.
There are two end points 
1 - to update the notification and calculate the percentage of amount spent to the total budget.
2 - handle the budget change activity.

There are no changes needed in the rest of the system.

I have added one more column in the t_budgets table to avoid sending duplication of notification.

Steps followed in the solution :

* Does your solution avoid sending duplicate notifications?
 The notification is based on the query,once the budget exceeds 50 % it will update the column a_notification as 1.
 
1 - to update the notification and calculate the percentage of amount spent to the total budget.
a ) get the shopId and month from the user
b ) get the data for the respective shop from the database
c ) calculate their percentage of amount spent to the total budget
d ) update the notification column , if the amount spent exceeds 50 % of the budget
e ) update the shop visiblity , if the amount spent exceeds 100 % no the budget 

2 - handle the budget change activity.
a ) get the shopId, month and budget from the user.
b ) update the budget for the shopId.
c ) update the notification and shop visiblity based on the new budget.

To start the application :
Prequesites:
python==3.9.6

1) create venv environment
2) install the following libraries

asgiref==3.4.1
Django==3.2.8
django-cors-headers==3.10.0
djangorestframework==3.12.4
mysqlclient==2.0.3
pytz==2021.3
sqlparse==0.4.2

3) in the root directory , you will find manage.py file
4) to create database table in the model , run python manage.py inspectdb > models.py
5) move the models.py under api folder.
6) run python manage.py to start the application

sample endpoints :
http://127.0.0.1:8000/Stylight/NotifyShopsView/?shopId=2&month=2020-07-01
http://127.0.0.1:8000/Stylight/updateBudgetChange/?shopId=3&month=2020-06-01&budget=200






