def imprimir_ronda (lista_imp):
    """Imprime el interfaz de la ronda"""
    for i in range(len(lista_imp)):
        print (lista_imp[i].capitalize(), end="   ")

def agregar_puntos (jugador_dic, jugador):
    """ Agrega los puntos como nuevo campo"""
    puntaje = 3*(jugador_dic[jugador]['kills']) + jugador_dic[jugador]['assists']
    if jugador_dic[jugador]['deaths'] == True:
        puntaje-=1
    jugador_dic[jugador]['points'] = puntaje
    return jugador_dic[jugador]

def ordenar_ronda (round):
    """Ordena la ronda para posteriormente imprimirla"""
    round = dict(sorted(round.items(), key =lambda item: item[1]['points'], reverse= True ))
    return round




def imprimir_bien (round):
    """Imprime la ronda ordenada con espacios entre campos"""
    for player in round:
        print (f'{player:<11} {round[player]['kills']:<9}{round[player]['assists']:<9}{round[player]['deaths']:<9}{round[player]['points']}')

def calcular_MVP (round):
    """Retorna el jugador de la ronda con mayor cantidad de puntos"""
    MVP = list (round.keys())[0]
    return MVP

def imprimir_final (dic, lista_imp):
    """Aunque esta funcion solo sirva para imprimir, dentro de ella se genera una lista de tuplas 
    usando lambda de los puntos como clave de ordenacion, 
    y un reverse para que se imprima de mayor a menor"""
    players = [(player, stats['points']) for player, stats in dic.items()]
    players.sort(key=lambda x: x[1], reverse= True)
    imprimir_ronda (lista_imp)
    print ('')
    print ('---------------------------------------------------')
    for player in players:
        print (f'{player[0]:<12}{dic[player[0]]['kills']:<9}{dic[player[0]]['assists']:<9}{dic[player[0]]['deaths']:<9}{dic[player[0]]['MVP´s']:<8}{dic[player[0]]['points']}')
    print('---------------------------------------------------')
        
        


      

