param(
[string]$email
)

if (!(Test-Path $Profile)) {
  New-Item -Type file -Path $Profile -Force
}

if (Get-Module -ListAvailable -Name MicrosoftTeams) {
  Write-Host "MicrosoftTeams Module alread installed"
}
else {
  Write-Host "Installing Microsoft Teams"
  Install-Module MicrosoftTeams –Repository PSGallery -Force
}