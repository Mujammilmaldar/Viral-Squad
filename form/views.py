from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from .models import TextData, DocumentData
from .validation import validate_email_address

# Create your views here.
def home(req):
    return render(req,'index.html')
def applicationForTeamLeader(req):
    if req.method == 'POST':
        # Handle file uploads
        if 'achievementfile' in req.FILES:
            achievementfile = req.FILES['achievementfile']
        else:
            achievementfile = None
        
        # Retrieve form data
        name = req.POST['name']
        dob_str = req.POST.get('dob')
        dob = datetime.strptime(dob_str, '%Y-%m-%d')
        CollegeName = req.POST['CollegeName']
        BranchOfStudy = req.POST['BranchOfStudy']
        yearofeducation = req.POST['yearofeducation']
        town = req.POST['town']
        city = req.POST['city']
        mobile = req.POST['mobile']
        mobile2 = req.POST['mobile2']
        insta = req.POST['insta']
        linkedin = req.POST['linkedin']
        email = req.POST['email']
        address = req.POST['address']
        photo = req.FILES['photo']  
        aadharcard = req.FILES['aadharcard']
        achievement = req.POST['achievement']
        statement1 = bool(req.POST.get('statement1'))
        statement2 = bool(req.POST.get('statement2'))
        statement3 = bool(req.POST.get('statement3'))

        
        error_context = validate_email_address(email)
        if 'error' in error_context:
            return render(req, 'application-for-team-leader.html', error_context)
        
        # Save text data to TextData model
        text_data = TextData.objects.create(
            name=name,
            dob=dob,
            CollegeName=CollegeName,
            BranchOfStudy=BranchOfStudy,
            yearofeducation=yearofeducation,
            town=town,
            city=city,
            mobile=mobile,
            mobile2=mobile2,
            insta=insta,
            linkedin=linkedin,
            email=email,
            address=address,
            achievement=achievement,
            statement1=statement1,
            statement2=statement2,
            statement3=statement3
        )

        # Save document data to DocumentData model
        document_data = DocumentData.objects.create(
            text_data=text_data,
            photo=photo,
            aadhar_card=aadharcard,
            achievement_file=achievementfile
        )
        context={}
        context['success']='Your Form Has Been Submitted Successfully! We Will Reply Soon'

        return render(req,'application-for-team-leader.html',context)
    
    return render(req,'application-for-team-leader.html')