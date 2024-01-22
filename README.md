# Web-based application for Esthetic clinic
#### Video Demo:  <URL https://youtu.be/AkY1u3rS2dg>
#### Description:


<div style="text-align: justify; text-justify: distribute;">
The aim of my project was to develope a web-based application using the combination of Python, HTML, CSS, SQL and a touch of JavaScript. This application represents a website for an esthetic clinic with main functions designed to fulfill user's essential needs. The main goal of this project was divided into few smaller parts :

<br></br>
**1. Creating MAIN.PY script and FLASK CONFIGURATION**
- Firstly, I created a project directory called "project". The aim was to create a web-based app, with Python serving as the backend.  Inside my project directory I created a Python script called "main.py". Looking back into my previous experience, especially those attained at CS50 course, it became clear that Flask was an appropriate framework for my web app developments. To fully utilize Flask, I began by installing it into my virtual environment. Subsequently, I imported the framework and laid the foundation for a basic Flask application. Then on the top of the main.py,  I thoughtfully imported the necessary libraries for this project. As the project progressed, I continually expanded the list of required libraries, as the project’s requirements became more evident.

**2. HOMEPAGE**
- For a start, I created HTML template for the homepage. The clinic’s name features on this page header, while there is a navigation bar that allows easy access to various sections of the app. In the center of the website, the main commercial image is located. Lastly, I included a footer containing the contact info of the clinic and links to its social media pages as well as bottom navigation bar. Then in the main.py I defined a Flask route that, when it is accessed, it displays the 'homepage.html' template.

**3. LAYOUT**
- To maintain a consistent and cohesive design structure in my web application, I developed a template named "layout.html". This template ensures a consistent and eye-catching appearance across all pages of my application. It is designed to create a visual layout and user interface for an esthetic clinic that provides visitors with information, navigation, and contact information. This layout page was later used for all pages including: login page, logout, registration page, treatments, boking page etc...

**4. REGISTER**
 - Primarily, I created a template called "register.html". This template extends a common layout and sets the page title as "Register". In next step I provided a registration form with fields for email, password, and confirmation. The aim of this form is to allow users to sign up for the application.
 - Based on the previous procedure, I created web route for user registration in "main.py". In the main.py I wrote code that processes user input, validates  email and password correctness and checks for duplicate email registrations in the database. If the registration is successful, it stores the user's information and redirects them to the login page. Otherwise, it provides error messages for various scenarios. The aim of this step was to ensure  a smooth and secure registration process.

 **5. Creatin Database for this project**
 - The previous step requires using SQLite to establish a database connection and using a database file named "mydatabasename.db".
 This database was used to create and manage two needed tables in this project. First table is named "users" where user registration information, including users_id, email and hashed passwords, is being stored. Then in this database we created another table for later used. This table is named "appointments" and stores information regarding users booking requests. This includes name, chosen date, treatments and time.

**6. LOG IN**
- Similarly, to the register page, I firstly create a suitable html template called "login.html" that extends a common layout and ask user for email and password.
- In next step, in "main.py": I have implemented the login functionality for the web application. Firstly, when a user tries to log in, it checks whether the request is made through a form submission (POST) or by visiting the login page (GET).
- If the request is a form submission, the code checks if the user provided an email and password. It then queries the database to find a user with the provided email and verifies if the password matches the hashed password stored in the database. If successful, it logs the user in by creating a session with their user ID and redirects them to the home page. If there are any issues with the login, appropriate error messages are displayed.
- On the other hand, if the user accesses the login page directly (via a GET request), the code simply renders the login page, allowing users to input their credentials.
- Lastly, I use a file system to manage user sessions and make them non-permanent. In the login function I wrote code that remembers the logged in user by storing the user ID in the session.
- Overall, this code handles user authentication, ensuring that only authorized users can access specific parts of your web application namely the booking page.

**7. LOG OUT PAGE**
- To ensure that users can easily log out from their account, I created a function in :main.py" where the user's session gets cleaned which results in effectively ending their session and then redirecting them to the homepage.

**8. HELPERS.py**
- In this step, I've created a file called "helper.py" with the primary purpose of assisting functions in "main.py." This separation of functionality helps maintain a clean and organized structure by preventing “main.py” from becoming cluttered and complex.
- Firstly, I imported required libraries. Then I created decorator function called "login_required." The aim of this function is to check whether a user is logged in by verifying the presence of a user ID in the session. If a user is not logged in, it redirects them to the login page. On the other hand, when user is correctly log-in, the is executed.
- In the "helper.py" I also created function for apologizing if registration, log in or other basic web-app functionalities does not work proper way. I've created a template named "apology.html" . This template is designed to display a meme featuring a "OPPSSS!!!" message along with an image generated using the https://memegen.link/ API. The image is customized with text provided through variables "top" and "bottom," creating customised error page.

**9. THEARTMENTS and PRICE PAGES**
- Since in the real world the beauty clinic page has a lot of required features, I created various sections of the app. These sections of the web-app were created by using a combination of Python, HTML, CSS.
- First of the pages is "treatments" page, which plays a crucial role in showcasing the various treatment options available at my fictional aesthetic clinic. Primarily, I created HTML template specifically for this page. Not only it extends the common layout it also highlights the various treatments offered at my fictional clinic. Each treatment is elegantly presented with corresponding images and descriptions, ensuring our visitors can easily explore the options available. In the end of this step, in the main.py I defined a Flask route that, when it is accessed, it displays the 'treatments" page.
- Similarly, I also created "pricing" page. Firstly, I created HTML template "prising.html" which showcases a pricing list for various treatments offered by a fictional aesthetic clinic. The page is structured in a way that each treatment is presented with a title, an image, a brief description, and the cost. Each treatment also includes a booking button that redirects users to a log in page so they can easily book their choosen treatment. Repeatedly, I defined in the main.py Flask route that, when user clink on the webpage on "Pricing" tag, it redirects him on the 'pricing" page.

**10. ABOUT US and CONTACT PAGE**
- In this step I created two more sections of my web-app. Namely "about us" and "contact" pages. For both I created suitable HTML templates and then I set up a Flask routes for these pages so upon their access, the app renders  corresponding HTML templates.
- The "about us" page begins with an introduction to "A4 Esthetic Clinic," describing it as a place for aesthetic transformations with a dedicated team offering a range of treatments and procedures. The page then introduces the clinic's team, featuring images and descriptions of key staff members, including the main doctor, CEO, and main surgeon, highlighting their expertise and roles within the clinic.
- The "contact" page represents a web page section for contact information and a map display. This section serves to inform visitors about the clinic's contact information and provides an interactive map for easy navigation to the clinic's location via an embedded Google Maps iframe.

**11. BOOKING PAGE**
- This section of the page was the most difficult to create and make work properly. It not only combines Python, SQL, HTML, CSS, but also some JavaScript code.
- Firstly, I created a suitable HTML template called "booking.html". This template represents a web page that serves a booking and availability system. It provides a user interface for selecting a date, showing available time slots, and booking appointments. Users can see the availability for specific hours, select a suitable time, and book appointments by providing their name, chosen date, treatments and time. The page also displays flash messages to notify users of the booking status, such as success or failure, and it dynamically updates the calendar to reflect booked appointments without requiring a full page refresh.
- This functionality is made possible by JavaScript code that handles form submission and updates the calendar view when a successful booking occurs.
- Lately, in the main.py I created function "booking". This function represents Flask route that handles both GET and POST requests for a booking page. When users access this page, it checks if a date has been provided as a query parameter. If so, it queries the database for existing appointments on that date, extracts the booked times, and then renders the booking page, providing the selected date and booked times as context data. If no date is specified, it simply renders the booking page.
- In main.py I also created function "book" that specifically handles POST requests. It retrieves the user's name, selected date, and time from the submitted form data. If the user is authenticated (checked by the presence of a user session), it queries the database to fetch the user's email. It then checks if the selected time slot is available by querying the database for existing appointments on the same date and time.
- The booking function is created in a way that, if the slot is already booked, it sends a message and redirects back to the booking page with a danger flash message. If the slot is available, it inserts the new appointment into the database, flashes a success message, and redirects to the homepage.
- Overall, these steps mentioned above collectively create a web application that allows users to book appointments, checks for availability.

**12. DESIGN in CSS**
- Throughout this project, I played around with different design elements on my website. Most of the design work was done using CSS code, allowing me to tweak the visual aspects of the web pages to my liking. I opted for colors commonly associated with the beauty and aesthetic industry, aiming to create a look and feel that resonates with women and exudes a sense of elegance.

- To make things even better, I harnessed the power of Bootstrap http://getbootstrap.com/docs/5.1/, which helped me streamline the design process and ensure that my website looked great on different devices and screen sizes.

- And for a final touch, I added a library of icons [cdnjs.cloudflare](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css). These icons not only spiced up the design but also made the website more user-friendly, offering visual cues and extra information for a more engaging and enjoyable user experience.

### Conclusion:
This project provided me with a fantastic opportunity to explore various programming languages while working on something that not only brings me joy but also enriches my knowledge. Simultaneously, it allowed me to reinforce the concepts I've already learned in the CS50 course. The process of creating a web-based application that seamlessly blends programming, design, and technical skills felt like a rewarding and enlightening journey.

By working on this project, I could dive into the world of different programming languages, each with its unique features and capabilities. Finally, I can say that this project has been great combination of creativity, talent development and learning, which was very interesting and meaningful as well for my programming way.

</div>
<div style="text-align: right">
Written by Diana Sablicova<br>
On 16.10.2023
</div>



