import json
from pygal.maps.world import World
from country_codes import get_country_code
# Carrega os dados em uma lista
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    # constrói um dicionário com dados das populações
    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010' and 'Value' in pop_dict:
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                cc_populations[code] = population
            else:
                print('Código não encontrado para:', country_name)
    
    wm = World()
    wm.force_uri_protocol = 'http'
    wm.title = 'World Population in 2010, by Country'
    wm.add('2010', cc_populations)
    wm.render_to_file('world_population.svg')
        
                #print('ERROR - '+ country_name)
            #print(country_name + ": " + str(population))