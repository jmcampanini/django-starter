import json
from django.http import HttpResponse
from django.shortcuts import render_to_response


def demo_view(request):
	return render_to_response("base.html", {})


def demo_ajax(request, num):
	data = {
		"html": "<li>From Server: %s" % num
	}
	jsond = json.dumps(data)
	return HttpResponse(jsond, mimetype="application/json")