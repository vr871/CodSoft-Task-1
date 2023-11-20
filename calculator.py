import os
import msvcrt as m
import math

def total():
        total = 0

        print("Provide addends: ")
        while True:
            try:
                number = int(input())
                total += number
            except ValueError:
                break

        return total

def product():
        product = 1

        print("Provide factors: ")
        while True:
            try:
                number = int(input())
                product *= number
            except ValueError:
                break

        return product

def exit_func1():
        sim_ch1=str(input("\n\n(1) Operations \n(2) Main Menu \n(3) Exit\n=> "))
        if(sim_ch1=='1'):
            simple_calc()

        elif(sim_ch1=='2'):
            os.system('cls')
            main()
        else:
            exit()

def simple_calc():
        os.system('cls')
        print("============= Basic Calculator ==============\n=============================================\n")
        choice2=str(input("Select operation:\n*********************\n1. Sum/Difference \n2. Multiplication \n3. Division \n4. Logarithm \n5. Exponent\n6. nth root\n*********************\n7. Go Back\n8. Exit\n*********************\n=> "))
        if(choice2=='1'):
            os.system('cls')
            print("\nSum/Difference~")
            result = total()
            print("Outcome:",result)

            exit_func1()

        elif(choice2=='2'):
            os.system('cls')
            print("\nMultiplication~")
            output = product()
            print("Product:", output)

            exit_func1()

        elif(choice2=='3'):
            os.system('cls')
            print("\nDivision~")
            var1=float(input("Divident: "))
            var2=float(input("Divisor: "))
            print("Quotient =>", var1/var2)

            exit_func1()

        elif(choice2=='4'):
            os.system('cls')
            print("\nLogarithm~")
            var1=float(input("Argument: "))
            var2=float(input("Base: "))
            print('Logarithm base', var2, 'of', var1, 'is', math.log(var1,var2))

            exit_func1()
                
        elif(choice2=='5'):
            os.system('cls')
            print("\nExponents~")
            var1=float(input("Base: "))
            var2=float(input("Power: "))
            print(var1, 'raised to the power', var2, 'is', pow(var1,var2))

            exit_func1()

        elif(choice2=='6'):
            os.system('cls')
            print("\nNth Root~")
            var1=float(input("Radicant: "))
            var2=float(input("Index: "))
            print('Root value:', pow(var1,1/var2))

            exit_func1()

        elif(choice2=='7'):
            os.system('cls')
            main()

        elif(choice2=='8'):
             exit()

        else:
            print("\nInvalid choice.\nPress any key to continue...")
            m.getch()
            simple_calc()


def temp():
    os.system('cls')
    print("\nWork in Progress.\nPress any key to return...")
    m.getch()
    main()

def main():

    print("\n=============================================")
    print("================ CALCULATOR =================\n")

    choice1=str(input("(1) Basic Operations \n(2) Advanced Operations \n(3) Terminate Session\n\n=============================================\n=> "))
    if(choice1=='1'):
        simple_calc()
    
    elif(choice1=='2'):
        temp()

    elif(choice1=='3'):
        exit()

    else:
        print("Invalid Input!")
        main()

if __name__=='__main__':
    main()