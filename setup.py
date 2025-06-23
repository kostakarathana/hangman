from setuptools import setup
from Cython.Build import cythonize

setup(
    name="cython_accel",
    ext_modules=cythonize("cython_accel.pyx", compiler_directives={"language_level": 3}),
)