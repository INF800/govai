### Insatallation

Install locally with sym-link for fast code updates
```
pip install -e .
```

Generate distributable file
```
python setup.py sdist
```
Can install using: `pip install https://github.com/INF800/govai/raw/main/dist/govai-0.0.0.tar.gz`

Share distributable using pypi
```
twine upload dist/* 
```

### Usage

1. Decide your working dir where all your code data will be shared. Let us call this `{wdir}`
2. generate configs in wdir using. After command runs, we will see `configs` directory in `{wdir}`
    ```shell
    python -m govai.setup_working_dir {wdir}
    ```