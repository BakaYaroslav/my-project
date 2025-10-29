repeat = True

while repeat:
        while True:
            op = input("Sisesta tehe (+, -, *, /, D,**0.5,**): ").strip().upper()
            if op in ['+', '-', '*', '/', 'D', '**0.5','**']:
                break
            else:
                print("Palun sisesta kehtiv tehe.")
            import math
            x = math.sqrt(a)
            if op == 'D':
                while True:
                    try:
                        a = float(input("Sisesta a: "))
                        b = float(input("Sisesta b: "))
                        c = float(input("Sisesta c: "))
                        D = b**2 - 4*a*c
                        break
                    except ValueError:
                            print("Palun sisesta kehtiv arv.")
            
                    if D < 0:
                         print("Puuduvad reaalarvulised juured")
            
                    else: D == 0
                    x = -b/(2*a)
                    print(f"Võrrandil on üks reaalne juur: / (2*{a}) = {x:.2f}")
                    if D > 0:
                        x1 = (-b + D**0.5)/(2*a)
                        x2 = (-b - D**0.5)/(2*a)
                        print(f"Võrrandil on kaks erinevat reaalset juurt: x1 = + √{D}) / (2*{a}) = {x1:.2f} ja x2 = - √{D}) / (2*{a}) = {x2:.2f}")
                    else:
                        print("Palun sisesta kehtiv arv.")
            else:
                
                while True:
                    try:
                        num = input("Sisesta num (või 'stop' lõpetamiseks): ").strip()
                        if num.lower() == 'stop':
                            break
                        num.append(float(num))
                    except ValueError:
                        print("Palun sisesta kehtiv arv.")
        if op == '**':
            result = num ** 2
            print(f"Tulemus: {result:.2f}")
        elif op == '**0.5':
            result = math.sqrt(num)
            print(f"Tulemus: {result:.2f}")
        elif op == '+':
            result = sum(num)
            print(f"Tulemus: {result:.2f}")
        elif op == '-':
            result = min(num)
            print(f"Tulemus: {result:.2f}")
        elif op == '*':
            result *= num 
            print(f"Tulemus: {result:.2f}")
        elif op == '/':
            if b == 0 and c == 0:
                print("Viga: Jagamine nulliga pole lubatud.")
            else:
                result /= num
                print(f"Tulemus: {result:.2f}")
        elif op == 'D':
            
            if D < 0:
                print("Puuduvad reaalarvulised juured")
            
            elif D == 0:
                x = -b/(2*a)
                print(f"Võrrandil on üks reaalne juur: / (2*{a}) = {x:.2f}")
            else:
                x1 = (-b + D**0.5)/(2*a)
                x2 = (-b - D**0.5)/(2*a)
                print(f"Võrrandil on kaks erinevat reaalset juurt: x1 = + √{D}) / (2*{a}) = {x1:.2f} ja x2 = - √{D}) / (2*{a}) = {x2:.2f}")

        question = input("Kas soovid veel arvutusi teha? (jah/ei): ").strip().lower()
        if question != 'jah':
            repeat = False
            print("Lõpp")
        else:
            repeat = True