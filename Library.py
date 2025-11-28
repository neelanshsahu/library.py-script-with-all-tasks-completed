import csv

books = {}
borrowed = {}

def print_header():
    print("="*40)
    print("NAME:Neelansh sahu")  
    print("ROLL NO:2501201049")
    print("PROGRAM: BCA ( AI & DS )")
    print("SECTION: C")
    print("="*40)

def load_data():
    try:
        with open("books.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    books[row[0]] = {"title": row[1], "author": row[2], "copies": int(row[3])}
    except FileNotFoundError:
        books.update({
            "B101": {"title": "Python Basics", "author": "Guido", "copies": 5},
            "B102": {"title": "Data Science", "author": "Cormen", "copies": 3},
            "B103": {"title": "AI Intro", "author": "Russell", "copies": 4},
            "B104": {"title": "Clean Code", "author": "Martin", "copies": 2},
            "B105": {"title": "Deep Learning", "author": "Hinton", "copies": 3}
        })
        save_data()

    try:
        with open("borrowed.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    borrowed[row[0]] = row[1]
    except FileNotFoundError:
        pass

def save_data():
    with open("books.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for b_id, data in books.items():
            writer.writerow([b_id, data["title"], data["author"], data["copies"]])
            
    with open("borrowed.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for student, b_id in borrowed.items():
            writer.writerow([student, b_id])

def add_book():
    print("\n--- Add New Book ---")
    b_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    try:
        copies = int(input("Enter Number of Copies: "))
        books[b_id] = {"title": title, "author": author, "copies": copies}
        save_data()
        print(f"Book {title} added successfully!")
    except ValueError:
        print("Invalid input. Please enter a number for copies.")

def view_books():
    print("\n--- Library Books ---")
    print(f"{'ID':<10} {'Title':<20} {'Author':<15} {'Copies':<5}")
    print("-" * 50)
    for b_id, details in books.items():
        print(f"{b_id:<10} {details['title']:<20} {details['author']:<15} {details['copies']:<5}")

def search_book():
    query = input("\nEnter Book ID or Title to search: ").lower()
    found = False
    print(f"\n{'ID':<10} {'Title':<20} {'Author':<15} {'Copies':<5}")
    print("-" * 50)
    
    for b_id, details in books.items():
        if query in b_id.lower() or query in details['title'].lower():
            print(f"{b_id:<10} {details['title']:<20} {details['author']:<15} {details['copies']:<5}")
            found = True
    
    if not found:
        print("No book found with those details.")

def borrow_book():
    name = input("\nEnter Student Name: ")
    b_id = input("Enter Book ID to borrow: ")

    if b_id in books:
        if books[b_id]['copies'] > 0:
            books[b_id]['copies'] -= 1
            borrowed[name] = b_id
            save_data()
            print(f"Book '{books[b_id]['title']}' issued to {name}.")
        else:
            print("Sorry, this book is currently out of stock.")
    else:
        print("Invalid Book ID.")

def return_book():
    name = input("\nEnter Student Name: ")
    b_id = input("Enter Book ID to return: ")

    if name in borrowed and borrowed[name] == b_id:
        books[b_id]['copies'] += 1
        del borrowed[name]
        save_data()
        print(f"Book '{books[b_id]['title']}' returned successfully.")
        
        borrowed_list = [f"{student} -> {book}" for student, book in borrowed.items()]
        print("\nCurrently Borrowed Books (Tracker):")
        if borrowed_list:
            for record in borrowed_list:
                print(record)
        else:
            print("No books are currently borrowed.")
    else:
        print("No record found for this student and book combination.")

load_data()
print_header()

while True:
    print("\n" + "="*30)
    print("LIBRARY BOOK MANAGER")
    print("="*30)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        borrow_book()
    elif choice == '5':
        return_book()
    elif choice == '6':
        print("Exiting Library Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


