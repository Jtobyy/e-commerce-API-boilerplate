# Scalable API Application with Django

## Business Requirements
At the very least, we want to keep record of our clients that visited our sites to purchase a particular product. In respect to this we want a table too that stores client login details, orders history and payment history.

## Objectives
1.Create apis that enables the client to register.
2.Apis that allows client to see their order history.
3.Apis that allows user to edit their information.
4.Write unit test for each of the apis.
5.Create documentation your apis.

### To get started,
- `git clone the repo`
- `cd into it`
- The create a virtual environment `python -m venv .env`
- Activate it. If on windows, then  `.env\Scripst\activate`, if linux, `.env/bin/activate`
- Install packages from the requirements file `pip install -r requirements.txt`
- Then `python manage.py makemigrations && python manage.py migrate`
- Finally `python manage.py runserver 8000`

- The root api will be at localhost:8000/api/
- Products endpoint at /api/products/
- Orders at /api/orders/
- Users aat /api/users/
- Summaries at /api/summary/x
###
- To create a user, make a post request to the endpoint /api/users/
- To login, make a post request containing your username and password to the endpoint /api/auth/, This will return a token which you can then use to authenticate successive calls by adding an Authorization header to your request whose value is set to 'Bearer <token>'
- Visit each endpoint on your browser to find the list of accepted parameters accepted by them.


### To run tests,
- `python manage.py test`