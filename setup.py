from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='genai-gemini',
    version='0.0.1',
    packages=find_packages(),
    install_requires=requirements,
    author='Swaraj Pande',
    author_email='swarajpande5@gmail.com'
)
