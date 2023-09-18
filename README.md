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

## **Strategy**

## **User Stories**

# **Design**

## **Website Structure**

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


## **Libraries and other credits**
This projects are inspired by:
ALLA MINA CREDIT LÄNKSR HÄR




## Getting Started


Explain how to set up your Django project locally. Make sure to include any prerequisites and detailed installation instructions.

### Prerequisites

List any software or tools that users need to have installed before setting up your project. For example:

- Python 3.x
- Django
- ...

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/your-django-project.git
