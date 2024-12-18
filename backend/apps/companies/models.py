
from django.db import models
from ..institutions.models import Institution

KIND_CHOICES = {
    "MATRIZ": "Matriz",
    "FILIAL": "Filial",
}

NATURE_LEGAL_CHOICES = {
    "101-5": "101-5 - Órgão Público do Poder Executivo Federal",
    "102-3": "102-3 - Órgão Público do Poder Executivo Estadual ou do Distrito Federal",
    "103-1": "103-1 - Órgão Público do Poder Executivo Municipal",
    "104-0": "104-0 - Órgão Público do Poder Legislativo Federal",
    "105-8": "105-8 - Órgão Público do Poder Legislativo Estadual ou do Distrito Federal",
    "106-6": "106-6 - Órgão Público do Poder Legislativo Municipal",
    "107-4": "107-4 - Órgão Público do Poder Judiciário Federal ",
    "108-2": "108-2 - Órgão Público do Poder Judiciário Estadual",
    "110-4": "110-4 - Autarquia Federal",
    "111-2": "111-2 - Autarquia Estadual ou do Distrito Federal",
    "112-0": "112-0 - Autarquia Municipal ",
    "113-9": "113-9 - Fundação Pública de Direito Público Federal",
    "114-7": "114-7 - Fundação Pública de Direito Público Estadual ou do Distrito Federal",
    "115-5": "115-5 - Fundação Pública de Direito Público Municipal",
    "116-3": "116-3 - Órgão Público Autônomo Federal",
    "117-1": "117-1 - Órgão Público Autônomo Estadual ou do Distrito Federal",
    "118-0": "118-0 - Órgão Público Autônomo Municipal",
    "119-8": "119-8 - Comissão Polinacional",
    "121-0": "121-0 - Consórcio Público de Direito Público (Associação Pública)",
    "122-8": "122-8 - Consórcio Público de Direito Privado",
    "123-6": "123-6 - Estado ou Distrito Federal",
    "124-4": "124-4 - Município",
    "125-2": "125-2 - Fundação Pública de Direito Privado Federal",
    "126-0": "126-0 - Fundação Pública de Direito Privado Estadual ou do Distrito Federal",
    "127-9": "127-9 - Fundação Pública de Direito Privado Municipal",
    "128-7": "128-7 - Fundo Público da Administração Indireta Federal",
    "129-5": "129-5 - Fundo Público da Administração Indireta Estadual ou do Distrito Federal",
    "130-9": "130-9 - Fundo Público da Administração Indireta Municipal",
    "131-7": "131-7 - Fundo Público da Administração Direta Federal",
    "132-5": "132-5 - Fundo Público da Administração Direta Estadual ou do Distrito Federal",
    "133-3": "133-3 - Fundo Público da Administração Direta Municipal",
    "134-1": "134-1 - União",
    "201-1": "201-1 - Empresa Pública",
    "203-8": "203-8 - Sociedade de Economia Mista",
    "204-6": "204-6 - Sociedade Anônima Aberta",
    "205-4": "205-4 - Sociedade Anônima Fechada",
    "206-2": "206-2 - Sociedade Empresária Limitada",
    "207-0": "207-0 - Sociedade Empresária em Nome Coletivo",
    "208-9": "208-9 - Sociedade Empresária em Comandita Simples",
    "209-7": "209-7 - Sociedade Empresária em Comandita por Ações",
    "212-7": "212-7 - Sociedade em Conta de Participação",
    "213-5": "213-5 - Empresário (Individual)",
    "214-3": "214-3 - Cooperativa",
    "215-1": "215-1 - Consórcio de Sociedades",
    "216-0": "216-0 - Grupo de Sociedades",
    "217-8": "217-8 - Estabelecimento, no Brasil, de Sociedade Estrangeira",
    "219-4": "219-4 - Estabelecimento, no Brasil, de Empresa Binacional Argentino-Brasileira",
    "221-6": "221-6 - Empresa Domiciliada no Exterior",
    "222-4": "222-4 - Clube/Fundo de Investimento",
    "223-2": "223-2 - Sociedade Simples Pura",
    "224-0": "224-0 - Sociedade Simples Limitada",
    "225-9": "225-9 - Sociedade Simples em Nome Coletivo",
    "226-7": "226-7 - Sociedade Simples em Comandita Simples",
    "227-5": "227-5 - Empresa Binacional",
    "228-3": "228-3 - Consórcio de Empregadores",
    "229-1": "229-1 - Consórcio Simples",
    "230-5": "230-5 - Empresa Individual de Responsabilidade Limitada (de Natureza Empresária)",
    "231-3": "231-3 - Empresa Individual de Responsabilidade Limitada (de Natureza Simples)",
    "232-1": "232-1 – Sociedade Unipessoal de Advogados",
    "233-0": "233-0 – Cooperativas de Consumo",
    "234-8": "234-8 – Empresa Simples de Inovação - Inova Simples",
    "235-6": "235-6 – Investidor Não Residente",
    "303-4": "303-4 - Serviço Notarial e Registral (Cartório)",
    "306-9": "306-9 - Fundação Privada",
    "307-7": "307-7 - Serviço Social Autônomo",
    "308-5": "308-5 - Condomínio Edilício",
    "310-7": "310-7 - Comissão de Conciliação Prévia",
    "311-5": "311-5 - Entidade de Mediação e Arbitragem",
    "313-1": "313-1 - Entidade Sindical",
    "320-4": "320-4 - Estabelecimento, no Brasil, de Fundação ou Associação Estrangeiras",
    "321-2": "321-2 - Fundação ou Associação Domiciliada no Exterior",
    "322-0": "322-0 - Organização Religiosa ",
    "323-9": "323-9 - Comunidade Indígena ",
    "324-7": "324-7 - Fundo Privado ",
    "325-5": "325-5 - Órgão de Direção Nacional de Partido Político",
    "326-3": "326-3 - Órgão de Direção Regional de Partido Político",
    "327-1": "327-1 - Órgão de Direção Local de Partido Político",
    "328-0": "328-0 - Comitê Financeiro de Partido Político",
    "329-8": "329-8 - Frente Plebiscitária ou Referendária",
    "330-1": "330-1 - Organização Social (OS)",
    "331-0": "331-0 - Demais Condomínios",
    "332-8": "332-8 - Plano de Benefícios de Previdência Complementar Fechada",
    "399-9": "399-9 - Associação Privada",
    "401-4": "401-4 - Empresa Individual Imobiliária",
    "402-2": "402-2 - Segurado Especial",
    "408-1": "408-1 - Contribuinte individual",
    "409-0": "409-0 - Candidato a Cargo Político Eletivo",
    "411-1": "411-1 - Leiloeiro ",
    "412-0": "412-0 - Produtor Rural (Pessoa Física)",
    "501-0": "501-0 - Organização Internacional",
    "502-9": "502-9 - Representação Diplomática Estrangeira",
    "503-7": "503-7 - Outras Instituições Extraterritoriais",
}

REGIME_CHOICES = {
    "PRESUMIDO": "Lucro Presumido",
    "REAL": "Lucro Real",
    "SIMEI": "SIMEI",
    "SIMPLES": "Simples Nacional",
}

RESPONSIBILITY_CHOICES = {
    "SÓCIO-ADMINISTRADOR": "Sócio-Administrador",
    "SÓCIO": "Sócio",
    "PROCURADOR": "Procurador",
    "ADMINISTRADOR": "Administrador",
    "CONSELHEIRO": "Conselheiro de Administração",
    "CONTADOR": "Contador",
    "DIRETOR": "Diretor",
    "PRESIDENTE": "Presidente",
    "RESPONSÁVEL": "Responsável Financeiro",
}

SITUATION_CHOICES = {
    "ATIVO": "Ativo",
    "INATIVO": "Inativo",
}

SIZE_CHOICES = {
    "GRANDE": "Empresa de Grande Porte",
    "MÉDIO": "Empresa de Médio Porte",
    "EPP": "Empresa de Pequeno Porte (EPP)",
    "ME": "Microempresa",
    "MEI": "Micro Empreendedor Individual (MEI)",
}


class Activity (models.Model):
    code = models.CharField(max_length=7)
    description =  models.CharField()

    class Meta:
        db_table = "activities"

    def __str__(self):
        return f"{ self.code } - { self.description}"


class Contact (models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.CharField(unique=True)
    # institution

    class Meta:
        db_table = "contacts"

    def __str__(self):
        return self.name


class Society (models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    responsibility = models.CharField(RESPONSIBILITY_CHOICES)

    class Meta:
        db_table = "societies"

    def __str__(self):
        return f"{ self.responsibility } - { self.contact}"


class Company (models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    constitution = models.DateField()
    kind = models.CharField(KIND_CHOICES)
    social_capital = models.DecimalField(decimal_places=2)
    primary_activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    secondary_activity = models.ManyToManyField(Activity, on_delete=models.CASCADE, related_name="secondary_activity")
    regime = models.CharField(max_length=7, choices=REGIME_CHOICES)
    size = models.CharField(max_length=7, choices=SIZE_CHOICES)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=8)
    nature_legal = models.CharField(choices=NATURE_LEGAL_CHOICES)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    situation = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "companies"

    def __str__(self):
        return f"{ self.name } - { self.cnpj}"




