# Loop Control Statemnts = change a loop execution from it's normal sequence
   
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as placeholder

while True:
    name =  input("Enter your name: ")
    if name != "":
        break

phone_number ="123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)