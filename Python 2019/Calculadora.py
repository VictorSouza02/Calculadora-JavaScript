while (True):
    
    print ("""
     _____        _            _           _                 
    /  __ \      | |          | |         | |                
    | /  \/  __ _| | ___ _   _| | __ _  __| | ___  _ __ __ _ 
    | |     / _` | |/ __| | | | |/ _` |/ _` |/ _ \| |__/ _` |
    | \__/\  (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |
     \____/ \__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|""")
    
    print ('Calculadora 1.0 beta by victor')
    
    print ('-------------------------------------')
    
    print ('     ')
    
    x1 = int (input ('Digite o primeiro número: '))
    
    x2 = int (input ('Digite o segundo número: '))
    
    s1 = x1+x2
    s2 = x1-x2
    s3 = x1*x2
    s4 = x1/x2
    s5 = x1**x2
    s6 = x1//x2
    
    print ('-------------------------------------')
    
    print ('     ')
    
    print ('● O resultado da adição dos números inseridos é {}'.format(s1))
    
    print ('● O resultado da subtração dos números inseridos é {}'.format(s2))
    
    print ('● O resultado da multiplicação dos números inseridos é {}'.format(s3))
    
    print ('● O resultado da divisão dos números inseridos é {:.2f}'.format(s4))

    print ('● O resultado da potência dos números inseridos é {}'.format(s5))

    print ('● O resultado da divisão inteira dos números inseridos é {}'.format(s6))
    
    print ('-------------------------------------')
    
    print ('     ')
    
    print ('   __  ___  ___ __  __ _   _ _      _     ___  ___   ___ _  _   _   ___ _  __   _   ___    _  ') 
    print ('  / _|/ _ \| _ \  \/  | | | | |    /_\   |   \| __| | _ ) || | /_\ / __| |/ /  /_\ | _ \  /_\  ')
    print (' |  _| (_) |   / |\/| | |_| | |__ / _ \  | |) | _|  | _ \ __ |/ _ \\__ \ | <  / _ \|   / / _ \ ')
    print (' |_|  \___/|_|_\_|  |_|\___/|____/_/ \_\ |___/|___| |___/_||_/_/ \_\___/_|\_\/_/ \_\_|_\/_/ \_\ ')
                                                                                             
    print (' ')
    
    A = int (input('qual é o valor de A? '))
    
    B = int (input('qual é o valor de B? '))
    
    C = int (input('qual é o valor de C? '))

    s = (B**2)-4*A*C
    x1 =(-B + s ** (1/2))/ 2*A
    x2 =(-B - s ** (1/2))/ 2*A

    print (' ')

    print ('■ fórmula de bhaskara (delta) é: Δ = B^2-4.A.C')
    
    print (' ')
    
    print ('■ fórmula de bhaskara (delta) é: Δ={}^2-4.{}.{}'.format(B,A,C))
    
    print (' ')
    
    print ('● o valor de delta é ',s)
    
    print (' ')
    
    print ('----------------- ')

    print ('■ o valor de x é encontrado na fórmula: x = (-B (+-) √Δ)/ 2.A')
    
    print (' ')
    
    print ('■ o valor de x é:: x = (-({}) (+-) √{})/ 2.{}'.format(B,s,A))
    
    print (' ')
    
    print ('● o valor de x positivo é {}, e o valor do x negativo é {}'.format(x1,x2))

    
    print ('     ')
    print ('---------- FIM DA  OPERAÇÃO ----------')
    print ('     ')
