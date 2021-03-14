# HiringTestBackEnd

This is the BeckEnd proyect for Tyrceo Hiring Task.

## Steps that I have followed to install python, the necessary dependencies and the initialization of the project

1. Python installation.

```bash
$ sudo apt-get update
$ sudo apt-get install python3.6
```

2. Virtual enviroment installation.

```bash
$ sudo pip install virtualenv
```

3. Creating and activating virtual enviroment.

This will create a new folder called env in your actual directory.
```bash
$ virtualenv env .
```

And this activate your virtual enviroment
```bash
$ cd env
$ source bin/activate
(env)$
```

3. Install dependencies (I installed the dependencies one by one but for short you can use the file called requiments.txt)
First go to requeriments.txt folder when you are there type the next command:

```bash
$ pip install -r requeriments.txt
```

3. Create a new project

```bash
django-admin startproject foo
```

4. Then go to the root folder of the project and create the app.

```bash
pyhton manage.py startapp foo
```

5. Finally run the server.

```bash
python manage.py runserver 0:8000
```


