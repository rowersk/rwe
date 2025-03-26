books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
        
    ]       
books.append(
    {
        "name": "Harry Potter a kámen mudrců",
        "price": 450,
        "author": "J.K. Rowling",
        "publication_year": 1997,
    }
)
books.append(
    {
        "name": "Harry Potter a Tajemná komnata",
        "price": 400,
        "author": "J.K. Rowling",
        "publication_year": 1998,
    }
)
books[0]["price"] = 550
print(books)
books.remove(
    {
        "name": "Harry Potter a kámen mudrců",
        "price": 450,
        "author": "J.K. Rowling",
        "publication_year": 1997,
    }
)
print(books)
print(len(books))

## bonus

x = input("Zadej název knihy: ")
print(x)

# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.

# 2. Změň cenu jedné libovolné knihy. Vypiš list.

# 3. Odstraň nějakou knihu. Vypiš list.

# 4. Vypiš celkový počet knih v listu.

# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)
