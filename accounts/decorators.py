from functools import wraps
from django.shortcuts import redirect


def candidate_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role == "CANDIDATE":
            return view_func(request, *args, **kwargs)

        return redirect("home")

    return wrapper

def employer_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role == "EMPLOYER":
            return view_func(request, *args, **kwargs)

        return redirect("home")

    return wrapper