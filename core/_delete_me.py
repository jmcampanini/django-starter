import json
from django.http import HttpResponse
from django.shortcuts import render_to_response


def demo_view(request):
    """
    Shows the `sample.html` template to the browser
    """
    return render_to_response("sample.html", {})


def demo_ajax(request, num):
    """
    Called by the `bootstrap-ajax` plugin.
    """
    html = "<li>From Server: %s" % num
    data = {
        "html": html
    }
    jsond = json.dumps(data)
    return HttpResponse(jsond, mimetype="application/json")
