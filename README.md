# Quick Polls - Django Based Polling Application

## Overview

Quick Polls is a Django-based polling application that allows users to create and participate in polls. Built with Django framework and styled with Bootstrap, this application offers features such as user authentication, dynamic poll creation, and customizable filtering options.

## Features

- **User Authentication**: Users can register, log in, and manage their accounts.
- **Login Required Middleware**: Ensure that certain views are accessible only to authenticated users.
- **Django Forms**: Utilize Django’s form handling to create and manage polls and user input.
- **Bootstrap UI**: A responsive and modern UI using Bootstrap for a better user experience.
- **Dynamic Poll Creation**: Create polls with multiple choices, tags, and images.
- **Filtering**: Filter polls based on sorting data and tags.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mohit-trootech/Quick-Polls
   cd Quick-Polls
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate 
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data**

   ```bash
   python manage.py loaddata data.json
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

8. **Access the Application**

   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or issues, please contact:

- **GitHub**: [https://github.com/yourusername](https://github.com/mohit-trootech)
