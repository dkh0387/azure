# Azure

Some exam preparation resources for Azure certification

## Installing of PowerShell and connecting to an azure account

- Install PowerShell: `brew upgrade powershell/tap/powershell`
- Look up for the installed version: `$PSVersionTable.PSVersion`
- Install azure CLI: `Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force`
- Look up for an installed version: `Get-Module -Name Az -ListAvailable`
- Connect to an azure account: `Connect-AzAccount`

## Deploy via GitHub Actions with Service principal in Azure

1. Create:
   `az ad sp create-for-rbac --name "github-actions-deploy" --role contributor \
     --scopes /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP> \
     --sdk-auth
   `
2. Add the secret to GitHub:

    - Settings → Secrets and variables → Actions → New secret
    - Name: AZURE_CREDENTIALS
    - Value: 👉 JSON-Output from 1. (incl. {...})

3. Change GitHub action file:

```
name: Deploy Python Azure Function App

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Log in to Azure
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          cd az204pythonfunctionappdemo
          pip install -r requirements.txt

      - name: Deploy to Azure Function App
        uses: azure/functions-action@v1
        with:
          app-name: az204funcapp20250526
          package: ./az204pythonfunctionappdemo

```