# podcastweb

## Installation
1. Clone podcastweb repo. 

    ```
    git clone git@github.com:tjgupta/podcastweb.git
    ```
2. Create python environment. 

   ```
   pyvenv [path where you want venv]
   ```
3. Activate python virtual env.

   ```
   source [path/to/env]/bin/activate
   ```
4. Install dependencies. The django-podcast dependency (editable) will get installed to [path/to/env]/src/django-podcast.

   ```
   cd [path/to/repo]
   pip install -r requirements.txt
   ```
 
5. Start server.

   ```
   python manage.py runserver
   ```
   
6. Visit http://localhost:8000 in a browser.

