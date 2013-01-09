import json
from django.http import HttpResponse
from django.shortcuts import render_to_response


def demo_view(request):
    return render_to_response("sample.html", {})


def demo_ajax(request, num):
    html = "<li>From Server: %s" % num
    data = {
        "html": html
    }
    jsond = json.dumps(data)
    return HttpResponse(jsond, mimetype="application/json")
