port = int(input("Enter port number: "))

if port == 80:
    print("HTTP port detected")
elif port == 22:
    print("SSH port detected")
else:
    print("Unknown port")
