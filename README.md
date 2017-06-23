# Bucket-List

This repository contains the following:

- Wireframes
- UI
- Bucket List applications

# Wireframes

Contains wireframe design for HTML/CSS templates in UI folder.

# UI

Contains HTML/CSS templates for Bucket List front end application.

# Bucket List

Contains a flask bucketlist application with the following features:

- A user can be able to register in the application.
- A user can Login to application.
- A logged in user can Create, Read, Update and Delete a BucketList.
- A logged in user, can to add, update, view or delete a Buckelist item (non-persistent data)

## Prerequisites
You need python 2.6 or a later version.

## Requirements

- click==6.7
- Flask==0.12.2
- itsdangerous==0.24
- Jinja2==2.9.6
- MarkupSafe==1.0
- Werkzeug==0.12.2

## Setup

###### Setting up python virtual environment

If you are on Mac OS X or Linux, use the following command:

```
$ sudo pip install virtualenv
$ mkdir bucket_list
$ cd bucket_list
$ virtualenv venv
```

Activating virtual environment

```
$ source venv/bin/activate
```

###### Setting up Flask

Enter the following command to install Flask in the virtualenv:

```
$ pip install Flask
```

Setting up `Pylint` for linting to ensure PEP8 style guide requirements.

```
$ sudo apt-get install pylint
```

###### Setting up Unit Test Environment

Enter the following command to install nose unit testing environment:

```
$ pip install nose
```

Once installed, you can execute a single test file.

```
$ nosetests test_User.py
```

# Running the program

1. Open the terminal and cd into the directory you extracted the project.
2. Run the program by typing the command : `python run.py`









