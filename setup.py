from setuptools import setup
import as3toplevel

setup(name="as3toplevel",
      version=as3toplevel.__version__,
      author="ajdelguidice",
      author_email="ajdelguidice@gmail.com"
      url="https://github.com/ajdelguidice/python-as3toplevel",
      py_modules=["as3toplevel"],
      description="Python implementation of the ActionScript3 toplevel",
      classifiers=[
            "Development Status :: 4 - Beta",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.8",
            "Topic :: Utilities"
            ],
      python_requires=">=3.8",
      install_requires=["numpy"],
      )
