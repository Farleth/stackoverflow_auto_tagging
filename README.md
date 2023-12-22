# stackoverflow_auto_tagging

Créer un .env avec l'url de Fast Api Locale:
```
API_URL = 'http://localhost:PORT_FASTAPI_LOCAL/'
```

Construire les image docker:
```
docker build -f Dockerfile -t streamtag:1.0 .
```
```
docker build -f Dockerfile_api -t apitag:1.0 .
```

Pour accéder à l'UI MLFLOW:
```
mlflow ui
```
[Doc Tech](Doc_technique.pdf)
