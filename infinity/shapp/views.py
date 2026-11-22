from django.shortcuts import render
def churn_rate(request):
    InitCust= float(request.POST.get('Initial_Customer_Count', '0'))
    CustLost=float(request.POST.get('Customers_Lost_Count', '0'))
    cr = (CustLost/InitCust) if InitCust !=0 else 0
    print("Initial Customer =",InitCust)
    print("Present Customer =",CustLost)
    print("Churn Rate =",cr)
    return render(request, 'sanjay.html',{'InitCust': InitCust, 'CustLost': CustLost, 'cr': cr})