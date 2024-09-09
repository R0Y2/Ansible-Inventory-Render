#! /usr/bin/env python
# -*- coding:utf-8 -*-

description = "Ansible Inventory Render"
options={
  'template_file':{
    'long': '--template',
    'short':'-t',
    'default': 'inventory.yml.j2'
  },
  'vars_file':{
    'long':'--vars',
    'short':'-v',
    'default':'vars.yml'
  },
  'out_file':{
    'long':'--outfile',
    'short':'-o',
    'default':'inventory.yml'
  }
}
