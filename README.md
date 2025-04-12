# LeafSense - Plant Disease Detection Platform

LeafSense is a Django-based web application that uses Google's Gemini 1.5 AI to detect plant diseases from leaf images. The platform provides detailed diagnosis, treatment recommendations, and care tips for various plant diseases.

## Features

- User Authentication System
- Plant Disease Detection using Gemini 1.5 AI
- Detection History Tracking
- Feedback System
- Dark Mode Support
- Mobile-Friendly Interface

## Tech Stack

- Backend: Django 5.0
- Database: PostgreSQL
- Frontend: Django Templates with TailwindCSS
- AI Integration: Google Gemini 1.5 API
- Deployment: Ready for Render/Railway/DigitalOcean

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file with the following variables:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://growmate_es40_user:c9JVKjOmO6D4CjeVtlo2YFXg5GV08rEm@dpg-cvd6gjhc1ekc73aubuo0-a.oregon-postgres.render.com/growmate_es40
   GEMINI_API_KEY=your-gemini-api-key
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
leafsense/
├── leafsense/             # Project settings
├── detection/             # Main app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/detection/
│       ├── dashboard.html
│       ├── history.html
│       └── feedback.html
├── media/                 # Uploaded images
├── static/                # CSS/JS if needed
├── requirements.txt
└── Procfile               # For deployment
```

## License

MIT License 