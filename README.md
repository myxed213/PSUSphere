# PSUSphere

PSUSphere is a Django-based student organization management system.

## Features
- Manage Colleges, Programs, and Organizations.
- Track Student memberships in various organizations.
- Custom Admin interface with search and filters.
- Data generation command for easy testing.

## Setup
1. Create a virtual environment: `python -m venv psusenv`
2. Activate the environment: `.\psusenv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Run the data generation command: `python manage.py create_initial_data`
6. Start the server: `python manage.py runserver`

## Authors
- Janry (Developer)
- Peter Joshua (Developer)
