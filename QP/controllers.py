#!/usr/bin/python
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
from django.shortcuts import render_to_response
from QPaperGenerator.QP.urls import *

def GenerationForm(request):
    if request.method == "POST" or (not request.user.is_authenticated()) :
        from django.shortcuts import redirect
        return redirect("/")
    
    
    from QPaperGenerator.QP.models import ExamConfiguration , Subject
    from django.template import RequestContext
    form ={
        "SubjectList":[],
        "ExamConfigs":[],
        "actionURL":GENERATION_URL
    }
    for Config in ExamConfiguration.objects.all():
        form ['ExamConfigs'].append(Config)
    for Sub in Subject.objects.all():
            form ['SubjectList'].append(Sub)
    return render_to_response('GenerationForm.html' ,form , context_instance=RequestContext(request))


    
def GenerateQuestionPaper(request):
    
    from django.shortcuts import redirect
    from django.http import HttpResponse
    
#####################    
    if request.method == "POST":
        return redirect(GENERATION_FORM_URL)
    if not request.user.is_superuser:
        return redirect("/")
    response = HttpResponse()
#####################    
    
    from QPaperGenerator.QP.models import Question , Subject, ExamConfiguration
    subject_id = request.REQUEST["SubjectID"]
    
    #Get the list of units which are to be added in the Question Paper
    exam_config = ExamConfiguration.objects.filter(id = request.REQUEST["ExamConfigurationID"])[0]
    
    num_of_questions_in_partA = exam_config.num_of_questions_in_partA
    num_of_questions_in_partB = exam_config.num_of_questions_in_partB
    
    exam_config = exam_config.getUnitList()
        
    questions_per_unit_partA = num_of_questions_in_partA / exam_config.__len__() 
    extra_questions_per_unit_partA = num_of_questions_in_partA % exam_config.__len__()
    
    questions_per_unit_partB = num_of_questions_in_partB / exam_config.__len__() 
    extra_questions_per_unit_partB = num_of_questions_in_partB % exam_config.__len__()
     
    partA_questions = []
    partB_questions = []
    from random import random
##########
#
#   Generate Part A Questions
#    
##########
    remaining_questions=[]
    for ex in exam_config:
        
        #Get all the Questions in a unit
        q_list = []
        for q in Question.objects.filter(unit_number = ex , question_type = 'A'):
            q_list.append(q)
        
        #Add the number of Questions per unit 
        for i in range(questions_per_unit_partA):
            
            #Select a random Question and add it to the list 
            random_no = int( q_list.__len__() * random() )
            partA_questions.append(q_list[random_no])
            
            #Remove the question from the list to prevent duplication
            q_list.remove(q_list[random_no])
        
        # If there are extra questions 
        # To generate the extra Questions 
        # add the remaining Questions to a list  
        if not(extra_questions_per_unit_partA == 0):
            for q in q_list:
                remaining_questions.append(q)
               
    # Add Extra Questions
    for i in range(extra_questions_per_unit_partA):
        random_no = int( remaining_questions.__len__() * random() )
        partA_questions.append(remaining_questions[random_no])
        remaining_questions.remove(remaining_questions[random_no] )
##########
#
#   Generate Part B Questions
#    
##########
    remaining_questions=[]
    for ex in exam_config:
        
        #Get all the Questions in a unit
        q_list = []
        for q in Question.objects.filter(unit_number = ex , question_type = 'B'):
            q_list.append(q)
        
        #Add the number of Questions per unit 
        for i in range(questions_per_unit_partB):
            
            #Select a random Question and add it to the list 
            random_no = int( q_list.__len__() * random() )
            partB_questions.append(q_list[random_no])
            
            #Remove the question from the list to prevent duplication
            q_list.remove(q_list[random_no])
        
        # If there are extra questions 
        # To generate the extra Questions 
        # add the remaining Questions to a list  
        if not(extra_questions_per_unit_partA == 0):
            for q in q_list:
                remaining_questions.append(q)
               
    # Add Extra Questions
    for i in range(extra_questions_per_unit_partA):
        random_no = int( remaining_questions.__len__() * random() )
        partB_questions.append(remaining_questions[random_no])
        remaining_questions.remove(remaining_questions[random_no] )
    
    
    for a  in partA_questions :
        response.write(a.__str__() +"<br>")
    for b in partB_questions:
        response.write(b.__str__()+"<br>")
    
    
    return response
