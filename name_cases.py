name = "Martin"
message = f"Hi {name}, how are ya?"
print (message)
print (f"Hi {name}, how are ya?")

name2 = "Klay"
print (name2.lower())
print (name2.upper())
print (name2.title())

quote = 'Marco Polo once said, "City never sleeps."'
print (quote)
famous_person = "Marco Polo"
message1 = f'{famous_person} once said, "City never sleeps."'
print (message1)
filename = "python_notes.txt"

print (filename)
print (filename.removesuffix('.txt'))

name3 = " Peter "
print (name3)
print (name3.lstrip(), name3.rstrip(), name3.strip())
print (f"\t\t{name3.lstrip()}\n {name3.rstrip()}\n\t {name3.strip()}")