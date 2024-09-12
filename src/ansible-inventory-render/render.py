#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import json
import args
from yaml import safe_load
from jinja2 import Environment, FileSystemLoader
from pyutils.wrappers import try_catch, init_args

CWD = os.getcwd()

def _load_json(f: 'filename') -> dict:
  with open(f, 'r') as jf:
    vdct = json.load(jf)
  return vdct

def _load_yaml(f: 'filename') -> dict:
  with open(f, 'r') as yf:
    vstr = yf.read()
  return safe_load(vstr)

def _get_vars(f: 'filename') -> dict:
  vdct = {}
  if f.endswith(('yml','yaml')):
    vdct = _load_yaml(f)
  elif f.endswith('json'):
    vdct = _load_json(f)
  return vdct


def render(vf: 'vars file', tf: 'template file') -> str:
  """Render the Ansible inventory from the template and yaml/json vars
  Args:
    vf (vars file): yaml or json file contains the variables
    tf (template file): the inventory template file
  Returns:
    res (str): the rendered yaml format inventory string
  """
  env = Environment(loader=FileSystemLoader(os.path.dirname(tf)), autoescape=True)
  tpl = env.get_template(os.path.basename(tf))
  res = tpl.render(_get_vars(vf))
  return res


@try_catch(print)
@init_args(
  args.description,
  args.options
)
def main(parsed_args=None):
  """Entry function, call render and output the result to file"""

  r = render(
    f'{CWD}/{parsed_args.vars}', f'{parsed_args.template}'
  )
  with open(parsed_args.outfile, 'w') as f:
    f.write(r)

if __name__ == '__main__':
  main()
