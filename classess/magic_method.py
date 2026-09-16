class Book:
    def __init__(self, title , author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self):
        return f"'{self.title}' by {self.author}"



book1 = Book("Atomic Habits", "J.Clear", 223)
book2 = Book("No More Mr. Nice Guy", "Robert A. Glover", 208)
book1 = Book("How to Win Friends and Influence People", " Dale Carnegie", 192)
print(book1)