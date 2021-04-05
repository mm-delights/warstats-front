# warstats-front
In Game WZ Stats

## Init Development Environment

make sure pyenv is installed
```
pyenv install 3.8.6
pyenv global 3.8.6
python -V
python -m venv .venv
source .venv/bin/activate #unix
pip install -r requirements_local.txt
```

## Running Tests 

```
pytest ./tests
```