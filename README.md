# Green Blog

Green Blog is a Django-based blog project designed to inspire the use of Sweden's "allemansrätt" (right to roam) and provide a platform for users to share and discover outdoor experiences through text and image posts. Users can create accounts, add and remove their own posts, like and comment on others' posts, and utilize geotagging and filtering posts based on location.

## Features

- **User Accounts**: Create and delete user accounts.
- **Posts**: Add text and image posts with the ability to delete your own posts.
- **Likes**: Like posts with a green leaf emoji.
- **Comments**: Leave comments on posts.
- **Geotagging**: Tag posts with a location.
- **Location-Based Filtering**: Filter posts by city or region.

## Technologies

- Django 4.x
- PostgreSQL (as the database)
- Bootstrap 5 for responsive design
- Whitenoise for static file management in production
- Git and GitHub for version control
- Heroku for deployment

## Installation

Follow these steps to get the project running locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/green_blog.git

Create and activate a virtual environment
First, create and activate a virtual environment to install the dependencies:

python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'

Install dependencies

pip install -r requirements.txt

Configure environment variables
Create a .env file in the project's root directory and add your environment variables:

DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/dbname

Migrate the database
python manage.py migrate

Collect static files
python manage.py collectstatic

Start the server
python manage.py runserver
Open your browser and go to http://localhost:8000 to view the blog.

Deployment
To deploy to Heroku, follow these steps:

Log in to Heroku and create a new application.

Use the Heroku CLI to link your project to Heroku:

heroku login
heroku create
git push heroku main

Set up the database on Heroku:

heroku run python manage.py migrate

Collect static files for Heroku:
heroku run python manage.py collectstatic

Open the app in your browser:
heroku open

Functionality
Homepage
The homepage displays a list of the latest blog posts, including an excerpt and images. Users can click on a post to read more and leave comments.

User Accounts
Users can register, log in, and create their own accounts. They can also delete their posts and see posts they have liked.

Geotagging and Filtering
Users can tag their posts with a location (e.g., a city or national park), allowing posts to be filtered based on geography.

Improvements and Future Features
Ability to search for specific posts or tags.
Improved responsiveness and optimization for mobile devices.
Admin functionality to edit or delete posts from other users.
Add a feature to upload profile pictures.
License
This project is licensed under the MIT License - see LICENSE for more information.

Contact
For questions or feedback, please contact me via [your email address or GitHub profile].


### Explanation of the sections:

1. **Project Description**: A brief introduction to what the project is about and its functionality.
2. **Features**: Key features that the application offers (user accounts, posts, likes, comments, geotagging, etc.).
3. **Technologies**: The technologies used in the project (Django, PostgreSQL, Bootstrap, Heroku, etc.).
4. **Installation**: Step-by-step instructions for installing and running the project locally.
5. **Deployment**: How to deploy the project to Heroku.
6. **Functionality**: A summary of the key functionalities of the app, like homepage, user accounts, and geotagging.
7. **Improvements**: Possible future improvements or features that could be added.
8. **License**: Information about the license (MIT License).
9. **Contact**: How to reach you for questions or feedback.


