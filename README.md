🛡️ TD-03 : Gestionnaire de Chiffrement & Exfiltration (Lab Cyber)
Ce programme est un outil de simulation pédagogique (Ransomware Lab) conçu pour démontrer les mécanismes de génération de clés, de transfert sécurisé via SFTP et de chiffrement récursif de fichiers sur un système Linux (Ubuntu).

📋 Sommaire
Fonctionnalités

Structure du Projet

Installation

Utilisation

Sécurité

✨ Fonctionnalités
Partie A : Bootstrapping & Dépendances
Vérification automatique de la version de Python (3.8+ requis).

Détection et installation automatisée des bibliothèques (cryptography, paramiko, tqdm) via apt ou pip.

Partie B : Interface Utilisateur
Menu textuel interactif et robuste.

Validation des saisies utilisateur et gestion propre des erreurs.

Partie C : Cryptographie
Support de l'algorithme AES-128/256 (via Fernet).

Stockage sécurisé des clés dans /var/keys/ avec permissions restreintes (chmod 600).

Partie D : Exfiltration SFTP
Transfert de la clé vers un serveur distant.

Authentification sécurisée (identifiants masqués lors de la saisie).

Partie E & F : Chiffrement Avancé
Chiffrement In-Place (remplacement direct des fichiers).

Mode récursif pour traiter des arborescences complètes.

Barre de progression visuelle pour le suivi des opérations.

📂 Structure du Projet
Plaintext
.
├── main.py              # Script principal (Interface & Logique)
├── README.md            # Documentation du programme
└── keys/                # Dossier local (si /var/keys/ est inaccessible)
🚀 Installation
Le programme est conçu pour être autonome. Sur une machine Ubuntu vierge, il suffit de cloner le script et de l'exécuter.

Bash
# Télécharger le script (exemple)
git clone https://github.com/votre-compte/td03-ransom-lab.git
cd td03-ransom-lab

# Lancer le script avec les droits root (requis pour /var/keys)
sudo python3 main.py
🛠️ Utilisation
1. Génération de Clé
Sélectionnez l'option 1. Le script créera une clé sécurisée. Sous Linux, elle sera protégée contre la lecture par d'autres utilisateurs.

2. Transfert SFTP
Sélectionnez l'option 2. Vous devrez fournir :

L'adresse IP du serveur de réception.

Votre identifiant et mot de passe (ce dernier ne s'affichera pas à l'écran).

Le chemin absolu de destination sur le serveur distant.

3. Chiffrement
Sélectionnez l'option 3.

Fichier : Entrez le chemin complet (ex: /home/ubuntu/important.txt).

Dossier : Entrez le chemin du dossier (ex: /home/ubuntu/data/). Tous les fichiers à l'intérieur seront chiffrés récursivement.

🔒 Sécurité
[!IMPORTANT] Ce programme est à usage strictement pédagogique.

Aucun mot de passe n'est stocké en clair dans le code source.

Permissions système : L'utilisation de /var/keys/ garantit que la clé de déchiffrement n'est accessible que par l'utilisateur root.

Validation des chemins : Le script convertit automatiquement les chemins Windows (\) en syntaxe Linux (/) pour éviter les erreurs de saisie.

⚖️ Licence
Ce projet est réalisé dans le cadre d'un Travail Dirigé (TD) en cybersécurité.

Une dernière chose à faire pour ton dépôt GitHub :
