# The Good People Shop

Milestone Project # 4 - [The Good People Shop](INSERT URL TO FINAL PROJECT)

The purpose of the site is a peer-to-peer shopping site. Buyers and Sellers will choose a verified charity to donate proceeds to.
Charities with no shop on the highstreet? That's fine, users can still sell items that they no longer need at home and buyers can purchase these items. 
All proceeds will go straight to the charity of their choice.


## UX and Elements of User Experiences

### Strategy: 
The purpose of this site is to provide users a peer-to-peer experience. An ecommerce experience which benefits everyone.

### Scope:
Functional Requirements

Content Requirements

### Structure
Information Architecture: Visual representation of the product's infustructure

### Skeleton

#### Wireframes

### User Stories:

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
    2. If user
## Deployment

### Deploying to Heroku ###

### Credit

#### Code
Home page was created with guidance from the Code Institute Boutique Ado Mini Project on creating a Ecommerce site with Django. 

#### Media
