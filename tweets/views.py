from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .forms import TweetForm
from .models import Tweet


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html")


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()
        form = TweetForm()
    return render(request, "components/form.html", context={'form': form})


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    """
    qs = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content": x.content, "likes": 42} for x in qs]
    data = {
        "isUser": False,
        "response": tweet_list,
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id):
    """
    REST API VIEW
    """
    data = {
        "id": tweet_id,
    }

    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except ObjectDoesNotExist:
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)
