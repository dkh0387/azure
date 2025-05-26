### 1. Azure Container Registry log in:

`docker login az04acr130525.azurecr.io`

### 2. Build image:

`docker build -t az204javawebappdemo-image .`

### 3. Tag image:

`docker tag az204javawebappdemo-image az04acr130525.azurecr.io/az204javawebappdemo-image`

### 4. Push image:

`docker push az04acr130525.azurecr.io/az204javawebappdemo-image`