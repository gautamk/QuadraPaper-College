
from QPaperGenerator.QP.models import *
sub = Subject.objects.filter(id=1)[0]
for i in range(50):
     Question(subject = sub,
      question = "Part A Unit 2 Question %d "%(i) , 
      question_type = "A" , 
      unit_number =2 ).save()
for i in range(50):
     Question(subject = sub,
      question = "Part B Unit 2 Question %d "%(i) , 
      question_type = "B" , 
      unit_number =2 ).save()
#######################################################
for i in range(50):
     Question(subject = sub,
      question = "Part A Unit 3 Question %d "%(i) , 
      question_type = "A" , 
      unit_number =3 ).save()
for i in range(50):
     Question(subject = sub,
      question = "Part B Unit 3 Question %d "%(i) , 
      question_type = "B" , 
      unit_number =3 ).save()
#######################################################
for i in range(50):
     Question(subject = sub,
      question = "Part A Unit 4 Question %d "%(i) , 
      question_type = "A" , 
      unit_number =4 ).save()
for i in range(50):
     Question(subject = sub,
      question = "Part B Unit 4 Question %d "%(i) , 
      question_type = "B" , 
      unit_number =4 ).save()
#######################################################
for i in range(50):
     Question(subject = sub,
      question = "Part A Unit 5 Question %d "%(i) , 
      question_type = "A" , 
      unit_number =5 ).save()
for i in range(50):
     Question(subject = sub,
      question = "Part B Unit 5 Question %d "%(i) , 
      question_type = "B" , 
      unit_number =5 ).save()
