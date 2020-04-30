Import-Module MicrosoftTeams
Connect-MicrosoftTeams
Get-Team -User jake.renzella@deakin.edu.au | Select-Object GroupID, DisplayName | Export-CSV -path ./teams.csv -NoTypeInformation
Import-Csv -Path ./csvs/SIT102.csv | ForEach-Object {Add-TeamUser -GroupId 2f99227c-3191-474d-910c-6a35a71fa2be -user $_.email}
