list_names = []
list_dob = []

dob = open("DOB.txt","r+")            # Import and open the txt file into the programm

names = dob.readlines()

for i in names:
    cut = i.split()
    list_names.append(cut[ :2])
    list_dob.append(cut[2: ])

dob.close()                             # Close the txt file

print("names:")
for i in list_names:
    print(i)
print("DOB:")
for i in list_dob:
    print(i)
