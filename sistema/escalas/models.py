from django.db import models

POSTO_CHOICE = (
    ('1', 'Soldado'),
    ('2', 'Cabo'),
    ('3', '3 Sargento'),
    ('4', '2 Sargento'),
    ('5', '1 Sargento'),
    ('6', 'Sub Tenente'),
    ('7', 'Aspirante'),
    ('8', '2 Tenente'),
    ('9', '1 Tenente'),
    ('10', 'Captao'),
    ('11', 'Major'),
    ('12', 'Tenente Coronel'),
    ('13', 'Coronel'),
)

SEXO_CHOICE = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

MAO_CHOICE = (
    ('E', 'Esquerda'),
    ('D', 'Direita'),
)

class Guarnicao(models.Model):
    nome = models.CharField(max_length=100)
    missao = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Guarnicoes"


class Militar(models.Model):
    nome = models.CharField(max_length=50)
    nome_de_guerra = models.CharField(max_length=40)
    matricula = models.CharField(max_length=7, unique=True)
    posto = models.CharField(max_length=20, choices=POSTO_CHOICE)
    data_de_nascimento = models.DateField()
    endereco = models.CharField(max_length=400)
    calcado = models.CharField(max_length=2)
    fardamento = models.CharField(max_length=3)
    boina = models.CharField(max_length=3)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICE)
    mao = models.CharField(max_length=1, choices=MAO_CHOICE)
    funcao = models.CharField(max_length=30)
    guarnicao = models.ForeignKey(Guarnicao, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.posto, self.nome_de_guerra)

    class Meta:
        verbose_name_plural = "Militares"

class Escala(models.Model):
    data = models.DateField()
    observacoes = models.CharField(max_length=500)
    guarnicoes = models.ManyToManyField(Guarnicao)

    def __unicode__(self):
        return 'Escala dia %s' % self.data

    class Meta:
        verbose_name_plural = "Escalas"


