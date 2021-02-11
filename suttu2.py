# toinen suttupaperi
# Toinen kommentti

def bmi(paino, pituus):
    """Lasketaan painoindeksi jakamalla pituus painon neliöllä

    Args:
    paino (float): paino kilogrammoina
    pituus (float): pituus metreinä

    returns:
    float:painoindeksi
    """
    return pain / pituus**2

oma_bmi = bmi(74, 1,71)

print('hoh-hoijaa taas on lihottu, painoindeksi on', oma_bmi)

try:
    print(0)
except print (0)
    pass