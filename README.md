# Airflow-Docker
---

### **Steps to Install Apache Airflow on Windows Using Docker**

1. **Create Directory Structure for Airflow**
   - Open a terminal or File Explorer and create a new directory for Airflow:
     ```
     mkdir airflow
     cd airflow
     mkdir logs dags plugins
     ```
   - You should now have three subdirectories inside the `airflow` folder: `logs`, `dags`, and `plugins`.

2. **Install Docker Desktop for Windows**
   - If you haven't already, download and install **Docker Desktop** from the official website: [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop).
   - After installation, ensure Docker is running.

3. **Download the Docker Compose YAML for Airflow**
   - Download the `docker-compose.yaml` file for the latest version of Airflow (2.8.1) from the link below and place it inside the `airflow` directory you created in Step 1: [Download docker-compose.yaml](https://airflow.apache.org/docs/apache-airflow/2.10.0/docker-compose.yaml)

   - Alternatively, you can use this terminal command to download the file directly:
     ```
     curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.1/docker-compose.yaml'
     ```

   - You can find more details about the latest releases here: [Airflow Releases](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html)

4. **Initialize Airflow**
   - Before starting Airflow, initialize it with the following command:
     ```
     docker-compose up airflow-init
     ```

5. **Start Airflow**
   - After initialization, start all the services with:
     ```
     docker-compose up
     ```

6. **Accessing the Airflow Web UI**
   - Once the services are up, you can access the Airflow UI in your browser by navigating to: **http://localhost:8080**

---

### **Clean Up (Optional)**
   - To stop and clean up all the containers, volumes, and memory, run the following command in the directory where you have the `docker-compose.yaml` file:
     ```
     docker-compose down --volumes --remove-orphans
     ```

---

### **Key Components in the Airflow Docker Setup**

- **airflow-scheduler**: Monitors and triggers task instances based on DAG dependencies.
- **airflow-webserver**: Hosts the web interface available at `http://localhost:8080`.
- **airflow-worker**: Executes the tasks as instructed by the scheduler.
- **airflow-triggerer**: Manages deferrable tasks using an event loop.
- **airflow-init**: Initializes the Airflow services.
- **postgres**: The database backend for storing metadata.
- **redis**: The message broker forwards messages between the scheduler and the worker.

For more details, refer to the official documentation: [Airflow Docker Compose Setup](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

---
