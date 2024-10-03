class BookNode:
    def __init__(self, book_name, author, date_published, read=False):
        self.book_name = book_name
        self.author = author
        self.date_published = date_published
        self.read = read  
        self.next = None

class BookLinkedList:
    def __init__(self):
        self.head = None

    def add_book(self, book_name, author, date_published, read=False):
        new_book = BookNode(book_name, author, date_published, read)
        new_book.next = self.head
        self.head = new_book
        print(f"Book '{book_name}' by {author} added.")
    
    def search_book(self, search_term):
        current = self.head
        while current:
            if search_term.lower() in current.book_name.lower() or \
               search_term.lower() in current.author.lower() or \
               search_term in current.date_published:
                read_status = "Read" if current.read else "Not Read"
                print(f"Found: {current.book_name} by {current.author}, Published: {current.date_published}, Status: {read_status}")
                return
            current = current.next
        print("Book not found.")

    def display_books(self):
        current = self.head
        if current is None:
            print("No books in the collection.")
            return
        while current:
            read_status = "Read" if current.read else "Not Read"
            print(f"{current.book_name} by {current.author}, Published: {current.date_published}, Status: {read_status}")
            current = current.next

    def remove_book(self, book_name):
        current = self.head
        prev = None
        while current:
            if current.book_name == book_name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Book '{book_name}' removed.")
                return
            prev = current
            current = current.next
        print(f"Book '{book_name}' not found.")

    def count_books(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Total books in collection: {count}")

    def sort_books(self, by='author'):
        if self.head is None or self.head.next is None:
            return
            
        swapped = True
        while swapped:
            current = self.head
            swapped = False
            while current.next:
                if by == 'author':
                    if current.author > current.next.author:
                        current.book_name, current.next.book_name = current.next.book_name, current.book_name
                        current.author, current.next.author = current.next.author, current.author
                        current.date_published, current.next.date_published = current.next.date_published, current.date_published
                        current.read, current.next.read = current.next.read, current.read
                        swapped = True
                elif by == 'read':
                    if not current.read and current.next.read:
                        current.book_name, current.next.book_name = current.next.book_name, current.book_name
                        current.author, current.next.author = current.next.author, current.author
                        current.date_published, current.next.date_published = current.next.date_published, current.date_published
                        current.read, current.next.read = current.next.read, current.read
                        swapped = True
                current = current.next

    def mark_as_read(self, book_name):
        current = self.head
        while current:
            if current.book_name == book_name:
                current.read = True
                print(f"Book '{book_name}' marked as read.")
                return
            current = current.next
        print(f"Book '{book_name}' not found.")

if __name__ == "__main__":
    book_list = BookLinkedList()

    while True:
        command = input("Enter command (add, search, display, remove, count, sort, mark read, exit): ").strip().lower()
        if command == "add":
            name = input("Enter book name: ")
            author = input("Enter author: ")
            date_published = input("Enter date published: ")
            read_status = input("Has the book been read? (yes/no): ").strip().lower() == "yes"
            book_list.add_book(name, author, date_published, read_status)
        elif command == "search":
            term = input("Enter search term (name, author, or date): ")
            book_list.search_book(term)
        elif command == "display":
            book_list.display_books()
        elif command == "remove":
            name = input("Enter the book name to remove: ")
            book_list.remove_book(name)
        elif command == "count":
            book_list.count_books()
        elif command == "sort":
            sort_by = input("Sort by (author/read): ").strip().lower()
            if sort_by in ['author', 'read']:
                book_list.sort_books(by=sort_by)
            else:
                print("Invalid sort option. Choose 'author' or 'read'.")
        elif command == "mark read":
            name = input("Enter the book name to mark as read: ")
            book_list.mark_as_read(name)
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")


