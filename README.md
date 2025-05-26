# Azure

Some exam preparation resources for Azure certification

## Installing of PowerShell and connecting to an azure account

- Install PowerShell: `brew upgrade powershell/tap/powershell`
- Look up for the installed version: `$PSVersionTable.PSVersion`
- Install azure CLI: `Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force`
- Look up for an installed version: `Get-Module -Name Az -ListAvailable`
- Connect to an azure account: `Connect-AzAccount`
