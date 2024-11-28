# Green Blog

Green Blog is a Django-based blog project designed to inspire the use of Sweden's "allemansrätt" (right to roam) and provide a platform for users to share and discover outdoor experiences through text and image posts. Users can create accounts, add and remove their own posts, like and comment on others' posts, and utilize geotagging and filtering posts based on location.

## Features

- **User Accounts**: Create and delete user accounts.
- **Likes**: Like posts with a green leaf emoji.
- **Comments**: Leave comments on posts.


## Technologies

- Django 4.x
- PostgreSQL (as the database)
- Bootstrap 5 for responsive design
- Whitenoise for static file management in production
- Git and GitHub for version control
- Heroku for deployment

## Installation

Follow these steps to get the project running locally:

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/green_blog.git
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure environment variables:
    - Create a `.env` file in the project's root directory and add your environment variables:
    ```text
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://user:password@localhost:5432/dbname
    ```

5. Migrate the database:
    ```bash
    python manage.py migrate
    ```

6. Collect static files:
    ```bash
    python manage.py collectstatic
    ```

7. Start the server:
    ```bash
    python manage.py runserver
    ```

    Open your browser and go to `http://localhost:8000` to view the blog.

## Deployment

[&lt; Back to README file](/README.md)

1. Clone the repository:
    -   Open a folder on your computer using the **Command Prompt** on Windows, **Terminal** on Mac or the respective on your device.
    -   Run the following command:
        -   `git clone https://github.com/MY OWN PROJEKT`
---
2. Create your own Github repository to host the code.
---
3. To set the remote repository location to your repository, run the command
    -   `git remote set-url origin <YOUR GITHUB REPO PATH>`
    ---
4. _Push_ the files to your repository to host the code, running the command:
    -   `git push`
    ---
5. Create a Heroku account, if you haven't already, click [Heroku sign-up](https://signup.heroku.com/?utm_source=google&utm_medium=paid_search&utm_campaign=emea_heraw&utm_content=general-branded-search-rsa&utm_term=heroku%20deploy&utm_source_platform=GoogleAds&gad_source=1&gclid=CjwKCAjw3624BhBAEiwAkxgTOnW3NMOV1WnmmRl3waphvbeJMziUKDW38F0Dy3uLfBJLsjNUm-vZdxoCp9MQAvD_BwE)
---
6. Create a new application, from selecting **Create new app** from the dropdown. Follow the steps on the page and click **Create app**.

![Create an app on Heroku_1](/static/test_images/dp_1.png)
![Create an app on Heroku_2](/static/test_images/dp_2.png)

---
7. Navigate to the **Deploy** tab, opening up the Deploy section.
![Deploy tab on Heroku](/static/test_images/dp_3.png)

---
8. Link your Github account and connect the application to the repository you just created.
![Connect Github account](/static/test_images/dp_4.png)

---
9. Navigate to the **Settings** tab, opening up the Settings section.
![Settings tab on Heroku](/static/test_images/dp_10.png)

---
10. Click **Add Buildpack**.
![Add buildpack](/static/test_images/dp_12.png)

--
11. Add the **Python** buildpack.
![Adding python buildpack](/static/test_images/dp_5.png)

---
12. Click **Reveal Configs**
![Reveal config vars](/static/test_images/dp_11.png)

---
13. Add these Config Vars:
    -   **KEY**: DISABLE_COLLECTSTATIC | **VALUE**: 1
    -   **KEY**: SECRET_KEY | **VALUE**: "YOUR OWN SECRET KEY"
    -   **KEY**: DATABASE_URL | **VALUE**: "YOUR OWN DATABASE URL"
![Adding config vars](/static/test_images/dp_6.png)

---
14. Return back to the **Deploy** tab, opening up the Deploy section.
![Deploy tab on Heroku](/static/test_images/dp_3.png)

---
15. At the bottom of the page, click **Deploy** branch.
![Deploy button](/static/test_images/dp_7.png)

---
16. Wait while Heroku is deploying your application.
![Awaiting deployment of project](/static/test_images/dp_8.png)

---
17. Once complete, click **View** to open the program in thw web browser.
![Deploy the project](/static/test_images/dp_9.png)

**Your project should now render in the browser! 

[&lt; Back to README file](/README.md)

## Functionality

### Homepage
The homepage displays a list of the latest blog posts, including an excerpt and images. Users can click on a post to read more and leave comments.

### User Accounts
Users can register, log in, and create their own accounts. They can also delete their posts and see posts they have liked.

### Geotagging and Filtering
Users can tag their posts with a location (e.g., a city or national park), allowing posts to be filtered based on geography.



## Improvements and Future Features


## Design Overview


### Colors
The project's design uses a calming, nature-inspired color palette to reflect its connection to Sweden's *allemansrätt* (right of public access). Below are the selected colors and their purposes:

| **Color Code** | **Usage**                     | **Description**                                |
|-----------------|-------------------------------|------------------------------------------------|
| `#F0F8F4`      | Background, main sections     | A calm, light green tone symbolizing nature and freshness. |
| `#355E3B`      | Primary color, navbar, text, buttons | A deep green tone providing stability and an earthy feel. |
| `#A4B8A9`      | Accent color, borders, text   | A soft gray-green used for subtle details.    |
| `#A8D5BA`      | Hover effects, accents        | A light green tone highlighting interactive elements. |
| `#6E9D77`      | Secondary color, buttons      | A balanced mid-green that complements the darker primary green. |
| `#4D774E`      | Text, links                   | A natural green tone emphasizing key elements. |
| `#B3CBB9`      | Subtle details                | A pastel green softening the overall design.  |
| `#FFFFFF`      | Card backgrounds, text        | Neutral white balancing the green tones.      |


### Colors
![From Colors](https://res.cloudinary.com/dlt0ybmve/image/upload/v1732793899/Screenshot_2024-11-28_at_10.00.59_k8jopf.png)



![From Colors](https://res.cloudinary.com/dlt0ybmve/image/upload/v1732793928/Screenshot_2024-11-28_at_10.01.55_bafnze.png)


### Typography
The font used throughout the project is:

- **'Lato', sans-serif**: A modern, clean, and highly legible font that ensures a professional and user-friendly experience.

### Design Rationale
The design focuses on a harmonious balance of colors and typography to create an inspiring and user-friendly environment. The green-dominant palette reflects nature and aligns with the blog's focus on sustainability and exploration of Sweden's natural landscapes.  
Interactive elements are highlighted with accent colors, while the 'Lato' font ensures readability and complements the modern aesthetic of the blog.



## License


## Contact
For questions or feedback, please contact me via [your email address or GitHub profile].

## Explanation of the sections:

1. **Project Description**: A brief introduction to what the project is about and its functionality.
2. **Features**: Key features that the application offers (user accounts, posts, likes, comments, geotagging, etc.).
3. **Technologies**: The technologies used in the project (Django, PostgreSQL, Bootstrap, Heroku, etc.).
4. **Installation**: Step-by-step instructions for installing and running the project locally.
5. **Deployment**: How to deploy the project to Heroku.
6. **Functionality**: A summary of the key functionalities of the app, like homepage, user accounts, and geotagging.
7. **Improvements**: Possible future improvements or features that could be added.
8. **License**: Information about the license (MIT License).
9. **Contact**: How to reach you for questions or feedback.
