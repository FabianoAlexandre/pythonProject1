motocycles = ["yamaha","honda","bmw","suzuki","dafra"]
print(motocycles)
motocycles.remove("yamaha") #Pode-se especificar o item que quer remover permanentemente
print(motocycles)
del motocycles[3] #Remove permanentemente o item do indice 3
print(motocycles)
popped_motocycle: str = motocycles.pop() #remove o ultimo item ou o item especificado do indice e quarda-o em outra variavel para utilização futura.
print(motocycles)
print(popped_motocycle)
too_expensive = 'bmw'
motocycles.remove(too_expensive)
print(motocycles)
print("\nA " + too_expensive.title() + " is too expensive for me")
