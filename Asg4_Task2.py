from decorator import append

file_name = "output.txt"

str = input("Enter text to write to the file: ")
file = open(file_name,"w")
file.write(str+"\n")
file.close()

str = input("Enter additional text to append : ")
file = open(file_name,"a")
file.write(str)
file.close()

print(f"Final content of file {file_name} :")
file = open(file_name,"r")
print(file.read())
file.close()
