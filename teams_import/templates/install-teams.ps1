param(
  [string]$email,
  [string]$teamsFileOutputPath
)

if ( Get-Module -ListAvailable -Name MicrosoftTeams ) {
  Write-Host "MicrosoftTeams Module alread installed"
}
else { 
Write-Host "Installing Microsoft Teams"
Install-Module -Name MicrosoftTeams -Force
# Install-Module -Name Az -AllowClobber -Force
}

Import-Module MicrosoftTeams
# Import-Module Az

# Write-Host "Connecting to Azure"
# $context = Connect-AzAccount -ContextName TeamsImport -Scope Process
# Save-AzContext -Path $tenantTempOutputPath

# $tenantId = $context.Context.Tenant.Id
# $tenantId = (Get-AzContext).Tenant.Id.trim().Replace([environment]::NewLine , '')

# $tenantId | Out-File -FilePath $tenantTempOutputPath

# Write-Output "test"
# $test2 = "<>" + $tenantId.Replace([environment]::NewLine , '') + "<>"
# Write-Output $test2
# Write-Host "Connecting to Teams"



# Write-Host "Connected to Teams"
Connect-MicrosoftTeams
Get-Team -User $email | Select-Object GroupID, DisplayName | Export-CSV -path $teamsFileOutputPath -NoTypeInformation