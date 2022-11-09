<h1 align="center">Zafiya2</h1>

[View the live project here](https://zafiya2.herokuapp.com/)

![Image of...]()

### Brief outline of websites purpose.
This is a fictational store with fully operational payment processing facilites.

## User Experience (UX)
***
- ### User stories
    - #### Unregistered User goals
        1. I want to be able to add and adjust items within my shopping bag.
        2. I want to be able to complete a purchase without having to log in.
        3. I want to be able to search products throughout the store.
    - #### Registered User goals:
        1. I want to be able to register an account that stores my details.
        2. I want to be able to see my past orders within my profile.
        3. I want to be able to add and adjust comments to the blog.
    - #### Admin Goals
        1. I want to be able to add, update and delete products within the store.
        2. I want to be able to add, update and delete blog posts.
- ### Design
    * #### Color Scheme
        -  

    * #### Imagery
        - 

- ### Wireframes
    <details><summary>Main Page Wireframe:</summary>

    ![Main Page Wireframe]()
    </details>

    <details><summary>Wireframe:</summary>

    ![Wireframe]()
    </details>

## Features
***
* ### Current Features
    * Main Page:
        1. All users can navigate products by type.
        2. Any user can register an account or log in.
        3. Any user can access the blog page and view comments.
        4. Any user can view the basket amount.
        5. Any user can search products throughout the store - fixed to the top.

    * Products Page:
        1. Any user can add a product to their bag.
        2. Admin can edit or delete a product.
    
    * Products Details Page:
        1. Any user can view the specific details of the product on its own dedicated page.
        2. The quantity of a product can be added using the increment and decrement button before adding to the basket.

    * Blog Page:
        1. Any user can add view a blogpost and read its details.
        2. Admin can create, edit or delete a blogpost.
        3. Any logged in user can create, update and delete their own comments to a blogpost.
        4. Any user can search through the blogpost.
    
    * My Profile Page:
        1. Registered users can store their delivery details and update it too.
        2. Registered users can view their order history.

    * Admin Access Page;
        1. Admin can add products from a dedicated page which is not viewable to non superusers.

    
* ### Future Features
    * Due to time constraints, the following features could not be added but will be enabled in the future;
        1. 
        2. 
        3. 
        4. 
        5. 
        
        
## Technologies Used
***
* ### Languages Used
    * HTML5
    * CSS3
    * jQuery
    * PYTHON 3
    * 
    * 
    * 
    * 

* ### Frameworks, Libraries & Programs Used
    * Bootstrap4
    * Django
    * 
    * 
    * 
* ### Development Tools.
    * Github:
        - Used to store the projects after being pushed using Git.
    * Gitpod:
        - Hosts the coding workspace.
    * Heroku:
        - Cloud platform for deploying the app.
    * AWS:
        - Used to store media files.
    * PostgreSQL:
        - Used to store backend relational data.
    * Google Fonts:
        - Used for fonts throughout the website.
    * Font Awesome:
        - Used to create icons for enhanced asthetics.

* ### Database structure.
    * PostgreSQL.
    <details><summary>PostgreSQL Model Diagram:</summary>

    ![PostgreSQL Model Diagram](static/docs/images/models-diagram.jpg)
    </details>        

## Testing
***
* ### Testing user stories from user experience (UX).
    - Unregistered User goals
        * #### Aim 1 - "I want to be able to add and adjust items within my shopping bag."
            - Test; 
            Adding an item;
                1. Go to the products page.
                2. Click 'view details' from the desired item. This will guide the user to the products details page.
                3. Either type straight into the input box - or use the increment or decrement button - to select the quantity of the item intended.
                4. Click 'add to bag' to place the item and quantity into the cart.
                5. If successfully added, a pop up note will appear in the top right hand corner.
            RESULT: PASS.
            Adjusting an item;
                1. Click on the basket, this will guide the user to the cart.
                2. To increase/decrease the quantity - click on the add/minus button.
                3. Click 'update.'
                4. Monetary amount adjusts accordingly aswell as the delivery amount.
                5. A confirmation note pops up in the toast message.
                6. Clicking 'remove' or setting quantity removes the item from the bag.
            RESULT: PASS.
                
        * #### Aim 2 - "I want to be able to complete a purchase without having to log in."
            - Test; - 
                1. 
                2. 
                3. 
                4. 
                5. 

        * #### Aim 3 - "I want to be able to search products throughout the store."
            - Test;
                1. Type the intended keyword into the search box at the top of the screen and click enter.
                2. Any product or description containing the keyword will display.
                3. Click the home button to reset.
            RESULT: PASS.
            
    - Registered Users;
        * #### Aim 1 - "I want to be able to register an account that stores my details."
            - Test;
                1. Click 'account' and then 'register' in the dropdown.
                2. Fill in all the details on the form.
                3. After clicking 'sign-up' a verification email will be sent to the users email address.
                4. Click on the verification link via the email.
                5. User will be diverted to login now.
                6. User can input their details ans it will store for future payments.
            RESULT: PASS. 
        * #### Aim 2 - "I want to be able to see my past orders within my profile."
            - Test;
                1. Log in and click on 'my profile' under 'account.'
                2. On the right hand side will be a list of previous orders if any.
                3. Click the order number and it will show you an order summary of the historic purchase.
            RESULT: PASS.

        * #### Aim 2 - "I want to be able to add and adjust comments to the blog."
            - Test;
                1. Log in the account.
                2. Click on the intended blog.
                3. Enter any comment into the comments box.
                4. Comment will save and attach to the bottom of the blog post.
                5. Users can click 'edit' or 'delete' to update or remove their comment.
            RESULT: PASS. 

    - Admin Goals
        * #### Aim 1 - "I want to be able to add, update and delete products within the store."
            - Test - adding a product;
                1. Log in as an admin.
                2. Click on 'product management' under 'account.'
                3. Fill in all required fields.
                4. Click 'add product.'
                5. Product will be added to all products and as per category.
            RESULT: PASS.
            - Test - editing a product;
                1. Find product to be eidted from the products page.
                2. Click the edit button.
                3. User will be guided to edit product page.
                4. Fill out the details.
                5. Click update and the updated changes will display on the product details page.
            RESULT: PASS.
            - Test - deleting a product;
                1. Click on the intended product.
                2. 
                3. 
                4. 
                5. 

        * #### Aim 2 - "I want to be able to add, update and delete blog posts."
            - Test - adding a blog post;
                1. Log in as a admin.
                2. Click on 'blog' from the main menu.
                3. Click 'create post' button.
                4. Fill in the form and click 'add.'
                5. The new post will be available on the main blog page.
            RESULT: PASS.
            - Test - editing a blog post;
                1. Click on the intended post.
                2. Click the edit button.
                3. Fill out the prefiled form.
                4. Replace with new content and click update.
                5. Post will update and guide back to the main blog page.
            RESULT: PASS.
            - Test - deleting a blog post;
                1. Click on the intended product.
                2. 
                3. 
                4. 
                5. 
        
* ### Code validation.
    <details><summary>HTML Validation Test;:</summary>

    ![HTML Validation Test;]()
    </details>

    <details><summary>CSS Validation:</summary>

    ![CSS Validation Test;]()
    </details>

    <details><summary>JSHint Validation:</summary>

    ![JSHint Validation Test;]()
    </details>
    
    <details><summary>PEP 8 Tests:</summary>

    ![PEP8 validation Test;]()

    </details>

* ### Supported screens and browsers.
    * Mobiles
        - Iphone 12 Pro, Iphone X, Iphone SE, Iphone XR , Samsung Galaxy S20 Ultra, Samsung Galaxy S20 Plus, Samsung Galaxy Note 9, Samsung SA51/71, Samsung Galaxy s9.
    * Tablets
        - iPad Mini, iPad Air, iPad, iPad Pro, Samsung Tab S6
    * Laptops
        - 15" - 17" screens
    

* ### Fixed bugs.
    1. Problem.
        - Fix: 

* ### Known errors.
    1. 
    2. 
    3. 


## Deployment
***


## Credits
***
* ### Code
    - 

* ### Media
    - 

* ### Acknowledgements
    - 
