from typing import Any
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class IsUserAuthenticatedMixin:
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("analytics:home")
        form = self.form_class()
        return render(request, self.template_name, {"form": form})


class LoginView(IsUserAuthenticatedMixin, generic.TemplateView):
    template_name = "accounts/auth-signin.html"
    form_class = LoginForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data["form"] = self.form_class()
        return context_data

    def post(self, request):
        form = self.form_class(request.POST)
        print(form.errors)
        print(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username)
            print(password)

            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                
                login(request, user)
                return redirect("analytics:home")
        message = "Login failed!"
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )


class SignupView(IsUserAuthenticatedMixin, generic.CreateView):
    template_name = "accounts/auth-signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("user:login")


class UserLogoutView(LogoutView):
    next_page = "user:login"
