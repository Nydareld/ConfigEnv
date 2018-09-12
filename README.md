# ConfigEnv
Gestionnaire de configuration en json, ini avec overide possible en variable d’environnement

## install

## how to use

## devlopping guide

we advise you to fork the depot, and if you have goot feature, we would appreciate pull request

### install developement environement

with virtualenv :

    virtualenv -p python3 .venv
    source .venv/bin/activate

install depenencies :

    pip install -r requirements.txt

### test

run tests :

    python -m unittest tests

### coverage

run coverage

    coverage run --source=ConfigEnv -m unittest tests

report coverage

    coverage report -m
