from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat meat every day",
    "february": "Walk every day",
    "march": "Learn django",
    "april": "Aprilllllll",
    "may": "Mayyyyyyyyyy",
    "june": "Juneeee",
    "july": "Julyyyyy",
    "august": "Augusttt",
    "september": "Septemberrrr",
    "october": "Octoberrrrr",
    "november": "Novemberrr",
    "december": None

}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "list_of_months": months
    })
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])

    #     list_items += f"<li><a href = \"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"""
    # <ul>
    #     {list_items}
    # </ul>
    # """
    # return HttpResponse(response_data)


# def january(request):
#     return HttpResponse("Eat meat every day")

# def february(request):
#     return HttpResponse("Walk every day")

# def march(request):
#     return HttpResponse("Learn django")

def monthly_challenge_by_number(request, month):
    all_months = list(monthly_challenges.keys())
    redirect_month = all_months[(month - 1) % len(monthly_challenges.keys())]
    # /challenges/redirect_month
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        raise Http404()
