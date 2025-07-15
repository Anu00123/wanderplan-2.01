from django.shortcuts import render, redirect, get_object_or_404
from .models import InsurancePlan,InsurancePayment
from django.contrib import messages

def Insurance(request):
    plans = InsurancePlan.objects.all
    return render(request, 'insurance.html', {'plans': plans})

def payment(request, pk):
    if request.method == 'POST':
        print("hello")
        full_name = request.POST.get('fullName')
        phone_number = request.POST.get('phoneNumber')
        age = request.POST.get('age')
        aadhar_number = request.POST.get('aadharNumber')
        trip_name = request.POST.get('tripName')
        transaction_id = request.POST.get('transactionId')
        print(full_name)
        
        InsurancePayment.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            age=age,
            aadhar_number=aadhar_number,
            trip_name=trip_name,
            transaction_id=transaction_id
        )
        messages.success(request, "Payment details submitted successfully.")
        return redirect('success_payment')
    else:
        print("myre")

    plan = get_object_or_404(InsurancePlan, pk=pk)
    
    # Get optional parameters with defaults
    duration = int(request.GET.get('duration', 7))  # Default 7 days
    travelers = int(request.GET.get('travelers', 1))  # Default 1 traveler
    
    # Calculate total price
    total_price = plan.daily_price * duration * travelers
    
    context = {
        'plan': plan,
        'duration': duration,
        'travelers': travelers,
        'total_price': total_price,
    }

    return render(request, 'payment.html',context)

def success_page(request):
    return render(request, 'payment_success.html')

