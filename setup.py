
### setup yo

from setuptools import setup, find_packages

setup(
    name='atl100',
    description='atl100 - atl 100 dishes to try',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'faunadb',
        'Click',
        'Hy',
    ],
    entry_points='''
        [console_scripts]
        atl100=atl100.scripts.clickit:cli
    ''',
    author='Glenn barry',
    author_email='gaak99@gmail.com',
    url='https://github.com/gaak99/atl100poc.git',
)
