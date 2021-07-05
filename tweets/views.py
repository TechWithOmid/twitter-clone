from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Tweet


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html")


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content": x.content, "likes": 489} for x in qs]
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
