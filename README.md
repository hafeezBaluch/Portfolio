# Portfolio Project in Django
- This repository contains the source code for a portfolio website built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. The portfolio showcases the projects, skills, and experiences of the developer, making it an excellent tool for showcasing your work to potential employers or clients.

## Features

- **Responsive Design**: The portfolio is designed to be responsive, ensuring it looks great on all devices, from desktops to mobile phones.
- **Dynamic Content**: The website dynamically loads content from the database, allowing for easy updates and maintenance.
- **Contact Form**: Includes a contact form for visitors to get in touch with the portfolio owner.
- **SEO Optimized**: The website is optimized for search engines, helping to improve visibility in search results.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Django 5 or higher
- SLQlite (optional, for database)

### Installation

1. **Clone the Repository**:
- https://github.com/hafeezBaluch/Portfolio.git

2. **Create a Virtual Environment**
- python -m venv venv and activate it venv\Scripts\activate

3. **Install Dependencies**
- pip install -r requirements.txt


4. **Configure the Database**
- If you're using PostgreSQL, update the `DATABASES` setting in `settings.py` with your database credentials.

5. **Run Migrations**
- python manage.py migrate

6. **Run the Server**
- python manage.py runserver
- Visit `http://127.0.0.1:8000/` in your web browser to view the portfolio.
## Customization

- **Update Content**: Modify the content in the `templates` and `static` directories to customize the portfolio.
- **Add Projects**: Add your projects to the database through the Django admin interface or by modifying the database directly.
- **Customize Styles**: Update the CSS in the `static/css` directory to change the look and feel of the portfolio.

## Contributing
- Contributions are welcome! If you find a bug or have a feature request, please open an issue on GitHub. If you'd like to contribute code, please fork the repository and submit a pull request.

## Contact
- If you have any questions or feedback, please feel free to contact the owner.
