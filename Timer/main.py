import time
seconds = int(input("Enter seconds: "))

for i in range(seconds):
    print(str(seconds-i)+"\n")
    time.sleep(1)
print("Time is over")
