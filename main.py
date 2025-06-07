import statistics

frequencia = [10, 3, 6, 5, 9, 8, 7, 4]
frequencia.sort()

amplitude = max(frequencia) - min(frequencia)
print(amplitude)

variancia = statistics.variance(frequencia)
print(variancia)

desvio = statistics.stdev(frequencia)
print(desvio)