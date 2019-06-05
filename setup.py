from setuptools import setup

setup(
    name='GoingAwayToCollegeApp',
    packages=['GoingAwayToCollegeApp'],
    include_packages_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
    ]
)
