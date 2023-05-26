from setuptools import setup
import as3toplevel

setup(name="as3toplevel",
      version=as3toplevel.__version__,
      author="ajdelguidice",
      url="https://github.com/ajdelguidice/python-as3toplevel",
      py_modules=["as3toplevel"],
      description="Python implementation of the ActionScript3 toplevel",
      python_requires=">=3.8",
      )
