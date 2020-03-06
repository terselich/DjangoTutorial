# DjangoWeb Server
This a web post created on base of a tutorial using Python - Django


# 1 How to run the server


To run the server is very simple, the repository comes with a virtual enviroment, you dont need to have install Python on your computer to run it, all libraries necessary to run the server are included in the /venv/bin folder.

To **run** use the following command in your terminal(Unix or Linux) remember to be in the folder ***DjangoTutorial/***: 

```python
    DjangoTutorial$ python3 manage.py runserver
```

The default port is **:8000/** how ever you can change it to any port as follows:

```python
    DjangoTutorial$ python3 manage.py runserver 0.0.0.0:<your_port>
```

# 2 Web server capabilities

You can create a profile in the top right of the web site **Register**, if you try to open a other user profile or post, the server will redirect you to the login home page.


[![Home Page](https://raw.githubusercontent.com/terselich/DjangoTutorial/master/media/nologged_user.png)]
