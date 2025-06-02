# General

1. We can initialize a new function by running `func init`. This will create a sceleton for the function
2. We can create a new function by running `func new`

# Running

Change into the root directory

1. In root directory run: `func extensions install`
2. Make sure to add storage account connection string to `AzureWebJobsStorage`
3. Add the `connection` entry to blob output binding in `function.json`
4. Go to `package.json` and:
    - change `"main": "<path-to>/index.js"`
    - run: `func start --verbose`
    - call local function url to trigger HTTPS
