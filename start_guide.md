# **Docker**

Docker is a platform that simplifies the development, deployment, and running of applications by utilizing containers. Let’s break it down step by step:

---

## **1. What is Docker?**

Docker is a tool that helps developers package and run applications inside containers. Containers bundle the application along with its dependencies, ensuring the app runs consistently across different environments.

---

## **2. What are Containers?**

Containers are lightweight, portable environments that allow applications to run in isolation. Unlike virtual machines (VMs), containers share the host system’s operating system (OS), which makes them more efficient and faster.

**Why use containers?**  
Imagine you build an app on your computer, but when you run it on another machine, it fails due to environment differences. Containers solve this issue by packaging everything the app needs, ensuring it behaves the same on any system.

---

## **3. Docker vs Virtual Machines**

Before Docker, virtual machines were commonly used to isolate applications, but they are large, resource-intensive, and slow because each VM requires its own OS. Docker containers, on the other hand, are lightweight because they share the host OS kernel.

### **Key Differences:**

| Feature             | **Virtual Machine**                 | **Container**                |
|---------------------|-------------------------------------|------------------------------|
| **OS**              | Requires its own OS                 | Shares host OS kernel        |
| **Resource Usage**   | Higher (includes OS resources)      | Lower (only app dependencies) |
| **Speed**           | Slower to start and run             | Fast and efficient           |
| **Portability**      | Complex                             | Highly portable              |

---

## **4. Why Use Docker?**

- **Consistency**: Ensures the application runs the same way in all environments.
- **Isolation**: Multiple applications can run independently on the same machine.
- **Portability**: Containers can run on any system supporting Docker (Windows, Mac, Linux, or in the cloud).
- **Efficiency**: Uses fewer resources than virtual machines.
- **Fast Deployment**: Quick start and stop of containers, enabling faster deployments.

---

## **5. Basic Concepts in Docker**

- **Dockerfile**: A script containing instructions to build a Docker image (e.g., "install this package," "copy these files").
  
- **Image**: A snapshot or blueprint of your application with everything it needs to run (code, libraries, settings). Think of it as a read-only template.

- **Container**: A running instance of an image. You can have multiple containers running from the same image, each one isolated.

- **Docker Hub**: A public registry for Docker images. You can pull ready-to-use images from Docker Hub or push your custom images.

---

## **6. Docker Workflow**

Here’s the basic Docker workflow to understand how it operates:

1. **Write a Dockerfile**: Define how to build your Docker image.
2. **Build the Image**: Using the Dockerfile, Docker creates an image.
3. **Run the Image as a Container**: Create a container from the image to run your app.
4. **Push/Pull Images**: Push your image to Docker Hub or pull an existing image for use.

---

## **7. Basic Docker Commands**

### **Pull an Image**
To download an image from Docker Hub:
```bash
docker pull ubuntu
```

### **Build an Image**
To build an image from a Dockerfile:
```bash
docker build -t myapp .
```

### **Run a Container**
To run a container from an image:
```bash
docker run -it ubuntu
```

### **List Running Containers**
To see all running containers:
```bash
docker ps
```

### **Stop a Running Container**
To stop a container:
```bash
docker stop <container_id>
```

### **Remove a Container**
To remove a container:
```bash
docker rm <container_id>
```

### **Remove an Image**
To delete an image:
```bash
docker rmi <image_name>
```

---

## **8. Getting Started with Docker on Windows**

Follow this guide to set up Docker on a Windows machine:

### **Step 1: Install Docker Desktop**
- Download and install Docker Desktop from the official Docker website.
- Once installed, launch Docker Desktop and ensure it is running.

### **Step 2: Verify Installation**
- Open PowerShell or Command Prompt and run the following command:
```bash
docker --version
```
- This will display the installed Docker version.

### **Step 3: Learn Basic Docker Commands**

#### **Check Docker Information**
To get detailed info about your Docker setup:
```bash
docker info
```

#### **Pull and Run a Hello World Container**
1. Pull the `hello-world` image from Docker Hub:
   ```bash
   docker pull hello-world
   ```
2. Run the `hello-world` container:
   ```bash
   docker run hello-world
   ```

#### **List Running Containers**
To see all running containers:
```bash
docker ps
```

#### **List All Containers**
To display all containers (running or stopped):
```bash
docker ps -a
```

#### **Stop a Running Container**
To stop a container (replace `<container_id>` with the actual container ID):
```bash
docker stop <container_id>
```

#### **Remove a Container**
To remove a stopped container:
```bash
docker rm <container_id>
```

#### **Remove an Image**
To delete an image (replace `<image_name>` with the actual image name):
```bash
docker rmi <image_name>
```

---
