from setuptools import find_packages, setup
from typing import List

HYPEN_E = "-e ."

def get_requirements(path:str) -> List[str]:
    """"
    Return the requirements into a list
    """
    requirements = []
    with open(path) as f:
       requirements = [ req.replace("\n", "") for req in f.readlines() ]

    if HYPEN_E in requirements:
        requirements.remove(HYPEN_E)

    return requirements
    
setup(
    name="ml-project",
    version="0.1",
    author="Eric",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
) 
