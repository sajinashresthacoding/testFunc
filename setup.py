import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='testFunc', ##name of repo enclosing folder (pip-package-demo)
    version='0.0.4',
    author='Sajina Shrestha', ## your name
    author_email='sajina.shrestha54@journalism.cuny.edu', ## your email
    description='math functions i use a lot', ## description of package
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sajinashresthacoding/testFunc',# url to repo
    project_urls = {
        "Bug Tracker": "https://github.com/sajinashresthacoding/testFunc/issues"
    }, ## url to issues page on your repo
    license='MIT',
    packages=['mathFunctions'], ## name of folder that holds the functions
    install_requires=[], ## names of packages required to run your functions
)