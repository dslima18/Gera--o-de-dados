from die import Die
import pygal
# Cria um D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(4000):
    result = die_1.roll() * die_2.roll() * die_3.roll()
    results.append(result)
# Analisa os resultados.
frequencies = []
max_results = die_1.num_sides * die_2.num_sides * die_3.num_sides
for value in range(1, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# Visualiza os resultados
hist = pygal.Bar()
hist.tilte = "Results of rolling three D6 1000 times."
hist.x_labels = [x for x in range(1,216)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 * D6 * D6', frequencies)
hist.render_to_file('die_visual.svg')
#print(frequencies)