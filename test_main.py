from main import saludo 

def test_saludo():
    assert saludo() == "Hola mundo" # para que falle pytest