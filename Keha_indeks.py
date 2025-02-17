print("Tere! Olen sinu uus sõber - Python!")
nimi=input("sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi")
while 1: 
    try:
        soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
        if soov == 1:
            print('tdeksi lidmie')
            while True:
                try:
                    pikkus=int(input("sisesta oma pikkus: "))
                    break
                except:
                    print("vale pikkuse formaat")
            while True:
                try:
                    mass=float(input("sisesta oma kaal: "))
                    break
                except:
                       print("vale kaalu formaat") 
            kindeks=round(mass/(0.01*pikkus)**2)
            print(f"{nimi}, sinu keha indeks on {kindeks}")
            if kindeks<16:
                print('Tervisele ohtlik alakaal')
            elif kindeks<19:
                print('Alakaal')
            elif kindeks<25:
                print('Normaalkaal')
            elif kindeks<30:
                print('Ülekaal')
            elif kindeks<35:
                print('Rasvuminel')
            elif kindeks<40:
                print('Tugev rasvumine')
            else:
                print('bebbeleraaaa')
        except:
                print("valed andmed")
        elif soov == 0:
            print("net tak net ")
            break
        else:
            print("vale valik. saab valida ainult 1 voi 0")
    except:
        print("vale soov")