# Create your views here.
from django.shortcuts import render_to_response , redirect
from QPaperGenerator.QP.forms import *
from QPaperGenerator.QP.models import *
from django.http import HttpRequest ,HttpResponse

def Root_url(request):
        return redirect('/admin')

def GenerateQuestionPaperGetDetails(request):
    form  = {
            "form" :False,
            'location' : '/GenerateQPaper',
            }
    if request.method == "GET":
        form['form'] = []
        for Sub in Subject.objects.all():
            form ['form'].append(Sub)       
    return render_to_response('Question_paper_internal.html' ,form)

def GenerateQuestionPaperFromDetails(request):
    
    template_values = {}
    UnitNumber = [3 , 4]
    if request.method == 'GET':
        if request.GET['SubjectName'] == '':
            return HttpResponse('Unkown Subject')
        from random import random
        subject = request.GET['SubjectName']
        subject = Subject.objects.all().filter(name = subject)
        questions = Question.objects.all().filter(subject = subject[0])
        
        part_a_questions = questions.filter(question_type = 'A')
        part_b_questions = questions.filter(question_type = 'B')
        
        part_a_unit_1 = part_a_questions.filter(unit_number = UnitNumber[0])
        part_a_unit_2 = part_a_questions.filter(unit_number = UnitNumber[1])
        
        part_b_unit_1 = part_b_questions.filter(unit_number = UnitNumber[0])
        part_b_unit_2 = part_b_questions.filter(unit_number = UnitNumber[1])
        QpaperA = []
        QpaperB = []
        
        qlist = []        
        for p in part_a_unit_1:
            qlist.append(p)
        for i in range(5):
            random_no = int( qlist.__len__() * random()  )
            QpaperA.append(   qlist[ random_no ]   )
            qlist.remove( qlist[ random_no ])
        
        qlist = []        
        for p in part_a_unit_2:
            qlist.append(p)
        for i in range(5):
            random_no = int( qlist.__len__() * random() )
            QpaperA.append(   qlist[ random_no ]   )
            qlist.remove( qlist[ random_no ])
        
        qlist = []        
        for p in part_b_unit_1:
            qlist.append(p)
        for i in range(2):
            random_no = int( qlist.__len__() * random() )
            QpaperB.append(   qlist[ random_no  ]   )
            qlist.remove( qlist[ random_no ])
        
        qlist = []        
        for p in part_b_unit_2:
            qlist.append(p)
        for i in range(2):
            random_no = int( qlist.__len__() * random() )
            QpaperB.append(   qlist[ random_no ]   )
            qlist.remove( qlist[ random_no ])
        template_values = {
        'form' : False ,
        'Subject':subject[0],
        'QpaperA' : QpaperA,
        'QpaperB' : QpaperB,
        }
    return render_to_response('Question_paper_internal.html', template_values)
        
    
