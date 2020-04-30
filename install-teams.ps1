param(
[string]$email
)

if (!(Test-Path -Path ./powershell/importerProfile)) {
  New-Item -ItemType File -Path ./powershell/importerProfile -Force
}

if (Get-Module -ListAvailable -Name MicrosoftTeams) {
  Write-Host "MicrosoftTeams Module alread installed"
}
else {
  Write-Host "Installing Microsoft Teams"
  Install-Module MicrosoftTeams -Force
}

Import-Module MicrosoftTeams
Connect-MicrosoftTeams
Get-Team -User $email | Select-Object GroupID, DisplayName | Export-CSV -path ./teams.csv -NoTypeInformation
