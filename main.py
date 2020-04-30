import click
import shell
import csv
import re
import os

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


def generageImport(csvsDir, dict, email):
    not_found = []
    found = []
    f = open("import.ps1", "w+")
    for key, value in dict.items():
        file_path = f"{csvsDir}/{key}.csv"
        if os.path.isfile(file_path):
            found.append(f"Preparing import for {file_path}")
            f.write(
                "Import-Module MicrosoftTeams\n"
                "Connect-MicrosoftTeams\n"
                f"Get-Team -User {email} | Select-Object GroupID, DisplayName | Export-CSV -path ./teams.csv -NoTypeInformation\n"
                f"Import-Csv -Path {file_path} | ForEach-Object {{Add-TeamUser -GroupId {value} -user $_.email}}\n")
        else:
            not_found.append(f"No CSV file found at {file_path}")

    print("\n".join(found))
    print("\n".join(not_found))


def process(csvsDir, email):
    dict = {}
    with open('teams.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            unitCode = getUnitcodeFromDisplayName((row['DisplayName']))
            if unitCode:
                dict[unitCode] = row['GroupId']
    generageImport(csvsDir, dict, email)


def init(email):
    result = shell.check_command_installed("pwsh")
    if not result:
        exit(2)
    else:
        shell.exec_powershell_script("./install-teams.ps1", email)


@click.command()
@click.argument('csvsDir', type=click.Path(exists=True))
@click.argument('email', required=True)
def cli(csvsdir, email):
    """The CLI tool for importing Deakin students into Microsoft teams"""
    init(email)
    process(csvsdir, email)
    invite()
