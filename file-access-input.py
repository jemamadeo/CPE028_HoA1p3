file= open("devices.txt", "a")
while True:
    newItem = input("Enter a device name: ")
    if newItem == "exit":
        print("All done! ")
        break
    file.write(newItem + "\n")
file.close