
import requests

print("===== DEVOPS TOOL (CONTAINERIZED) =====")

response = requests.get("https://api.github.com")

if response.status_code == 200:
    print("✅ GitHub API reachable")
else:
    print("❌ API issue")

print("===== DONE =====")
