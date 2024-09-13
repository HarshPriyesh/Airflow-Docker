Here's a step-by-step guide for setting up a web server (Nginx) and a MySQL database using Docker Compose, along with a basic HTML page served by Nginx.

---

### **Step-by-Step Guide: Nginx + MySQL Setup with Docker Compose**

#### **1. Create the Project Folder**
Start by creating a folder for your project. We'll call it `myapp`.

```bash
mkdir myapp
cd myapp
```

#### **2. Create a `docker-compose.yml` File**
Inside the `myapp` folder, create a file named `docker-compose.yml`. This will define your web and database services.

```bash
touch docker-compose.yml
```

#### **3. Define Services in `docker-compose.yml`**
Edit the `docker-compose.yml` file and define two services: one for Nginx (web server) and one for MySQL (database).

Here’s the configuration:

```yaml
version: '3'
services:
  web:
    image: nginx:latest    # Pull the latest Nginx image
    ports:
      - "8080:80"          # Map host port 8080 to container port 80
    volumes:
      - ./html:/usr/share/nginx/html  # Mount local html directory to the Nginx container
    depends_on:
      - db                 # Ensure Nginx waits for the database to start

  db:
    image: mysql:5.7       # Use MySQL version 5.7
    environment:
      MYSQL_ROOT_PASSWORD: example  # Set root password for MySQL
    volumes:
      - db_data:/var/lib/mysql  # Persist MySQL data using a named volume

volumes:
  db_data:  # Declare a named volume for MySQL persistence
```

This setup does the following:
- **web**: Runs the latest Nginx container, mapping the host port `8080` to Nginx's default port `80`. It uses the `html` directory on your local machine to serve web files.
- **db**: Runs a MySQL 5.7 container with a root password `example`, and persists data using the `db_data` volume.
- **volumes**: The `db_data` volume ensures the database data persists across container restarts.

#### **4. Create a Simple HTML Page**
To serve content via Nginx, create an HTML file.

1. Create an `html` directory inside the `myapp` folder:

   ```bash
   mkdir html
   ```

2. Add an `index.html` file inside the `html` directory with some basic content:

   ```bash
   echo "<h1>Hello from Docker Compose!</h1>" > html/index.html
   ```

#### **5. Run the Application**
Now, let’s start the multi-container application using Docker Compose:

```bash
docker-compose up
```

- This command will pull the necessary images, create the containers, and run them.
- You can visit `http://localhost:8080` in your browser to see the message "Hello from Docker Compose!" served by Nginx.

#### **6. Stopping the Application**
To stop and remove the containers and networks:

```bash
docker-compose down
```

The MySQL data will still persist because of the volume defined for the database.

#### **7. Check Running Containers**
To check the status of your running services, use:

```bash
docker-compose ps
```

This will show the containers started by Docker Compose, their status, and ports.

---

### **Additional Customizations**
- **Connecting Nginx to MySQL**: If you need the web server to interact with the database (e.g., through PHP or an app server), you can add a PHP service to the configuration.
  
- **Scaling Web Instances**: To scale the Nginx web service to multiple instances:

  ```bash
  docker-compose up --scale web=3
  ```

This will launch three instances of the web service, useful in load-balancing or high-availability setups.

--- 

By following these steps, you'll have a basic web server and database setup using Docker Compose, with room for further customization.