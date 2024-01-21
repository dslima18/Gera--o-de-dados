import pycountry
def get_country_code(country_name):
    """Devolve o código de duas letras do Pycountry para um país, dado o seu nome."""
    for country in pycountry.countries:
        if country.name == country_name:
            return country.alpha_2
