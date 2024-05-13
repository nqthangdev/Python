class Person:

    def __init__(self, Fullname, Birth, Email, Address):
        self.Fullname = Fullname
        self.Birth = Birth
        self.Email = Email
        self.Address = Address

    def showInf(self):
        print("Ho ten : ", self.Fullname)
        print("Nam sinh : ",self.Birth)
        print("Email : ",self.Address)

class Course:

    def __init__(self, Name, Language):
        self.Name = Name
        self.Language = Language
        
    def showCourse(self):
        print("Ten khoa hoc : ", self.Name)
        print("Ngon ngu : ",self.Language)

class Student(Person, Course):

    def __init__(self, Fullname, Birth, Email, Address, student_id, university, Name, Language):
        super().__init__(Fullname, Birth, Email, Address)
        self.student_id = student_id
        self.university = university
        self.course = Course(Name, Language)

    def show(self):
        super().showInf()
        print(f"Mã sinh viên: {self.student_id}")
        print(f"Trường đại học: {self.university}")
        self.course.showCourse()

def main():
    student = Student("Nguyễn Quý Thắng", 2003, "ngqthang@gmail.com", "Thái Bình", "SV12345", "Đại học Kinh Tế Kỹ Thuật Công Nghiệp (UNETI)", "Lập trình Python", "Python")

    student.showInf()

main()
        