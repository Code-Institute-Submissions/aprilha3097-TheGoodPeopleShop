# The Good People Shop

Milestone Project # 4 - [The Good People Shop](https://thegoodpeopleshop.herokuapp.com/)

Do you have items in your home you no longer need? Want to donate to a charity, but you don't have any cash to give?
Donate your no longer needed items and sell them to people that want to buy them. All the money from your sale will go straight
to your favorite charity of choice.

In TheGoodPeopleShop, you can view all of the available products we currently have, add a product to the cart, and if 
you are a registered user you can add an itemto sell. 

Deployed in Heroku: [Final Project](https://thegoodpeopleshop.herokuapp.com/)

## UX and Elements of User Experiences

### Strategy: 
The purpose of this site is to provide users a peer-to-peer experience. An ecommerce experience which benefits everyone.

### Wireframes
* Wireframes for the initial structural design of the site was created using [Balsamiq](https://balsamiq.com/).

#### Desktop

Home Page:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/desktop/homepage.png" width="400">

About Page:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/desktop/about.png" width="400">

View All Products:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/desktop/all-products.png" width="400">

View Product in Detail:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/desktop/product-detail.png" width="400">

View Shopping Cart:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/desktop/shopping-cart.png" width="400">

Contact Us:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/desktop/contact-us.png" width="400">

Checkout View:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/desktop/checkout.png" width="400">

View All Charities:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/desktop/charities.png" width="400">

Add Product:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/desktop/add-product.png" width="400">

#### Mobile

Home Page:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/mobile/mobile-home.png" width="400">

About Page:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/mobile/mobile-about.png" width="400">

View All Products:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/mobile/mobile-all-products.png" width="400">

View Product in Detail:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/mobile/mobile-product-detail.png" width="400">

View All Charities:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/mobile/mobile-charity.png" width="400">

View Shopping Cart:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/mobile/mobile-cart.png" width="400">

Checkout View:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/mobile/mobile-checkout.png" width="400">

Contact Us:

<img src="https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/wireframes/mobile/mobile-contact-us.png" width="400">

### User Stories:

#### Generic user stories for all users 
* As a user, I want to access the website from a computer, mobile or tablet to be able to use the sites functionality anywhere
* As a user, I want to view a list of all avilable products, to select to buy
* As a user, I want to view individual product details, so I can view pricing of item and further details of the condition of the item
* As a user, I want to search and identify items that I particularily want, so I can quickly navigate to the item of my choice
* As a user, I want to easily view the total price of my items in my shopping cart, so I can know if I am spending too much
* As a user, I want to sort through all products by name and price, so I can choose items more carefully
* As a user, I want to view items in my cart including delivery, so I can have a good calculated cost of my purchases 
* As a user, I want to be able to adjust the available items in my cart view, so I can easily make changes before checkout if I changed my mind
* As a user, I want to easily enter my payment information at checkout, aso I can checkout securly and easily
* As a user, I want to view an order confirmation after my checkout, so I can verify the items that I have bought are correct in the confirmation
* As a user, I want to recieve an email confirmation after checkout, so I can keep the information for my personal records

#### New Users
* As a user, I want to easily register for a new account, so I can have a personalised account
* As a user, I want to recieve and email confirmation once completing registration, so I can verify with the site that my account was created successfully

#### Returning Users
* As a user, I want to easily login or logout of my account, to access my details or log out so others don't have access to my details
* As a user, I want to be able to recover my password incase I forget my password, so I can recover access to my account
* As a user, I want to be able to view personalised information, such as order history and order confirmation details and saved delivery information

#### Administrator
* As the site owner, I want to be able to edit or update product details, so owner can manually change details of the product
* As the site owner, I want to be able to delete a product, so if the product is not appropriate or not available the owner can manually do this 

### Features: 

#### Navbar
* The navbar is fixed to the top of the site at all times. This allows users to easily access pages throughout the site. 
TheGoodPeopleShop's basic textlogo is avilable at the top left corner of the screen. Onclick of this directs users back to the home page.
The main navigation links (All Products, Abou, Charity and Contact Us) are clearly visable at the top of the screen on large screens.
The special navigation links (Register, Logout, Login, My Account) are hidden inside a dropdown icon on the right side of website. 
The navigation links are collapsed into a burger icon, onclick this opens and reveals the naviagation links when on a mobile device.

* The navbar also contains the search box, allowing users to search products by product name, description information or my name of charity. 
Navbar is collapsed into a magnifying glass when on mobile and tablet view, this slides open revealing the text box for searching products.

* The navbar also contains the cart icon, which on click will redirect users to the cart page. User is able to view items placed into the cart in this view.
The cart icon will display the total price of items that have been added to the cart. The cart icon changed to a light blue once user has placed items into the cart. 

#### Home
* The home page is a simple design. The page consists of a hero image with button that directs users to the all products view.
The purpose of the home page is to attract users to the business. It provides a quick idea of what the purpose of the site is and encourages users to 
continue to the site and navigate throughout. 

##### Hero image
* The hero image section contains a full sized image, containing the sites name and a subheading. The button "Shop Now" wil direct users to the all products view. 

##### About Page
* The site includes an About page. The page will provide users the back stories to the founders purpose in creating the site. It will also
provide more details of how the site works. 

#### Contact Page
* The contacts page contains a form that allows users to provide full name, email address and a message that they may submit to the sites owners.
If the user has any questions or queries on the site, they may submit an easy form that we will recieve. Once user has submitted the form successfully,
user will be redirected to the contact success form. 

#### Products Page
* The All Products page will display products in a card format with Bootstrap stylings. All of the products will redirect users to the products details view when user clicks on
the product image.

* In the products details view, user is able to view the pricing information, detail of the product and its condition and an enlarged image of the selected product.
User will be able to click on the Add to Cart button, which will add a quantity of 1 item to the cart. Or, user can click on Keep Shopping if user is not interested in
purchasing the product. User will not be able to add the item into the cart again, a warning message will display notifying user that item is already in the cart. This is the prevent
users from adding the same item into the cart and getting charged multiple times. Because anyone is able to add products to the site, there is an assumption there 
is only 1 of the available items for sell.

* Only if user is an authorised superuser, they will see additional buttons, Edit and Delete. Onclicking the edit button, user will be redirected to the Edit Product view. 
Site owner will be able to amend the details of the page and update. This will redirect to the product details page where the amended details will be available for view.
The delete button will delete the item from the products view and remove the item from the products view. 

#### Shopping Cart:
* When the cart icon is selected, the user will be redirected to the shopping cart view. If there are no items added in the cart, the page 
will display that there are no items currently in their cart. The Continue Shopping button will direct users back to the products page.

* The cart is avilable for both registered and not registered users, so anyone is able to make a purchase. 
The cart page will provide a summery of the product once user has added these items to the cart. User will be able to view product image, name, and price.

* A delete button is available, so users can remove items from their cart if they no longer require these items. 
A toast message will display when user removes an item from the cart. 

* A calculation of the cart subtotal, delivery cost and grand total of the cart at bottom of page.
The Checkout button will direct users to the checkout page where they can submit a form with their payment information

#### Checkout Page:
* An order summery of the available items in the cart (name, image and price) is avilable to view.
The Edit Cart link will direct user back to the cart page if user wants to amend an item in their cart.
The checkout form will require users to submit details of themselves including delivery information and payment details.

* If the user already has a profile with the shipping information saved, the form will be populated with this information. 
The save info checkbox will save the users delivery information if user is already registered. 

#### Checkout Success:
* Once form has been submitted successfully, user will be directed to the order summery page. 
They will be provided an order summery containing information of the items that the user has purchased.

#### Profile Page:
* The profile page is only avilable only for authenticated users.

* The profile page will contain the users personal information, also displaying the users shipping information if already saved from previous checkouts.
User is able to amend and update the delivery information form.

* Order summeries are avilable to the side of the site. User will be able to click on the order number, this will redirect
users to the order confirmation page. A toast alert will display notifying users that they are currently viewing an old order.

#### Django Allath Features:

#### Sign Up:
* The sign up page allows users to create a new account. User will be asked to complete a form that requires their email address, a username and password.
Once form has been submitted a verification email will be sent to the user's email address to complete the registration process.
The sign up page will only be available to users that do not have an account. Users will be notified if email or username has been taken.
Users that already have an account will be directed to login.

#### Login:
* The login page has a form that requires username and password fields. If login was successfull, user wil be redirected the the home page and an alert will confirm user has 
successfully logged in. Otherwise, user will be warned that their information is incorrect. 
User will be able to reset their password with the Forgot Password funcationality. User requires their email that they used to register, they will be sent an email to reset their password. 

#### Logout:
* The logout button will only be availble to users that are already logged in. On clicking the logout button, users will be asked again if they want to logout. 
Once user confirms, they will be logged out of their session and redirected to the home page. A toast message will display confirming user has been logged out successully. 

#### Back to Top button:
* The back to the top button at the bottom of the view all products page will jump users back to the top of the site.


### Future Features to Implement

#### User Authentication and Permissions
* Feature to implement is for users that add in an item are able to perform CRUD functionality on the item that they had added themselves.
User can add a product and only they will be able to edit the item or delete the item from the site. Other users will not be able to see the edit and delete funcationalities.

#### Seller Inventory
* When user adds a product to sell on the site, user will be able to specify the amount of items available for pruchase. Buyers will then be able to adjust quantity
to avilablility of the items the seller is able to provide.

#### Remove Item Once purchased
* When a buyer pruchases an item, it is assumed there is only a quantity of 1 for that item. To prevent other users from pruchasing that item, 
once a verified user pruchases the item it will be removed from the site.


## Technologies Used

### Languages
1. [HTML5](https://en.wikipedia.org/wiki/HTML5)
    * The markup language used for structuring and presenting content of the site
2. [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    * The Cascading Style Sheet used to to design the site
3. [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    * The programming langauge to program specific behaviors for the application
4. [Python](https://www.python.org/)
    * The programming language to program the backend behaviors for the site
5. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    * The templating language for Python3 to display the back-end-dat into HTML

### Libraries and Tools 
1. [Django](https://www.djangoproject.com/)
    * Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
2. [Boostrap](https://getbootstrap.com/)
    * Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.
3. [GoogleFonts](https://fonts.google.com/)
    * Used Google fonts for main font style for site.  
4. [FontAwesome](https://fontawesome.com/)
    * Toolkit and icon set for vector icons
5. [GUnicorn](https://gunicorn.org/)
    * Python Web Server Gateway Interface HTTP server.
6. [Psycopg2](https://pypi.org/project/psycopg2/)
    * Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
7. [Stripe](https://stripe.com/gb)
    * Payment infrastructure for processing and authenticating secure payments
8. [DjangoCrispyForms](https://django-crispy-forms.readthedocs.io/en/latest/)
    * Render forms in a more elegent way with Django forms
9. [GitPod](https://www.gitpod.io/)
    * Online IDE
10. [Git](https://git-scm.com/)
    * Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
11. [GitHub](https://github.com/)
    * Used for hosting my code and controling versions of my project. 
12. [Heroku](https://dashboard.heroku.com/)
    * Heroku is a cloud platform as a service supporting several programming languages. 

### Databases
1. [SQlite3](https://www.sqlite.org/index.html)
    * SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
2. [PostgreSQL](https://www.postgresql.org/)
    * PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.


### Information Architecture

### Data Modelling

#### Profile App
##### Profile
| **Name** | **Database Key** | **Field Type** | **Validation** |
---     | --- | --- | --- 
 User | user | OneToOneField 'User' |  on_delete=models.CASCADE
 Phone number | default_phone_number | CharField | max_length=20, null=True, blank=True
Street Address 1 | default_street_address_1 | CharField | max_length=80, null=True, blank=True
Street Address 2 | default_street_address_2 | CharField | max_length=80, null=True, blank=True
 Town/City | default_town_or_city | CharField | max_length=40, null=True, blank=True
 County | default_county | CharField | ax_length=80, null=True, blank=True
 Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
 Country | default_country | CountryField | blank_label='Country', null=True, blank=True

#### Products App
##### Product
| **Name** | **Database Key** | **Field Type** | **Validation** |
---     | --- | --- | --- 
Name | name | CharField |  max_length=254
Description | description | TextField | n/a
Charity | charity | CharField | max_length=254, choices=sorted_charities, default = '',
Price| price | DecimalField | max_digits=6, decimal_places=2
Image| image | ImageField | null=True, blank=True

##### Charities
| **Name** | **Database Key** | **Field Type** | **Validation** |
---     | --- | --- | --- 
Name | name | CharField |  max_length=254
Description | description | TextField | n/a
URL | url | URLField | max_length=200
Image| image | ImageField | null=True, blank=True

#### Checkout App
##### Order
| **Name** | **Database Key** | **Field Type** | **Validation** |
---     | --- | --- | --- 
Order Number | order_number | CharField | max_length=32, null=False, editable=False
User Profile | user_profile | ForeignKey 'UserProfile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
Full Name | full_name | CharField | max_length=50, null=False, blank=False
Email | email | EmailField | max_length=254, null=False, blank=False
Phone Number | phone_number | CharField | max_length=20, null=False, blank=False
Country | country | CountryField | blank_label='Country *', null=False, blank=False
Postcode | postcode | CharField | max_length=20, null=True, blank=True
Town or City| town_or_city | CharField | max_length=40, null=False, blank=False 
Street Address 1| street_address_1 | CharField | max_length=80, null=False, blank=False 
Street Address 2 | street_address_2 | FCharField | max_length=80, null=True, blank=True 
County | county | CharField | max_length=80, null=True, blank=True 
Date | date | DateTimeField | auto_now_add=True 
Delivery Cost | delivery_cost | max_digits=6, decimal_places=2, null=False, default=0
Order Total | order_total | Decimal Field | max_digits=10, decimal_places=2, null=False, default=0 
Grand Total | grand_total | Decimal Field | max_digits=10, decimal_places=2, null=False, default=0 
Original Cart | original_cart | Text Field | null=False, blank=False, default='' 
Stripe PID | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

##### Order Item Details
| **Name** | **Database Key** | **Field Type** | **Validation** |
---     | --- | --- | --- 
Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product | product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.CASCADE
Quantity | quantity | IntegerField | null=False, blank=False, default=0
LineItem Total| DecimalField | ImageField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False

### Testing 
You can view more in depth the testing required for this project in the following documentation: [Testing Document](https://github.com/aprilha3097/THIS_IS_MILESTONE_4/blob/master/TESTING.md)

## Deployment

## Deployment

*TheGoodPeopleShop* was developed using GitPod as its IDE and Github for the verions control.

### Cloning *TheGoodPeopleShope* from GitHub ###

1: **Clone** the *TheGoodPeopleShop* repository by downloading from [source](https://github.com/aprilha3097/TheGoodPeopleShop.git),

2: **Navigate** to this folder in your terminal window and **install** required modules to run the application using the following command:

```bash
python -m pip -r requirements.txt
```

Note: More information on the cloning processing can be found: [GitHub Help page](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).
   

3: **Initialize** virtual environment by typing the following command into the terminal:

```
py -m venv virtual
```

4: Set up environment variables.     
Note, that this process will be different depending on IDE you use.     
    ```bash 
    import os  
    os.environ["DEVELOPMENT"] = "True"   

    os.environ["SECRET_KEY"] = "<Your Secret key>"  

    os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    

    os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    

    os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"    
    
    os.environ["GOOGLE_MAP_KEY"] = "<Your Google Map key>" 
    ```
       
Note: Read more about how to set up the Stripe keys in the [Stripe Documentation](https://stripe.com/docs/keys)
    
5: Install all requirements from the **requirements.txt** file putting this command into your terminal:     
`pip3 install -r requirements.txt`     

6: In the terminal in your IDE migrate the models to crete a database using the following commands:    
`python3 manage.py makemigrations`     
`python3 manage.py migrate`     

7: Load the data fixtures(**products**, **charities**) in that order into the database using the following command:    
`python3 manage.py loaddata <fixture_name>`

8: Create a superuser to have an access to the the admin panel(you need to follow the instructions then and insert username,email and password):    
`python3 manage.py createsuperuser`   

9: You will now be able to run the application using the following command:     
`python3 manage.py runserver`     

10: To access the admin panel, you can add the `/admin` path at the end of the url link and login using your superuser credentials.

### Heroku Deployment
*To start Heroku Deployment process, you need to clone the project as described in the local deployment from the above section* 

To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:    
1: Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:    
`pip3 freeze > requirements.txt`    

2: Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:      
`web: gunicorn config.wsgi:application`    

3: `git add`, `git commit` and `git push` these files to GitHub repository.     

4: Install the following required for deployment:

**gunicorn**

**dj-database-url**

**Psycopg** 

These items are available already in the requirements.txt file. 

5: On the [Heroku](https://heroku.com/) website you need to create a **new app**, assigne a name (must be unique),set a region to the closest to you and click **Create app**.  

6: Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**, select **Hobby Dev — Free** and click **Provision** button to add it to your project.     

7: In Heroku **Settings** click on **Reveal Config Vars**.   

8: Set the following config variables there:     

| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| DATABASE_URL| `<your postgres database url>`  |
| EMAIL_HOST_PASS | `<your email password(generated by Gmail)>` |
| EMAIL_HOST_USER| `<your email address>`  |
| SECRET_KEY | `<your secret key>`  |
| STRIPE_PUBLIC_KEY| `<your stripe public key>`  |
| STRIPE_SECRET_KEY| `<your stripe secret key>`  |
| STRIPE_WH_SECRET| `<your stripe wh key>`  |
| USE_AWS | `True`  |
     

9: Migrate the database models to the Postgres database using the following commands in the terminal:    
`python3 manage.py makemigrations`     
`python3 manage.py migrate`     

11: Load the data fixtures(**products**, **charities**) into the  Postgres database using the following command:     
`python3 manage.py loaddata <fixture_name>`   

12: Create a **superuser** for the Postgres database by running the following command(*you need to follow the instructions and inserting username,email and password*):      
`python3 manage.py createsuperuser`     

13: You need to remove your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.    
    
14: Add your Heroku app URL to **ALLOWED_HOSTS** in the settings.py file.

15: You can connect Heroku to GitHub to automatically deploy each time you push to GitHub.    


### Credit

#### Code
* This project was developed by following the Code Institutes video lessons and project, Boutique Ado. The stylings and basic funcationalities were
influced by the project. TheGoodPeopleShop project was modified to fit the purposes of the site. 

* Stack Overflow - was a great aid in understanding and working through errors that came up during the creation of the project. 

* [HelloWebhooks](https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/) was referanced when creating the 
contact us funcationality. 

* [Django for Begineers](https://djangoforbeginners.com/) & [Django for Professionals](https://djangoforprofessionals.com/) by William S. Vincent were
used as great resources in understanding the complexities of Django.

#### Media
* All images in this site were discovered through Google Images. The lower quality images reflect the type of images user will
upload when selling items on the site. 
* Charity images were taken from their respected charities website. 