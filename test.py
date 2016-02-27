if 5>2:
	print('5 jest jednak wieksze od 2')
else:
	print('5 nie jest wieksze od 2')
name='Magda'
if name=='Magda':
	print('Hej Magda')
elif name=='Magda':
	print('Hej Magda')
else:
	print('Hej Magdaleno!')	
glosnosc = 57
if glosnosc<20:
	print('Prawie nic nie slychac')
elif 20 <= glosnosc < 40:
	print('0,muzyka leci w tle')
elif 40 <= glosnosc <60:
	print('Idealnie, moge sluchac')
elif 60<= glosnosc <80:
	print('Dobre na imprezy')
elif 80 <= glosnosc < 100:
	print('Troszke za glosno!')
else:
	print('Ojoj! MOje uszy!:(')
def hej():
	print("Hej!")
	print("Jak sie masz?")
hej()
def hej(imie):
	if imie=='Magda':
		print("Hej Magda!")
	elif imie=="Magda":
		print("Hej Magda")
	else:
		print("Hej Magdaleno!")
hej("Magda")
def hej(imie):
	print("Hej" + imie + '!')
hej(" Kaska")
def hej(imie):
	print("Hej" + imie + '!')
dziewczyny=['Magda', "Ania", "Ola", 'Kamila']
for number, imie in enumerate(dziewczyny):
	print(number)
	hej(imie)
	print('Kolejna dziewczyna')

for i in range(1, 6):
	print(i)