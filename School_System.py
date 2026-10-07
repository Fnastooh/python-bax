names = ["Parsa","Taha","Hessam","Mohammad","Akbar","Aria","Reza","Amir"]

marks = [18.5, 12, 8, 10.75, 6, 16.5, 9.5, 20]

for i in range(len(marks)):
    if marks[i] > 10:
        print(f"{names[i]} with Mark: {marks[i]} Has Graduated")
