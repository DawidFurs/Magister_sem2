import Student.zad_1_Student
import Library.zad_2_Library
import Property.zad_3_Property

Dawid = Student.zad_1_Student.Student("Dawid", [10, 20, 30, 40, 50, 60, 70, 80, 90])

Dawid.is_passed()

# jeśli wewnątrz importu są już wywołania to będą wywołane podczas importowania