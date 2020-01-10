from django.shortcuts import render, redirect
from .models import createresume
from django.contrib.auth.models import User  # , Group

from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.
def resume(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        objective = request.POST['objective']
        experiance = request.POST['experiance']
        organization = request.POST['organization']
        skills = request.POST['skills']

        user = createresume(first_name=first_name,last_name=last_name, email=email, phone=phone, address=address, 
                            objective=objective,experiance=experiance,organization=organization,skills=skills)
        user.save()
        return redirect('resume')

    return render(request, 'resume.html')


def save(request):
    return render(request, 'save.html')

def fetch_data(request):
    data = createresume.objects.all()
    context = {'user': data}
    return render(request, 'view.html', context)


def some_view(request):
    if request.method == 'GET':
        first_name = request.GET['first_name']
        last_name = request.GET['last_name']
        email = request.GET['email']
        phone = request.GET['phone']
        address = request.GET['address']
        objective = request.GET['objective']
        experiance = request.GET['experiance']
        organization = request.GET['organization']
        skills = request.GET['skills']

        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

        # Create the PDF object, using the response object as its "file."
        p = canvas.Canvas(response)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(100, 600, "Resume Headline")
        p.drawString(100, 590, first_name)
        p.drawString(150, 590, last_name)
        p.drawString(100, 570, "Email Addess")
        p.drawString(100, 560, email)
        p.drawString(100, 550, "Contact Number")
        p.drawString(100, 540, phone)
        p.drawString(100, 520, "Address")
        p.drawString(100, 510, address)
        p.drawString(100, 490, "objective")
        p.drawString(100, 480, objective)
        p.drawString(100, 460, "Experiance in years")
        p.drawString(100, 450, experiance)
        p.drawString(100, 430, "Company nam")
        p.drawString(100, 420, organization)
        p.drawString(100, 400, "Your skills")
        p.drawString(100, 390, skills)

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        return response