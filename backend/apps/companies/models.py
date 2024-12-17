from django.db import models
from ..institutions.models import Institution

ACTIVITY_CHOICES = {
    "COMÉRCIO": "Comércio",
    "INDÚSTRIA": "Indústria",
    "PRESTAÇÃO DE SERVIÇOS": "Prestação de Serviços",
    "COMÉRCIO E INDÚSTRIA": "Comércio e Indústria",
    "COMÉRCIO E PRESTAÇÃO DE SERVIÇOS": "Comércio e Prestação de Serviços",
}

REGIME_CHOICES = {
    "PRESUMIDO": "Lucro Presumido",
    "REAL": "Lucro Real",
    "SIMPLES": "Simples Nacional",
}

SECTOR_CHOICES = {
    # AGRICULTURA
    "AGRICULTURA - GERAL": "AGRICULTURA - GERAL",
    "AGRICULTURA - CAFÉ": "AGRICULTURA - CAFÉ",
    "AGRICULTURA - INDÚSTRIA SUCROALCOOLEIRA": "AGRICULTURA - INDÚSTRIA SUCROALCOOLEIRA",
    "AGRICULTURA - SOJA E BIODIESEL": "AGRICULTURA - SOJA E BIODIESEL",    
    # Alimentos e Bebidas

    # Autopeças e Veículos
    
    # BENS DE CAPITAL
    "BENS DE CAPITAL - MÁQUINAS E EQUIPAMENTOS": "BENS DE CAPITAL - MÁQUINAS E EQUIPAMENTOS",
    # CARTÕES DE CRÉDITO
    "CARTÃO DE CRÉDITO - MEIOS DE PAGAMENTO": "CARTÃO DE CRÉDITO - MEIOS DE PAGAMENTO",
    # Comércio
    
    # Construção
    
    # Eletroeletrônia
    
    # EMBALAGENS
    "EMBALAGENS": "EMBALAGENS",
    # Energia Elétrica
    
    # ENSINO
    "ENSINO": "ENSINO",
    # FUNDIÇÃO
    "FUNDIÇÃO": "FUNDIÇÃO",
    # GÁS NATURAL
    "GÁS NATURAL": "GÁS NATURAL",
    # HOTÉIS E TURISMO
    "HOTÉIS E TURISMO": "HOTÉIS E TURISMO",

    # Instituições Financeiras
    # 
    # Insumos Agrícolas
    # 
    # Mineração e Metais
    # 
    # MÓVEIS
    "MÓVEIS": "MÓVEIS",
    # PAPEL E CELULOSE
    "PAPEL E CELULOSE": "PAPEL E CELULOSE",
    # Petróleo, Derivados e Biocombustível

    # Produtos de Higiene e Limpeza

    # Química e Petroquímica

    # SAÚDE
    "SAÚDE": "SAÚDE",
    # SIDERURGIA
    "SIDERURGIA": "SIDERURGIA",
    # Telecomunicações

    # Têxtil e Vestuário

    # Transporte e Logística
      
}

SIZE_CHOICES = {
    "GRANDE": "Empresa de Grande Porte",
    "MÉDIO": "Empresa de Médio Porte",
    "EPP": "Empresa de Pequeno Porte (EPP)",
    "ME": "Microempresa",
    "MEI": "Micro Empreendedor Individual (MEI)",
}


class Company (models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    activity = models.CharField(max_length=10, choices=SIZE_CHOICES)
    regime = models.CharField(max_length=7, choices=SIZE_CHOICES)
    size = models.CharField(max_length=7, choices=SIZE_CHOICES)
    sector = models.CharField(max_length=7, choices=SECTOR_CHOICES)    
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "companies"

    def __str__(self):
        return f"{ self.name } - { self.cnpj}"
