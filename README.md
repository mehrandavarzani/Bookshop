# Bookshop
A Django-based web application for managing a bookshop. This project includes features for user account management, book inventory management, and order processing. The application uses SQLite for the database and follows best practices for Django project structure.

## Detailed Description
The Bookshop project is a comprehensive web application designed to help manage various aspects of a bookshop. It is built using the Django web framework and includes the following features:

- **User Accounts:** Allows users to register, log in, and manage their profiles.
- **Book Management:** Admins can add, edit, and delete books in the inventory.
- **Order Processing:** Users can browse books, add them to their cart, and place orders.
- **Database:** Utilizes SQLite for data storage and management.
- **Admin Interface:** Provides an admin interface for managing users, books, and orders.

This project serves as a foundation for developing more complex e-commerce applications using Django.

## Key Features
- User authentication and authorization
- Book inventory management
- Order processing and management
- SQLite database integration
- Django admin interface for easy management

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/bookshop.git
   cd bookshop

2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install django

3. Apply migrations:
   ```sh
   python manage.py migrate

4. Run the development server:
   ```sh
   python manage.py runserver

5. Access the project:
   Open your web browser and navigate to http://127.0.0.1:8000/ to see your project running.


## Technologies Used
Python
Django
SQLite
