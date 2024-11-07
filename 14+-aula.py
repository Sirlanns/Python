
ValorA = int(input("coloque o valor A: "))
ValorB = int(input("coloque o valor B: "))
ValorC = int(input("coloque o valor C: "))

Delta = ValorB ** 2 -  4 * ValorA * ValorC

if Delta < 0:
    raizDelta = (-Delta) ** 0.5
    x1_real = -ValorB / (2 * ValorA)
    x1_imag = raizDelta / (2 * ValorA)
    
    x2_real = x1_real
    x2_imag = -x1_imag
    
    print(f"As raízes complexas são: x1 = {x1_real} + {x1_imag}i e x2 = {x2_real} - {x2_imag}i")
    
else:
    raizDelta = Delta ** 0.5
    x1 = (-ValorB + raizDelta) / (2 * ValorA)
    x2 = (-ValorB - raizDelta) / (2 * ValorA)
    
    print(f"As raízes reais são: x1 = {x1} e x2 = {x2}")
