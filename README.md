# 🏦 AI Bank Data Extraction POC

**AI-Powered Banking Automation Proof of Concept with Skyvern**

An intelligent banking data extraction system that uses Skyvern to automate web navigation and extract real financial information from ParaBank.

## 📋 Table of Contents

- [🎯 Overview](#overview)
- [✨ Features](#features)
- [🔧 Installation](#installation)
- [⚙️ Configuration](#configuration)
- [🚀 Usage](#usage)
- [📁 Project Structure](#project-structure)
- [🧪 Tests](#tests)
- [📊 Results](#results)
- [🔍 Troubleshooting](#troubleshooting)
- [📚 References](#references)

## 🎯 Overview

This project demonstrates the use of **Skyvern** (AI-powered web automation platform) to automatically extract real banking data from **ParaBank**, a banking demonstration website.

## 🎬 Demo Video

https://github.com/MedDhiee/AI-Bank-Data-Extraction-POC-with-Skyvern/issues/1#issue-3384704974

> 📹 **The video shows**: Automatic navigation on ParaBank, real account extraction, and transaction retrieval in real-time with Skyvern AI.

**🎥 What you'll see in the demo:**
- ✅ Skyvern interface in action with your workflow
- ✅ Automatic login to ParaBank via AI
- ✅ Intelligent navigation between banking pages
- ✅ Real-time data extraction without human intervention
- ✅ Automatically generated structured JSON results

---

### 🎭 Problem Solved

- **Challenge**: Automatically extract complex banking data (accounts, transactions, investments)
- **Solution**: Using Skyvern for intelligent web navigation and structured data extraction
- **Innovation**: Dynamic account detection and intelligent error handling

### 🏆 Results Achieved

- ✅ **16 bank accounts** extracted with complete details
- ✅ **Transaction history** with 9 real transactions
- ✅ **Intelligent navigation** without infinite loops
- ✅ **Automatic detection** of the first available account

## ✨ Features

### 🔍 Simple Extraction
- **Quick test** with minimal credit usage
- **Overview** of all available accounts
- **Validation** of API and credentials

### 🔥 Advanced Extraction
- **Complete details** of accounts (type, balance, status)
- **Transaction history** with dates, amounts, references
- **Systematic navigation** through detail pages
- **Intelligent return** to overview page

### 🎯 Dynamic Detection
- **Auto-detection** of the first available account
- **Intelligent fallback** with multiple accounts
- **Robust error handling** for API limitations

### 🛡️ Advanced Features
- **Pydantic schemas** for data validation
- **Human intervention** handling (2FA, CAPTCHA)
- **Structured JSON** export of results
- **Detailed logging** for debugging

## 🔧 Installation

### Prerequisites
- **Python 3.8+**
- **Skyvern account** with API key
- **Git** (optional)

### 1. Clone the Project
```bash
git clone https://github.com/your-username/ai-bank-skyvern-poc.git
cd ai-bank-skyvern-poc
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
python -c "import skyvern; print('✅ Skyvern installed successfully')"
```

## ⚙️ Configuration

### 1. Get a Skyvern API Key

1. **Create an account**: [app.skyvern.com](https://app.skyvern.com)
2. **Navigate to**: Settings → API Keys
3. **Generate** a new API key
4. **Add credits**: Billing → Add Credits

### 2. Environment Configuration

Copy the example file and configure it:
```bash
cp .env.example .env
```

Edit the `.env` file:
```properties
# Banking Configuration
TARGET_URL=https://parabank.parasoft.com/parabank/index.htm
USERNAME='MedDhia'
PASSWORD='MedDhia123'

# Skyvern API Key (REQUIRED)
SKYVERN_API_KEY='your_skyvern_api_key_here'

# LLM Configuration (Optional)
ENABLE_OPENAI=true
OPENAI_API_KEY=your_openai_key_here
```

### 3. Configuration Validation

Test the configuration:
```bash
python simple_test.py
```

**Expected output**:
```
✅ Skyvern imported successfully
🎯 AI Banking Automation POC - REAL DATA EXTRACTION
✅ Simple workflow created: wpid_xxxxx
✅ SIMPLE TEST COMPLETED!
   Status: completed
   Accounts: 16
```

## 🚀 Usage

### 🧪 Simple Test (Recommended first)

Quick extraction of account overview:
```bash
python simple_test.py
```

**Uses**: Minimal credits  
**Extracts**: List of all accounts with balances  
**Duration**: ~30 seconds  

### 🔥 Advanced Extraction

Complete extraction of a specific account:
```bash
python enhanced_extractor.py
```

**Uses**: More credits  
**Extracts**: Complete details + transactions  
**Duration**: ~5-10 minutes  

### 🎯 Extraction with Specific Account

```python
from enhanced_extractor import EnhancedBankExtractor

extractor = EnhancedBankExtractor()

# Auto-detection of first account
result = await extractor.extract_account_details_and_transactions()

# Specific account
result = await extractor.extract_account_details_and_transactions("12567")
```

### 🔄 Multi-Account Extraction

```python
# Process multiple accounts
accounts = ["12345", "12456", "12567"]
results = await extractor.extract_multiple_accounts(accounts)
```

## 📁 Project Structure

```
ai-bank-skyvern-poc/
├── 📄 README.md                    # This file
├── 📄 requirements.txt             # Python dependencies
├── 📄 .env                        # Configuration (to create)
├── 📄 .env.example                # Configuration example
├── 📄 SKYVERN_API_SETUP.md        # Detailed API guide
│
├── 🐍 simple_test.py              # Simple and quick test
├── 🐍 enhanced_extractor.py       # Main advanced extractor
├── 🐍 test_dynamic_detection.py   # Automatic detection tests
│
├── 📂 recipes/                    # Skyvern YAML workflows
│   └── enhanced_bank_extraction.yaml
│
├── 📂 utils/                      # Utilities and schemas
│   └── schemas.py                 # Pydantic models
│
├── 📂 handlers/                   # Specialized handlers
│   └── intervention_broker.py     # Human intervention management
│
├── 📂 outputs/                    # Extraction results
│   └── enhanced_extraction_*.json
│
└── 📂 .venv/                      # Python virtual environment
```

### 🔑 Key Files

| File | Description | Usage |
|------|-------------|-------|
| `simple_test.py` | Quick test with minimal credits | First test, setup validation |
| `enhanced_extractor.py` | Main extractor with complete details | Production extraction |
| `recipes/enhanced_bank_extraction.yaml` | Skyvern workflow for extraction | AI navigation configuration |
| `utils/schemas.py` | Pydantic data models | Data validation and structure |

## 🧪 Tests

### Quick Validation Test
```bash
python simple_test.py
```
**Verifies**: API key, connection, available accounts

### Dynamic Detection Test
```bash
python test_dynamic_detection.py
```
**Verifies**: Automatic first account detection, fallbacks

### Complete Extraction Test
```bash
python enhanced_extractor.py
```
**Verifies**: Detailed extraction with transactions

## 📊 Results

### 📈 Real Extracted Data

**ParaBank Accounts Extracted**:
```json
{
  "accounts": [
    {"account_number": "12345", "balance": "-$3400.00", "type": "CHECKING"},
    {"account_number": "12456", "balance": "-$189.55", "type": "CHECKING"},
    {"account_number": "12567", "balance": "$100.00", "type": "SAVINGS"},
    // ... 13 other accounts
  ]
}
```

**Real Transactions Extracted**:
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
    // ... 7 other transactions
  ]
}
```

### 📊 Performance Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **Accounts extracted** | 16 | All available accounts |
| **Transactions extracted** | 9 | 10-month period |
| **Success rate** | 100% | With sufficient credits |
| **Execution time** | 5-10 min | Complete extraction |
| **Data accuracy** | 100% | Real ParaBank data |

## 🔍 Troubleshooting

### ❌ Common Errors

#### 1. `No module named 'skyvern'`
**Solution**:
```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall
pip install skyvern
```

#### 2. `Insufficient credit balance`
**Cause**: Not enough Skyvern credits  
**Solution**:
1. Go to [app.skyvern.com/billing](https://app.skyvern.com/billing)
2. Add credits to your account
3. Use `simple_test.py` to test with fewer credits

#### 3. `SKYVERN_API_KEY not found`
**Cause**: Missing or incorrect API key  
**Solution**:
1. Check the `.env` file
2. Ensure the key starts with `eyJ...`
3. No extra spaces or quotes

#### 4. `Simple test YAML not found`
**Cause**: Missing workflow file  
**Solution**:
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

### 🏦 ParaBank (Test Site)

- **URL**: [parabank.parasoft.com](https://parabank.parasoft.com/parabank/index.htm)
- **Test Credentials**: `MedDhia` / `MedDhia123`
- **Documentation**: [Parasoft ParaBank](https://parabank.parasoft.com/parabank/about.htm)

### 🧠 AI and Automation Concepts

- **AI Web Scraping**: [Introduction](https://www.scrapehero.com/web-scraping-with-ai/)
- **Banking Automation**: [Banking Automation](https://www.finextra.com/blogposting/21456/the-future-of-banking-automation)
- **Pydantic for Validation**: [Real Python Guide](https://realpython.com/python-pydantic/)

## 🤝 Contribution

### 🔄 Future Improvements

- [ ] **Multi-bank support** (Chase, Bank of America, etc.)
- [ ] **Graphical interface** with Streamlit
- [ ] **Automatic scheduling** with cron jobs
- [ ] **Excel/CSV export**
- [ ] **Email alerts** for anomalies
- [ ] **Database integration**

### 🐛 Report Bugs

1. **Check** existing issues
2. **Create** a detailed issue
3. **Include** logs and configuration (without API keys!)

### 💡 Suggest Improvements

1. **Fork** the repository
2. **Create** a feature branch
3. **Implement** the improvement
4. **Test** thoroughly
5. **Create** a pull request

## 📄 License

This project is for educational and demonstration purposes. Please respect Skyvern and ParaBank terms of use.

## 🙏 Acknowledgments

- **Skyvern Team** for the AI automation platform
- **Parasoft** for ParaBank, excellent test environment
- **Python Community** for tools and libraries

---

**🎯 Created by [MedDhia] - September 2025**

*Banking automation POC with artificial intelligence*
