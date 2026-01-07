#Core-Track Clinical Data Audit System
#Patient Detail
name=input("Enter Patient name: ")
age=input("Enter Age : ")
num_reading=int(input("Enter number of heart rate readings: \n"))
def hr(num_reading):
	if num_reading==0:
		return None
	else:
		h=int(input("Enter Heart Rate Reading : "))
		hr_list.append(h)
		hr(num_reading-1)
hr_list=[]
hr(num_reading)
#validating age
if age.isdigit():
	if 0<int(age)<121:
		d=None
	if int(age)<=0 or int(age)>120:
		d="flag"
else:
	d="flag"
#raising warning
g="None"
for i in hr_list:
	if i>180:
		g="High heart rate detected"
#raising invalid
if d=="flag":
	j="Invalid Age"
else:
	j="None"
#Final Audit Status
print(f"\n ---CILINICAL AUDIT RESULT--- \nPatient : {name}")
if j=="Invalid Age":
	Status="Fail"
elif j=="None" and g=="High heart rate detected":
	Status="Review"
else:
	Status="Pass"
print(f"Status : {Status}")
print(f"Flag : {j}")
print(f"Warning : {g}")
