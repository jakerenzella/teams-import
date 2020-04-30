import platform
import click
import subprocess

def __exec_macos(args):
    return subprocess.run(args)

def check_command_installed(command):
    return subprocess.run(["command", "-v", command]).returncode == 0

def exec(commands):
    if platform.system() == 'Darwin':
        return __exec_macos(commands)
    elif platform.system() == 'Windows':
        click.echo("Windows not currently supported")
        exit(1)
    else:
        click.echo('Platform Unsupported')
        exit(1)

def exec_powershell_script(script, *args):
    command = ["pwsh", script] + list(args)
    print (command)
    exec(command)

def exec_powershell_command(*args):
    command = ["pwsh", "-c", args]
    if platform.system() == 'Darwin':
        click.echo("Running Command: ")
        click.echo(command)
        subprocess.run(command)
    elif platform.system() == 'Windows':
        pass
    else:
        click.echo('Platform Unsupported')
        exit(1)

    click.echo(args)
