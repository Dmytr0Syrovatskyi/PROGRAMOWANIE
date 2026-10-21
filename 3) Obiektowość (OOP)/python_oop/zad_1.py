class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False
        # Obliczanie średniej ocen
        srednia = sum(self.marks) / len(self.marks)
        return srednia > 50
    
    def __str__(self):
        return f"Student {self.name}"

if __name__ == '__main__':
    # Średnia > 50 (np. 70)
    student_zdajacy = Student("Anna Kowalska", [60, 70, 80])
    # Średnia <= 50 (np. 30)
    student_niezdajacy = Student("Jan Nowak", [20, 30, 40])

    print(f"{student_zdajacy.name} zdał(a)? {student_zdajacy.is_passed()}")
    print(f"{student_niezdajacy.name} zdał(a)? {student_niezdajacy.is_passed()}")