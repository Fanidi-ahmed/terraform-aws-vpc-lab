# 🚀 Terraform AWS VPC + EC2 + Boto3 Lab

Projet DevOps complet permettant de :

- Créer une infrastructure AWS avec Terraform
- Déployer une instance EC2 automatiquement configurée
- Accéder en SSH
- Copier des fichiers sur la machine
- Exposer un serveur web
- Interroger l’infrastructure avec boto3
- Versionner le projet avec GitHub

---

## 🎯 Objectif

Ce projet a pour but de maîtriser les fondamentaux du cloud et du DevOps :

- Infrastructure as Code (Terraform)
- Administration Linux (SSH, SCP)
- Automatisation AWS (boto3)
- Bonnes pratiques Git / GitHub

---

## 🧱 Architecture


AWS
└── VPC
├── Subnet public
│ └── EC2 (Amazon Linux)
│ ├── Apache installé automatiquement
│ ├── Accès SSH (clé)
│ └── Fichiers copiés via SCP
├── Internet Gateway
└── Route Table


---

## 📁 Structure du projet


terraform-aws-vpc-lab/
├── README.md
├── .gitignore
├── provider.tf
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
├── app-info.txt
├── boto3/
│ ├── ec2_info.py
│ └── requirements.txt
└── terraform-key.pem (NON versionné)


---

## ⚙️ Technologies utilisées

- Terraform
- AWS (EC2, VPC, Networking)
- Python (boto3)
- Linux (SSH, SCP)
- Git / GitHub

---

## 🚀 Déploiement

### 1. Initialisation

```bash
terraform init
2. Vérification
terraform validate
terraform plan
3. Déploiement
terraform apply
🌐 Accès à l’instance
Récupérer l’IP
terraform output ec2_public_ip
SSH
ssh -i ./terraform-key.pem ec2-user@$(terraform output -raw ec2_public_ip)
📦 Copie de fichier vers EC2
scp -i ./terraform-key.pem app-info.txt ec2-user@$(terraform output -raw ec2_public_ip):/home/ec2-user/
🌍 Accès web
curl http://$(terraform output -raw ec2_public_ip)

Exemple de résultat :

Hello from Terraform EC2
🐍 Script Boto3
Installation
pip install -r boto3/requirements.txt
Exécution
python3 boto3/ec2_info.py
Fonctionnalités
Liste les instances EC2
Affiche :
ID
état
IP publique
IP privée
key pair
Teste automatiquement l’accès HTTP
🔐 Sécurité
Clé SSH non versionnée (.pem dans .gitignore)
Accès SSH ouvert (lab uniquement)
Recommandations production :
limiter SSH à ton IP
utiliser AWS SSM au lieu de SSH
utiliser des rôles IAM
⚠️ Bonnes pratiques Terraform
Utilisation de variables (variables.tf)
Centralisation des tags (locals)
Outputs pour récupérer les infos dynamiques
Utilisation d’une AMI dynamique (data source)
🧹 Nettoyage
terraform destroy

⚠️ Important pour éviter les coûts AWS.

🧠 Concepts appris
VPC / Subnet / Routing
EC2 provisioning
user_data (bootstrap automatique)
SSH / SCP
Infrastructure as Code
Automatisation AWS avec boto3
Gestion d’un projet DevOps complet
🚀 Améliorations possibles
Elastic IP (IP fixe)
SSH limité à une IP
Accès via AWS SSM (sans clé)
Terraform modules
CI/CD avec GitHub Actions
Scanner AWS avancé avec boto3
👨‍💻 Auteur

Projet réalisé dans un objectif d’apprentissage avancé DevOps / Cloud AWS / Automatisation.

