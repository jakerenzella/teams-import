import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    description="A command line tool for bulk importing students to MicrosoftTeams",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Jake Renzella",
    author_email="jake.renzella@deakin.edu.au",
    license="MIT",
    name='teams-import',
    version='1.0.8b2',
    py_modules=['main'],
    packages=['teams_import'],
    install_requires=[
        'click',
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "teams-import=teams_import.__main__:cli",
        ]
    }
)
