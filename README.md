# **My Blog**

![am i respomnsive( LÄNK TILL BILD)]

## About
**My Blog** is a BESKRIVA MIN BLOGG HÄR
Provide a brief introduction to your Django project. Explain what it does, its main features, and why it exists. You can also include any relevant badges here.

<u>Required tecgnologies:</u> 


**Test Accounts**

* For the purposes of testing the website and its features, a test-account have been created(as an admin).

* Test accounts allows you to test the websites features, such as editing profile, add a post, delete/edit posts, comment on posts and so on.

* A test account details are shown here: Username: admintest Password: admintest



## Table of Contents

- [**My Blog**](#my-blog)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)


# **Project Purpose**

My Blog is a website application designed to post, edit, like and comment on others posts.
You can also check the creators profile, and bio.
The purpose of the site is to share anything you want to share with others, It could be news,
gamin, food, feelings, toughts, or whatever!you like!

## Target Audience

The target audience for this Django blog is broad and inclusive. The blog is designed to cater to a diverse range of users, including:

1. **Blog Readers**: Anyone interested in reading and exploring blog posts on various topics.

2. **Blog Writers**: Individuals who wish to contribute by creating and publishing their own blog posts.

3. **Editors**: Users who want to edit and improve existing blog posts.

4. **Community Interaction**: Users who want to engage with the content by liking, commenting, and sharing posts.

This blog is open to all, fostering a sense of community and collaboration. Whether you're a passionate writer, an avid reader, or simply looking to engage with interesting content, you're welcome to be a part of our blogging community.


# **UX** 

## **Project Scope**

* **Functionality**
    * To be able to sign-up using usernname, and a password
    * To be able to login/logout of the account
    * To be able to add, edit, delete, like posts as logged in
    * To be able to view posts, and bios of users
    * To be able to comment posts
    * To be able to edit user settings such as password
    * To be able to add categories as a user

* **Content requirments**
    * Clear, consistant info how to use the website
    * Easy navigation as nav-bar to guide the user
    * Simple form to make the user cofident to post
    * Responsive website that responds to the user

## **User Stories**

* As a **developer** getting started with **web development** using Django and Cloudinary, I want to install Django, set up a basic project, and integrate Cloudinary for media management
so that **I can create a web application that handles media uploads and serves them efficiently**
* As a new **user**, I wantto be able to create an account by providing my email address and a secure password so that **I can access the features of the blog**
* As a **registered user**, I want **to be able to log in using my email and password** so that **so that I can access my profile and interact with the blog**
* As a **logged-in user** I  want to **be able to create a new blog post** by providing  **a title, content, and optionally adding images or media**
* As a **logged-in user who created a post** I can **edit or delete my own posts** if in case **I need to make changes or remove outdated content**
* As a **user** I expect  **the blog to be responsive, and easily accessible on all kind of devices** so that **everyone can use the blog**
* As a **user**, I can update my profile information so that I can modify my user profile dashboard/information, like settings, name and so on
* As a **user**, I can comment, and like the blogposts, and also see how many likes I got on my posts
* As a **user**, I can add new categories, to implement it for my posts
* As a **first-time site visitor**, I can view a post and I can get information about the user who published the post
* As a **first-time site visitor**, I can view a landingpage/homepage so that I can get information about a website's purpose
* As a **first-time site visitor**, I can comment, and like the blogposts, and also see how many likes the user got on its post
* As an **admin**, I can view user profile information so that I can modify any needed user details or delete users.
* As an **admin**, I can access an admin profile so that I can create, edit and delete users, or edit them.


# **Design**

## **Website Structure**

* The website is structured into 9 principal pages
* All of the pages extend the same base, therefore producing a consistent style across the web-app
* Pages are the following:
    * **Navbar**
    The navbar is structured up very easy for the user, with a button and the header "**My Blog**", dropdown menu with "**categories**", where all the blog-categories are stored. A "**Register**" button for new users, and a "**Login**" button for the ones with registerd accounts already. 
    !!IMAGE LOGGED OUT
    * If the user is logged in, the navbar says: same "**My Blog**" button, and "**Categories**" dropdown menu, but then we come to the "**Add Post**" followed by "**Add Category**" since you can do this stuff as logged in. To the right, we find another dropdown menu, where the user sees the profile-name, the dropdown menu has 4 links. "**User settings**", "**Edit Profile Page**", "**Show profile page**" and a "**Logout**" button. !!!! image logged in
    
    * **Footer**
    The footer is a simple footer with copyright text, and 3 icons linked to social medias.

    * **Homepage**
    Here can we see the most recent posts for the blog.
    We have a link to the post itself, and also links to the category.

    * **Categories**
    In the category navbar, we see all the categories created by the users.
    If we post a blogpost, and we use the category, it will appear under its correct category.
    BILD PÅ KATEGORI MED NÅÅGOT I
    
    * **Register** 
    This is a simple register form for the user to use, and it is created to assign a post by the user.
    Here, we want a username, first/last name, an email and a password.
    BILD PÅ REGISTER SIDAN

    * **Login**
    Here is a simple loginpage with username and password required. 
    If you dont have created an account yet, you can press the hyperlink Sign up Here, to get to the register page.

    Biuld på LOGIN!!!

    ### As a logged in user
    
    * **Add Post**
    We can add a post, and then we enter a title, a title tag, 

## **Relational Database Diagram**

## **Design Diagram**

## **Color Design**

# **Features**

List the key features of your Django project. This section can help potential users understand what your project can do.
## **Existing features**

## **Features to implement in the future**

## **CRUD Operations**

# **Data Validation**



# **Technologies and libraries used**

## **Languages**

The languages used are:

* [HTML](https://html.spec.whatwg.org/multipage/)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
* [JavaScript](https://javascript.info/intro)
* [Python](https://www.python.org/)

## **Database Platform and Cloud Storage**

REDIGERA DENNA TILL MIN EGNA TEXT..-----
* [ElephantSQL Postgres](https://www.elephantsql.com/): SQL database service provided by ElephantSQL for data storage.
* [SQLite](https://www.sqlite.org/index.html): SQL database engine used by default as part of Django Framework and used during development.
* [Cloudinary](https://cloudinary.com/home-102622): to store images and static files.
* [Heroku](https://id.heroku.com/login): to deploy and run the application.

# **Testing**

## **Introduction**

* Site has been continuously tested throughout development stages using the following features:
    * Python terminal for backend functionalities
    * Google Developer Tools 
    * Manual Testing
    * Automated Testing
  
## **Testing User Stories**

## **Automated Testing**
REDIGERA MIN EGNA TEXT-------

* 19 automated tests have been implemented.
* Automated tests were carried out during the creation of website functions and classes.
* The tool use to measure coverage of code was the Coverage.py tool.
* To check coverage in the HTML format run in the terminal:
    * `coverage run --source=appname manage.py test`
    * `coverage html`
    * Run `python3 -m http.server` (in case there is a server already running, enter `python3 -m http.server 8080`, for example).
    * Live server should be running with a list of HTML options.
    * Pick 'htmlcov/'.



## **Testing Accessibility and Performance**

* Testing for accessibility and performance is made from Google Chrome extention, called Lighthouse extension:

    * For Desktop:
    IMAGE PÅ RESULATAT 

    * For Mobile devices:
    IMAGE PÅ RESULTAT

## Validator Testing 
The HTML was validated using 

![W3C HTML Validator](readme-assets/html-validator.PNG) 

- My JavaScript was validated, without errors with 

![ExtendsClass](readme-assets/JS-validator.png)
- CSS showed no errors aswell, and validated with 

![Jigsaw W3C Validator](readme-assets/css-validator.PNG)

## Lighthouse
- The google chrome has a very good built-in performance-tool that is called Lighthouse.
This was used on my website, and i got a performance on 83/100.
- It showed an error message "form elements do not have associated labels",
and also a error message "document does not have a meta description" 

![Lighthouse performance](readme-assets/lighthouse-performance83.PNG)

![Error form-element](readme-assets/form-element-error.PNG)

![No meta desctiption](readme-assets/metadescription.PNG)

- I invesitgated my HTML and found out very quick that i forgot to put a label in my code.
So instead of my <span>, i placed a <label>, and a **for** attribute for every option.
- Afterwards, i checked the meta description, and found out i forgot to add the keywords and a description on top of my HTML file [index.html].

- I ran the lighthouse again, and got a much better result. The game was validated to a 100/100 score in Accessibillity. 

![Lighthouse fixed accessibility](readme-assets/performance-fixed.png)

## Wave
- Wave is a tool to check the accessibillity on the site. 
Here did i only get one "error"/"alert". This is an error where your text is supposed to be a header, but are not one.
i had wrapped my score in a <p>, instead of a <h5> element.

![Error message](readme-assets/heading-helement-fix-message.png)

![Error message displayed on website](readme-assets/heading-helement-fix.png)

This was fixed very easy by swapping out the <p> to a <h5>. And the error has ben removed. You can see that the image below shows an h5 instead.

![Error-fixed](readme-assets/heading-helement-fix-done.png)



## **Code Validation**

* **W3C HTML Code Validator**

    * Each page of the deployed website was run through the [HTML Markup Validation Service](https://validator.w3.org/) and returned no errors.

* **W3C CSS Jigsaw Validator**

    * CSS code was tested with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) via direct input and returned no errors.

    ![css-validator](/documents/readme_images/css%20validator%20.jpg)

* **JSHint validator**

    * No custom JavaScript code has been written for this project, only what is included with Bootstrap4. 

* **Python Validator**

    * All Python files across the application returned no errors.


# **Bugs during development**

## **Fixed bugs and solutions:**
When using smaller screens, the navigation bar felt quite chunky and took up a lot of the screen. navbar dropdown menu fixed
KOLLA GP CHAT frågor

## **Ongoing bugs:**

# **Development and deployment**
EGNA ORD NEDAN!!!
The development environment used for this project was GitPod. Regular commits and pushes to Github have been employed to be able to track and trace the development process of the website. The Gitpod environment for this particular project was created using a template provided by Code Institute.

For local deployments instructions shall be written below, along with instructions with deployment to Heroku, the hosting service used to deploy this particular website. Heroku was chosen as the hosting service due to its database maintenance capabilities. 



## **Local Deployment**
EGNA ORD!!!!!

This repository can be cloned and run locally with the following steps:

1. Login to [GitHub](https://www.github.com).
2. Select repository named: [keironchaudhry/p4-lingomeets](https://github.com/keironchaudhry/p4-lingomeets).
3. Click code toggle button and copy the url (i.e., https://github.com/keironchaudhry/p4-lingomeets.git).
4. In your IDE, open terminal and run the git clone command (i.e., git clone https://github.com/keironchaudhry/p4-lingomeets.git).
5. The repository will now be cloned in your workspace.
6. Create an [env.py file](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1) (this file should normally be included in .gitignore, therefore it'll not be committed publicly in the root folder of your project) and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values. For example:

`import os`

`os.environ['SECRET_KEY'] = 'ADDED_BY_YOU'`

`os.environ['DATABASE_URL'] = 'ADDED_BY_YOU'`

`os.environ['CLOUDINARY_URL'] = 'ADDED_BY_YOU'`

7. Install the relevant packages as per the requirements.txt file
8. In `settings.py` file, ensure the connection is set to either the Heroku Postgres Database or the local SQLite database
9. Ensure debug is set to true in the `settings.py` file for local development
10. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in `settings.py`
11. Run `python3 manage.py showmigrations` to check the status of the migrations
12. Run `python3 manage.py migrate` to migrate the database
13. Run `python3 manage.py createsuperuser` to create a super/admin user
14. Start the application by running `python3 manage.py runserver`

## **Deployment to Heroku**
EGNA ORD!!!!
Deployment to Heroku can be done with the following guideline:

1. Create an account on Heroku
2. Create an app and give it the desired name and select a region
3. <del>Under resources, search for Postgres, and add _Heroku Postgres_ database to the app</del>
    * Due to changes taking place as from the 28/11/2022 with regards to Heroku and their PostgreSQL Add-on, student developers at Code Institute have had to migrate their project database to [ElephantSQL](https://www.elephantsql.com/).
        1. Create an account on ElephantSQL.
        2. Click on 'Create an instance'
        3. Give your plan a Name, select the appropriate Plan and then select a region and data-center closest to your location.
        4. Once details are completed, click 'Create instance'. 
        5. Copy and paste dashboard `DATABASE_URL` and copy and paste into Heroku Config Vars in Settings, and be sure to set your `env.py` in your project IDE to the same URL. 
4. The `DATABASE_URL` needs to be set as an environment variable in both Heroku and in the IDE local environment variables
5. Create a `Procfile` with the following text: `web: gunicorn project_name.wsgi`
6. Make sure you add your environment variables (env.py) to Heroku's Config Vars
7. Ensure `Debug` is set to `False` in the settings.py file
8. Add 'localhost', and 'project_name.herokuapp.com' to the `ALLOWED_HOSTS` variable in `settings.py`
9. Run `python3 manage.py showmigrations` to check the status of the migrations
10. Run `python3 manage.py migrate` to migrate any necessary data to the database
11. Run `python3 manage.py createsuperuser` to create an admin user
12. Connect the app to GitHub, and enable automatic deploys from main (or you can manually deploy).
13. Click 'deploy' to deploy your application to Heroku for the first time


## **Libraries and other credits**
This projects are inspired by:
ALLA MINA CREDIT LÄNKSR HÄR