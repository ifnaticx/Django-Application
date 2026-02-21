from django.http import HttpResponse
from .models import TextRecord

def add_record(request):
    TextRecord.objects.create(content="Hello from Django!")
    return HttpResponse("Text added successfully!")

def show_records(request):
    records = TextRecord.objects.all()
    output = ""
    for record in records:
        output += f"{record.content}<br>"
    return HttpResponse(output)