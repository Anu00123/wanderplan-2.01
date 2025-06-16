from django.shortcuts import render, redirect,get_object_or_404, redirect
from .models import Package,PackageImage,Booking
from django.urls import reverse
from .models import ContactSubmission
from django.contrib import messages
from django.http import JsonResponse




# Create your views here.
def index(request):
    return render(request,'index.html')

def destination(request):
    packages = Package.objects.all()
    context = {
        'packages': packages
    }
    return render(request, 'destination.html', context)

def about(request):
    return render(request, 'about.html')



def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    related_packages = Package.objects.exclude(pk=pk).filter(is_featured=True)[:3]
    images = PackageImage.objects.all()
    second_img = Package.objects.all()




    if request.method == 'POST':
        try:
            # Get the package ID from the form
            package_id = request.POST.get('package_id')
            
            # Get the actual Package instance
            package = get_object_or_404(Package, id=package_id)
            
            # Create the booking with the Package instance
            booking = Booking(
                package=package,  # This must be a Package object, not just an ID
                check_in=request.POST.get('check_in'),
                check_out=request.POST.get('check_out'),
                guests=int(request.POST.get('guests')),
                name=request.POST.get('name'),
                phone_number=request.POST.get('phone_number'),
                
            )
            booking.save()
            
            return redirect('booking_done')
            
        except Exception as e:
            messages.error(request, f'Error creating booking: {str(e)}')
            return redirect('package_detail', pk=package_id)


    # Get rating stars for template
    rating_stars = package.get_rating_stars()
    
    context = {
        'package': package,
        'related_packages': related_packages,
        'rating_stars': rating_stars,
        'images': images,
        'second_img': second_img
    }


    return render(request, 'destination_details.html', context)

from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        # Get data from POST request
        fullName = request.POST.get('fullName')
        emailAddress = request.POST.get('emailAddress')
        phoneNumber = request.POST.get('phoneNumber')
        travelType = request.POST.get('travelType')
        travelDetails = request.POST.get('travelDetails')
        
        # Validate required fields
        errors = []
        if not fullName:
            errors.append('Full name is required')
        if not emailAddress:
            errors.append('Email address is required')
        if not phoneNumber:
            errors.append('Phone number is required')
        if not travelType:
            errors.append('Travel type is required')
        if not travelDetails:
            errors.append('Travel details are required')
            
        if errors:
            # Add error messages and return to form
            for error in errors:
                messages.error(request, error)
            return render(request, 'contact.html', {
                'fullName': fullName,
                'emailAddress': emailAddress,
                'phoneNumber': phoneNumber,
                'travelType': travelType,
                'travelDetails': travelDetails,
            })
        
        # Create and save the submission if no errors
        try:
            submission = ContactSubmission.objects.create(
                fullName=fullName, 
                email=emailAddress,
                phone=phoneNumber,
                subject=travelType,
                message=travelDetails
            )
            # Redirect to success page with the submission ID
            return redirect(reverse('success_page') + f'?ref={submission.id}')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'contact.html', {
                'fullName': fullName,
                'emailAddress': emailAddress,
                'phoneNumber': phoneNumber,
                'travelType': travelType,
                'travelDetails': travelDetails,
            })
        


    
    return render(request, 'contact.html' )

def success_page(request):
    submission_id = request.GET.get('ref')
    
    try:
        # Try to get the submission from database
        submission = ContactSubmission.objects.get(id=submission_id)
        topic = ContactSubmission.objects.all()
        context = {
            'submission': submission,
            'submission_date': submission.submitted_at.strftime('%B %d, %Y'),
            'topic':topic
        }
    except ContactSubmission.DoesNotExist:
        context = {
            'error': 'Submission not found'
        }
    
     
    
    return render(request, 'success.html', context)



def booking_done(request):
    return render(request, 'booking_done.html')







def health_check(request):
    return JsonResponse({"status": "ok", "service": "your_service_name"})