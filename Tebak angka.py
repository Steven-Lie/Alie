import random
def mulai():
    print ("Permainan Tebak Angka")
    print ("1. Baby level (0-30)")
    print ("2. Intermediate level (0-50)")
    print ("3. Extreme level (0-100)")

    ans = input("Pilih level (1-3): ")

    if ans == "1":
        a = random.randrange(0,30)
        nyawa = 4
        print ("nyawa : ",nyawa)
        print()
        pil = int(input("Input terkaan anda "))
        while pil != a:
            if pil > a:
                print ("Angka terlalu besar")
                nyawa = nyawa - 1
                print("nyawa : ",nyawa)
                print ()
                if nyawa == 0:
                    print ("Maaf anda gagal. angkanya adalah : ",a)
                    again()
                pil = int(input("Input terkaan anda "))

            elif pil < a:
                print ("Angka terlalu kecil")
                nyawa = nyawa - 1
                print("nyawa : ",nyawa)
                print()
                if nyawa == 0:
                    print ("Maaf anda gagal. angkanya adalah : ",a)
                    again()
                pil = int(input("Input terkaan anda "))
                    

        if pil == a:
            print ("Selamat! Terkaan anda benar")
            print ("Angkanya adalah ",a)
            again()

    elif ans == "2":
        a = random.randrange(0,50)
        nyawa = 5
        print ("nyawa : ",nyawa)
        print()
        pil = int(input("Input terkaan anda "))
        while pil != a:
            if pil > a:
                print ("Angka terlalu besar")
                nyawa = nyawa - 1
                print("nyawa : ",nyawa)
                print()
                if nyawa == 0:
                    print ("Maaf anda gagal. angkanya adalah : ",a)
                    again()
                pil = int(input("Input terkaan anda "))

            elif pil < a:
                print ("Angka terlalu kecil")
                nyawa = nyawa - 1
                print("nyawa : ",nyawa)
                print()
                if nyawa == 0:
                    print ("Maaf anda gagal. angkanya adalah : ",a)
                    again()
                pil = int(input("Input terkaan anda "))
                    

        if pil == a:
            print ("Selamat! Terkaan anda benar")
            print ("Angkanya adalah ",a)
            again()
            
    elif ans == "3":
        a = random.randrange(0,100)
        nyawa = 6
        print ("nyawa : ",nyawa)
        print()
        pil = int(input("Input terkaan anda "))
        while pil != a:
            if pil > a:
                print ("Angka terlalu besar")
                nyawa = nyawa - 1
                print("nyawa : ",nyawa)
                print()
                if nyawa == 0:
                    print ("Maaf anda gagal. angkanya adalah : ",a)
                    again()
                pil = int(input("Input terkaan anda "))

            elif pil < a:
                print ("Angka terlalu kecil")
                nyawa = nyawa - 1
                print("nyawa : ",nyawa)
                print()
                if nyawa == 0:
                    print ("Maaf anda gagal. angkanya adalah : ",a)
                    again()
                pil = int(input("Input terkaan anda "))
                    

        if pil == a:
            print ("Selamat! Terkaan anda benar")
            print ("Angkanya adalah ",a)
            again()
            
def again():                 
        a=input('want to play again (y/n) : ')
        if a=='y' :
            print()
            mulai()
        if a=='n' :
            exit()
mulai()
