from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension("miomodulo", ["miomodulo.cpp"]),
]

setup(
    name="my_module",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)

# Eseguire nel terminal: python setup.py build_ext --inplace