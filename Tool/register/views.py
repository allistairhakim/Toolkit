from django.shortcuts import render

def logout_request(request):
    logout(request)
    message.info(request, "Logged out successfuly!")
    return redirect("gadgets-home")
