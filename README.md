##  E-commerce Store with Flask

This is a simple e-commerce store built with Flask. The project allows users to register, login, browse products, and add items to their cart. It includes basic user authentication and a simple in-memory database to store user data.

### index.py

This file contains the main Flask application logic.

**Functionality:**

* **Routing:** Defines routes for the home page (`/`), login (`/login`), registration (`/register`), cart view (`/cart`), adding items to cart (`/add-to-cart`), login submission (`/login-submit`), registration submission (`/register-submit`), and logout (`/logout`).
* **Templating:** Uses Jinja2 templating to render HTML pages for the different routes.
* **User Authentication:** Implements basic user login and registration functionality. User data is stored in an in-memory dictionary (`users`).
* **Session Management:** Uses cookies to manage user sessions.
* **Cart Management:** Allows users to add items to their cart. Cart data is stored in an in-memory dictionary (`cart`).
* **Global `logged_in` variable:** Tracks the user's login status and is updated during login and logout.
* **Error Handling:** Provides a simple error handling mechanism for incorrect login attempts.

**Key Components:**

* **Flask:** The web framework used to build the application.
* **Jinja2:** The templating engine used to render HTML pages.
* **`users` dictionary:**  Stores user data (username, password, email).
* **`sessions` dictionary:** Tracks active user sessions.
* **`cart` dictionary:** Stores items in the user's shopping cart.
* **`logged_in` variable:** Tracks user login status.

**Improvements:**

* **Database Integration:** Currently, user data and cart information are stored in memory, which makes them volatile. Integrating a database (e.g., SQLite, PostgreSQL) would provide persistence and scalability.
* **Product Data:** The `add_to_cart` function uses placeholder product data. Replace this with actual product information from a database or external API.
* **Security:** Implement robust security measures such as password hashing, input validation, and CSRF protection.

**To run the application:**

1. Make sure you have Python and Flask installed.
2. Navigate to the directory containing the `index.py` file in your terminal.
3. Run `flask run`. 
4. Access the application in your web browser at `http://127.0.0.1:5000/`.

This README provides a basic overview of the project. Further documentation for specific functionalities or additional features can be added as needed.
