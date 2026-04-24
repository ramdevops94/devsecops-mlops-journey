file = open("/var/log/nginx/access.log", "r")

lines = file.readlines()

print("Last 5 log entries:")

for line in lines[-5:]:
    print(line)

file.close()
