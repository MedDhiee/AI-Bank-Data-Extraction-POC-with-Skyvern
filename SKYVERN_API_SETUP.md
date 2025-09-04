# 🔑 Skyvern API Key Setup Guide

## Current Status
❌ **Your current API key is invalid** (receiving 403 errors)
✅ **POC is working with enhanced mock implementation**

## Step-by-Step Guide to Get Valid API Key from app.skyvern.com

### 1. **Visit Skyvern App**
- Go to: [https://app.skyvern.com/](https://app.skyvern.com/)
- Click "Sign Up" if you don't have an account
- Or "Log In" if you already have one

### 2. **Create Account** (if new user)
- Enter your email address
- Create a secure password
- Verify your email address through the confirmation email
- Complete any onboarding steps or tutorials

### 3. **Access Dashboard & Navigate to Settings--API Keys**
- Log into your Skyvern dashboard at https://app.skyvern.com/
- Look for the navigation menu (on the left sidebar )
- Find and click on Settings:
  
  - **"Settings"** → **"API Keys"**


### 5. **Verify API Key Format**
A valid Skyvern API key from app.skyvern.com should:

- ✅ Start with standard API key prefixes
- ✅ Be approximately 40-150 characters long
- ✅ Not contain obvious formatting errors

### 5. **Update Your Environment**
Once you have a valid API key from app.skyvern.com:

1. **Edit your `.env` file**:
   ```bash
   # Replace the invalid key with your new valid key from app.skyvern.com
   SKYVERN_API_KEY='your_actual_api_key_here'
   ```

2. **Test the connection**:
   ```bash
   cd "C:/Users/meddh/OneDrive/Bureau/ai-bank-skyvern-poc"
   .venv/Scripts/Activate.ps1
   python exhanced_extractor.py
   ```

   You should see:
   ```
   🔑 API key detected: your_key_prefix...
   Connecting to Skyvern Cloud API...
   Created workflow with ID: workflow_xxx
   ```

## Alternative: Local Skyvern Development

If you prefer to run Skyvern locally instead of using the cloud API:

### Option A: Docker (Recommended)
```bash
# Run local Skyvern server
docker run -p 8000:8000 skyvern/skyvern

# Then comment out API key in .env to use local server
# SKYVERN_API_KEY='...'
```

### Option B: Source Installation
```bash
# Clone and setup Skyvern locally
git clone https://github.com/Skyvern-AI/skyvern.git
cd skyvern
# Follow installation instructions in their README
```

## API Key Format Validation

A valid Skyvern API key typically:
- ✅ Starts with standard prefixes
- ✅ Is a single JWT token or API key string
- ✅ Has proper length (usually 40-100+ characters)
- ❌ Should NOT be multiple concatenated tokens

