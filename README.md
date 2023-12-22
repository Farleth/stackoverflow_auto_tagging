# stackoverflow_auto_tagging

Créer un .env avec :
- API_URL = 'VOTRE_URL'

Construire les image docker:
docker build -f Dockerfile -t streamtag:1.0 .
docker build -f Dockerfile_api -t apitag:1.0 .
