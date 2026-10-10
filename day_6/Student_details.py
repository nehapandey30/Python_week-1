student = {
    "name": "neha",
    "age": 18,
    "marks": 97
}
print(student["age"])
print(student["marks"])
print(student.get("name"))
print(student)
# marks update
student["marks"]=100
print(student)
# name and roll no update
student["name"]="Jyoti"
student["roll_no"]=10
print(student)
print(student.keys())