# ⚡ Quick Start Guide

**Start AI banking extraction in 5 minutes!**

## 🚀 Express Installation

```bash
# 1. Clone and navigate
git clone https://github.com/your-repo/ai-bank-skyvern-poc.git
cd ai-bank-skyvern-poc

# 2. Virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configuration
cp .env.example .env
# Edit .env with your Skyvern API key
```

## 🔑 Minimal Configuration

In the `.env` file:
```properties
# REQUIRED - Get from app.skyvern.com
SKYVERN_API_KEY='your_api_key_here'

# ParaBank (already configured)
TARGET_URL=https://parabank.parasoft.com/parabank/index.htm
USERNAME='MedDhia'
PASSWORD='MedDhia123'
```

## ⚡ Quick Tests

### Test 1: Setup Validation (30 seconds)
```bash
python simple_test.py
```
**Expected**: ✅ List of 16 bank accounts

### Test 2: Complete Extraction (5 minutes)
```bash
python enhanced_extractor.py
```
**Expected**: ✅ Account details + 9 transactions

## 📊 Expected Results

### Simple Test
```json
{
  "accounts_summary": [
    {"account_number": "12345", "balance": "-$3400.00"},
    {"account_number": "12456", "balance": "-$189.55"},
    // ... 14 other accounts
  ],
  "login_success": true,
  "page_title": "Accounts Overview"
}
```

### Complete Extraction
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
    // ... 8 other transactions
  ]
}
```

## 🔧 Express Troubleshooting

| Error | Quick Solution |
|-------|----------------|
| `No module named 'skyvern'` | Activate `.venv` then `pip install skyvern` |
| `Insufficient credit balance` | Add credits on [app.skyvern.com/billing](https://app.skyvern.com/billing) |
| `SKYVERN_API_KEY not found` | Check `.env` - key must start with `eyJ` |
| `Simple test YAML not found` | Missing file - download complete repository |

## 🎯 Next Steps

1. **✅ Tests successful?** → Read complete [README.md](README.md)
2. **🔍 Understand the code?** → Check [TECHNICAL_GUIDE.md](TECHNICAL_GUIDE.md)
3. **🚀 Customize?** → Modify `recipes/enhanced_bank_extraction.yaml`
4. **📊 Analyze data?** → Examine `outputs/*.json` files

## 💡 Useful Commands

```bash
# Test automatic account detection
python test_dynamic_detection.py

# Extract specific account
python -c "
from enhanced_extractor import EnhancedBankExtractor
import asyncio
async def main():
    extractor = EnhancedBankExtractor()
    result = await extractor.extract_account_details_and_transactions('12567')
    print(f'Account {result[\"target_account\"]} processed successfully!')
asyncio.run(main())
"

# Check project structure
find . -name "*.py" -o -name "*.yaml" -o -name "*.json" | head -10
```

---

**🎉 You're ready! In case of problems, check the complete documentation.**
