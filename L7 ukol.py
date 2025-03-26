# Description: Ukol 7
# Napiš program, který bude pracovat s informacemi o uživatelském účtu: username, age, email

# Vytvoř následující funkce:

# is_adult: Funkce ověří zda je uživatel dospělý

def is_adult(age: int) -> bool:
    return age >= 18

# is_name_valid: Funkce ověří zda uživatelské jméno je alespoň 4 znaky dlouhé

def is_name_valid(name: str) -> bool:
    return len(name) >= 4
    
# def has_email(email: str) -> bool:
#     return email alebo @ in email(???)
# tohle je zbytečné, protože email je povinný parametr, takže pokud ho uživatel nezadá, funkce create_user vrátí False

# create_user:
# Funkce vytvoří slovník reprezentujícího uživatele.

def create_user(name: str, age: int, email: str) -> dict:
    
# Uvnitř funkce zkontroluj, zda je uživatel dospělý a jeho jméno je validní.
# # Pokud validace selže, create_user vrátí:
# {
# "success": False,
# "error": "Chybová zpráva..."
# }  
    # validace veku

    if not is_adult(age):
        return {"success": False, "error": "User is not an adult."}

    # validace mena

    if not is_name_valid(name):
        return {"success": False, "error": "Name is not valid."}
    
# Pokud je vše v pořádku, create_user vrátí následující slovník:

    return {"success": True, "username": {"name": name, "age": age, "email": email}}

# print_user_info: 
# Funkce vytiskne uživatele do konzole s libovolným formátováním, případně vytiskne chybovou zprávu při neúspěšném vytvoření.

def print_user_info(user: dict) -> None:
    if user["success"]:
        print(f"User {user['username']['name']} , {user['username']['age']} , {user['username']['email']}.")
    else:
        print(f"User is not valid.")

# Pomocí metody create_user vytvoř alespoň 4 různé uživatele. Hodnoty si zvol podle sebe přímo v programu.

user1 = create_user("Ivana", 25, "ivana@gmail.com")
user2 = create_user("Oliver", 17, "oliver@gmail.com")
user3 = create_user("Mary", 37, "mary@gmail.com")
user4 = create_user("Bob", 56, "peter@gmail.com") 

users = [user1, user2, user3, user4]

# Nakonec vytvořené uživatele vytiskni pomocí cyklu a metody print_user_info.

for user in users:
    print_user_info(user)