choice = None
students = []
def getChoice():

	choice = input("""Please enter your choice:
			1. Add a student.
			2. View a student.
			3. View all students.
			4. Update student info.
			5. Delete a student.\n""")

	if choice == "1":
		name = input("What's the student's name?\n")
		age = input("How old is the student?\n")
		grade = input("What's the student's grade?\n")

		students.append({"Name":name, "Age":age, "Grade":grade})
		print(f"*{name} succesfully added to students list.")

	elif choice == "2":
		name = input("What is the student's name?\n")
		for student in students:
			if student['Name'] == name:
				print(f"""  
		Name: {student["Name"]}
		Age: {student["Age"]}
		Grade: {student["Grade"]}\n""")

	elif choice == "3":
		print("Students:\n")
		for student in students:
			print(f"\t{student['Name']}")

	elif choice == "4":
		name = input("What is the student's name?\n")
		for student in students:
			if student['Name'] == name:
				student["Name"] = input(f"What name do you want to Update to?(current name is {student['Name']})")
				student["Age"] = input(f"What is the new age?(current age is {student['Age']})")
				student["Grade"] = input(f"What is the new Grade?(current age is {student['Grade']})")

			print("*Student info succesfully updated.")

	elif choice == "5":
		name = input("What is the student's name?\n")
		for student in students:
			if student['Name'] == name:
				students.remove(student)

		print(f"*{student['Name']} removed from student list.")

	getChoice()


getChoice()