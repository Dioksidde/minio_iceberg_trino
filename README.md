# 🚀 Data Lake Environment with MinIO, Nessie, and Trino

**Highlights**  
- **All-in-One Setup:** Quickly spin up a containerized data lake environment for rapid prototyping and exploration.  
- **Modern Stack:** Integrate MinIO (S3-compatible storage), Nessie (Git-like data catalog), and Trino (fast, distributed SQL engine).  
- **Easy Onboarding:** Minimal configuration required; just `docker compose up -d` and you’re good to go!  
- **Flexible & Approachable:** Perfect for learning, testing new ideas, or building proofs-of-concept.

## ℹ️ Overview
This project provides a pre-configured environment to jump-start your data lake exploration. It bundles three key components:

- **MinIO:** An S3-compatible object store to hold your raw and processed data.  
- **Nessie:** A version-controlled data catalog for Iceberg tables, allowing you to “time-travel” through your data’s history and manage schema evolution effortlessly.  
- **Trino:** A distributed SQL query engine that lets you interactively explore and analyze your datasets at scale.

With a single `docker compose up -d`, you can experiment locally without wrestling with complex cluster setups. Whether you’re a student, a data engineer, or just curious about modern data lake technologies, this environment offers a friendly starting point.

## 📦 Installation & Setup

### Prerequisites
- Docker: https://docs.docker.com/get-docker/  
- Docker Compose: https://docs.docker.com/compose/install/

### Quick Start
1. Clone the repository:  
   git clone https://github.com/yourusername/your-repo.git  
   cd your-repo

2. Start the environment:  
   docker compose up -d

   This command will:  
   - Pull and run the MinIO, Nessie, and Trino containers.  
   - Set up a dedicated Docker network for seamless communication.  
   - Create a persistent data volume for MinIO so your data persists between sessions.

3. Verify the services are running:  
   docker ps

   You should see containers for MinIO, Nessie, and Trino all in a “running” state.

## 🌐 Accessing the Services

- **MinIO Console:**  
  URL: http://localhost:9001  
  Credentials: minioadmin / minioadmin

- **Nessie UI & API:**  
  URL: http://localhost:19120

- **Trino Web UI:**  
  URL: http://localhost:8080/ui/login.html  
  Login with any username (e.g., test).

## 🚀 Usage Instructions

**Run SQL Queries with Trino:**
1. Open a Trino CLI session:  
   docker exec -it trino trino

2. Explore your Iceberg catalog (powered by Nessie):  
   SHOW SCHEMAS FROM iceberg;

3. Run queries (for example):  
   SELECT * FROM iceberg.my_schema.my_table LIMIT 10;

**Visualize It:**  
Consider adding screenshots or GIFs to show what the UI looks like and how queries return results—this can be more inviting than plain text.

## ⬇️ Installation Instructions (Recap)
Just `docker compose up -d` after cloning. That’s it! Your environment is now ready for exploration.

**Minimum Requirements:**  
- Runs on Linux, macOS, and Windows (with Docker installed).  
- Ensure you have recent versions of Docker and Docker Compose.

## 🏗 Project Structure
.
├─ docker-compose.yml      # Orchestrates MinIO, Nessie, Trino services  
├─ src/                    # Trino configuration files  
├─ data/                   # Persistent storage for Trino  
└─ README.md               # This documentation file

- **docker-compose.yml:** Defines the services and how they connect.  
- **src/:** Holds configuration for Trino to discover and query Nessie-based Iceberg tables.  
- **data/:** Contains Trino’s persistent state and logs.  
- **README.md:** The guide you’re reading now.

## 😅 Troubleshooting

- **Port Conflicts:** If ports (9000, 9001, 19120, 8080) are in use, update them in docker-compose.yml.  
- **Services Not Starting:** Check the logs with:  
  docker compose logs -f

- **Credentials Issues:** Ensure MINIO_ROOT_USER and MINIO_ROOT_PASSWORD in docker-compose.yml match what you’re using in the MinIO console.

## 💭 Feedback & Contributions
If you find this environment helpful or have ideas for improvement:

- Open Issues: Request new features or report bugs.  
- Pull Requests: Contribute directly to the codebase or docs.  
- Discussions: Start a conversation about how we can make this environment even better.

Your feedback helps shape a more accessible and user-friendly data lake tooling experience.

## ⚖️ License
MIT License

Happy exploring! Don’t hesitate to suggest improvements or show off what you build with this setup.