# The Movie DB

Congratulations! You've been hired by the worlds largest internet movie database, The Movie DB. They've been around for a while and have a lot of data, but they're looking to modernize their systems and make their data more accessible to the public.

It's your first day and you've realised a terrible reality of your new job, even though you're working for The Movie DB they have actually never used a database before! They've been storing all their data in a single massive CSV file and they need your help to move it into a database as they scale their operations from 1,000s to 1,000,000s of movies.

In this repository, I have used SQL to create a database, import data from CSV files, build an API to serve data to the organization and the public, and use SQL to query the data.

## Tasks

In this week you'll have to complete a few tasks to help The Movie DB get their data into a database:

- Task 1: Model a database to ensure it has the correct tables and relationships to store the data.
- Task 2: Create a database and tables to store the data.
- Task 3: Write a script to import the data from the CSV files into the database.
- Task 4: Adapt the companies existing API to serve the data to the organization and the public.
- Task 5: Write SQL queries to answer questions about the data.

## Files

In this repository you can find:

- `imdb_movies.csv`: A CSV file containing data about movies
- `schema.sql`: A SQL file containing the schema for the database
- `api.py`: A Flask application that will serve the data to the organization and the public
- `database.py`: A module that contains functions to interact with the database
- `import.py`: A Python script that will read data from the movies.csv file and inserts it into your database
- `queries.sql`: A SQL file that contains the queries you need to answer about the data
- `test_api.py`: A Python file to test the api.py file