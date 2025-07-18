# AutoMax

AutoMax is a web application for buying and selling used cars. It serves as a feature-rich marketplace where users can list their cars, browse available vehicles, and connect with sellers or buyers.

Visit the deployed site: [AutoMax on Render](https://automax-04az.onrender.com/)

---

## Features

- **User Registration & Authentication**: Secure sign-up and login system.
- **Car Listing**: Users can create, edit, and manage their used car listings with details like brand, model, VIN, mileage, color, engine, and images.
- **Marketplace Browsing**: Search and filter available car listings.
- **Profile Management**: Users can view their own listings and keep track of cars they've liked.
- **Responsive and Modern UI**: Clean, mobile-friendly interface built with Bootstrap and Django templates.
- **Video Background Homepage**: Engaging landing page for a modern marketplace feel.
- **Like/Favorite Listings**: Users can like cars and manage their favorites.
- **Admin Panel**: Django-powered admin interface for full control over listings and users.

---

## Getting Started

These instructions will help you set up and run the project locally.

### Prerequisites

- Python 3.8+
- pip
- PostgreSQL (for production) or SQLite (for development)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gandharvk422/automax.git
   cd automax
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   - Copy `.env.example` to `.env` and set your environment variables as needed (DB credentials, secret key, etc).

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000/`

---

## Project Structure

```
automax/
├── src/
│   ├── automax/         # Django project configuration
│   ├── main/            # Main app: models, views, templates for car listings
│   ├── users/           # User management: registration, profile, authentication
│   ├── static/          # Static files (CSS, JS, images, videos)
│   └── templates/       # HTML templates
├── requirements.txt
├── .env.example
└── README.md
```

---

## Technologies Used

- Django 5.x
- PostgreSQL (or SQLite for dev)
- Bootstrap 5
- Crispy Forms
- HTML5/CSS3/JS

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is currently unlicensed.

---

## Credits

Developed by Gandharv Kulkarni.  
Powered by [Django](https://www.djangoproject.com/) and [Preneure.com](https://www.preneure.com).
