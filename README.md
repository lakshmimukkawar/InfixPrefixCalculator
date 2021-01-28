# Infix Prefix Calculator
## Description

Evaluates the infix / prefix expressions

## How to build

Docker: `docker build -t calculator .`
Python: `pip install pipenv`

## How to run

Docker : run `docker run -p 5000:5000 calculator`


- Test suite: 
    - Run: `pipenv sync`
    - Activate the environment: `pipenv shell`
    - Run: `pipenv run pytest -v tests/`


### Things to improve on 
- Add more test cases
- Handle different types of input validations on the upcoming request
- Better exception handling
- Add multiprocessing for handling more load
- Add prometheus metrics to help and monitor the API metrics suchs as latency, error rate. We can use prometheus clients from python