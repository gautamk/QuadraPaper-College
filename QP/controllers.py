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
    form ={
        "SubjectList":[],
        "ExamConfigs":[],
        "actionURL":GENERATION_URL
    }
    for Config in ExamConfiguration.objects.all():
        form ['ExamConfigs'].append(Config)
    for Sub in Subject.objects.all():
            form ['SubjectList'].append(Sub)
    return render_to_response('GenerationForm.html' ,form)
    
    
    
def GenerateQuestionPaper(request):
    from django.shortcuts import redirect
    if request.method == "GET":
        return redirect(GENERATION_FORM_URL)
    if not request.user.is_authenticated():
        return redirect("/")
