# LIBRARY MANAGEMENT SYSTEM

An app made with **Django**. This app automates tasks of a librarian and keep records organised.
 
# INSTALLATION
Create a virtual environment and install from `requierments.txt`	. This will make all dependencies install required for the project.

# FLOW CHART
Admin
```mermaid
graph LR
C[USER] -- request --> A[DATABASE]
A[DATABASE] -- authentication --> B((ADMIN))
B --> D{VIEW}
```
Adding user

```mermaid
graph LR
