from django.shortcuts import render
import google.generativeai as genai

def home(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        genai.configure(api_key="AIzaSyC2NV9f63VL10pRlBgYk0tFyas439wypnY")
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        if user_input:
            response = model.generate_content(user_input)
            result = response.text


    return render(request, "home.html", {"result": result})
