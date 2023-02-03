# HackReboot - Community Project

1. Install MySQL in your system, configure the settings, and set the password..
</br></br>
2. To check whether MySQL is installed properly or not, launch the MySQL command line client, and enter your password, if the window opens successfully, you are good to go.
</br></br>
3. Once, you're done with checking your MySQL installation, run command:
<br>
```>>> CREATE DATABASE bitclubs;```
<br><br>
It's mandatory to run the commands as given, and now it's time to set up the project into your local system. 
</br></br>

4. Fork the project into your profile, and then clone it into your local system.
</br></br>
5. After you're done installing the project, move inside the **CommunityProject** directory, and open the **settings.py** file and locate this part in it:
<br>
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bitclubs',
        'USER': 'root',
        'PASSWORD': 'shashwat123',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```
Replace the text **shashwat123** with your MySQL login password, so that the database can be accessed by the project.

6. Now open your terminal in the same directory where **manage.py** file is located, and run the following commands one-by-one to install all the dependencies and required python libraries:
```
> pip install virtualenv
> virtualenv myvenv
> myvenv\scripts\activate 
> pip install django
> pip install mysqlclient
> pip install Pillow
```

7. Once these dependencies, and python libraries are installed, now configure the database by running the commands in the same terminal below:
```
> python manage.py makemigrations
> python manage.py migrate
```

8. Now, all the required tables have been configured into your database, let's now import the data to populate our database by running these commands:
```
> python manage.py loaddata fixtures/mydata_utf8.json
```

9. Now your project is ready to be run in your local system, and to do so everytime, that is run the project in your local
server/system/computer, always use the terminal and migrate to the folder where **manage.py** file is placed, and execute this command everytime:
```
> python manage.py runserver
```
This will generate a link something like this - http://127.0.0.1:8000/
<br>
Use this link to view the project running in your local server..

And now, the project is ready to take in your contributions🚀


If you face any issues regarding contributing to the frontend, reach out to us in our socials:
<br><ul><li> [Sakshi Mishra](https://www.instagram.com/sak_shi7221/) </li>
<br><li> [Poorva Diwan](https://www.instagram.com/poorva_diwan_07/) </li></ul>


And regarding any queries about backend, reach out to [Shashwat Gupta](https://www.instagram.com/shashwat_g27/)


### Happy Hacking & Keep Contributing ✨


