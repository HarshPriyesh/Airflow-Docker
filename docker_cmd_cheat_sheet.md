
# Docker Commands Cheat Sheet

## 1. Docker Basics

- **Check Docker Version**  
  ```bash
  docker --version
  ```
  Displays the version of Docker installed.

- **Display Docker System Information**  
  ```bash
  docker info
  ```
  Shows detailed information about your Docker installation, including the number of containers, images, and more.

## 2. Container Management

- **Run a Container**  
  ```bash
  docker run [options] IMAGE_NAME
  ```
  Runs a container from an image. Example:
  ```bash
  docker run -d nginx
  ```
  Options:
  - `-d`: Run container in detached mode (in the background).
  - `-it`: Run container in interactive mode (with a terminal).

- **List Running Containers**  
  ```bash
  docker ps
  ```
  Lists all currently running containers.

- **List All Containers (Running & Stopped)**  
  ```bash
  docker ps -a
  ```

- **Stop a Running Container**  
  ```bash
  docker stop CONTAINER_ID
  ```

- **Start a Stopped Container**  
  ```bash
  docker start CONTAINER_ID
  ```

- **Remove a Container**  
  ```bash
  docker rm CONTAINER_ID
  ```

## 3. Image Management

- **List All Docker Images**  
  ```bash
  docker images
  ```

- **Pull an Image from Docker Hub**  
  ```bash
  docker pull IMAGE_NAME
  ```
  Example:
  ```bash
  docker pull ubuntu
  ```

- **Remove an Image**  
  ```bash
  docker rmi IMAGE_ID
  ```

- **Build an Image from a Dockerfile**  
  ```bash
  docker build -t IMAGE_NAME .
  ```
  The `-t` flag tags the image with a name.

- **Clean Up Dangling/Unused Images**  
  ```bash
  docker image prune
  ```

## 4. Working with Volumes

- **List Docker Volumes**  
  ```bash
  docker volume ls
  ```

- **Create a Volume**  
  ```bash
  docker volume create VOLUME_NAME
  ```

- **Remove a Volume**  
  ```bash
  docker volume rm VOLUME_NAME
  ```

## 5. Network Management

- **List Docker Networks**  
  ```bash
  docker network ls
  ```

- **Create a Network**  
  ```bash
  docker network create NETWORK_NAME
  ```

- **Connect a Container to a Network**  
  ```bash
  docker network connect NETWORK_NAME CONTAINER_ID
  ```

## 6. Inspecting and Logs

- **View Logs of a Container**  
  ```bash
  docker logs CONTAINER_ID
  ```

- **Inspect a Container**  
  ```bash
  docker inspect CONTAINER_ID
  ```
  Provides detailed information about a specific container.

## 7. Exec Command in a Running Container

- **Run a Command in a Running Container**  
  ```bash
  docker exec -it CONTAINER_ID COMMAND
  ```
  Example:  
  ```bash
  docker exec -it CONTAINER_ID /bin/bash
  ```
  This will open a shell session inside the container.

## 8. Clean Up System

- **Remove All Stopped Containers, Networks, and Unused Images**  
  ```bash
  docker system prune
  ```

### Common Use Cases:
- **Run and Remove a Container After It Stops**  
  ```bash
  docker run --rm IMAGE_NAME
  ```

---
