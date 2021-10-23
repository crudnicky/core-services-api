# Core Services API

The Core Services API powers the UI for the integrated Absci Core Services Apps.
## Project Setup

Before working with the Core Services API, you will need to install Docker on you laptop, and 
add several sensitive files to the project.

### Docker

The core services api is hosted inside of a Docker container that runs a python image. This
creates an isolated environment that any developer can run on their laptop without needing
to globally install project dependencies.

> _[Get Docker](https://docs.docker.com/get-docker/)_

### Python Poetry

Core Services uses Python Poetry to manage dependencies for the project. Poetry is very easy
to use, and mimics how you would use a tool like pip. 
|Tool| Command|
|---|---|
| **pip** | `$ pip install x`|
|**poetry**| `$ poetry add x` |


Rather than installing packages to a global module, Poetry adds package data to two files in
the root: `poetry.lock` and `pyproject.toml`. This creates an account of the project dependencies
that are referenced during the Docker container build. 

> _[Get Poetry](https://python-poetry.org/)_

### Required Files

**.env.dev** - Use the `.env-example` as a scaffold for the `.env.dev`. It must be placed in
the project root.

**config/unlimiter.config.yaml** - This is required for Unlimiter SDK to function. Make the directory
in the project root and _[follow the directions for authentication and configuration](https://github.com/AbSciBio/unlimiter#authentication-configuration)._

## Commands

|Command | Purpose |
|---|---|
| `bash index.sh` | This command builds and starts the Core Services API inside a Docker container. |
| `pytest` | Initiates unit test run. |



## Testing

Tests can be excuted inside the docker container by opening the CLI and running `pytest`. If you
have the project dependencies installed globally, tests can be run outside the docker container.