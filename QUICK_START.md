# ⚡ Guide de Démarrage Rapide

**Commencez l'extraction bancaire IA en 5 minutes !**

## 🚀 Installation Express

```bash
# 1. Cloner et naviguer
git clone https://github.com/votre-repo/ai-bank-skyvern-poc.git
cd ai-bank-skyvern-poc

# 2. Environnement virtuel
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# 3. Installer dépendances
pip install -r requirements.txt

# 4. Configuration
cp .env.example .env
# Éditer .env avec votre clé API Skyvern
```

## 🔑 Configuration Minimale

Dans le fichier `.env` :
```properties
# OBLIGATOIRE - Obtenir sur app.skyvern.com
SKYVERN_API_KEY='votre_cle_api_ici'

# ParaBank (déjà configuré)
TARGET_URL=https://parabank.parasoft.com/parabank/index.htm
USERNAME='MedDhia'
PASSWORD='MedDhia123'
```

## ⚡ Tests Rapides

### Test 1 : Validation Setup (30 secondes)
```bash
python simple_test.py
```
**Attend** : ✅ Liste de 16 comptes bancaires

### Test 2 : Extraction Complète (5 minutes)
```bash
python enhanced_extractor.py
```
**Attend** : ✅ Détails compte + 9 transactions

## 📊 Résultats Attendus

### Simple Test
```json
{
  "accounts_summary": [
    {"account_number": "12345", "balance": "-$3400.00"},
    {"account_number": "12456", "balance": "-$189.55"},
    // ... 14 autres comptes
  ],
  "login_success": true,
  "page_title": "Accounts Overview"
}
```

### Extraction Complète
```json
{
  "account_details": {
    "account_number": "12345",
    "account_type": "CHECKING", 
    "balance": "-$3400.00"
  },
  "transactions": [
    {
      "date": "12-10-2024",
      "description": "Check # 1111",
      "amount": "+$300.00"
    }
    // ... 8 autres transactions
  ]
}
```

## 🔧 Résolution Problèmes Express

| Erreur | Solution Rapide |
|--------|-----------------|
| `No module named 'skyvern'` | Activer `.venv` puis `pip install skyvern` |
| `Insufficient credit balance` | Ajouter crédits sur [app.skyvern.com/billing](https://app.skyvern.com/billing) |
| `SKYVERN_API_KEY not found` | Vérifier `.env` - clé doit commencer par `eyJ` |
| `Simple test YAML not found` | Fichier manquant - télécharger repository complet |

## 🎯 Prochaines Étapes

1. **✅ Tests réussis ?** → Lire [README.md](README.md) complet
2. **🔍 Comprendre le code ?** → Consulter [TECHNICAL_GUIDE.md](TECHNICAL_GUIDE.md)
3. **🚀 Personnaliser ?** → Modifier `recipes/enhanced_bank_extraction.yaml`
4. **📊 Analyser données ?** → Examiner fichiers `outputs/*.json`

## 💡 Commandes Utiles

```bash
# Test détection automatique comptes
python test_dynamic_detection.py

# Extraction compte spécifique
python -c "
from enhanced_extractor import EnhancedBankExtractor
import asyncio
async def main():
    extractor = EnhancedBankExtractor()
    result = await extractor.extract_account_details_and_transactions('12567')
    print(f'Compte {result[\"target_account\"]} traité avec succès!')
asyncio.run(main())
"

# Vérifier structure projet
find . -name "*.py" -o -name "*.yaml" -o -name "*.json" | head -10
```

---

**🎉 Vous êtes prêt ! En cas de problème, consultez la documentation complète.**
