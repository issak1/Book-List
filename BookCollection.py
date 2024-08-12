class BookNode:
  def __init(self, book_name), author, date_published, read=False):
        self.book_name = book_name
        self.author = author
        self.date_published = date_published
        self.read = read # indicate if a book has been read
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
