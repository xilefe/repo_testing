import time # Importamos temporizador
import termcolor

# Función para saber si es autonomo o trabaja por cuenta ajena
def claseTrabajo():
    while(True): #Forzamos a que la respuesta sea 1 o 2
        
        # Pedimos tipo de trabajo
        tipotrabajo = str(input(termcolor.colored('''¿Trabaja por cuenta ajena o es autonomo? 1 para ajena/ 2 para autonomo
        ''', 'cyan')))
        
        if tipotrabajo == '1' or tipotrabajo == '2':
            break # Damos la salida del bucle
        else:
            print (termcolor.colored('\nLo siento, introduzca 1 o 2, Por favor,\n', 'red'))
    
    # Modificamos la respuesta numerica por el texto correspondiente
    if tipotrabajo == '1':
        tipotrabajo = 'Ajena'
    else:
        tipotrabajo = 'Autonomo'
    return tipotrabajo

# Función para saber si trabaja a tiempo parcial o jornada completa
def tipo_jornada(tipotrabajo):
    
    while(True): #Forzamos a que la respuesta sea 1 o 2
        
        # Preguntamos por su jornada
        jornada= str (input(termcolor.colored('''¿Trabaja a tiempo parcial o a jornada completa? 1 para parcial/ 2 para completa
        ''', 'cyan')))
        
        if jornada == '1' or jornada == '2':
            # Modificamos la respuesta numerica por el texto correspondiente
            if jornada == '1':
                jornada ='Parcial'
            else:
                jornada = 'Completa'
            break # Damos la salida del bucle
        else:
            print (termcolor.colored('\nLo siento, introduzca 1 o 2, Por favor,\n', 'red'))
    return jornada

# Funcion para determinar los ingresos
def ingresos(tipotrabajo, jornada):
    # Pedimos datos por pantalla
    if tipotrabajo == 'Autonomo':
        # Si és autonomo le preguntamos su facturación mensual y ponemos a 0 las variables que no le aplican
        facturacion_mensual = float(input('''¿Cual és su facturación mensual neta habitual?
        ''').replace(',','.'))
        
        horas_extra = 0
        num_pagas = 0
        jornada =''
        EU_semana = 0
    else:
        if tipotrabajo == 'Ajena':
            EU_horas = float(input(termcolor.colored('''¿A cuanto cobra la hora?
            ''','green')).replace(',','.'))
            
            facturacion_mensual = 0
            
            if jornada == 'Parcial':
                horas_semana = float(input(termcolor.colored('''¿Cuantas horas a la semana trabaja?
                ''', 'green')).replace(',','.'))
                
            else:
                if jornada == 'Completa':
                    horas_semana = 40.0
        horas_extra = float(input(termcolor.colored('''¿Realiza horas extras ocasionalmente? cuantas por semana:
        ''', 'green')).replace(',','.'))
        
    # Preguntamos si tiene pagas extra y nos aseguramos que la respuesta sea si o no
    while(True):
        # Si es autonomo salimos del bucle
        if tipotrabajo == 'Autonomo':
            break
        pagas_extra = input(termcolor.colored('''¿Tiene pagas extra? (si / no)
        ''', 'green'))
        pagas_extra = pagas_extra.lower()
        if pagas_extra == 'si':
            num_pagas = float(input(termcolor.colored('''¿Cuantas pagas extra tiene al año?
            ''', 'green')).replace(',','.'))
            
            break
        else:
            if pagas_extra == 'no':
                num_pagas = int(0)
                break
            else:
                print(termcolor.colored('\nLo siento, introduzca si o no, Por favor,\n', 'red'))
    
    if tipotrabajo == 'Ajena':
        # Calculamos las horas extras en EU, las multiplicamos por dos por que se cobran dobles
        EU_extra = float(horas_extra * (EU_horas * 2))
        # Calculamos la ganancia total por semana
        EU_semana = float ((EU_horas * horas_semana) + (EU_extra))
    return facturacion_mensual, EU_semana, num_pagas

# Función para determinar los gastos
def gastos():
    # Pedimos datos por pantalla de los gastos
    print (termcolor.colored('''· A continuacion vamos a realizar una serie de preguntas sobre sus gastos mensuales.
    ''', 'blue'))
    # Temporizador
    time.sleep(2)
    alqui_hipo,agua,luz,gas,comida,movil = float(input(termcolor.colored('''- ¿Que tasa de alquiler o hipoteca paga? 
    ''', 'green')).replace(',','.')) , float(input(termcolor.colored('''- ¿Que tasa paga de agua?
    ''', 'green')).replace(',','.')) , float(input(termcolor.colored('''- ¿Que tasa paga de luz?
    ''', 'green')).replace(',','.')) , float(input(termcolor.colored('''- ¿Que tasa paga de gas?
    ''', 'green')).replace(',','.')) , float(input(termcolor.colored('''- ¿Cuanto gasta en comida?
    ''', 'green')).replace(',','.')) , float(input(termcolor.colored('''- ¿Que tasa paga de movil?
    ''', 'green')).replace(',','.'))
    
    # Preguntamos si tiene gastos anuales
    while(True):
        g_anuales = input(termcolor.colored('''- ¿Tiene gastos anuales como seguros de coche/moto, hogar, mutuas, suscripciones..? (si/no)
        ''', 'cyan'))
        g_anuales = g_anuales.lower()
        if g_anuales == 'si':
            g_anuales = float(input(termcolor.colored('''-¿A cuánto asciende la suma de estos gastos anuales?
            ''', 'green')).replace(',','.'))
            
            break
        else:
            if g_anuales == 'no':
                g_anuales = int(0)
                break
            else:
                print(termcolor.colored('\nLo siento, introduzca si o no, Por favor,\n', 'red'))
    
    # Preguntamos si tiene gastos extra
    while(True):
        g_extra = str(input(termcolor.colored('''- ¿Tiene gastos extra? (si/no)
        ''', 'cyan')))
        g_extra = g_extra.lower()
        if g_extra == 'si':
            gastos_extra = float(input(termcolor.colored('''- ¿Cuanto dinero gasta en extras?
            ''', 'green')).replace(',','.'))
            
            break
        else:
            if g_extra == 'no':
                gastos_extra = int(0)
                break
            else:
                print (termcolor.colored('\nLo siento, introduzca si o no, Por favor,\n' , 'red'))
    return alqui_hipo,agua,luz,gas,comida,movil,g_anuales,gastos_extra

# Función que calcula los resultados y los imprime por pantalla
def resultados(alqui_hipo,agua,luz,gas,comida,movil,g_anuales,gastos_extra, facturacion_mensual,num_pagas):
    if tipotrabajo == 'Autonomo':
        EU_mes = facturacion_mensual
    else:
        # Calculamos ganancia total mensual contando de media que el mes tiene 4 semanas
        EU_mes = float (EU_semana * 4 )
    #Calculamos ganancia anual
    EU_año = float((EU_mes * (12 + num_pagas)))
    #Calculamos el gasto total mensual que tiene 
    gasto_total_mes = int(alqui_hipo + agua + luz + gas + comida + movil + gastos_extra)
    # Calculamos el gasto anual multiplicando por 12 que son la cantidad de meses que tiene el año
    gastos_anuales = (gasto_total_mes * 12) + g_anuales
    # Calculamos el ahorro anual
    ahorro_anual = round(EU_año - gastos_anuales , 2)
    #Damos datos por pantalla
    print (termcolor.colored('''· Estamos calculando sus datos...
    ''', 'yellow'))
    # Temporizador
    time.sleep(2)
    # Damos datos por pantalla de los resultados
    print (termcolor.colored(nombre.title(), 'blue'))
    if ahorro_anual < 0:
        print(termcolor.colored('''- Sus gastos superan a sus ingresos y su ahorro queda en negativo:''' + str(ahorro_anual) + 'EU\n', 'red'))
    else:
        print (termcolor.colored('''
        - Sus ganancias mensuales calculando de media que el mes tiene 4 semanas son de: ''' + str(EU_mes) + 'EU' + '''
        - El total de ganancias anual es de: ''' + str(EU_año) + 'EU' + '''
        - El total de sus gastos mensuales es de: ''' + str(gasto_total_mes) + 'EU' + '''
        - Con un total de gastos anuales de : ''' + str(gastos_anuales) + 'EU' + '''
        - El total a ahorrar cada año es de: ''' + str(ahorro_anual) + 'EU\n', 'cyan'))

print (termcolor.colored('----------------------', 'blue'))
print (termcolor.colored('CALCULADORA DE AHORROS', 'blue')) # titulo
print (termcolor.colored('''----------------------
''', 'blue'))
# Temporizador
time.sleep(2) 
# Pedimos nombre por pantalla y saludamos al usuario
nombre = str(input(termcolor.colored('''¿Cual es su nombre? 
''', 'green')))
print (termcolor.colored('Hola: ' + nombre.title(), 'cyan'))

# Llamamos a la función clase de trabajo
tipotrabajo = claseTrabajo()

if tipotrabajo == 'Ajena':
    # Llamamos a la función tipo de jornada
    jornada = tipo_jornada(tipotrabajo)
else:
    jornada = ''


# Llamamos a la función ingresos
facturacion_mensual, EU_semana, num_pagas = ingresos(tipotrabajo, jornada)

# Llamamos a la función gastos
alqui_hipo,agua,luz,gas,comida,movil,g_anuales,gastos_extra = gastos()

# Llamamos a la función resultados
resultados(alqui_hipo,agua,luz,gas,comida,movil,g_anuales,gastos_extra, facturacion_mensual,num_pagas)