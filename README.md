# 🏦 AI Bank Data Extraction POC

**Proof of Concept d'automatisation bancaire alimenté par l'IA avec Skyvern**

Un système intelligent d'extraction de données bancaires qui utilise Skyvern pour automatiser la navigation web et extraire des informations financières réelles de ParaBank.

## 📋 Table des Matières

- [🎯 Vue d'ensemble](#vue-densemble)
- [✨ Fonctionnalités](#fonctionnalités)
- [🔧 Installation](#installation)
- [⚙️ Configuration](#configuration)
- [🚀 Utilisation](#utilisation)
- [📁 Structure du Projet](#structure-du-projet)
- [🧪 Tests](#tests)
- [📊 Résultats](#résultats)
- [🔍 Dépannage](#dépannage)
- [📚 Références](#références)

## 🎯 Vue d'ensemble

Ce projet démontre l'utilisation de **Skyvern** (plateforme d'automatisation web alimentée par l'IA) pour extraire automatiquement des données bancaires réelles à partir de **ParaBank**, un site de démonstration bancaire.

## 🎬 Démonstration Vidéo

https://github.com/user-attachments/assets/votre-video-id-ici

> 📹 **La vidéo montre** : Navigation automatique sur ParaBank, extraction de comptes réels, et récupération des transactions en temps réel avec Skyvern AI.

**🎥 Ce que vous verrez dans la démo :**
- ✅ Interface Skyvern en action avec votre workflow
- ✅ Login automatique sur ParaBank via l'IA
- ✅ Navigation intelligente entre les pages bancaires
- ✅ Extraction de données en temps réel sans intervention humaine
- ✅ Résultats structurés JSON générés automatiquement

---

### 🎭 Problème Résolu

- **Défi** : Extraire automatiquement des données bancaires complexes (comptes, transactions, investissements)
- **Solution** : Utilisation de Skyvern pour une navigation web intelligente et une extraction de données structurées
- **Innovation** : Détection dynamique des comptes et gestion intelligente des erreurs

### 🏆 Résultats Obtenus

- ✅ **16 comptes bancaires** extraits avec détails complets
- ✅ **Historique des transactions** avec 9 transactions réelles
- ✅ **Navigation intelligente** sans boucles infinies
- ✅ **Détection automatique** du premier compte disponible

## ✨ Fonctionnalités

### 🔍 Extraction Simple
- **Test rapide** avec utilisation minimale de crédits
- **Vue d'ensemble** de tous les comptes disponibles
- **Validation** de l'API et des credentials

### 🔥 Extraction Avancée
- **Détails complets** des comptes (type, solde, statut)
- **Historique des transactions** avec dates, montants, références
- **Navigation systématique** à travers les pages de détails
- **Retour intelligent** à la page d'aperçu

### 🎯 Détection Dynamique
- **Auto-détection** du premier compte disponible
- **Fallback intelligent** avec comptes multiples
- **Gestion d'erreurs** robuste pour les limitations d'API

### 🛡️ Fonctionnalités Avancées
- **Schémas Pydantic** pour validation des données
- **Gestion des interventions** humaines (2FA, CAPTCHA)
- **Export JSON** structuré des résultats
- **Logging détaillé** pour débogage

## 🔧 Installation

### Prérequis
- **Python 3.8+**
- **Compte Skyvern** avec API key
- **Git** (optionnel)

### 1. Cloner le Projet
```bash
git clone https://github.com/votre-username/ai-bank-skyvern-poc.git
cd ai-bank-skyvern-poc
```

### 2. Créer un Environnement Virtuel
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Installer les Dépendances
```bash
pip install -r requirements.txt
```

### 4. Vérifier l'Installation
```bash
python -c "import skyvern; print('✅ Skyvern installé avec succès')"
```

## ⚙️ Configuration

### 1. Obtenir une Clé API Skyvern

1. **Créer un compte** : [app.skyvern.com](https://app.skyvern.com)
2. **Naviguer vers** : Settings → API Keys
3. **Générer** une nouvelle clé API
4. **Ajouter des crédits** : Billing → Add Credits

### 2. Configuration de l'Environnement

Copier le fichier d'exemple et le configurer :
```bash
cp .env.example .env
```

Modifier le fichier `.env` :
```properties
# Configuration Bancaire
TARGET_URL=https://parabank.parasoft.com/parabank/index.htm
USERNAME='MedDhia'
PASSWORD='MedDhia123'

# Clé API Skyvern (OBLIGATOIRE)
SKYVERN_API_KEY='votre_cle_api_skyvern_ici'

# Configuration LLM (Optionnel)
ENABLE_OPENAI=true
OPENAI_API_KEY=votre_cle_openai_ici
```

### 3. Validation de la Configuration

Tester la configuration :
```bash
python simple_test.py
```

**Sortie attendue** :
```
✅ Skyvern imported successfully
🎯 AI Banking Automation POC - REAL DATA EXTRACTION
✅ Simple workflow created: wpid_xxxxx
✅ SIMPLE TEST COMPLETED!
   Status: completed
   Accounts: 16
```

## 🚀 Utilisation

### 🧪 Test Simple (Recommandé en premier)

Extraction rapide de la vue d'ensemble des comptes :
```bash
python simple_test.py
```

**Utilise** : Crédits minimaux  
**Extrait** : Liste de tous les comptes avec balances  
**Durée** : ~30 secondes  

### 🔥 Extraction Avancée

Extraction complète d'un compte spécifique :
```bash
python enhanced_extractor.py
```

**Utilise** : Plus de crédits  
**Extrait** : Détails complets + transactions  
**Durée** : ~5-10 minutes  

### 🎯 Extraction avec Compte Spécifique

```python
from enhanced_extractor import EnhancedBankExtractor

extractor = EnhancedBankExtractor()

# Auto-détection du premier compte
result = await extractor.extract_account_details_and_transactions()

# Compte spécifique
result = await extractor.extract_account_details_and_transactions("12567")
```

### 🔄 Extraction Multi-Comptes

```python
# Traiter plusieurs comptes
accounts = ["12345", "12456", "12567"]
results = await extractor.extract_multiple_accounts(accounts)
```

## 📁 Structure du Projet

```
ai-bank-skyvern-poc/
├── 📄 README.md                    # Ce fichier
├── 📄 requirements.txt             # Dépendances Python
├── 📄 .env                        # Configuration (à créer)
├── 📄 .env.example                # Exemple de configuration
├── 📄 SKYVERN_API_SETUP.md        # Guide détaillé API
│
├── 🐍 simple_test.py              # Test simple et rapide
├── 🐍 enhanced_extractor.py       # Extracteur avancé principal
├── 🐍 test_dynamic_detection.py   # Tests de détection automatique
│
├── 📂 recipes/                    # Workflows YAML Skyvern
│   └── enhanced_bank_extraction.yaml
│
├── 📂 utils/                      # Utilitaires et schémas
│   └── schemas.py                 # Modèles Pydantic
│
├── 📂 handlers/                   # Gestionnaires spécialisés
│   └── intervention_broker.py     # Gestion interventions humaines
│
├── 📂 outputs/                    # Résultats des extractions
│   └── enhanced_extraction_*.json
│
└── 📂 .venv/                      # Environnement virtuel Python
```

### 🔑 Fichiers Clés

| Fichier | Description | Usage |
|---------|-------------|-------|
| `simple_test.py` | Test rapide avec crédits minimaux | Premier test, validation setup |
| `enhanced_extractor.py` | Extracteur principal avec détails complets | Extraction de production |
| `recipes/enhanced_bank_extraction.yaml` | Workflow Skyvern pour extraction | Configuration navigation IA |
| `utils/schemas.py` | Modèles de données Pydantic | Validation et structure données |

## 🧪 Tests

### Test de Validation Rapide
```bash
python simple_test.py
```
**Vérifie** : API key, connexion, comptes disponibles

### Test de Détection Dynamique
```bash
python test_dynamic_detection.py
```
**Vérifie** : Détection automatique premier compte, fallbacks

### Test d'Extraction Complète
```bash
python enhanced_extractor.py
```
**Vérifie** : Extraction détaillée avec transactions

## 📊 Résultats

### 📈 Données Extraites Réelles

**Comptes ParaBank Extraits** :
```json
{
  "accounts": [
    {"account_number": "12345", "balance": "-$3400.00", "type": "CHECKING"},
    {"account_number": "12456", "balance": "-$189.55", "type": "CHECKING"},
    {"account_number": "12567", "balance": "$100.00", "type": "SAVINGS"},
    // ... 13 autres comptes
  ]
}
```

**Transactions Réelles Extraites** :
```json
{
  "transactions": [
    {
      "date": "12-10-2024",
      "description": "Check # 1111",
      "amount": "+$300.00",
      "reference_number": "12145"
    },
    {
      "date": "08-18-2025",
      "description": "Funds Transfer Sent",
      "amount": "-$1000.00",
      "reference_number": "12589"
    }
    // ... 7 autres transactions
  ]
}
```

### 📊 Métriques de Performance

| Métrique | Valeur | Notes |
|----------|--------|-------|
| **Comptes extraits** | 16 | Tous les comptes disponibles |
| **Transactions extraites** | 9 | Période 10 mois |
| **Taux de réussite** | 100% | Avec crédits suffisants |
| **Temps d'exécution** | 5-10 min | Extraction complète |
| **Précision des données** | 100% | Données réelles ParaBank |

## 🔍 Dépannage

### ❌ Erreurs Communes

#### 1. `No module named 'skyvern'`
**Solution** :
```bash
# Activer l'environnement virtuel
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Réinstaller
pip install skyvern
```

#### 2. `Insufficient credit balance`
**Cause** : Pas assez de crédits Skyvern  
**Solution** :
1. Aller sur [app.skyvern.com/billing](https://app.skyvern.com/billing)
2. Ajouter des crédits à votre compte
3. Utiliser `simple_test.py` pour tester avec moins de crédits

#### 3. `SKYVERN_API_KEY not found`
**Cause** : Clé API manquante ou incorrecte  
**Solution** :
1. Vérifier le fichier `.env`
2. S'assurer que la clé commence par `eyJ...`
3. Pas d'espaces ou de guillemets supplémentaires

#### 4. `Simple test YAML not found`
**Cause** : Fichier de workflow manquant  
**Solution** :
```bash
# Vérifier la présence des fichiers
ls recipes/
# Doit contenir : enhanced_bank_extraction.yaml
```

### 🔧 Débogage Avancé

#### Logs Détaillés
Activer les logs détaillés :
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Test de Connectivité API
```python
from skyvern import Skyvern
client = Skyvern(api_key="votre_cle")
# Si ça fonctionne, l'API est accessible
```

## 📚 Références

### 🛠️ Technologies Utilisées

| Technologie | Version | Usage | Documentation |
|-------------|---------|-------|---------------|
| **Skyvern** | Latest | Automatisation web IA | [docs.skyvern.com](https://docs.skyvern.com) |
| **Python** | 3.8+ | Langage principal | [python.org](https://python.org) |
| **Pydantic** | 2.x | Validation données | [pydantic.dev](https://pydantic.dev) |
| **AsyncIO** | Built-in | Programmation asynchrone | [docs.python.org/asyncio](https://docs.python.org/3/library/asyncio.html) |

### 🌐 Ressources Skyvern

- **Documentation officielle** : [docs.skyvern.com](https://docs.skyvern.com)
- **API Reference** : [api.skyvern.com/docs](https://api.skyvern.com/docs)
- **Communauté Discord** : [discord.gg/skyvern](https://discord.gg/skyvern)
- **GitHub** : [github.com/skyvern-ai/skyvern](https://github.com/skyvern-ai/skyvern)

### 🏦 ParaBank (Site de Test)

- **URL** : [parabank.parasoft.com](https://parabank.parasoft.com/parabank/index.htm)
- **Credentials de test** : `MedDhia` / `MedDhia123`
- **Documentation** : [Parasoft ParaBank](https://parabank.parasoft.com/parabank/about.htm)

### 🧠 Concepts IA et Automatisation

- **Web Scraping avec IA** : [Introduction](https://www.scrapehero.com/web-scraping-with-ai/)
- **Automatisation bancaire** : [Banking Automation](https://www.finextra.com/blogposting/21456/the-future-of-banking-automation)
- **Pydantic pour validation** : [Real Python Guide](https://realpython.com/python-pydantic/)

## 🤝 Contribution

### 🔄 Améliorations Futures

- [ ] **Support multi-banques** (Chase, Bank of America, etc.)
- [ ] **Interface graphique** avec Streamlit
- [ ] **Planification automatique** avec cron jobs
- [ ] **Export vers Excel/CSV**
- [ ] **Alertes par email** pour anomalies
- [ ] **Intégration base de données**

### 🐛 Signaler des Bugs

1. **Vérifier** les problèmes existants
2. **Créer** une issue détaillée
3. **Inclure** logs et configuration (sans API keys!)

### 💡 Proposer des Améliorations

1. **Fork** le repository
2. **Créer** une branche feature
3. **Implémenter** l'amélioration
4. **Tester** thoroughly
5. **Créer** une pull request

## 📄 Licence

Ce projet est à des fins éducatives et de démonstration. Respectez les conditions d'utilisation de Skyvern et ParaBank.

## 🙏 Remerciements

- **Skyvern Team** pour la plateforme d'automatisation IA
- **Parasoft** pour ParaBank, excellent environnement de test
- **Communauté Python** pour les outils et bibliothèques

---

**🎯 Créé par [MedDhia] - Septembre 2025**

*POC d'automatisation bancaire avec intelligence artificielle*
