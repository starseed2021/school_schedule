from school_schedule.student import Student

def test_student_class_name_is_correct():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])
  # assert
  assert student.name == "Trenisha"

def test_add_class_adds_class():
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])
  
  student.classes.append("Ceramics")
  assert student.classes == ["Calculus", "Choir", "Photography", "AP History", "Ceramics"]

def test_length_is_correct():

  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])

  list_length = student.get_num_classes()
  assert list_length == 4


