# The Good People Shop

Milestone Project # 4 - [The Good People Shop](INSERT URL TO FINAL PROJECT)

Do you have items in your home you no longer need? Want to donate to a charity, but you don't have any cash to give?
Donate your no longer needed items and sell them to people that want to buy them. All the money from your sale will go straight
to your favorite charity of choice.

In TheGoodPeopleShop, you can view all of the available products we currently have, add a product to the cart, and if 
you are a registered user you can add an itemto sell. 

## UX and Elements of User Experiences

### Strategy: 
The purpose of this site is to provide users a peer-to-peer experience. An ecommerce experience which benefits everyone.

### Wireframes
* Wireframes for the initial structural design of the site was created using [Balsamiq](https://balsamiq.com/).

#### Desktop

Home Page:
<img src="" width="400">

About Page:
<img src="" width="400">

View All Products:
<img src="" width="400">

View Product in Detail:
<img src="" width="400">

View All Charities:
<img src="" width="400">

View Shopping Cart:
<img src="" width="400">

Checkout View:
<img src="" width="400">

Contact Us:
<img src="" width="400">

#### Mobile

Home Page:
<img src="" width="400">

About Page:
<img src="" width="400">

View All Products:
<img src="" width="400">

View Product in Detail:
<img src="" width="400">

View All Charities:
<img src="" width="400">

View Shopping Cart:
<img src="" width="400">

Checkout View:
<img src="" width="400">

### User Stories:

#### Generic user stories for all users 
- As a user, I want to access the website from a computer, mobile or tablet to be able to use the sites functionality anywhere
- As a user, I want to view a list of all avilable products, to select to buy
- As a user, I want to view individual product details, so I can view pricing of item and further details of the condition of the item
- As a user, I want to search and identify items that I particularily want, so I can quickly navigate to the item of my choice
- As a user, I want to easily view the total price of my items in my shopping cart, so I can know if I am spending too much
- As a user, I want to sort through all products by name and price, so I can choose items more carefully
- As a user, I want to view items in my cart including delivery, so I can have a good calculated cost of my purchases 
- As a user, I want to be able to adjust the available items in my cart view, so I can easily make changes before checkout if I changed my mind
- As a user, I want to easily enter my payment information at checkout, aso I can checkout securly and easily
- As a user, I want to view an order confirmation after my checkout, so I can verify the items that I have bought are correct in the confirmation
- As a user, I want to recieve an email confirmation after checkout, so I can keep the information for my personal records

#### New Users
- As a user, I want to easily register for a new account, so I can have a personalised account
- As a user, I want to recieve and email confirmation once completing registration, so I can verify with the site that my account was created successfully

#### Returning Users
- As a user, I want to easily login or logout of my account, to access my details or log out so others don't have access to my details
- As a user, I want to be able to recover my password incase I forget my password, so I can recover access to my account
- As a user, I want to be able to view personalised information, such as order history and order confirmation details and saved delivery information

#### Administrator
- As the site owner, I want to be able to edit or update product details, so owner can manually change details of the product
- As the site owner, I want to be able to delete a product, so if the product is not appropriate or not available the owner can manually do this 

### Features: 

#### Navbar
The navbar is fixed to the top of the site at all times. This allows users to easily access pages throughout the site. 
TheGoodPeopleShop basic textlogo is avilable at the top left corner of the screen. Onclick of this directs users back to the home page.
The main navigation links (All Products, Abou, Charity and Contact Us) are clearly visable at the top of the screen on large screens.
The special navigation links (Register, Logout, Login, My Account) are hidden inside a dropdown icon on the right side of website. 
The navigation links are collapsed into a burger icon, onclick this opens and reveals the naviagation links when on a mobile device.

The navbar also contains the search box, allowing users to search products by product name, description information or my name of charity. 
Navbar is collapsed into a magnifying glass when on mobile and tablet view, this slides open revealing the text box for searching products.

The navbar also contains the cart icon, which on click will redirect user to the cart page. User is able to view items placed into the cart in this view.
The cart icon will display the total price of items that have been added to the cart. The cart icon changed to a light blue once user has placed items into the cart. 

#### Home
The home page is a simple design. The page consits a hero image with button that directs users to the all products view.
The purpose of the home page is to attract users to the business. It provides a quick idea of what the purpose of the site, encouraging users to 
continue to the site and navigate through the site. 

Hero Image
The hero image section contains a full sized image, containing the sites name and a subheading. The button "Shop Now" wil direct users to the all products view. 

About Page
The site includes an About page. The page will provide users the back stories to the founders purpose in creating the site. It will also
provide more details of how the site works. 

Contact Page
The contacts page contains a form that allows user to provide full name, email address and a message that they may submit to the sites owners.
If the user has any questions or queries on the site, they may submit an easy form that we will recieve. Once user has submitted the form successfully,
user will be redirected to the contact form success form. 

Products Page
The All Products page will display products in a card format with Bootstrap stylings. All of the products will redirect users to the products details view when user clicks on
the product image. In the products details view, user is able to view the pricing information, detail of the product and its condition and an enlarged image of the selected product.
User will be able to click on the Add to Cart button, which will add a quantity of 1 item to the cart. Or, user can click on Keep Shopping if user is not interested in
purchasing the product. User will not be able to add the item into the cart again, a warning message will display notifying user that item is already in the cart. This is the prevent
users from add the same item into the cart and getting charged multiple times. Because anyone is able to add products to the site, there is an assumption there 
is only 1 of the available items for sell.

Only if user is an autherised superuser, they will see additional buttons, Edit and Delete. Onclicking the edit button, user will be redirected to teh Edit Product view. 
Site owner will be able to amend the details of the page and Update. This will redirect to the product details page where the amended details will be available for view.
The delete button will delete the item from the products view and remove the item from the products view. 

Shopping Cart:
When the cart icon is selected, the user will be redirected the the shopping cart view. If there are no items added in the cart, the page 
will display that there are no items currently in their cart. The Continue Shopping button will direct users back to the products page.
The cart is avilable for both registered and not registered users, so anyone is able to make a purchase. 
The cart page will provide a summery of the product once user has added these items to the cart. User will be able to view product image, name, and price.
A delete button is available, so users can remove items from their cart if they no longer require these items. 
A toast message will display when user removes an item from the cart. 
A calculation of the cart subtotal, delivery cost and grand total of the cart at bottom of page.
The Checkout button will direct users to the checkout page where they can submit a form with their payment information

Checkout Page:
An order summery of the available items in the cart (name, image and price) is avilable to view.
The Edit Cart link will direct user back to the cart page if user wants to amend an item in their cart.
The checkout form wil require users to submit details of themselves including delivery information and payment details.
If the user already has a profile with the shipping information saved, the form will be populated with this information. 
The save info checkbox will save the users delivery information if user is already registered. 

Checkout Success:
Once form has been submitted successfully, user will be directed to the order summery page. 
They will be provided an order summery containing information of the items that the user has purchased.

Profile Page:
The profile page is only avilable for authenticated users.

The profile page will contain the users personal information, also displaying the users shipping information if already saved from previous checkouts.
User is able to amend and update the delivery information form.
Order summeries are avilable to the side of the site. User will be able to click on the order number, this will redirect
users to the order confirmation page. A toast alert will display notifying users that they are currently viewing an old order.

Django Allath Features:
Sign Up:
The sign up apge allows users to create a new account. User will be asked to complete a form that requires their email address, a username and password.
Once form has been submitted a verification eamil will be sent to the user's email address to complete the registration process.
The sign up page will only be available to users that do not have an account. Users will be notified if email or user has been taken.
Users that already have an account will be directed to login to their account.

Login:
The login page has a form that requires username and password fields. If login was successfull, user wil be redirected the the home page and an alert will confirm user has 
successfull logged in. Otherwise, user will be warned that their information is incorrect. 
User will be able to reset their password with the Forgot Password funcationality. User requires their email that they used to register, they will be sent an email to reset their password. 

Logout:
The logout button will only be availble to users that are already logged in. On clicking the logout button, users will be asked again if they want to logout. 
Once user confirms, they will be logged out of their session and redirected to the home page. A toast message will display confirming user has been logged successully. 

Back to Top button:
The back to the top button at the bottom of the view all products page will jump users back to the top of the site.

#### Features Implemented



#### Future Features to Implement

### Database design

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
6. [Django](INSERT URL)
    * DESCRIPTION
6. [Boostrap](INSERT URL)
    * DESCRIPTION
6. [GoogleFonts](INSERT URL)
    * DESCRIPTION
6. [FontAwesome](INSERT URL)
    * DESCRIPTION
6. [GUnicorn](INSERT URL)
    * DESCRIPTION
6. [Psycopg2](INSERT URL)
    * DESCRIPTION
6. [Stripe](INSERT URL)
    * DESCRIPTION
6. [DjangoCrispyForms](INSERT URL)
    * DESCRIPTION
6. [GitPod](INSERT URL)
    * DESCRIPTION
6. [Git](INSERT URL)
    * DESCRIPTION
6. [GitHub](INSERT URL)
    * DESCRIPTION
6. [Heroku](INSERT URL)
    * DESCRIPTION

Databases
6. [SQlite3](INSERT URL)
    * DESCRIPTION
6. [PostgreSQL](INSERT URL)
    * DESCRIPTION

### Testing 
You can view more in depth the testing required for this project in the following documentation: [Testing Document](INSERT TESTING DOCUMENTATION LINK)
## Deployment

### Deploying to Heroku ###

### Credit

#### Code
Home page was created with guidance from the Code Institute Boutique Ado Mini Project on creating a Ecommerce site with Django. 

#### Media
