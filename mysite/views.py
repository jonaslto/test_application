from __future__ import absolute_import

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from braces import views

from talks.models import TalkList

from .forms import RegistrationForm, LoginForm, NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse_lazy('send'))
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

class SignUpView(views.AnonymousRequiredMixin, views.FormValidMessageMixin,
                 generic.CreateView):
    form_class = RegistrationForm
    form_valid_message = "Thanks for signing up! Go ahead and login."
    model = User
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        resp = super(SignUpView, self).form_valid(form)
        TalkList.objects.create(user=self.object, name='To Attend')
        return resp


class LoginView(views.AnonymousRequiredMixin, views.FormValidMessageMixin,
                generic.FormView):
    form_class = LoginForm
    form_valid_message = "You're logged into your account."
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class OutPageView(generic.TemplateView):
    template_name = 'out.html'

class LogoutView(views.LoginRequiredMixin, views.MessageMixin,
                 generic.RedirectView):
    url = reverse_lazy('out')
    def get(self, request, *args, **kwargs):
        self.messages.success("You've been logged out. Come back soon!")
        logout(request)
        #return super(LogoutView, self).get(request, *args, **kwargs)
        return HttpResponseRedirect('/')

class SendPageView(generic.TemplateView, generic.RedirectView):
    template_name = 'send.html'

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('sendconf'))

class SendConfirmPageView(generic.TemplateView, generic.RedirectView):
    template_name = 'send.html'
