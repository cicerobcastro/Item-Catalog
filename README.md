# Item-Catalog

# About
This project is a RESTful web application with Flask framework and accesses a SQL database who is populated by categories and items. OAuth2 this protocol allows third-party applications to grant limited access to an HTTP service, either on behalf of a resource owner or by allowing the third-party application to obtain access on its own behalf.

# In This Repo
This project has one main Python module app.py which runs the Flask application. A SQL database is created using the database_setup.py module and you can populate the database with test data using database_init.py. The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application. CSS/JS/Images are stored in the static directory.

Vagrant
Python
HTML
CSS
OAuth
Flask Framework
Udacity Vagrantfile
VirtualBox

# How to Install
 
Install Vagrant & VirtualBox
Clone the Udacity Vagrantfile
Go to Vagrant directory and either clone this repo or download and place zip here
Launch the Vagrant VM (vagrant up)
Log into Vagrant VM (vagrant ssh)

# Navigate to Folder
Navigate to cd/vagrant as instructed in terminal
Sudo pip install requests
Navigate to /item-catalog/

# Run Aplication
To run files .py use python before the file
If you don't want populate another database just run "project.py"
project already works with him or to create a application database run database_setub.py
The same to menus you don't want populate another just run "project.py" 
or to populate the menus run "lotsofmenus.py"

# Configuring "client_Secrets.json"
The project already configured but you can create another one and change this file with your Client ID
If you create place JSON file in Item-Catalog directory 
And paste your Client ID into the data-clientid in login.html
On the Dev Console Select Download JSON
Rename JSON file to client_secrets.json
Place JSON file in Item-Catalog directory of project
Run application using python /item-catalog/app.py

# Access
To access the application go to http://localhost:5000

# Login
Using Google Login
To get the Google login working there are a few additional steps:
Sign up or Login
Select your google account
Authorized JavaScript origins = 'http://localhost:5000'
Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'

# JSON Endpoints
The following are open to the public:

Catalog JSON: /catalog/JSON - Displays the whole catalog. Categories and all items.
Categories JSON: /catalog/categories/JSON - Displays all categories
Category Items JSON: /catalog/<path:category_name>/items/JSON - Displays items for a specific category
Category Item JSON: /catalog/<path:category_name>/<path:item_name>/JSON - Displays a specific category item.
