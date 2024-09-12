## Familiarizing Docker on Windows (step-by-step guide)

---

#### 1. **Install Docker Desktop on Windows**
   - Install Docker Desktop and ensure it's running and accessible by opening the Docker Dashboard.

#### 2. **Verify Installation**
   - Open a terminal (PowerShell or Command Prompt) and run the following command to check if Docker is installed correctly:
     ```bash
     docker --version
     ```
   - This should display the Docker version installed.

#### 3. **Learn Basic Docker Commands**
   - Start with some basic commands to get comfortable with Docker:

   - **Check Docker Info:**
     ```bash
     docker info
     ```
     This gives you detailed information about your Docker setup.

   - **Pull an Image:**
     Download a Docker image from Docker Hub. Let's start with a basic `hello-world` container:
     ```bash
     docker pull hello-world
     ```

   - **Run a Container:**
     To run the `hello-world` container:
     ```bash
     docker run hello-world
     ```
     This command downloads and runs a container that prints a hello message.

   - **List Running Containers:**
     ```bash
     docker ps
     ```
     This shows all running containers.

   - **List All Containers:**
     ```bash
     docker ps -a
     ```
     This will display all containers, including stopped ones.

   - **Stop a Running Container:**
     First, list the container ID using `docker ps` and then stop it:
     ```bash
     docker stop <container_id>
     ```

   - **Remove a Container:**
     After stopping a container, you can remove it:
     ```bash
     docker rm <container_id>
     ```

   - **Remove an Image:**
     To remove an image, find the image name using `docker images` and then:
     ```bash
     docker rmi <image_name>
     ```
