numbers = [ 4,7,3,7,2,7,4,3, 12 ,45,32,5,7,9,3,2,55,88,53,8,95,3,51,3,5,64]

x = input("Please enter your number: ")
y = input("Please enter your second number: ")

a = int(x)
b = int(y)


for i in range(len(numbers)):
    if a > numbers[i] or b < numbers[i]:
        print(f"index = {i}, value = {numbers[i]}")

z = input("hvchcf")

# ----------------------------------------------------------------------------------------

friends = ["akbar" , "ali", "karim", "hossein" , "reza" , "javad", "amir", "kabir", "zohre", "parsa", "zahra", "mehdi", "abdi", "samira", "amirhossein", "amirmohammad", "amirkabir"]

x = input("Enter your Letter: ")

y = x.lower()

for i in range(len(friends)):
    if y in friends[i] and friends[i].startswith("amir"):
        print(f"index = {i}, name = {friends[i]}")