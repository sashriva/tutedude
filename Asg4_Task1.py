
try:
    file_name = "sample.txt"
    f = open(file_name,"r")

    print("Reading file content:")
    list_lines = f.readlines()
    i=1
    for x in list_lines:
      print("Line ",i," : ",x.strip("\n"))
      i = i+1

    f.close()
except FileNotFoundError:
  print(f"Error : The file '{file_name}' was not found")

