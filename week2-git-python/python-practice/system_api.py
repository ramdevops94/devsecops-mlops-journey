import requests
import os

print("=== SYSTEM INFO ===")
os.system("uptime")

print("\n=== GITHUB API ===")
response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
