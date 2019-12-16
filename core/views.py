from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .forms import ContactForm
from .models import (
    Information,
    Skill,
    Contact,
    Project,
    Education,
    Services
)


class HomeView(View):
    def get(self, *args, **kwargs):
        try:
            form = ContactForm()
            info = Information.objects.get(id=1)
            skills = Skill.objects.all()
            contact = Contact.objects.all()
            projects = Project.objects.all()
            education = Education.objects.all()
            services = Services.objects.all()
            print(info)
            context = {
                'form': form,
                'info': info,
                'skills': skills,
                'contact': contact,
                'projects': projects,
                'education': education,
                'services': services
            }
            return render(self.request, "home.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "Object not Found.")
            return render(self.request, "home.html")
        except ValueError:
             return render(self.request, "home.html")

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST or None)
        try:
            if form.is_valid():
                name = form.cleaned_data.get('name')
                email = form.cleaned_data.get('email')
                subject = form.cleaned_data.get('subject')
                comments = form.cleaned_data.get('comments')

                contact = Contact(
                    name=name,
                    email=email,
                    subject=subject,
                    comments=comments
                )
                contact.save()
            return redirect('/')

        except ObjectDoesNotExist:
            return render(self.request, "home.html")
        except ValueError:
            return render(self.request, "home.html")
