Ansible inventory rendering tool implemented in Python(3.11) and Jinja2.

How to use it

- Setup [Miniconda](https://docs.anaconda.com/miniconda/) and activate the Python3 env 3.11
```shell
conda create -n py311 python=3.11
conda env list
conda activate py311
```

- Generate and install the pip dependencies
```shell
pip freeze > reqs.txt
pip install -r reqs.txt
```

- Show help or Call rendering
```shell
python render.py -h
python render.py -t example/inventory.j2 -v example/vars.yaml
```
