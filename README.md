# fastapi-starter-template


##  Description

This is a basic python api setup using the FastAPI framework.

###  Directory Structure
```
fastapi-starter-template
├── app
│   ├── api
│   │   ├── endpoints
│   │   │   ├── __init__.py
│   │   │   └── hello.py
│   │   └── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   └── application.py
│   ├── __init__.py
│   └── main.py
├── tests
│   ├── endpoints
│   │   └── hello_test.py
│   ├── __init__.py
│   └── conftest.py
├── Dockerfile
├── README.md
├── docker-compose.yaml
├── poetry.lock
├── pyproject.toml
└── tox.ini
```

##  Getting Started

Getting started developing with this template is pretty simple using docker and docker-compose.

In the terminal:

```shell script
# Clone the repository
git clone git@github.com:zdmwi/fastapi-starter-template.git

# cd into project root
cd fastapi-starter-template

# Create virtual env
python -m venv .venv

# Activate the environment
source .venv/bin/activate

# Install dependencies
pip install poetry && poetry install --no-root

# Launch the project
uvicorn app.main:api --reload
```

Afterwards, the project will be live at [http://localhost:8000](http://localhost:8000).

## Documentation

FastAPI automatically generates documentation based on the specification of the endpoints you have written. You can find the docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## Testing

Run the command:
`pytest`

