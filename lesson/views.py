from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def learning_content(request):
  template = loader.get_template('learning_content.html')
  return HttpResponse(template.render())

def implementation(request):
  template = loader.get_template('implementation.html')
  return HttpResponse(template.render())

def pdf_viewer(request):
  template = loader.get_template('pdf_viewer.html')
  return HttpResponse(template.render())