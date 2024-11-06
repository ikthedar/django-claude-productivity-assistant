from django.shortcuts import render
import os
import requests
from django.http import JsonResponse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

# URL for Claude Sonnet API
CLAUDE_API_URL = "https://api.anthropic.com/v1/complete"

# Function to interact with Claude Sonnet API
def query_claude(prompt):
    headers = {
        "Authorization": f"Bearer {CLAUDE_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": prompt,
        "model": "claude-sonnet",  # Using the Claude Sonnet model
        "max_tokens": 300,
        "temperature": 0.5,
    }
    response = requests.post(CLAUDE_API_URL, headers=headers, json=data)
    
    # Check for errors in the response
    if response.status_code == 200:
        return response.json().get("completion")
    else:
        return "Error: Could not get a valid response from Claude API."

# View to handle user input and output
def productivity_assistant_view(request):
    if request.method == "POST":
        prompt = request.POST.get("query")
        response = query_claude(prompt)
        return JsonResponse({"response": response})
    return render(request, "assistant/home.html")