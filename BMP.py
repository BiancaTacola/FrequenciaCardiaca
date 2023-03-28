#IDADE BPM
#Até 2 anos 120 a 140
#De 8 anos até 17 anos 80 a 100
#Adulto sedentário 70 a 80
#Idosos 50 a 60

print("Verificador de Frequências Cardíacas")
idade = int(input("Por favor, informe sua idade"))
bpm= int(input("Por favor, informe sua frequência cardiaca"))

if idade <= 2:
    if bpm >= 120 and bpm <=140:
        print("Frequencia cardiaca adequada")
    else:
       print("Frequencia cardiaca inadequada")
elif idade >= 8 and idade <=17:
    if bpm >= 80 and bpm <100:
       print("Batimentos normais para a idade fornecida")
    else:
       print("Frequencia cardiaca inadequada")
elif idade >= 18 and idade <60:
    if bpm >= 70 and bpm <80:
       print("Batimentos normais para a idade fornecida")
    else:
       print("Frequencia cardiaca inadequada")
elif idade >= 60:
    if bpm >= 50 and bpm <60:
       print("Batimentos normais para a idade fornecida")
    else:
       print("Frequencia cardiaca inadequada")