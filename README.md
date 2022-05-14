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
