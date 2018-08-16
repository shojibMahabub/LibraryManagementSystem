
# Library Management System

A Django application made for librarians. This application will automate the tasks assigned for a librarian and keep data organized.

## Getting Started

Make a virtual environment and clone the github project in it. If you have git installed use this command in your terminal to clone the repository

    git clone https://github.com/shojibMahabub/LibraryManagementSystem.git

### Prerequisites

Add all the required dependencies needed for the project. While activeting the virtualenv with `source bin/activate` from the directory of`requirement.txt` use this command.

    pip install -r requirements.txt

### Running the app

After cloning the repository in virtualenv and add dependencies from `requirements.txt` file. Migrate all changes of models into the Database with `manage.py` by using this command. Make sure you are on the same directory as `manage.py`.

```
python manage.py makemigrations
```
And run the development server by this command.

    python manage.py runserver



## Authors


* [Mahabub Elahi](https://github.com/ShojibMahabub) - *Development*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Stack overflow
* Django user documentation
