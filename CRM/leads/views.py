from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Agent, Lead
from .forms import LeadModelForm

class LandingPageView(generic.TemplateView):
    template_name="landing.html"

# def landing_page(request):
    # return render(request, "landing.html")

class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset= Lead.objects.all()

# def lead_list(request):
    # leads = Lead.objects.all()
    # context = {
            # "leads": leads
            # }
    # return render(request, "leads/lead_list.html", context)

class LeadDetailView(generic.DetailView):
    template_name="leads/lead_detail.html"
    queryset= Lead.objects.all()
    context_object_name="lead"



# def lead_detail(request, pk):
    # lead = Lead.objects.get(id=pk)
    # context = {
            # "lead":lead
            # }
    # return render(request, "leads/lead_detail.html", context)

class LeadCreateView(generic.CreateView):
    template_name="leads/lead_create.html"
    form_class=LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
                subject="A new lead has been created",
                message="Visit our website to see the new lead.",
                from_email="test@test.com",
                recipient_list=["test2@test.com"]
                )
        return super(LeadCreateView, self).form_valid(form)


# def lead_create(request):
    # form = LeadModelForm()
    # if request.method == 'POST':
        # form = LeadModelForm(request.POST)
        # if form.is_valid():
            # form.save()
            # # first_name = form.cleaned_data['first_name']
            # # last_name = form.cleaned_data['last_name']
            # # age = form.cleaned_data['age']
            # # agent = form.cleaned_data['agent']
            # # Lead.objects.create(
                    # # first_name=first_name,
                    # # last_name=last_name,
                    # # age=age,
                    # # agent=agent
                    # # )
            # return redirect("/leads")
    # context = {
            # "form": form
    # }
    # return render(request, "leads/lead_create.html", context)

class LeadUpdateView(generic.UpdateView):
    template_name="leads/lead_update.html"
    form_class=LeadModelForm
    queryset= Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

# def lead_update(request, pk):
    # lead = Lead.objects.get(id=pk)
    # form = LeadModelForm(instance=lead)
    # if request.method == 'POST':
        # form = LeadModelForm(request.POST, instance=lead)
        # if form.is_valid():
            # form.save()
            # return redirect("/leads")
    # context = {
            # "form": form,
            # "lead": lead
            # }
    # return render(request, "leads/lead_update.html", context)

class LeadDeleteView(generic.DeleteView):
    template_name="leads/lead_delete.html"
    queryset= Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

# def lead_delete(request, pk):
    # lead = Lead.objects.get(id=pk)
    # lead.delete()
    # form = LeadModelForm(instance=lead)
    # return redirect("/leads")

