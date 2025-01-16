class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author


class Library:
  books = []

  def __init__(self, name):
    self.name = name

  def add_book(self, book):
    self.books.append(book)

  def remove_book(self, book):
    for b in self.books:
      if b.title.lower() == book.title.lower():
        self.books.remove(b)

  def search_books(self, search_string):
    matched_books = []
    for book in self.books:
      title = book.title.lower()
      author = book.author.lower()
      if search_string in title or search_string in author:
        matched_books.append(book)
    return matched_books


run_cases = [
    (
        "Jane's Library",
        ["The Trial"],
        ["Franz Kafka"],
        Book("The Trial", "Franz Kafka"),
        "Kafka",
        [],
    ),
    (
        "John's Library",
        ["The Catcher in the Rye", "To Kill a Mockingbird", "1984"],
        ["J.D. Salinger", "Harper Lee", "George Orwell"],
        Book("1984", "George Orwell"),
        "kill",
        ["To Kill a Mockingbird"],
    ),
]

submit_cases = run_cases + [
    (
        "Lane's Library",
        [
            "The Great Gatsby",
            "Pride and Prejudice",
            "The Lord of the Rings",
            "Great Expectations",
            "To Kill a Mockingbird",
        ],
        [
            "F. Scott Fitzgerald",
            "Jane Austen",
            "J.R.R. Tolkien",
            "Charles Dickens",
            "Harper Lee",
        ],
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        "great",
        ["Great Expectations"],
    ),
]


def test(
    library_name,
    book_titles,
    book_authors,
    book_to_remove,
    search_query,
    expected_search_results,
):
  print("---------------------------------")
  try:
    print(f"Testing Library: {library_name}")

    library = Library(library_name)
    for title, author in zip(book_titles, book_authors):
      library.add_book(Book(title, author))
      print(f"Adding book {title} by {author}")

    print(f"Removing book {book_to_remove.title} by {book_to_remove.author}")
    library.remove_book(book_to_remove)

    print(f"Searching for '{search_query}'")
    search_results = library.search_books(search_query)
    results_titles = [book.title for book in search_results]
    print(f"Expected: {expected_search_results}")
    print(f"Actual: {results_titles}")

    if results_titles != expected_search_results:
      print("Fail")
      return False

    print("Pass")
    return True
  except Exception as e:
    print(f"Error: {e}")
    return False


def main():
  passed, failed = 0, 0
  for test_case in test_cases:
    correct = test(*test_case)
    if correct:
      passed += 1
    else:
      failed += 1

  if failed == 0:
    print("============= PASS ==============")
  else:
    print("============= FAIL ==============")
  print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
  test_cases = run_cases

main()
