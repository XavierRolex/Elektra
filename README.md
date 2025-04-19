# Elektra

## Overview
Elektra is a clothing-focused e-commerce platform developed using Python and the Django web framework. While the project is still a work in progress, it already implements several essential features required for a functional online store. Elektra serves as a solid foundation for building a complete and scalable e-commerce website tailored to the fashion industry.

---

##  Features

-  Wishlist Functionality  
-  Cart Management with Quantity Control  
-  Search Bar to Find Products Quickly  
-  Checkout Preprocessing  
-  Order Tracking and Management  
-  Easy Order Cancellation  
-  Product Management for Full Control  
-  Category List for Easy Browsing  
-  User Profiles with Purchase History  
-  Customer Support Integration

---

##  Tech Stack

- **Backend**: Python, Django  
- **Documentation**: Sphinx  
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap 5

---

##  Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/elektra.git
   cd elektra
   ```
   
2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Access the site**
    
    Open your browser and go to http://127.0.0.1:8000/

---

##  Project Structure
```bash
elektra/
├── elektra/             # Main project config
├── store/               # Django app with models, views, and templates
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── tests.py
├── templates/           # Global templates
├── manage.py
└── requirements.txt
```

---

## Documentation

The project is documented using Sphinx. Run the following to generate docs:
```bash
cd docs
make HTML
```

---

## Contributors

- Nafis Anzum
- Israt Zaman Srity
- Sajed Junaid Moeen Huda
- Nova Khan
- Md. Farhadul Hasan Nayon
