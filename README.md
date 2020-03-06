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

You can create a profile in the top right of the web site **Register**, if you try to open a other user profile or post, the server will redirect you to the login **Home** page, and the default image is an eagle.


![Home Page](https://raw.githubusercontent.com/terselich/DjangoTutorial/master/media/nologged_user.png)


The register page requeres a username, email and password must match and follow the indications displayed.

![Register form](https://github.com/terselich/DjangoTutorial/blob/master/media/register.png?raw=true)


To login after the registration, you will be redirected to the login form.

![Login form](https://github.com/terselich/DjangoTutorial/blob/master/media/login.png?raw=true)


Once you're logged, you can create a post in the top left corner of the website ***New Post***.

![Home Logged](https://github.com/terselich/DjangoTutorial/blob/master/media/loggedUser.png)


The form is simple and redirects you to the post details instead of ***Home**.


![New Post](https://github.com/terselich/DjangoTutorial/blob/master/media/new%20post.png?raw=true)


You can change your picture and information by going to your profile


![update information](https://github.com/terselich/DjangoTutorial/blob/master/media/profile.png?raw=true)


Additionally, you can change your publications and update the information provided that the posts belongs to the logged user.

![Other user post](https://github.com/terselich/DjangoTutorial/blob/master/media/post_other_user.png?raw=true)

And..

![Your Post](https://github.com/terselich/DjangoTutorial/blob/master/media/post_modify.png?raw=true)

![Sure](https://github.com/terselich/DjangoTutorial/blob/master/media/Are_you_sure.png?raw=true)


Note at the botton of the web site there is pagination of posts, ordered by lastest posted.

![Pagination](https://github.com/terselich/DjangoTutorial/blob/master/media/pagination.png?raw=true)


Finally, you can logout.

![Logout](https://github.com/terselich/DjangoTutorial/blob/master/media/user_logged_out.png?raw=true)
