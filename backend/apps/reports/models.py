from django.db import models
from ..institutions.models import Institution
from ..companies.models import Company

YES_OR_NO_CHOICES = {
    "NÃO": "Não",
    "SIM": "Sim",
}

class Report (models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    company =  models.ForeignKey(Company, on_delete=models.CASCADE)

    #ide_activity = 
    #ide_activity_change =
    #ide_society_change = 

    #adm_documents = 
    #adm_management = 
    #adm_qualification = 
    #adm_decision_process = 
    #adm_powers = 
    #adm_succession_process = 
    #adm_other = 
    
    #fac
    #inf
    #loc
    #tal
    #pro
    #pss
    #com
    #sto
    #sup
    #cus
    #mkt
    #inv
    #fin
    #ctr
    #peo
    #ite
    #esg
    #res
    #tre
    
    #opinion = 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

