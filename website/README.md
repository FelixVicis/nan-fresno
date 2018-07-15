# Website

Website files for NanFresno

### Development Installation Instructions

**Prerequisites:**

 - Have PostgreSQL installed and a connection string for a database.
	Something like: `postgres://user:password@domain:5432/database`


**1. Virtual Environment (optional)**

 We use `virtualenv` to create our own virtual environment, allowing you to sandbox this project's requirements from any global installation you may have.

 ```bash
 pip3 install virtualenv;
 virtualenv env -p python3.6;
 source env/bin/activate
 ```

**2. Dependency Installation**

 ```bash
 pip install -r requirements.txt
 ```

**3. `.env` Enviroment Variables**

Create a file (at this directory) titled `.env`

This should follow the same format as `example.env` and will need it's variables filled out by you.

**4. Run Server!**
 ```bash
 python3 manage.py runserver;
 ```
