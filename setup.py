from distutils.core import setup
from distutils.extension import Extension

setup(name="PackageName",
    ext_modules=[
        Extension("hello", ["testBoost.cpp", 'PyLogger.cpp'],
                  extra_compile_args=['-std=gnu++11'],
                  libraries=["boost_python3"])
    ])
