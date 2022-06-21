## *learnhub* - A Django-based elearning-platform to maintain all your study-related stuff clustered at one place.

#### Deployed version - https://learnhub-elearning.herokuapp.com/

### Features :
1. **Assignments** - Keep all your pending assignments with due date.
2. **Todos**       - Have your all todolist in front of your eyes always.
3. **Youtube**     - Browse and learn at a single platform.
4. **Books**       - Get your concepts clear by reading the books at the same time.
5. **Notes**       - Maintain all your notes, handy with you.
6. **Dictionary**  - Got stuck, get the meaning of the difficult words at a single click.


## Home page - 
<img src="https://user-images.githubusercontent.com/85562020/174881314-6dfabb90-acec-47f8-ac3a-09e7d9a5aa30.png" width="700">

## Assignment page - 
<img src="https://user-images.githubusercontent.com/85562020/174881531-7d1a94ff-85f0-4e2c-94e0-5399ecb2c0f3.png" width="700">

## Youtube page - 
<img src="https://user-images.githubusercontent.com/85562020/174881765-aea86aa5-0e0e-48be-b060-45aa5880f726.png" width="700">

## Book page - 
<img src="https://user-images.githubusercontent.com/85562020/174881819-af479264-8025-48b5-a3ff-585c9ac24a19.png" width="700">

## Notes page - 
<img src="https://user-images.githubusercontent.com/85562020/174882322-fe2a3e89-8889-4b0e-9991-88a6fe33e73d.png" width="700">

## Profile page - 
<img src="https://user-images.githubusercontent.com/85562020/174882345-f0546933-5ecb-4480-b87a-1906230e1599.png" width="700">



### Cloning the repository -
1. Clone the repository : ```git clone https://github.com/shubham-techie/learnhub-elearning_app.git```
2. Move into the directory : ```cd learnhub-elearning_app```
3. Creating a virtual environment : First install virtual environment ```pip install virtualenv``` and then create virtual environment ```virtualenv venv```
4. Activate the virtual environment : ```venv/Scripts/activate```  (Try this if the previous one isn't working : ```cd venv/Scripts``` --> ```activate``` --> ```cd../..```)
5. Install the required packages : ```pip install -r requirements.txt```                                                                                                

7. (Now, I have set the environment variables for SECRET_KEY and DATABASE CREDENTIALS. So, you need to generate SECRET_KEY and change the settings for Database file)
8.  Generate SECRET_KEY : First enable the python interpreter (using cmd```python```) and in interpreter run following two python lines ```from django.core.management.utils import get_random_secret_key``` and ```get_random_secret_key()```.  Copy the generated string SECRET_KEY in SECRET_KEY of setting.py file.
9.  Replace the DATABASES configuration with ```DATABASES = {                                                                                                                               'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
       }
    }```
8.  Set the ```DEBUG=True``` in settings.py file.
9.  Generate SQL executable commands using ```python manage.py makemigrations``` and create database using ```python manage.py migrate```.
10.  Create admin : ```python manage.py createsuperuser``` and enter the prompted details.
11.  Now, the app is ready to go. Run the app : ```python manage.py runserver```
