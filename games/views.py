from django.shortcuts import render

import json
from django.http import JsonResponse
from games.models import GameScore
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.views.generic import FormView

# Create your views here.
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class ContactUsView(TemplateView):
    template_name = "contact.html"

    

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class GameScoresView(TemplateView):
    template_name = "game-scores.html"

    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context

def record_score(request):
    data = json.loads(request.body)

    user_name = data["user-name"]
    game = data["game"]
    score = data["score"]

    new_score = GameScore(user_name=user_name, game=game, score=score)
    new_score.save()

    response = {
        "success": True
    }

    return JsonResponse(response)

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='What do you need?', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    def send_email(self):
        name = self.cleaned_data['name']
        contact_email = self.cleaned_data['contact_email']
        description = self.cleaned_data['description']
        
        send_mail(
            subject=f'New Contact Request from {name}',
            message=f'Name: {name}\nEmail: {contact_email}\n\nDescription:\n{description}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['btginnver1130@gmail.com'],
        )

    def contact_view(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    
class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm  # Ensure this is defined
    success_url = "/contact/"  # Redirect upon success

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Your message has been sent successfully!')
        return super().form_valid(form)