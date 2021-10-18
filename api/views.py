from .models import TBudgets,TShops
from datetime import datetime,date
from django.http import HttpResponse
import json

## getNotifyShopsView is a method to calculate the percentage of amount spent to the budget and invoke the updateNotification to update the notification & shop visiblity  in the database

def getNotifyShopsView(request):
    shopId=int(request.GET.get('shopId'))
    month=request.GET.get('month')
    currentMonth=datetime.strptime(month, "%Y-%m-%d").date()
    currentDate=date.today()
    result=list(TBudgets.objects.filter(a_shop_id=shopId).filter(a_month=currentMonth).values_list('a_budget_amount','a_amount_spent','a_shop_id'))
    resultTuple=result[0]
    budgetAmount=resultTuple[0]
    amountSpent=resultTuple[1]
    shopId=resultTuple[2]
    percentageOfAmountSpent=int((amountSpent/budgetAmount)*100)
    updateNotification(percentageOfAmountSpent,currentMonth,shopId,amountSpent,budgetAmount)
    result=TBudgets.objects.filter(a_shop_id=shopId).filter(a_month=currentMonth).filter(a_notification=1)
    if result:
        notificationMessage= "shopId {shopId} has spent {amountSpent} Euros of totalBudget {budgetAmount} Euros ie,{percentage} % in the month of {currentMonth} on {currentDate}".format(shopId=shopId,amountSpent=amountSpent,budgetAmount=budgetAmount,percentage=percentageOfAmountSpent,currentMonth=currentMonth,currentDate=currentDate)
        return HttpResponse(json.dumps(notificationMessage))
    else:
        return HttpResponse(json.dumps(" shopId {shopId} have not exceeded the 50 % of this month budget").format(shopId=shopId))
    

def updateNotification(percentageOfAmountSpent,currentMonth,shopId,amountSpent,budgetAmount):
    if ( percentageOfAmountSpent > 50 ):
        result=TBudgets.objects.filter(a_shop_id=shopId).filter(a_month=currentMonth).filter(a_notification=1)
        if not result:
            TBudgets.objects.filter(a_shop_id=shopId).filter(a_month=currentMonth).update(a_notification=1)
    else:
        TBudgets.objects.filter(a_shop_id=shopId).filter(a_month=currentMonth).update(a_notification=0)
    if(amountSpent >= budgetAmount ):
        TShops.objects.filter(a_id=shopId).update(a_online=0)
    else:
        TShops.objects.filter(a_id=shopId).update(a_online=1)

## updateBudgetChange is a method to handle the budget change of the shop.
def updateBudgetChange(request):
    shopId=int(request.GET.get('shopId'))
    month=request.GET.get('month')
    currentDate=date.today()
    budget=request.GET.get('budget')
    currentMonth=datetime.strptime(month, "%Y-%m-%d").date()
    TBudgets.objects.filter(a_shop_id=shopId).filter(a_month=currentMonth).update(a_budget_amount=budget)
    result=list(TBudgets.objects.filter(a_shop_id=shopId).filter(a_month=currentMonth).values_list('a_budget_amount','a_amount_spent','a_shop_id'))
    resultTuple=result[0]
    budgetAmount=resultTuple[0]
    amountSpent=resultTuple[1]
    percentageOfAmountSpent=int((amountSpent/budgetAmount)*100)
    updateNotification(percentageOfAmountSpent,currentMonth,shopId,amountSpent,budgetAmount)
    result=TBudgets.objects.filter(a_shop_id=shopId).filter(a_month=currentMonth).filter(a_notification=1)
    if result:
        notificationMessage= "shopId {shopId} has spent {amountSpent} Euros of totalBudget {budgetAmount} Euros ie,{percentage} % in the month of {currentMonth} on {currentDate}".format(shopId=shopId,amountSpent=amountSpent,budgetAmount=budgetAmount,percentage=percentageOfAmountSpent,currentMonth=currentMonth,currentDate=currentDate)
        return HttpResponse(json.dumps(notificationMessage))
    else:
        return HttpResponse(json.dumps(" shopId {shopId} have not exceeded the 50 % of this month budget").format(shopId=shopId))


