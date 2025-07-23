from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menurad(request, phone):
    items = {
        'Apple': 'Is a technology company known for the iPhone, offering premium devices with iOS as the operating system',
        'Samsung': 'Is a South Korean company producing a wide range of smartphones, especially known for its Galaxy series running Android',
        'Xiaomi': 'Is a Chinese electronics company offering budget-friendly and flagship smartphones with MIUI (based on Android)',
        'Huawei': 'Is a major Chinese smartphone brand known for its strong camera systems and custom EMUI interface',
        'OnePlus': 'Is a smartphone brand known for performance-focused Android devices with clean software and competitive pricing',
        'Google': 'Is the maker of the Pixel phones, offering a pure Android experience and early access to the latest features'
    }
    des =items[phone]
    return HttpResponse(f"<h1> {phone}</h1>\n"+ des)
