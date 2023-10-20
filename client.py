import Pyro4 as pyro
if __name__ == '__main__':
    uri = "PYRONAME:Math@localhost:9090"
    a = input('Numero: ').strip()
    b = input('Expoente : ').strip()
    
    math = pyro.Proxy(uri) 
    result = math.pow(a,b) 
    print('Result: {} ^ {} = {}'.format(a,b,result))
