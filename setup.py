import setuptools

with open("README.md", "r") as fh: long_description = fh.read()
setuptools.setup(name='jsonconfig',
                 version='0.1',
                 description="Simple JsonConfig",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author="Julian Stobbe",
                 author_email="julian-stobbe@gmx.de",
                 python_requires='>=3',
                 url="https://github.com/flamel90/jsonconfig",
                 packages=setuptools.find_packages(),
                 include_package_data=True,
                 license='MIT',
                 classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent", ], )
