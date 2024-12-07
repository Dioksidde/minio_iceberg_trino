# Data Lake Environment with MinIO, Nessie, and Trino

A streamlined, fully-containerized environment to jump-start your data lake adventures! This setup provisions a **MinIO** S3-compatible object store, a **Nessie** catalog service for Iceberg table management, and **Trino** for interactive SQL queries over your data.

## Table of Contents
- [Overview](#overview)
- [Key Components](#key-components)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Accessing the Services](#accessing-the-services)
- [Running Queries](#running-queries)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project brings together three core components in the modern data lake stack:

1. **MinIO**: A self-hosted, S3-compatible object store for persisting your raw data files.
2. **Nessie**: A Git-like version-controlled data catalog for Iceberg, enabling easy table evolution and reproducibility.
3. **Trino**: A fast, distributed SQL query engine that allows you to query data from MinIO (through Iceberg) at scale.

By running `docker compose up -d`, you'll have a fully functional environment ready for experimentation, prototyping, or local development—no complex configuration required.

## Key Components

- **MinIO**:
  - Purpose: Acts as S3-compatible storage for your data lake files.
  - Ports: 9000 (API), 9001 (Web UI)
  - Credentials: minioadmin/minioadmin

- **Nessie**:
  - Purpose: Provides a metadata catalog with Git-like versioning capabilities, enabling time travel and branching for your data.
  - Port: 19120 (REST API and Web UI)
  - Default Profile: prod

- **Trino**:
  - Purpose: Serves as the SQL query engine that sits atop Nessie/Iceberg, providing lightning-fast, ANSI SQL-compatible queries.
  - Port: 8080 (Web UI)
  - Configurations: Mounted from ./src for config files and ./data for persistent state.

## Prerequisites

- **Docker & Docker Compose**: Ensure Docker and Docker Compose are installed and running.
  - Install Docker: https://docs.docker.com/get-docker/
  - Install Docker Compose: https://docs.docker.com/compose/install/

## Installation & Setup

1. **Clone the repository**:  
   Run the following commands in your terminal:
   
       git clone https://github.com/yourusername/your-repo.git
       cd your-repo

2. **Launch the environment**:  
   Use Docker Compose to start all services:
   
       docker compose up -d

   This will:
   - Pull the latest images of MinIO, Nessie, and Trino.
   - Create and start the containers.
   - Initialize a Docker network (trino_network) for service communication.
   - Provision a Docker volume (minio_data) for persistent storage.

3. **Verify the containers are running**:  
   Check the status of your containers:
   
       docker ps

   You should see minio, nessie, and trino containers listed as running.

## Accessing the Services

- **MinIO Console**:  
  URL: http://localhost:9001/  
  Credentials: minioadmin / minioadmin

- **Nessie Web UI & API**:  
  URL: http://localhost:19120/

- **Trino Web UI**:  
  URL: http://localhost:8080/ui/login.html  
  Login: Use any username (e.g. test)

## Running Queries

To execute SQL queries against Iceberg tables via Trino:

1. **Exec into the Trino container**:
   
       docker exec -it trino trino

   This opens a Trino CLI session inside the container.

2. **Explore the Nessie-backed Iceberg catalog**:
   
       show schemas from iceberg;

   From here, you can run standard SQL queries (SELECT, CREATE TABLE, INSERT, DESCRIBE) against your data.

## Project Structure

    .
    ├─ docker-compose.yml          # Defines MinIO, Nessie, Trino services
    ├─ src/                        # Trino configuration files
    ├─ data/                       # Data directory for Trino
    └─ README.md                   # Project documentation (this file)

- **docker-compose.yml**: The main orchestrator for all services.
- **src/**: Contains configuration files for Trino to discover Nessie and query Iceberg tables.
- **data/**: Holds Trino state and query logs.
- **README.md**: This documentation file.

## Troubleshooting

- **Port Conflicts**: If a port is in use, modify the published ports in docker-compose.yml.
- **Services Not Starting**: Run `docker compose logs -f` to view logs and diagnose issues.
- **Credential Issues**: Check that MINIO_ROOT_USER and MINIO_ROOT_PASSWORD in docker-compose.yml match the credentials used in the MinIO console.

## Contributing

Contributions are welcome! Feel free to:
- Open issues for feature requests, bug reports, or improvements.
- Submit pull requests with clear documentation and test cases.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
