f = open("/opt/homebrew/etc/mosquitto/mosquitto.log", "r")
lines = f.readlines()
line = ""
count = 0
for line in lines:
    if "SUBSCRIBE" in line:
        x = line.split("from ")
        print((x[-1:])[0].strip())