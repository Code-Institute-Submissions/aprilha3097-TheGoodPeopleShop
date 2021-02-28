## Manual Testing
Manual testing was conducted for each of the features implemented and user stories. These were tested on the different screen resolutions,
devices and in different browsers. 

### Responsiveness:

#### NavBar:

#### Search Bar:
* Search:
    1. If user searches nothing, no products will appear and error toast will appear
    2. If search is entered, but no items match, no products will appear in result 
    3. If search is entered and items match by name, description or charity, products will appear correctly 

* Filter: 
    1. Filter by price and name work as expected 

#### About Page:
* Home:
    1. Link to Home page directs to correct template when clickin on top left icon

#### About Page:
* About Us:
    1. Link to About Us page directs to correct template

#### Contact Us Page:
* Contact Form:
    1. Name is a requried field
    2. Email is a required field
    3. Message section is a required field
    4. Email requires an @ symbol in order to be valid
    5. Form submits once completed correctly 
    6. User is directed to the contact success template with button that redirects to home page 
    7. Email is sent to site owner with email, name and message correctly displayed

#### Products and Product Details Page:
* Product Detail:
    1. Product detail page displays correct information
    2. Only superuser is able to edit or delete a product, this funcationality is not visable to normal users
    3. Increment and Decrement buttons are disabled (intentional, so future users can add stock inventory or how many items are available,
    but for now buttons are disabled and user can only add 1 item of each product to cart.)
    4. If user manually inputs more than one item quantity field, prompted 1 is the max quantity
    5. Add to Cart button works and user can add product to cart
    6. Toast success message displays item in the cart secion with calculated total
    7. If user attempts to add item again, error message will display with correct message that user is not able to add item in again
    8. If user manually attemps to submit more than 1 quantity, correct error message displays (only 1 item can be added to cart)
    9. Keep Shopping button will direct users back to products page
    10. When item is successully added to cart, user will remain on product details page

#### Cart Page:
* Cart:
    1. If cart is empty, nothing displays on cart icon
    2. On click of cart, user is directed to shopping bag page and displayed is bag is empty if only cart has no products
    3. If items are added to cart, product is displayed correctly to cart view
    4. When user adds item to cart, the cart icon will display blue with the total value calculated and displayed beneath icon
    5. Price is total correctly with free delivery threshold calculated

#### Checkout and Checkout Success Page:
* Checkout:
    1. If user is not a registered user, checkout form will not be pre-populated
    2. Required fields are acutally required, form will not submit if not filled in correctly
    3. Choices for countries work, so user is able to choose from the avilable list
    4. User will be prompted to either create and accountr of login to save their information
    5. If user logs in to an account they already have, the cart will remain the same and form will now be pre-populated with saved information
    6. Card Number (4242 4242 4242 4242) using Stripe payment processing, user will be able to pay for items
    7. If card details are not valid, error will occur and payment will not get processed
    8. If card number is successfull, loading spinner will load and redirect to order confirmation page
    9. If checkout success, toast message with success message will displayu with order number and email
    10. Order detail will appear with information of the delivery
    11. Back to profile button directs to the My Profile page

#### Authentication Pages:
* Login:
    1. URL link to login to account works - goes to correct template and works as expected
    My Account > Login
    2. Username input is required
    3. If username is incorrect to what has been registered, message notifies user username is incorrect
    4. Password is required
    5. If password is incorrect, user will be notified
    6. When successful, Sign In button will redirect to home page

* Forgotten Password:
    1. Forgotten Password link redirects to correct page
    2. User required to input correct email address
    3. Email from console directs to correct password reset page
    4. Password reset successfull page redirect
    5. Password reset functionality works correctly 

* Logout: 
    1. My Account > Logout will redirect to Sign Out page
    2. User is prompted to confirm signout
    3. Sign Out will end session user 
    4. Toast message will be success and confirm user signout
    5. User is redirected to the home page

* Registration: 
    1. My Account > Register
    2. Redirects to correct Sign Up page
    3. Email, username, password is required.
    4. If email or username is already registered, user is warned email or username has been taken
    5. Email and password confirmations must match initial email and password
    6. Signup redirects to home page once form has been successfully completed

#### Profile and Order History:
* My Profile:
    1. Displays correct profile form
    2. Order history displays correctly to the right
    3. User is able to change information and update and update is immediately reflected
    4. Correct message will display if user updates information

* Order History:
    1. User clicks on order number on My Profile page and directs to correct order history detail page
    2. Correct alert displays that user is viewing a previous order
    3. Back to Profile button directs back to profile view

#### Admin Product Management Functionality:
* Add Product: 
    1. Name, Description, Price and Image are required to submit form
    2. Price must not be more than 4 digits before decimal point or error will appear
    3. User must submit an image that is choosen locally to their machine
    4. Once valid form is submitted, button redirects to the new products detail page

* Product Edit:
    1. From product detail, edit button directs to edit mode
    2. Correct Alert displays warning user is in edit mode 
    3. Only user that is a superuser is able to use this funcationality

* Product Delete:
    1. User is able to delete product 
    2. Only user that is superuser is able to use this funcationality

### Validators:

#### HTML:
All HTML files will be tested using the W3C Markup Validation Services
https://validator.w3.org/#validate_by_input

#### CSS:
All CSS files will be tested through the W3C CSS Validation Services. 
https://jigsaw.w3.org/css-validator/

#### Javascript:
All JS scripts will be tested with JHint
https://jshint.com/

#### Python:
Python files will be tested for PEP8 compliant code using the PEP8 Online validator.
http://pep8online.com/


Compatibility and Responsiveness

BUGS:

FIXES:





