# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

#Ask for student's grade percentage.
def gradePercentage():
    gradeInput = float(input("Input grade: "))
    return gradeInput 

#Test grade percentage to display Grade/Mark and Description
def gradingSystem():
    # Test grades from 97-100
    if student_grade >= 97 and student_grade <=100:
        print("Grade/Mark: 1.0")
        print("Description: Excellent")
    else:
        # Test grades from 94-96
        if student_grade >= 94 and student_grade <=96:
            print("Grade/Mark: 1.25")
            print("Description: Excellent")
        else:
            # Test grades from 91-93
            if student_grade >= 91 and student_grade <=93:
                print("Grade/Mark: 1.5")
                print("Description: Very Good")
            else:
                 # Test grades from 88-90
                if student_grade >= 88 and student_grade <=90:
                    print("Grade/Mark: 1.75")
                    print("Description: Very Good")
                else:
                    # Test grades from 85-87
                    if student_grade >= 85 and student_grade <=87:
                        print("Grade/Mark: 2.0")
                        print("Description: Good")
                    else:
                        # Test grades from 82-84
                        if student_grade >= 82 and student_grade <=84:
                            print("Grade/Mark: 2.25")
                            print("Description: Good")
                        else:
                            # Test grades from 79-81
                            if student_grade >= 79 and student_grade <=81:
                                print("Grade/Mark: 2.5")
                                print("Description: Satisfactory")
                            else:
                                # Test grades from 76-78
                                if student_grade >= 76 and student_grade <=78:
                                    print("Grade/Mark: 2.75")
                                    print("Description: Satisfactory")
                                else:
                                    # Test grade 75
                                    if student_grade == 75:
                                        print("Grade/Mark: 3.0")
                                        print("Description: Passing")
                                    else:
                                        # Test grades from 65-74
                                        if student_grade >= 65 and student_grade <=74:
                                            print("Grade/Mark: 5.0")
                                            print("Description: Failure")
    # Add some inspiring messages.    
    if student_grade >=75 and student_grade <=100:
        print("Great job! Keep up the good work. Always strive for success.")
    if student_grade >=65 and student_grade <=74:
        print("You can do so much better, just keep trying, real failures are quitters. Always be the best version of yourself.")

student_grade = gradePercentage()
grade_description = gradingSystem()