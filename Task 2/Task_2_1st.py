import datetime 

class Book: 
    ID = 1 
    def __init__(self,name,author,dop):
        self.name = name
        self.author = author 
        self.id =  Book.ID
        self.dop = dop
        Book.ID += 1

class member: 
    ID = 1 
    def __init__(self,name,phoneNumber,address):
        self.name = name
        self.phoneNumber = phoneNumber
        self.address = address
        self.id = member.ID 
        member.ID += 1

class LibraryManagementSystem:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.borrowedBooks = {}
        self.log = {}

    def addMember(self,member):
        self.members[member.id] = member
        self.log[member.id]=[]

    def addBook(self,book):
        self.books[book.name] = book

    def showBooks(self): 
        for key,value in self.books.items():
            print(f'{value.id}- {value.name} | Author: {value.author} | Date of Publish: {value.dop}')

    def borrowBook(self,book,member,duration): 
        today = datetime.datetime.now().date()
        self.log[member.id].append(f'{book.name} for {duration} starting at {today}')
        self.borrowedBooks[book.name] = member.id
        self.books.pop(book.name)
        
    def returnBook(self,book,member): 
        today = datetime.datetime.now().date()
        self.log[member.id].append(f'Returned {book.name} at {today}')
        self.borrowedBooks.pop(book.name)
        self.books[book.name] = book

    def showBorrowedBooks(self):
        for key,value in self.borrowedBooks.items(): 
            print(f"{key} borrowed by member: {value}")

    def showLog(self): 
        for key, value in self.log.items() :
            if len(value) != 0 :
                print(f"{key} - {value}")



def runLibraryManagementSystem(): 
    while True : 
        print("")
        print("     Library Managment System        ")
        print("1- Show available books")
        print("2- Register as a new member or enter your member id")
        print("3- Borrow a book")
        print("4- Return a book")
        print("5- Show borrowed books")
        print("6- Exit")

        userSelection = int(input("Enter: "))

        match userSelection :
            case 1: 
                BiblothicaAlexandria.showBooks() 

            case 2: 
                option = int(input("Enter 1 to register as a new member, 2 to enter your id: "))
                if option == 1:
                    name = input("Enter your name: ")
                    phoneNumber = input("Enter your phone number: ")
                    address = input("Enter your address: ")
                    newMember = member(name,phoneNumber,address)
                    print(f"Your member id is : {newMember.id}")
                    BiblothicaAlexandria.addMember(newMember)
                    currentMember = newMember

                elif option == 2:
                    memberID = int(input("Enter your member id: "))
                    if memberID in BiblothicaAlexandria.members:
                        currentMember = BiblothicaAlexandria.members[memberID]
                    else:
                        print("No member with that id.")
                else:
                    print("Invalid option, please enter 1 or 2.")
                
            case 3: 
                bookName = input("Enter the name of the book: ")
                book = BiblothicaAlexandria.books[bookName]
                duration = int(input("Enter the duration: "))
                BiblothicaAlexandria.borrowBook(book,currentMember,duration)

            case 4: 
                bookName = input("Enter the name of the book you want to return: ")
                book = BiblothicaAlexandria.borrowedBooks[bookName]
                BiblothicaAlexandria.returnBook(book,currentMember)

            case 5: 
                BiblothicaAlexandria.showBorrowedBooks()

            case 6: 
                currentMember = None 
                break 



if __name__ == '__main__' : 

    BiblothicaAlexandria = LibraryManagementSystem()

    Dune = Book("Dune", "Frank Herbert", "1965")
    ProjectHailMary = Book("Project Hail Mary", "Andy Weir", "2021")
    ItEndsWithUs = Book("It Ends With Us", "Colleen Hoover", "2016")
    AtomicHabits = Book("Atomic Habits", "James Clear", "2018")
    TheHobbit = Book("The Hobbit", "J.R.R. Tolkien", "1937")
    CleanCode = Book("Clean Code", "Robert C. Martin", "2008")
    ThePragmaticProgrammer = Book("The Pragmatic Programmer", "Andrew Hunt", "1999")
    TheAlchemist = Book("The Alchemist", "Paulo Coelho", "1988")

    BiblothicaAlexandria.addBook(Dune)
    BiblothicaAlexandria.addBook(ProjectHailMary)
    BiblothicaAlexandria.addBook(ItEndsWithUs)
    BiblothicaAlexandria.addBook(AtomicHabits)
    BiblothicaAlexandria.addBook(TheHobbit)
    BiblothicaAlexandria.addBook(CleanCode)
    BiblothicaAlexandria.addBook(ThePragmaticProgrammer)
    BiblothicaAlexandria.addBook(TheAlchemist)

    currentMember = None

    runLibraryManagementSystem()
