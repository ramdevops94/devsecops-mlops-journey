import requests
import os

print("===== DEVOPS AUTOMATION TOOL =====\n")

# 1. Check Nginx Status
print("\n🔹 Checking Nginx Status...")
status = os.popen("systemctl is-active nginx").read().strip()

if status == "active":
    print("✅ Nginx is running")
else:
    print("❌ Nginx is not running")

# 2. Show Last Logs
print("\n🔹 Last 5 Nginx Logs:")
os.system("tail -n 5 /var/log/nginx/access.log")

# 3. API Call
print("\n🔹 GitHub API Status:")
response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)

print("\n===== DONE =====")
