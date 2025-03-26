# Description: Program pro výpočet ceny tramvajové jízdenky
def ticket_price(age, is_employee):
    base_price = 45  # Plná cena jízdenky

    if age < 12:
        return 0  # Děti do 12 let jezdí zdarma
    elif is_employee and age >= 55:
        return 0  # Zaměstnanci nad 55 let jezdí zdarma
    elif is_employee:
        return base_price * 0.2  # Zaměstnanci mají 80% slevu
    elif age < 18:
        return base_price * 0.5  # Cestující mladší 18 let mají 50% slevu
    elif age > 65:
        return base_price * 0.7 # Cestující nad 65 let mají 30% slevu
    else:
        return base_price  # Plná cena pro ostatní

def main():
    print("Vítejte v programu pro výpočet ceny tramvajové jízdenky.")
    
    try:
        age = int(input("Zadejte věk zákazníka: "))
    except ValueError:
        print("Chyba: Prosím zadejte platnou hodnotu - celé číslo.")
        
    while True: 
        is_employee = str(input("Je zákazník zaměstnancem tramvajové služby? (ano/ne): "))
    
        if is_employee in ["ano", "a"]:
            is_employee = True
            break
        elif is_employee in ["ne", "n"]:
            is_employee = False
            break
        else:
            print("Chyba: Prosím zadejte platnou odpověď (ano/ne).")
    
    final_price = ticket_price(age, is_employee)
    print(f"Konečná cena jízdenky je: {final_price} Kč")

if __name__ == "__main__":
    main()
    
    