### **1. Folder Structure**

Update your project structure as follows:

```bash
myapp/
├── docker-compose.yml
├── flask-app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── templates/
│       └── form.html
```

This structure contains:
- `docker-compose.yml`: Defines the services (Flask and MySQL).
- `flask-app/`: Directory for the Flask app, including the Python code, dependencies, and HTML templates.

### **2. Updated `docker-compose.yml` File**

Create the `docker-compose.yml` file inside the `myapp/` folder with the following content:

```yaml
version: '3'
services:
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: user_data  # Database to store user names
    volumes:
      - db_data:/var/lib/mysql  # Persist MySQL data

  flask:
    build: ./flask-app
    ports:
      - "5000:5000"  # Flask app runs on port 5000
    environment:
      - FLASK_ENV=development  # Enable Flask debugging
    depends_on:
      - db  # Ensure the Flask service waits for the database to start

volumes:
  db_data:  # Declare a named volume for MySQL data persistence
```

Key aspects:
- **db**: Runs MySQL 5.7 with a root password and creates a database `user_data`.
- **flask**: Runs the Flask app, exposing it on port `5000`. It builds the image from the `flask-app` directory.

### **3. Create the Flask Back-End**

Inside the `myapp/flask-app/` directory, create the `app.py` file for the Flask web server:

```python
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="db",  # Docker service name for MySQL
    user="root",
    password="root",
    database="user_data",
)

cursor = db.cursor()

# Create a table to store names
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
)
db.commit()

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    db.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

This script:
- Connects Flask to MySQL.
- Displays a form where users can submit their names.
- Saves submitted names to the MySQL `users` table.

### **4. Flask Dependencies (requirements.txt)**

In the `myapp/flask-app/` folder, create a `requirements.txt` file for the required Python packages:

```txt
Flask==2.1.1
Werkzeug==2.1.1
mysql-connector-python==8.0.30
```

### **5. Basic HTML Form (form.html)**

Inside `myapp/flask-app/templates/`, create a `form.html` file to render the user form:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Your Name</title>
</head>
<body>
    <h1>Enter Your Name</h1>
    <form action="/submit" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

This form allows users to enter their names, which are then submitted to the Flask app.

### **6. Create the Flask Dockerfile**

In `myapp/flask-app/`, create the `Dockerfile` to build the Flask app container:

```Dockerfile
# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask's default port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
```

This Dockerfile:
- Uses a Python 3.9 base image.
- Copies the Flask app into the container.
- Installs dependencies and runs the Flask app on port `5000`.

### **7. Run the Application**

After setting up everything, run the application using Docker Compose:

```bash
docker-compose up --build
```

This will:
- Build the Flask container.
- Pull the MySQL image and start both services.

You can now visit `http://localhost:5000` to access the Flask app.

### **8. Verify Data in the MySQL Database**

To check that the submitted names are stored in MySQL, connect to the MySQL container:

To see the databases in MySQL, you need to log in to the MySQL server and then use the appropriate SQL commands. Here are the steps:

#### 1. **Access the MySQL Container**

First, log in to the MySQL container using `docker-compose`:

```bash
docker-compose exec db mysql -u root -p
```

- Replace `db` with the name of your MySQL service in `docker-compose.yml`.
- After running the command, you'll be prompted to enter the password. In your case, it's `example`.

#### 2. **View All Databases**

Once you're inside the MySQL prompt, you can list all the available databases with this command:

```sql
SHOW DATABASES;
```

This will display a list of all databases on the MySQL server.

#### 3. **Select a Database**

To start using a specific database (e.g., `user_data`), run:

```sql
USE user_data;
```

You should see a message like `Database changed`.

#### 4. **View Tables in the Database**

After selecting the database, you can view all tables inside it by running:

```sql
SHOW TABLES;
```

#### 5. **View Data in a Table**

To see the data inside a specific table (e.g., `users`), use the following SQL command:

```sql
SELECT * FROM users;
```

This will display all rows from the `users` table.

#### 6. **Exit MySQL**

To exit the MySQL prompt, type:

```sql
exit;
```

---

### **Conclusion**

With this setup, you have:
- A **Flask** web application with a simple form for submitting names.
- A **MySQL** database that stores submitted names persistently.
- Docker Compose orchestrating the services.