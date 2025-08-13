\# TrainTime for Home Assistant



\[!\[hacs]\[hacsbadge]]\[hacs]



TrainTime est une intégration Home Assistant qui permet de suivre les prochains trains depuis une gare spécifique en utilisant l'API SNCF.



\## Fonctionnalités



\- Configurable via l'interface (config\_flow) :

&nbsp; - Clé API SNCF

&nbsp; - Gare à suivre

&nbsp; - Intervalle d’actualisation (5 à 10 min)

&nbsp; - Plage horaire d’actualisation (ex. 6h → 22h)

&nbsp; - Nombre de trains à afficher (3 à 5)

\- Création automatique d’un sensor avec les prochains trains

\- Carte Lovelace personnalisée optionnelle (`traintime-card.js`)

\- Stocke tous les trains dans les attributs pour usage avancé



\## Installation



\### Via HACS

1\. Ajoutez votre dépôt GitHub `Mick-Lab59/traintime` comme dépôt personnalisé.

2\. Installez l’intégration depuis HACS → Intégrations.

3\. Redémarrez Home Assistant.



\### Manuellement

1\. Copiez le dossier `traintime` dans `config/custom\_components/`.

2\. Redémarrez Home Assistant.

3\. Ajoutez l’intégration via \*\*Ajouter une intégration → TrainTime\*\*.



\## Configuration



\- API key : votre clé API SNCF

\- Station name : code ou nom de la gare

\- Update interval : 5–10 minutes

\- Active hours : plage horaire pour récupérer les trains

\- Max trains : nombre de trains affichés (3–5)



\## Carte Lovelace



Pour afficher la carte personnalisée, ajoutez le fichier `traintime-card.js` dans `config/www/traintime/` et déclarez-le comme ressource :  



```yaml

resources:

&nbsp; - url: /local/traintime/traintime-card.js

&nbsp;   type: module



