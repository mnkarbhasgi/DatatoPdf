from django.shortcuts import render, redirect
from .models import createresume

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
        p.drawString(70, 800, "Resume Headline")
        p.drawString(70, 785, first_name)
        p.drawString(120, 785, last_name)
        p.drawString(70, 770, "-------------------------------------------------------------------------------------")
        p.drawString(70, 755, "Email Addess:")
        p.drawString(70, 740, email)
        p.drawString(70, 725, "-------------------------------------------------------------------------------------")
        p.drawString(70, 710, "Contact Number")
        p.drawString(70, 695, phone)
        p.drawString(70, 680, "-------------------------------------------------------------------------------------")
        p.drawString(70, 665, "Address")
        p.drawString(70, 650, address)
        p.drawString(70, 635, "-------------------------------------------------------------------------------------")
        p.drawString(70, 620, "objective")
        p.drawString(70, 605, objective)
        p.drawString(70, 590, "-------------------------------------------------------------------------------------")
        p.drawString(70, 575, "Experiance in years")
        p.drawString(70, 560, experiance)
        p.drawString(70, 545, "-------------------------------------------------------------------------------------")
        p.drawString(70, 530, "Company name")
        p.drawString(70, 515, organization)
        p.drawString(70, 500, "-------------------------------------------------------------------------------------")
        p.drawString(70, 485, "Technical skills")
        p.drawString(70, 470, skills)
        p.drawString(70, 455, "-------------------------------------------------------------------------------------")
        

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        return response
