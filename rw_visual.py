import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Continua criando novos passeios enquanto o programa estiver tivo
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()
    #plt.figure(dpi=128, figsize=(10,6))
    #15.3plt.plot(rw.x_values, rw.y_values, linewidth = 15)
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues, edgecolor='none', s=1)
    # Enfatiza o primeiro e o último ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s= 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # Remove os eixos
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y\n): ")
    if keep_running == 'n':
        break