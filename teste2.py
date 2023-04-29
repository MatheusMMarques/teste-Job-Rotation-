valor = int(input("digite um valor: "))
v1=0
v2=1
soma = v2 + v1

while valor > soma:
    v1 = v2
    v2 = soma 
    soma = v2 + v1   
if valor == soma:
    print("este numero está na sequencia Fibonacci")
else:
    print("este numero não está na sequencia Fibonacci")
    
    

    
    

    
