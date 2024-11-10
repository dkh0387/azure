# azure

Some exam preparation resources for Azure certification

## Installing of powershell and connecting to azure account

- Install PowerShell: `brew upgrade powershell/tap/powershell`
- Look up for the installed version: `$PSVersionTable.PSVersion`
- Install azure CLI: `Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force`
- Look up for installed version: `Get-Module -Name Az -ListAvailable`
- Connect to azure account: `Connect-AzAccount`
