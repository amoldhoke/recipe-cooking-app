# Cooking Recipe API

### App description

Recipe API built using the Django web framework. This API allows users to store and manage their favorite recipes along with accompanying photos and tags for ingredients. With this Recipe API, users can easily search and browse their recipes by tag, ingredient, or any other criteria they choose.

The API provides a simple and intuitive interface for adding, editing, and deleting recipes. Users can create new recipes by adding ingredients and instructions, and then upload photos to provide a visual representation of the finished dish. In addition, users can tag ingredients with relevant labels such as "vegetarian", "gluten-free", "spicy", or any other descriptive term they choose.

The Recipe API is designed to be flexible and customizable, so that users can easily adapt it to their specific needs. Whether you are an amateur cook or a professional chef, this Recipe API can help you organize your recipes and streamline your cooking process. So why not give it a try and start building your own personal cookbook today?

### Key Features
- Store and manage favorite recipes
- Add accompanying photos and tags for ingredients
- Search and browse recipes by tag, ingredient, or any other criteria
- Create new recipes by adding ingredients and instructions
- Upload photos to provide a visual representation of the finished dish
- Tag ingredients with relevant labels such as "vegetarian", "gluten-free", "spicy"
- Flexible and customizable for specific needs


# Installation
To install the project, follow these steps:

1. Clone the repository
2. Install the dependencies by running pip install -r requirements.txt
3. Create a .env file and add your environment variables
4. Run migrations with python manage.py migrate
5. Start the server with python manage.py runserver


## Usage

Once the server is running, you can access the web application at http://127.0.0.1 and the API at http://127.0.0.1/api/.

Use the registration form to submit resumes as a student, and login as an admin or staff member to access the relevant panels. Staff members can only access approved resumes and can send emails to selected candidates.


### To use app

```sh
docker-compose -f docker-compose-deploy.yml build
```

### To start app

```sh
docker-compose -f docker-compose-deploy.yml up
```
