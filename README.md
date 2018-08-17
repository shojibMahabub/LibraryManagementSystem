

# Library Management System

A Django application made for librarians. This application will automate the tasks assigned for a librarian and keep data organized.

## Getting Started

Make a virtual environment and clone the github project in it. If you have git installed use this command in your terminal to clone the repository

    git clone https://github.com/shojibMahabub/LibraryManagementSystem.git

#### Prerequisites:

Add all the required dependencies needed for the project. While activeting the **virtualenv** with `source bin/activate` from the directory of`requirement.txt` use this command.

    pip install -r requirements.txt

## Running the app

After cloning the repository in virtualenv and add dependencies from `requirements.txt` file. Migrate all changes of models into the Database with `manage.py` by using this command. Make sure you are on the same directory as `manage.py`.

```
python manage.py makemigrations
```
```
python manage.py migrate
```
And run the development server by this command.

    python manage.py runserver
#### Credentials:

    Admin 	: 	shojib
    password: 	8842

## Features

 - **Keeps records of available books**
		Admin of the system can add books into the database. A model named 
		**Book**  of the system has necessary fields. This model gives Admin 
		to keep records of available books
		
 - **Keeps records of members**
  		Admin of the system can add members into the database. Every member 
  		have unique field to represent a specific member of the library. The 
  		system specificly contain a model named **User**.
  		
- **Keeps records of issued books** 
		Admin of the system can issue a book to a member and keep track of a 
		issue ticket. **Issue** model have linked with **Book** and **User** model by foreign key


- **Keeps records of returned books**
		Admin of the system can take books retrun from the user. **Return** model is linked to the **Issue** model. When Admin initiates to take a book as return the system will simple clear the issue ticket for the specific member and update the remaining book data.
- **Keeps track about how many books are available after issue and return**
		The system is able to keep records about available books so that the 
		Admin can see wheather a book is available or not
- **Generate a FINE ticket for users who crossed returned date**
		The system generates a return date which is default at the time of issue a 
		book and checks the date at the time of returned date.If the member 
		cross his day limit the system tags him with a flag fine
## Authors


* [Mahabub Elahi](https://github.com/ShojibMahabub) - *Development*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Stack overflow
* Django user documentation
