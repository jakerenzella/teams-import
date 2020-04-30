# teams-import
A PowerShell tool to bulk import students to Microsoft Teams.

## Requirements
* MacOS with Powershell installed: [Install Powershell on MacOS](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-macos?view=powershell-7)
* A Deakin University email address which is a member of the Microsoft Team(s) you are looking to import students to.
* A directory, containing CSV file(s). The files must have the unit ID as the name of the file. For example: 

```
/unit-csvs/sit102.csv
/unit-csvs/sit111.csv
```

### CSV Format
* A single column CSV with the title "email", followed by the list of student deakin emails which will be imported.

## Usage

1. Run the tool:

`teams-import [OPTIONS] CSV_DIR EMAIL`

example:

`teams-import ./unit-csvs jake.renzella@deakin.edu.au`

2. Follow the command line instructions and authenticate the teams Powershell environment. You will see a line like the following:

> WARNING: To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code GUXEKTDPP to authenticate.`

Open the link, log in, and authenticate with the code.

3. Once authenticated, the command line will try and import the students. Note: for large units, the import may take several minutes.