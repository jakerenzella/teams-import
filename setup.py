from setuptools import setup

setup(
  name='teams-import',
  version='1.0',
  py_modules=['main'],
  install_requires=[
    'click',
  ],
  entry_points='''
    [console_scripts]
    teams-import=main:cli
  '''
)