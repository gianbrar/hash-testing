x = .5
print("Welcome to Infinite Hash.")
hashStr = input("Please insert what you wish to be hashed.")
y = hashStr
while True:
   hashStr2 = str(hash(y))
   print("Your hash is: " + hashStr2)
   y = hashStr2
