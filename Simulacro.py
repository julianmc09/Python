catalog={}

def RegisterBook(title, author, genre,yearP,qty,price):
    if title in catalog:
        print(f"The book {title} already exists")
    else:
        catalog[title] = (price,author,genre,yearP,qty)
        print(f"Book {title} successfully added")

def SearchBook(title):
    book = catalog.get(title)
    if book:
        print(f"book: {title}\nPrice: {book[0]}\nAuthor: {book[1]}\nGenre: {book[2]}\nYear of publication: {book[3]}\nQuantity: {book[4]}")
    else:
        print(f"The book {title} is not in catalog, you can register it")

def UpdatePrice(title,NewPrice):
    if title in catalog:
        _, author, genre, yearP, qty = catalog[title]
        catalog[title] = (NewPrice, author, genre, yearP, qty)
        print(f"The price of {title} has been updated to: {NewPrice}")
    else:
        print(f"Unable to update, the product {title} is not in the catalog.")

def UpdateQuantity(title,NewQty):
    if title in catalog:
        price, author, genre, yearP, _ = catalog[title]
        catalog[title] = (price, author, genre, yearP, NewQty)
        print(f"Quantity of {title} has been updated to: {NewQty}.")
    else:
        print(f"Unable to update, the product {title} is not in the catalog.")

def DeleteBooks(title):
    if title in catalog:
        del catalog[title]
        print(f"the book {title} has been removed from the catalog ")
    else:
        print(f"cannot be deleted, the book {title} is not in the catalog")

def TotalValue():
    total = 0
    for dat in catalog.values():
        price = dat[0]
        qty = dat[4]
        total += price * qty
    print(f"Total value of catalog: {total}")


def BookNewAndOld():
    if not catalog:
        print("The catalog is empty.")
        return

    # Crear una lista de tuplas (title, year) para poder buscar el libro más antiguo y el más reciente
    BooksWithYears = [(title, data[3]) for title, data in catalog.items()]

    # Obtener el libro más antiguo y el más reciente usando las funciones min() y max()
    oldest = min(BooksWithYears, key=lambda x: x[1])
    newest = max(BooksWithYears, key=lambda x: x[1])

    print(f"Oldest book: {oldest[0]} published in {oldest[1]}")
    print(f"Newest book: {newest[0]} published in {newest[1]}")
def ReadPositive(message):
    entry = input(message)
    number = int(entry)
    if number > 0:
        return number
    else:
        print("Invalid information entered")
        return None
    
while True:
    option = input("Enter the option you wish to perform:\n 1.Register new book\n 2.Search book in catalog\n 3.Update price\n 4.Update quantity\n 5.Delete books\n 6.Calculate total value of the inventory\n 7.Show book from the oldest to the newest\n 8.Exit menu\n")
    if option =="1":
        title = (input("Name of book: ").strip().lower())
        author = input("Author of book: ")
        genre = input("Genre of book: ")
        try:
            yearP = int(input("Year of publication: "))
            if yearP > 2025:
                print("The year of publication must be 2025 or less.")
                continue  
        except ValueError:
            print("Invalid input. Please enter a numeric year.")
            continue  
         
        price = ReadPositive("Price of the book: ")
        qty = ReadPositive("Quantity of books: ")
        if price is not None and qty is not None:
            RegisterBook(title,author,genre,yearP,qty,price)
        

    elif option =="2":
        title = input("Title of book to be consulted: ").strip().lower()
        SearchBook(title)

    elif option =="3":
        title = input("book title to update its price: ").strip().lower()
        NewPrice = ReadPositive("New price: ")
        if NewPrice is not None:
            UpdatePrice(title,NewPrice)

    elif option =="4":
        title = input("book title to update its quantity: ").strip().lower()
        NewQty = ReadPositive("New quantity: ")
        if NewQty is not None:
            UpdateQuantity(title,NewQty)

    elif option =="5":
        title = input("Tile of book to eliminate: ")
        DeleteBooks(title)

    elif option =="6":
        TotalValue()

    elif option =="7":
        BookNewAndOld()
    
    elif option =="8":
        print("you have exited the menu")
        break
    else:
        print("Invalid option")


