# README.md

## Project Overview

This project is a web application built using Django on the backend and JavaScript on the frontend. The application is designed to be a platform that allows users to perform complex financial calculations related to option pricing models, such as the Black-Scholes model and Binomial option pricing model. Upon pressing the 'Calculate' button, users can see the computed value of their Call and Put options based on their inputs, along with a heat map of values displaying the change in that value with change in Stock Prices and Volaility. Users can create logins to save their calculation inputs, which they can later revisit and edit. The application is mobile-responsive, ensuring a seamless user experience across devices.

### Distinctiveness and Complexity

This project is distinct and complex for several reasons:

Unlike the other projects from the Harvardx CS50w course, this application focuses on financial calculations, specifically related to options trading. The project dives into a specialized area that requires a deep understanding of mathematical models. I believe, since the project serves a widely different use case as compared to the other projects in the course, and performs multiple complex calculations entirely through JavaScript, ensuring minimal loading screens. 

The application involves complex user interactions, and deals with them hastily. Any update to the inputs while calculating models, instantly affects the output and displays the required results completely through client side code. Additionally, inputting and optional 'premium' input in the Black-Scholes model, lets users see the profit and loss they could make at different values of Stock Price and Volatility. Along with result values, the website also displays a heatmap of how the computed value changes with a change in the Stock Price and Volatility. Using d3.js to render these two heatmaps as an svg adds to the complexity of this project, as this framework was not covered in the lectures. Utilising this framework, I could easily display the required plots without having to create them with matplotlib in python. This again allowed me to minimise load times and helped me avoid a refresh of the page to get these plots from my backend.

Lastly, I focused on the UI of the project, adding subtle animations and hover effects to various elements. I learnt a lot about CSS styling through this project, including but not limited to disabled buttons, opacity of elements, z-indexes and managing overflow. I made the application mobile responsive, utilising media queries to change the styling of elements based on the viewport width.

### File Descriptions

- **`manage.py`**: The main entry point for Django’s command-line utility for administrative tasks.
- **`settings.py`**: Configuration file for the Django project, including installed apps, middleware, database connections, and static files.
- **`urls.py`**: URL configuration for the Django project, mapping URLs to views.
- **`models.py`**: Contains the data models for the application, defining the structure of the database tables.
- **`views.py`**: Contains the logic for handling user requests and returning the appropriate responses. It includes views for rendering forms, processing user input, and managing saved calculation data.
- **`layout.html`**: Includes the html for the layout of the website, such as the navbar and the sidebar.
- **`login.html`**: Includes the html for the login page.
- **`register.html`**: Includes the html for the register page.
- **`index.html`**: Includes the html for the landing page.
- **`bino.html`**: Includes the html for rendering the binomial model calculation page. Has multiple javascript functions and event listeners to generate required the outputs and heatmaps.
- **`bsm.html`**: Includes the html for rendering the Black Scholes model calculation page. Has multiple javascript functions and event listeners to generate required the outputs and heatmaps.
- **`saved.html`**: Includes the html for the saved calculations page, rendering the calculations in cards and buttons for users to go to the respective calculations.
- **`static/`**: Directory containing static files like CSS, JavaScript, and svgs. The CSS files ensure the application is mobile-responsive.
- **`templates/`**: Directory containing HTML templates used by the Django views. These templates are dynamically populated with data from the backend.

### How to Run the Application

1. **Clone the Repository**: Start by cloning the repository to your local machine.
   ```bash
   git clone https://github.com/Amaruq0703/Options-Pricing-Models.git
   cd options_pricing
   ```

2. **Install pip and Django**: Ensure you have Python installed, then install pip and Django. If you are using Ubuntu, you can run the following command to download pip.
   ```bash
   sudo apt install python3-pip -y
   ```
   ```bash
   pip install django
   ```

3. **Run Migrations**: Apply the database migrations to set up your database schema.
   ```bash
   python3 manage.py makemigrations
   ```
   ```bash
   python3 manage.py migrate
   ```

4. **Start the Development Server**: Run the Django development server.
   ```bash
   python3 manage.py runserver
   ```

5. **Access the Application**: Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

### Additional Information

- **Security**: User authentication is managed using Django's built-in authentication system, ensuring that user data is secure. Additionally, the application employs CSRF protection and input validation to guard against common web vulnerabilities.
- **Extensibility**: The application is designed with extensibility in mind. New financial models or additional features, such as more complex calculations or reporting tools, can be easily integrated without requiring major changes to the existing codebase.

### Conclusion

This project is a sophisticated web application that stands out from the other projects in the course due to its unique focus on financial calculations, its use of advanced Django and JavaScript techniques, and its commitment to providing a high-quality user experience across devices.