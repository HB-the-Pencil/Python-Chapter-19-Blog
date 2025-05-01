from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Display a blank form.
        form = UserCreationForm()
    else:
        # Submit the form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the new user in.
            login(request, new_user)
            return redirect("blogs:index")

    # Display the form.
    context = {"form": form}
    return render(request, "registration/register.html", context)