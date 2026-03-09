from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    '''This function will return the list of requirements'''
    try:
        with open("requirements.txt", "r") as f:
            requirements = f.readlines()
            requirements = [req.replace("\n", "") for req in requirements]
            requirements = [req for req in requirements if not req.startswith("-e")]
        return requirements
    
    except FileNotFoundError:
        print("requirements.txt file not found.")

setup(
    name="networksecurity",
    version="0.0.1",
    author="MD ALTAF HOSSAIN SUNNY",
    author_email="www.altafhossainsunny@email.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)