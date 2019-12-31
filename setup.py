from setuptools import setup, find_packages

setup(
    name='catslab',
    entry_points={
        'console_scripts': [
            'catslab = catslab.main:main',
        ],
    },
    version='0.1',
    description='',
    author='RV',
    author_email='yo-maruya@rescala.jp',
    install_requires=['numpy', 'pandas', 'mypy', 'argparse', 'matplotlib', 'seaborn', 'scipy'],
    url='https://finance.rescala.jp',
    license=license,
    packages=find_packages(exclude=('tests'))
)
