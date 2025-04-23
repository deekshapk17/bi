from bottle import Bottle, run

app = Bottle()

@app.route('/')
def index():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8" />
      <title>Book Manager</title>
      <style>
        /* Basic reset and styles */
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
          font-family: Arial, sans-serif;
        }

        body {
          background: #f4f4f4;
          padding: 20px;
        }

        h1 {
          text-align: center;
          margin-bottom: 20px;
        }

        /* Form Styles */
        #bookForm {
          max-width: 400px;
          margin: 0 auto 20px auto;
          display: flex;
          gap: 10px;
        }

        #bookForm input {
          flex: 1;
          padding: 8px;
          border: 1px solid #ccc;
          border-radius: 4px;
        }

        #bookForm button {
          padding: 8px 16px;
          border: none;
          background: #007BFF;
          color: #fff;
          border-radius: 4px;
          cursor: pointer;
        }

        #bookForm button:hover {
          background: #0056b3;
        }

        /* Search Box */
        #searchContainer {
          max-width: 400px;
          margin: 0 auto 20px auto;
          display: flex;
        }

        #searchInput {
          flex: 1;
          padding: 8px;
          border: 1px solid #ccc;
          border-radius: 4px;
        }

        /* Book List */
        #bookList {
          max-width: 400px;
          margin: 0 auto;
          list-style-type: none;
          background: #fff;
          border-radius: 4px;
          border: 1px solid #ccc;
          padding: 10px;
        }

        #bookList li {
          padding: 8px;
          border-bottom: 1px solid #eee;
        }

        #bookList li:last-child {
          border-bottom: none;
        }
      </style>
    </head>
    <body>
      <h1>Book Manager</h1>

      <!-- Form to Add Books -->
      <form id="bookForm">
        <input type="text" id="title" placeholder="Book Title" required />
        <input type="text" id="author" placeholder="Author" required />
        <button type="submit">Add Book</button>
      </form>

      <!-- Search Box -->
      <div id="searchContainer">
        <input type="text" id="searchInput" placeholder="Search books..." />
      </div>

      <!-- Display Book List -->
      <ul id="bookList"></ul>

      <script>
        // Global array to hold books
        let books = [];

        // Handle form submission to add a new book
        const bookForm = document.getElementById('bookForm');
        bookForm.addEventListener('submit', function(e) {
          e.preventDefault();

          // Get form values
          const titleInput = document.getElementById('title');
          const authorInput = document.getElementById('author');

          // Create a book object
          const newBook = {
            title: titleInput.value.trim(),
            author: authorInput.value.trim()
          };

          // Add the new book to the books array
          books.push(newBook);

          // Clear form inputs
          titleInput.value = '';
          authorInput.value = '';

          // Re-render the book list
          renderBooks();
        });

        // Function to render books (with optional search filter)
        function renderBooks(filterText = '') {
          const bookList = document.getElementById('bookList');
          bookList.innerHTML = ''; // Clear existing items

          // Filter books by search text
          const filteredBooks = books.filter((book) => {
            return (
              book.title.toLowerCase().includes(filterText.toLowerCase()) ||
              book.author.toLowerCase().includes(filterText.toLowerCase())
            );
          });

          // Create an <li> for each book
          filteredBooks.forEach((book) => {
            const li = document.createElement('li');
            li.textContent = `${book.title} by ${book.author}`;
            bookList.appendChild(li);
          });
        }

        // Handle search input to filter books
        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', function() {
          const filterText = searchInput.value.trim();
          renderBooks(filterText);
        });

        // Initial render (even if no books exist yet)
        renderBooks();
      </script>
    </body>
    </html>
    """
    return html_code

if __name__ == '__main__':
    run(app, host='localhost', port=8000, debug=True)
