# Fetch

# Tech stack

- Docker
- Docker-compose
- Python

# Prerequisite
- Install Docker
  - [MacOS](https://docs.docker.com/desktop/setup/install/mac-install/)
  - [Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

# Get started

- Run the app
    - `docker compose up --build`

# Clean up

- Shut down app
    - `docker compose down`

# How-to

## Change the input file for health-checking API endpoints

- By default, `.env` has a `API_ENDPOINT_FILE` variable assigned to value `./api_endpoints.yml`
- Developers can override the environment variable through `docker-compose.yml` 

# Demo

![alt text](./doc/demo.png)
