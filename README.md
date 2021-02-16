# architecture-patterns-with-python
Archtecture Patterns with Python book


## Build
```sh
make build
make up # or 
make all # builds, brings containers up, runs tests
```

## Tests
```sh
make test
# or, to run individual test types
make unit
make integration
make e2e
# or, if you have a local virtualenv
make up
pytest tests/unit
pytest tests/integration
pytest tests/e2e
