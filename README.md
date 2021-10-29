### Insatallation

Install locally with sym-link for fast code updates
```
pip install -e .
```

Generate distributable file
```
python3 setup.py sdist
```
Can install using: `pip install https://github.com/INF800/govai/raw/main/dist/govai-0.0.0.tar.gz`

Share distributable using pypi
```
twine upload dist/* 
```

### Usage

1. Decide your working dir where all your code data will be shared. Let us call this `{wdir}`
2. Generate folder structure for `{task_type}`. After command runs, we will see `configs` directory in `{wdir}`
    ```shell
    python3 -m govai.setup_wdir {task_type} {wdir}
    ```
    eg.
    ```shell
    python3 -m govai.setup_wdir regression /workspaces/olympiad
    ```
3. Follow instructions here for your specific setup
    - [Regression](docs/regression/README.md)
    - [Binary Classifcation]()