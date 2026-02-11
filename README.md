# 🛡️ TD-03 : Gestionnaire de Chiffrement & Exfiltration (Lab Cyber)

Ce programme est un outil de simulation pédagogique conçu pour démontrer les mécanismes de gestion de dépendances, de génération de clés sécurisées, de transfert SFTP et de chiffrement récursif sur un système Linux.

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
- **Stockage sécurisé** : Les clés sont enregistrées dans `/var/keys/` avec des permissions restreintes. (`chmod 600`).

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
# Collez le code source du script ici.

### 2. Exécution
Le script doit impérativement être lancé avec les privilèges **sudo** pour pouvoir créer le répertoire sécurisé `/var/keys/` et installer les dépendances système / librairies Python si nécessaire :

```bash
sudo python3 main.py
```
## 🛠️ Utilisation

* **Génération (Option 1)** : Créez une clé de chiffrement. Elle sera générée selon l'algorithme choisi et protégée par des permissions restrictives au niveau du système de fichiers.
* **Exfiltration (Option 2)** : Transférez la clé sur votre machine via le protocole SFTP. Demande une saisie de votre adresse IP, utilisateur et mot de passe ubuntu et le port 22 d'ouvert (SSH).
* **Chiffrement (Option 3)** : Indiquez le chemin d'un fichier ou d'un dossier. Le script effectuera un chiffrement des fichiers ou dossiers concernés.

---

## ✅ Conformité TD

| Partie | Libellé | État |
| :--- | :--- | :--- |
| **A** | Vérification Dépendances & Auto-install | 🆗 Validé |
| **B** | Menu Principal Interactif | 🆗 Validé |
| **C** | Génération Clés & Permissions `/var/keys/` | 🆗 Validé |
| **D** | Transfert SFTP (Identifiants masqués) | 🆗 Validé |
| **E** | Sélection Fichiers/Dossiers & Chiffrement In-Place | 🆗 Validé |
| **F** | Récursivité & Barre de Progression | 🆗 Validé |

---

## ⚠️ Avertissement

Ce projet est réalisé dans un cadre **strictement pédagogique**. L'objectif est de comprendre les méthodes de défense en analysant les vecteurs d'attaque. L'auteur décline toute responsabilité en cas d'usage inapproprié ou malveillant du code fourni.
