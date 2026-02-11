# 🛡️ TD-03 : Gestionnaire de Chiffrement & Exfiltration (Lab Cyber)

Ce programme est un outil de simulation pédagogique conçu pour démontrer les mécanismes de gestion de dépendances, de génération de clés sécurisées, de transfert SFTP et de chiffrement récursif sur système Linux.

---

## 📋 Sommaire
- [Fonctionnalités](#-fonctionnalités)
- [Structure du Projet](#-structure-du-projet)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Conformité TD](#-conformité-td)

---

## ✨ Fonctionnalités

### 🏗️ Partie A : Bootstrapping
- Vérification automatique de la version de Python (3.8+).
- **Auto-réparation** : Installation automatisée des paquets système (`apt`) et des bibliothèques Python (`pip`) si l'environnement est vierge.

### 🎮 Partie B : Menu Interactif
- Menu textuel structuré permettant de naviguer entre les différentes phases du lab.
- Gestion robuste des erreurs de saisie et validation des chemins.

### 🔑 Partie C : Cryptographie
- Utilisation de l'algorithme **AES-128/256** (Fernet).
- **Stockage sécurisé** : Les clés sont enregistrées dans `/var/keys/` avec des permissions restreintes (`chmod 600`), les rendant inaccessibles aux utilisateurs non-root.



### 🚀 Partie D : Transfert SFTP
- Exfiltration de la clé vers un serveur distant via le protocole SSH/SFTP.
- **Sécurité** : Saisie masquée du mot de passe (via `getpass`).

### 🔒 Partie E & F : Chiffrement In-Place
- Sélection de fichiers uniques ou de répertoires entiers.
- **Récursivité** : Traitement automatique de tous les sous-dossiers.
- **Interface** : Barre de progression `tqdm` pour le suivi en temps réel.

---

## 📂 Structure du Projet

```text
.
├── main.py              # Script principal (contenant les parties A à F)
├── README.md            # Documentation technique
└── .gitignore           # Exclusion des clés et caches

```
## 🚀 Installation

Le script est conçu pour être totalement autonome. Pour le déployer sur un serveur Ubuntu :

### 1. Création du fichier
Utilisez un éditeur de texte (comme `nano`) pour créer le script :
```bash
nano main.py
```
# Collez le code source du script ici, puis faites CTRL+O (sauvegarder) et CTRL+X (quitter)

### 2. Exécution
Le script doit impérativement être lancé avec les privilèges **sudo** pour pouvoir créer le répertoire sécurisé `/var/keys/` et installer les dépendances système si nécessaire :

```bash
sudo python3 main.py
```
