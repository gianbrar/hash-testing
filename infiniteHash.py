x = .5
print("Welcome to Infinite Hash.")
hashStr = input("Please insert what you wish to be hashed.")
y = hashStr
hashQ = input("Do you wish to have an infinite hash [IH] or a multihash [MH]?").lower()
if hashQ == "ih":
    while True:
        hashStr2 = str(hash(y))
        print("Your hash is: " + hashStr2)
        y = hashStr2
