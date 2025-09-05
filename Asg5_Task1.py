results = { "Saurabh":70,
            "Alice":39,
            "Deepika":85,
            "Ali": 55
}

name = input("Enter student's name: ")
try:

    marks = int(results[name])
    print(f"{name}'s marks:",marks)

except KeyError:
    print("Student not found")
