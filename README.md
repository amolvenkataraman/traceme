# TraceMe - Track your life visually
## Final project for CS50's Web Programming with Python and JavaScript
### Created by Amol Venkataraman

<br>

This is a web application for viewing all of the places that you have been to in one map, color coded by purpose.

This site uses Django for its backend, and Bootstrap and JavaScript for the frontend.

All the places are stored in the database

### Features
- Users can register or login to the website.
- Users can add places to their life map.
- Users can view their life map.

### Files
Since there are a lot of files in a Django application, I can not go through each one in detail. The following are ones that I have created / modified:
- `views.py`: The main backend file. It does all of the processing on the backend.
- `urls.py`: It routes each route to a function.
- `models.py`: Defines all the models for the database.
- `forms.py`: Used to customize the registration form.
- All the HTML files: `base.html`, `login.html`, `register.html`, `addlocation.html`, `maps.html`. All of these serve the purpose as evident from their names. They all extend the `base.html` template.
- `styles.css`: The stylesheet.
- `db.sqlite3`: The database, used to store all the items and orders.

### How to Run
- Open a Terminal or Command Prompt window in the folder where the web app is located.
- When running the app for the first time, run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` to make sure that all of the necessary Python packages are installed.
- Run the app: Run the command `python manage.py runserver`.
- Open a browser window and go to `127.0.0.1:8000` *(unless the app was made to run on a different host or port)* to see the web app.

Video demonstration: https://youtu.be/H4c4PkF7uD0
