# Grupo 80 (TG080) - Manuel Sousa (84740) & Tiago Novais (84888) #


# = = = = = = = = = = = = = = = = = = = = = = = = = #
#                                                   #
# = = = = = = =  C O N S T A N T E S  = = = = = = = #
#                                                   #
# = = = = = = = = = = = = = = = = = = = = = = = = = #


circulos_eleitorais =  \
            (('Circulo Eleitoral de Aveiro', 16), 
            ('Circulo Eleitoral de Beja', 3),
            ('Circulo Eleitoral de Braga', 19),
            ('Circulo Eleitoral de Braganca', 3),
            ('Circulo Eleitoral de Castelo Branco', 4),
            ('Circulo Eleitoral de Coimbra', 9),
            ('Circulo Eleitoral de Evora', 3),
            ('Circulo Eleitoral de Faro', 9),
            ('Circulo Eleitoral da Guarda', 4),
            ('Circulo Eleitoral de Leiria', 10),
            ('Circulo Eleitoral de Lisboa', 47),
            ('Circulo Eleitoral de Portalegre', 2),
            ('Circulo Eleitoral do Porto', 39),
            ('Circulo Eleitoral de Santarem', 9),
            ('Circulo Eleitoral de Setubal',  18),
            ('Circulo Eleitoral de Viana do Castelo', 6),
            ('Circulo Eleitoral de Vila Real', 5),
            ('Circulo Eleitoral de Viseu', 9),
            ('Circulo Eleitoral dos Acores', 5),
            ('Circulo Eleitoral da Madeira', 6),
            ('Circulo Eleitoral da Europa', 2),
            ('Circulo Eleitoral de Fora da Europa', 2))


partidos_nome_sigla =  \
            (('Partido Democratico Republicano', "PDR"), 
            ('CDU - Coligacao Democratica Unitaria', "PCP-PEV"),
            ('Portugal a Frente', "PPD/PSD-CDS/PP"),
            ('Partido da Terra', "MPT"),
            ('LIVRE/Tempo de Avancar', "L/TDA"),
            ('Pessoas-Animais-Natureza', "PAN"),
            ('Agir', "PTP-MAS"),
            ('Juntos pelo Povo', "JPP"),
            ('Partido Nacional Renovador', "PNR"),
            ('Partido Nacional Monarquico', "PPM"),
            ('Nos, Cidadaos!', "NC"),
            ('Partido Comunista dos Trabalhadores Portugueses', "PCTP/MRPP"),
            ('Partido Socialista', "PS"),
            ('Bloco de Esquerda', "B.E."),
            ('Partido Unido dos Reformados e Pensionistas', "PURP"))


# = = = = = = = = = = = = = = = = = = = = = = = = = #
#                                                   #
# = = =  F U N C O E S   A U X I L I A R E S  = = = #
#                                                   #
# = = = = = = = = = = = = = = = = = = = = = = = = = #


def atualizar_tuple (t_tuple , valor_a_alterar , posisao):
    """ 
        atualizar_tuple : tuplo , int , int -> tuplo
        atualizar_tuple(t_tuple , valor_a_alterar , posisao) atualiza um valor de um tuple, com um valor recebido (valor_a_alterar),
        com uma posisao especifica (posisao).
    """ 
    lista = list(t_tuple)
    lista[posisao] = valor_a_alterar
    t_tuple = tuple(lista)  

    return t_tuple
# -- Fim: atualizar_tuple -- #

def soma_tuplos(A , B):
    """ 
        soma_tuplos : tuplo , tuplo -> tuplo
        soma_tuplos(A, B) devolve o tuplo da soma entre o tuplo A e B
    """     
    somatorio = []
    for i in range(len(A)):
        somatorio.append(A[i] + B[i])
        
    return tuple(somatorio)
# -- Fim: soma_tuplos -- #


# = = = = = = = = = = = = = = = = = = = = = = = = = #
#                                                   #
# = = =  F U N C O E S   P R I N C I P A I S  = = = #
#                                                   #
# = = = = = = = = = = = = = = = = = = = = = = = = = #


def mandatos(nr_mandatos , nr_votos):
    """ 
    mandatos : int , tuplo -> tuplo
    mandatos(nr_mandatos , nr_votos) retorna um tuplo que contem o numero de 
    mandatos atribuidos a cada partido calculado pelo metodo de Hondt
    """
    divisores = [1] * len(nr_votos)
    mandatos = [0] * len(nr_votos)
    mandatos_atribuidos = (0,) * len(nr_votos)
    espelho_nr_votos = nr_votos
    i = maximo_posisao = 0
    maximo =- 1

    while nr_mandatos != 0:
        
        if nr_votos[i] > maximo:
            maximo = nr_votos[i]
            maximo_posisao = i
        elif nr_votos[i] == maximo and espelho_nr_votos[i] < espelho_nr_votos[maximo_posisao]:
                maximo_posisao = i

        if (i+1) == len(nr_votos):
            """ 
            Verifica se chegou ao fim da Ronda apos percorrer as votacoes de partido a partido. 
            Se ainda houver mandatos a distribuir -> Nova Ronda, senao, acaba o programa 
            e retorna um tuple com os mandatos atribuidos a cada partido
            """
            divisores[maximo_posisao] += 1
            nr_votos = atualizar_tuple (nr_votos , espelho_nr_votos[maximo_posisao] / divisores[maximo_posisao] , maximo_posisao)
            maximo_mandatos = int(mandatos_atribuidos[maximo_posisao])
            mandatos_atribuidos = atualizar_tuple(mandatos_atribuidos , maximo_mandatos + 1 , maximo_posisao)
            nr_mandatos -= 1            
            maximo = i = 0 
        else:
            i += 1

    return (mandatos_atribuidos)
# -- Fim: mandatos -- #

def assembleia(assembleia_votacoes):
    """
    assembleia : tuplo -> tuplo
    assembleia(assembleia_votacoes) retorna um tuplo com o numero de deputados 
    eleitos em cada partido tendo em consideracao os resultados e o numero 
    de mandatos correspondentes a cada circulo eleitoral
    """
    i = 0
    soma = (0,) * len(assembleia_votacoes[0])

    while i < len(assembleia_votacoes):
        soma = soma_tuplos(soma, mandatos(circulos_eleitorais[i][1] , assembleia_votacoes[i]))
        i += 1

    return soma
# -- Fim: assembleia -- #
 
def max_mandatos(mandatos):
    """ 
    max_mandatos : tuplo -> string
    max_mandatos(mandatos) retorna uma string com a sigla e nome do 
    partido politico com maior representacao na Assembleia da Republica.
    """
    mandatos_atribuidos = assembleia(mandatos)
    maximo = max(mandatos_atribuidos)
    maximo_posisao = mandatos_atribuidos.index(maximo) # Atribui a variavel maximo_posisao o indice do tamanho maximo
    conta_maximo = mandatos_atribuidos.count(maximo) # Usa o objeto ".count" para verificar o numero de vezes que o valor da variavel maximo se repete
    
    if conta_maximo > 1:
        return "Empate tecnico"
    else:
        return partidos_nome_sigla[maximo_posisao][1] + "\t" + partidos_nome_sigla[maximo_posisao][0]  
# -- Fim: max_mandatos -- #