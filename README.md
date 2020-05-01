# teams-import
A secure Powershell wrapper tool to securely bulk import students to Microsoft Teams.

## Features
* Uses secure Microsoft authentication, doesn't store any authentication tokens.
* Can bullk import students to multiple teams.
* Configuration based: Simply provide CSV(s) with the student emails to import.

## Requirements
* Currently MacOS only
* Powershell installed: [Install Powershell on MacOS](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-macos?view=powershell-7)
* A Deakin University email address which is a member of the Microsoft Team(s) you are looking to import students to.
* A directory, containing CSV file(s). The files must have the unit ID as the name of the file. For example: 

```
/unit-csvs/sit102.csv
/unit-csvs/sit111.csv
```

### CSV Format
* A single column CSV with the title "email", followed by the list of student deakin emails which will be imported.

## Usage

1. Install Powershell for MacOS: [Install Powershell on MacOS](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-macos?view=powershell-7)

2. Run the tool:

`teams-import [OPTIONS] CSV_DIR EMAIL`

example:

`teams-import ./unit-csvs jake.renzella@deakin.edu.au`

3. Follow the command line instructions and authenticate the teams Powershell environment. You will see a line like the following:

> WARNING: To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code XXXXXXXX to authenticate.`

Open the link, log in, and authenticate with the code.

> Note, currently you will have to authenticate two seperate times. One to generate the list of teams to import, and another to actually perform the import.

4. Once authenticated, the command line will try and import the students. Note: for large units, the import may take several minutes.