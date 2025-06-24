class student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll_no = roll
        self.sub_marks = marks
    def percentage(self):
        total_marks = sum(self.sub_marks.values())
        total_subject = len(self.sub_marks)
        percentage =( total_marks/(total_subject*100))*100
        return round(percentage,2)

    def display(self):
        print("Name of student:",self.name)
        print("Roll_Number:",self.roll_no)
        print("Percentage:",self.percentage())



subject_marks = {"Marathi":99,"Hindi":89,"English":97,"Maths":98,"science":88}

s = student("Pallavi Mohite",36,subject_marks)
s.display()