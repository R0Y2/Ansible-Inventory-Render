#! /usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import functools
import traceback

def init_args(des: "description", ops: "options dict"):
  """Init commandline arguments"""
  def deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      parser = argparse.ArgumentParser(
        description=des,
        formatter_class=argparse.RawTextHelpFormatter
      )
      for opk,opv in ops.items():
        parser.add_argument(
          opv['long'],
          opv['short'],
          metavar=opk,
          default=opv['default'],
          help="(default: %(default)s)"
        )
      #kwargs['args'] = parser.parse_args()
      rtn = func(parser.parse_args(), *args, **kwargs,)
      return rtn
    return wrapper
  return deco

def try_catch(func):
  """Catch exceptions"""
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    try:
      func(*args, **kwargs)
    except Exception as e:
      print(repr(e))
      print(traceback.format_exc())
  return wrapper
