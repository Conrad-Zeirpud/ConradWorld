# Utiliser une image de base officielle Node.js
FROM node:22

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 1 : Construction de l'application Vue.js
FROM node:16-alpine AS build

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier package.json et package-lock.json
COPY package*.json ./

# Installer les dépendances de l'application
RUN npm install

# Copier tout le reste du code source de l'application
COPY . .

# Compiler l'application Vue.js pour la production
RUN npm run build

# Étape 2 : Utiliser Nginx pour servir l'application
FROM nginx:alpine

# Copier les fichiers de construction de l'application depuis l'étape précédente
COPY --from=build /app/dist /usr/share/nginx/html

# Copier le fichier de configuration Nginx personnalisé
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exposer le port 80 pour le serveur web
EXPOSE 80

# Démarrer Nginx lorsque le conteneur démarre
CMD ["nginx", "-g", "daemon off;"]

