
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements() -> List[str]:
    requirements = []

    with open("requirements.txt", 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='phising',
    version='0.0.1',
    author='kunal',
    author_email='kunalchopde98@gmail.com',
    install_requires=get_requirements(),
    packages=find_packages()
)
