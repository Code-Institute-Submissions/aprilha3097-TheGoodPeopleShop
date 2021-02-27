# The Good People Shop

Milestone Project # 4 - [The Good People Shop](INSERT URL TO FINAL PROJECT)

Do you have items in your home you no longer need? Want to donate to a charity, but you don't have any cash to give?
Donate your no longer need items and sell them to people that want to buy them. All the money from your sale will straight
to your favorite charity of choice.

In TheGoodPeopleShop, you can view all of the available products we currently have, add a product if 
you are a registered user and view a list of great charities we currently have verified. 

## UX and Elements of User Experiences

### Strategy: 
The purpose of this site is to provide users a peer-to-peer experience. An ecommerce experience which benefits for everyone.

### Scope:
Functional Requirements

Content Requirements

### Structure
Information Architecture: Visual representation of the product's infustructure

### Skeleton

#### Wireframes

### User Stories:
Generic user stories for all users 
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

New users
- As a user, I want to easily register for a new account, so I can have a personalised account
- As a user, I want to recieve and email confirmation once completing registration, so I can verify with the site that my account was created successfully

Returning users
- As a user, I want to easily login or logout of my account, to access my details or log out so others don't have access to my details
- As a user, I want to be able to recover my password incase I forget my password, so I can recover access to my account
- As a user, I want to be able to view personalised information, such as order history and order confirmation details and saved delivery information

Administrator
- As the site owner, I want to be able to edit or update product details, so owner can manually change details of the product
- As the site owner, I want to be able to delete a product, so if the product is not appropriate or not available the owner can manually do this 

### Features: 

#### Features Implemented

#### Future Features to Implement

### Database design

## Technologies Used

### Languages
1. [HTML5](https://en.wikipedia.org/wiki/HTML5)
    * The markup language used for structuring and presenting content of the site
2. [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    * The Cascading Style Sheet used to to design the site
4. [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    * The programming langauge to program specific behaviors for the application
6. [Python](https://www.python.org/)
    * The programming language to program the backend behaviors for the site

### Libraries and Tools 
6. [Django](INSERT URL)
    * DESCRIPTION
6. [Allauth](INSERT URL)
    * DESCRIPTION


### Testing 
You can view more in depth the testing required for this project in the following documentation: [Testing Document](INSERT TESTING DOCUMENTATION LINK)

Manual Testing
1. On index (home page) navigation links go to correct urls

Login:
    1. URL link to login to account works - goes to correct template and works as expected
    My Account > Login
    2. Username input is required
    3. If username is incorrect to what has been registered, message notifies user username is incorrect
    4. Password is required
    5. If password is incorrect, user will be notified
    6. When successful, Sign In button will redirect to home page
Forgotten Password:
    1. Forgotten Password link redirects to correct page
    2. User required to input correct email address
    3. Email from console directs to correct password reset page
    4. Password reset successfull page redirect
    5. Password reset functionality works correctly 
Logout: 
    1. My Account ? Logout will redirect to Sign Out page
    2. User is prompted to confirm signout
    3. Sign Out will end session user 
    4. Toast message will be success and confirm user signout
    5. User is redirected to the home page
Registration: 
    1. My Account > Register
    2. Redirects to correct Sign Up page
    3. Email, username, password is required.
    4. If email or username is already registered, user is warned email or username has been taken
    5. Email and password confirmations must match initial email and password
    6. Signup redirects to home page once form has been successfully completed
Search:
    1. If user searches nothing, no products will appear and error toast will appear
    2. If search is entered, but no items match, no products will appear in result 
    3. If search is entered and items match by name, description or charity, products will appear correctly 
Filter: 
    1. Filter by price and name work as expected 
About Us:
    1. Link to About Us page directs to correct template
Add Product: 
    1. Name, Description, Price and Image are required to submit form
    2. Price must not be more than 4 digits before decimal point or error will appear
    3. User must submit an image that is choosen locally to their machine. 
    4. Once valid form is submitted, button redirects to the new products detail page
Product Detail:
    1. Product detail page displays correct Information
    2. ANY user is able to edit and delete a product (requires amending so only creators of product can have these funcationality)
    3. Increment and Decrement buttons are disabled (intention, so future users can add stock inventory or how many items are available, but for now buttons are disabled and user can only add 1 item of each product to cart.)
    4. If user manually inputs more than one item quantity field, prompted 1 is the max quantity
    5. Add to Cart button works and user can add product to cart
    6. When item is added to cart, success message displays with correct message
    7. If user attempts to add item again, error message with display with correct message
    8. If user manually attemps to submit more than 1 quantity, correct error message displays (only 1 item can be added to cart)
    9. Keep Shopping button will direct users back to products page
    10. When item is successully added to cart, user will remain on product details page
Product Edit:
    1. From product detail, edit button directs to edit mode.
    2. Correct Alert displays warning user is in edit mode 
Prouct Delete:
    1. User is able to delete product 
My Profile:
    1. Displays correct profile form
    2. Order history displays correctly to the right
    3. User is able to change information and update and update is immediately reflected
    4. Correct message will display if user updates information
Order History:
    1. User clicks on order number on My Profile page and directs to correct order history detail page
    2. Correct alert displays that user is viewing a previous order
    3. Back to Profile button directs back to profile view
Cart:
    1. Cart icon displays correct value of 0 when no items are in cart
    2. On click of cart, user is directed to shopping bag page and displayed is bag is empty
    3. If items are added to cart, product is displayed correctly to cart
    4. Price is total correctly with free delivery threshold caculated
## Deployment

### Deploying to Heroku ###

### Credit

#### Code
Home page was created with guidance from the Code Institute Boutique Ado Mini Project on creating a Ecommerce site with Django. 

#### Media
