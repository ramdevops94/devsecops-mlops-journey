import requests

url = "https://api.github.com/repos/ramdevops94/devsecops-mlops-journey"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Repo Name:", data["name"])
    print("Stars:", data["stargazers_count"])
    print("Forks:", data["forks_count"])
else:
    print("Error:", response.status_code)
