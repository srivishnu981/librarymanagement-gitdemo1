#i made a change
print("Library Management System")
from member import Member
from library import  Library


def main():
    library = Library()

    # Load books from the data file
    library.load_books("data/books.txt")

    # Create members
    member1 = Member(1, "Rahul")
    member2 = Member(2, "Priya")

    library.add_member(member1)
    library.add_member(member2)

    print("BOOKS")
    print("-----------------------------")
    library.show_books()

    print("\nIssuing book...")
    library.issue_book(101, 1)

    print("\nBOOKS AFTER ISSUE")
    print("-----------------------------")
    library.show_books()

    print("\nReturning book...")
    library.return_book(101, 1)

    print("\nBOOKS AFTER RETURN")
    print("-----------------------------")
    library.show_books()


if __name__ == "__main__":
    main()
