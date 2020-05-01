import click
import csv
import re
import os
import tempfile

import teams_import
from teams_import import shell

try:
    import importlib.resources as pkg_resources

except ImportError:
    import importlib_resources as pkg_resources

temp = tempfile.NamedTemporaryFile(mode="w+", suffix='.csv')
print(temp.name)

def invite():
    if os.path.isfile("./import.ps1"):
        shell.exec_powershell_script("./import.ps1")
    else:
        print("Can't find import powershell file")


def getUnitcodeFromDisplayName(displayName):
    m = re.search('SIT[0-9]{3}', displayName)
    if m:
        return m.group(0)
    else:
        click.echo("No valid unit code in: " + displayName)
        return None


def generateImport(csvsDir, dict, email):

    not_found = []
    found = []
    f = open("import.ps1", "w+")
    for key, value in dict.items():
        file_path = f"{csvsDir}/{key}.csv"
        if os.path.isfile(file_path):
            found.append(f"Preparing import for {file_path}")
            print(
                "Import-Module MicrosoftTeams\n"
                f"Connect-MicrosoftTeams\n"
                f"Import-Csv -Path {file_path} | ForEach-Object {{Add-TeamUser -GroupId {value} -user $_.email}}\n")
            f.write(
                "Import-Module MicrosoftTeams\n"
                f"Connect-MicrosoftTeams\n"
                f"Import-Csv -Path {file_path} | ForEach-Object {{Add-TeamUser -GroupId {value} -user $_.email}}\n")
        else:
            not_found.append(f"No CSV file found at {file_path}")

    print("\n".join(found))
    print("\n".join(not_found))


def process(csvsDir, email):
    dict = {}
    with open(temp.name, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            unitCode = getUnitcodeFromDisplayName((row['DisplayName']))
            if unitCode:
                dict[unitCode] = row['GroupId']
    generateImport(csvsDir, dict, email)


def init(email):
    result = shell.check_command_installed("pwsh")
    if not result:
        exit(2)
    else:
        with pkg_resources.path('teams_import.templates', 'install-teams.ps1') as file:
            shell.exec_powershell_script(file, email, temp.name)


@click.command()
@click.argument('csvsDir', type=click.Path(exists=True))
@click.argument('email', required=True)
def cli(csvsdir, email):
    """The CLI tool for importing Deakin students into Microsoft teams"""
    init(email)
    process(csvsdir, email)
    invite()
