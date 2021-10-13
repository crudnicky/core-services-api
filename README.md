# Core Services API

The Core Services API powers the UI for the integrated Absci Core Services Apps.
## Project Setup

Before working with the Core Services API, you will need to configure you laptop, and add a
few files to the API.

### Docker

This project is hosted inside of a Docker container, and you will need the software on your
computer.

> _[Get Docker](https://docs.docker.com/get-docker/)_

### Python Poetry

Core Services uses Python Poetry to manage dependencies for the project. Poetry is very easy
to use, and mimics how you would use a tool like pip. 

**pip**
```
$ pip install x
```

**poetry**
```
$ poetry add x
```

Rather than installing packages to a global module, Poetry adds package data to two files in
the root: `poetry.lock` and `pyproject.toml`.

> [Get Poetry](https://python-poetry.org/)_

### Files

**.env.dev** - Use the `.env-example` as a scaffold for the `.env.dev`. It must be placed in
the project root.

**.unlimiter/config.yaml** - This is required for Unlimiter SDK to function. Make the directory
in the project root and _[follow the directions for authentication and configuration](https://github.com/AbSciBio/unlimiter#authentication-configuration)._

## Commands

|Command | Purpose |
|---|---|
| `bash index.sh` | This command builds and starts the Core Services API inside a Docker container.|

