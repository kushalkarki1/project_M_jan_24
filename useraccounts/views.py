from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from useraccounts.forms import CustomSignupForm
from django.contrib.auth.views import LoginView
from django.template.loader import render_to_string
from django.core.mail import send_mail

# def login_view(request):
#     form = AuthenticationForm(request.POST or None)
#     if request.POST:
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if user.is_superuser:
#                 return HttpResponseRedirect("/admin/")
#             return HttpResponseRedirect(reverse("product:product_list"))
#     context = {"form": form}
#     return render(request, "login.html", context)

class UserLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    # def get_success_url(self):
    #     if self.request.user.is_superuser:
    #         return HttpResponseRedirect()
    #     else:
    #         return HttpResponseRedirect()


def signup_view(request):
    form = CustomSignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("user:login"))
    context = {"form": form}
    return render(request, "register.html", context)

def send_confirm_email(request):
    subject = "Test Subject"
    message = "Test message"
    from_email = "ytddash@gmail.com"
    recipient_list = ["samankhadgi@gmail.com", ]
    context = {'name': 'Python'}
    html_message = render_to_string('test.html',context)
    result = send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    return HttpResponse(result)