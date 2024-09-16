Ansible inventory rendering tool implemented in Python(3.11) and Jinja2.

##### Getting Started

+ [Pixi](https://pixi.sh/)
  ```
  pixi shell && pixi install
  pixi update (optional)
  ```

+ Conda (*[Miniconda](https://docs.anaconda.com/miniconda/)/Anaconda*)

  - Setup conda and activate the Python3 env 3.11
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


##### Usage
- Show help or Call rendering
```shell
python render.py -h
```

- Generate ansible inventory
```
python render.py -t example/inventory.j2 -v example/vars.yaml
```
