## Dockerizing a Python Flask Application: A Complete Step-by-Step Example

This guide walks through creating a Docker image for a Python Flask application, including all necessary components like the Python script (`app.py`), `Dockerfile`, and `requirements.txt`.
Note: Check the start_guide.md to get familiarize with Docker on Windows.

---

#### 1. **Create a Simple Python Script (`app.py`)**

We will create a basic Python web app using the Flask framework. The app will respond with a simple message when accessed.

**Example `app.py`:**
```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

- **Explanation**: This is a simple Flask application that returns "Hello, Docker!" when a user accesses the root URL (`/`). The `app.run` method ensures that the app listens on all interfaces (`0.0.0.0`) and on port 5000.

---

#### 2. **Set Up a Virtual Environment and Install Dependencies**

A virtual environment allows you to isolate your project’s dependencies. Though optional, it’s recommended for Python projects.

- **Create a virtual environment**:
  ```bash
  python -m venv venv
  ```

- **Activate the virtual environment**:
  - On Windows:
    ```bash
    venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

- **Install Flask**:
  ```bash
  pip install flask
  ```

- **Generate the `requirements.txt` file**:
  ```bash
  pip freeze > requirements.txt
  ```

- **Explanation**: `requirements.txt` will list all the installed packages, allowing Docker to install them later in the container. In this case, `requirements.txt` will contain:
  ```
  Flask==2.3.2
  ```

---

#### 3. **Create the `Dockerfile`**

A `Dockerfile` is a script of instructions that Docker uses to build your image. Here’s a well-documented `Dockerfile` that will set up a minimal Python environment and run the Flask app.

**Example `Dockerfile`:**
```Dockerfile
# Step 1: Use an official Python runtime as the base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install any Python packages required by the app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Step 5: Make port 5000 available outside the container
EXPOSE 5000

# Step 6: Disable buffered output for better logging in real time
ENV PYTHONUNBUFFERED=1

# Step 7: Define the command to run the Flask app
CMD ["python", "app.py"]
```

- **Explanation**:
  - **Base Image**: We use the `python:3.9-slim` image to keep the image size small.
  - **Working Directory**: The `WORKDIR` command sets `/app` as the working directory inside the container.
  - **COPY**: The `COPY . /app` command copies all files from the local directory to `/app` inside the container.
  - **RUN**: This installs the required dependencies from `requirements.txt`.
  - **EXPOSE**: This makes port 5000 accessible to the host machine.
  - **CMD**: This tells Docker to run the `app.py` script when the container starts.

---

#### 4. **Build the Docker Image**

Once your `Dockerfile`, `app.py`, and `requirements.txt` are in place, build the Docker image.

- **Build the image**:
  ```bash
  docker build -t my_flask_app .
  ```

- **Explanation**: The `-t` option allows you to tag (name) your image as `my_flask_app`, and the `.` at the end specifies that Docker should use the current directory as the build context (where `Dockerfile` is located).

---

#### 5. **Run the Docker Container**

Now, run a container using the Docker image you've built.

- **Run the container**:
  ```bash
  docker run -d -p 5000:5000 --name my_flask_container my_flask_app
  ```

- **Explanation**:
  - `-d`: Runs the container in detached mode, so it runs in the background.
  - `-p 5000:5000`: Maps port 5000 on your local machine to port 5000 inside the container.
  - `--name my_flask_container`: Assigns a custom name (`my_flask_container`) to the running container.
  - `my_flask_app`: The name of the image to run.

---

#### 6. **Access the Application**

Once the container is running, open your web browser and navigate to:

```
http://localhost:5000
```

You should see the message:

```
Hello, Docker!
```

---

#### 7. **Managing the Container**

You can manage your running container using Docker commands.

- **View running containers**:
  ```bash
  docker ps
  ```

- **Stop the container**:
  ```bash
  docker stop my_flask_container
  ```

- **Remove the container** (optional, if you want to clean up):
  ```bash
  docker rm my_flask_container
  ```

- **Remove the image** (optional):
  ```bash
  docker rmi my_flask_app
  ```

---

### Common Scenarios

#### Rebuilding the Image After Updates

If you make changes to your `app.py` or `requirements.txt`, you need to rebuild the Docker image.

- **Rebuild the image**:
  ```bash
  docker build -t my_flask_app .
  ```

- **Stop and remove the old container**:
  ```bash
  docker stop my_flask_container
  docker rm my_flask_container
  ```

- **Run the updated container**:
  ```bash
  docker run -d -p 5000:5000 --name my_flask_container my_flask_app
  ```

---

### Summary of Files:

- **`app.py`**: Python Flask application.
- **`requirements.txt`**: File listing the required Python packages (Flask in this case).
- **`Dockerfile`**: Instructions for building a Docker image that runs the Flask application.

---
