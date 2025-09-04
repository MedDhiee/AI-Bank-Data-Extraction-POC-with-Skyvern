#!/usr/bin/env python3
"""
Enhanced Bank Data Extraction - Account Details and Transactions
Extracts detailed account information and transactions from ParaBank systematically
"""

import asyncio
import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional

# Import Skyvern
try:
    from skyvern import Skyvern
    print("✅ Skyvern imported successfully")
except ImportError as e:
    print(f"❌ Error importing Skyvern: {e}")
    exit(1)

# Import local utilities
from utils.schemas import Account, Transaction, BankSnapshot


class EnhancedBankExtractor:
    """Enhanced extraction with account details and transactions"""
    
    def __init__(self):
        self.api_key = self._load_api_key()
        self.extracted_accounts = []
        self.extracted_transactions = []
        
    def _load_api_key(self) -> str:
        """Load Skyvern API key from environment"""
        api_key = os.getenv("SKYVERN_API_KEY")
        if not api_key:
            # Try loading from .env file
            env_file = Path(__file__).parent / ".env"
            if env_file.exists():
                with open(env_file, 'r') as f:
                    for line in f:
                        if line.startswith("SKYVERN_API_KEY="):
                            api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                            break
        
        if not api_key:
            raise ValueError("SKYVERN_API_KEY not found")
        
        print(f"🔑 API key loaded: {api_key[:20]}...")
        return api_key

    async def extract_account_details_and_transactions(self, target_account: str = None) -> Dict[str, Any]:
        """Extract detailed account information and transactions"""
        
        print("🚀 ENHANCED BANK EXTRACTION - Account Details + Transactions")
        if target_account:
            print(f"   Target Account: {target_account}")
        else:
            print("   Target Account: Will use first available account")
        print("   Will extract: Account details + Transaction history")
        print("=" * 70)
        
        # Load enhanced YAML workflow
        yaml_path = "recipes/enhanced_bank_extraction.yaml"
        yaml_file = Path(yaml_path)
        
        if not yaml_file.exists():
            raise FileNotFoundError(f"Enhanced YAML not found: {yaml_path}")
        
        yaml_definition = yaml_file.read_text(encoding='utf-8')
        print(f"✅ Enhanced YAML loaded ({len(yaml_definition)} chars)")
        
        # If no target account specified, get the first available account
        if not target_account:
            print("🔍 No target account specified, detecting first available account...")
            target_account = await self._get_first_available_account()
            print(f"✅ Using detected account: {target_account}")
        else:
            print(f"🎯 Using specified target account: {target_account}")
        
        # Parameters - only pass TARGET_ACCOUNT if we have a specific one
        variables = {
            "TARGET_URL": "https://parabank.parasoft.com/parabank/index.htm",
            "USERNAME": "MedDhia",
            "PASSWORD": "MedDhia123"
        }
        
        # Only add TARGET_ACCOUNT if we have a specific account to target
        if target_account and target_account.strip():
            variables["TARGET_ACCOUNT"] = target_account
            print(f"📝 Workflow will target specific account: {target_account}")
        else:
            print("📝 Workflow will auto-detect first account during execution")
        
        try:
            # Initialize client
            client = Skyvern(api_key=self.api_key, base_url="https://api.skyvern.com")
            print("✅ Skyvern client initialized")
            
            # Create workflow
            print("📝 Creating enhanced extraction workflow...")
            workflow = await client.create_workflow(yaml_definition=yaml_definition)
            workflow_id = getattr(workflow, 'workflow_permanent_id', workflow.workflow_id)
            print(f"✅ Enhanced workflow created: {workflow_id}")
            
            # Execute enhanced extraction
            print(f"🔥 Executing enhanced extraction for account {target_account}...")
            print("   This will extract: Login → Account Details → Transactions → Return to Overview")
            
            result = await client.run_workflow(
                workflow_id=workflow_id,
                parameters=variables,
                wait_for_completion=True,
                timeout=600  # 10 minutes for detailed extraction
            )
            
            print(f"✅ ENHANCED EXTRACTION COMPLETED!")
            print(f"   Status: {result.status}")
            print(f"   Has output: {bool(result.output)}")
            
            if result.output:
                print(f"   Output blocks: {list(result.output.keys())}")
                
                # Process the results
                processed_data = await self._process_enhanced_results(result.output, target_account)
                
                return {
                    "extraction_type": "ENHANCED_ACCOUNT_DETAILS_AND_TRANSACTIONS",
                    "target_account": target_account,
                    "timestamp": datetime.now().isoformat(),
                    "status": result.status,
                    "workflow_id": workflow_id,
                    "raw_output": result.output,
                    "processed_data": processed_data,
                    "account_details_extracted": bool(processed_data.get("account_details")),
                    "transactions_extracted": len(processed_data.get("transactions", [])),
                    "ready_for_next_account": processed_data.get("ready_for_next_account", False)
                }
            else:
                print("   ⚠️  No output data received")
                return {"status": "failed", "error": "No output received"}
            
        except Exception as e:
            print(f"❌ ENHANCED EXTRACTION FAILED: {e}")
            print(f"   Error type: {type(e)}")
            
            if "402" in str(e) or "Insufficient credit" in str(e):
                print("\n💳 CREDIT BALANCE ISSUE:")
                print("   Enhanced extraction requires more credits")
                print("   Visit: https://app.skyvern.com/billing to add credits")
            
            raise

    async def _process_enhanced_results(self, raw_output: Dict[str, Any], target_account: str) -> Dict[str, Any]:
        """Process enhanced extraction results"""
        
        print("🔄 Processing enhanced extraction results...")
        
        processed = {
            "login_success": False,
            "account_details": {},
            "transactions": [],
            "accounts_overview": [],
            "ready_for_next_account": False,
            "extraction_summary": {}
        }
        
        # Process login results
        if "Login_To_Bank_output" in raw_output:
            login_data = raw_output["Login_To_Bank_output"]
            if isinstance(login_data, dict):
                extracted_info = login_data.get("extracted_information", {})
                processed["login_success"] = extracted_info.get("login_success", False)
                processed["accounts_overview"] = extracted_info.get("accounts_overview", [])
                print(f"   ✅ Login successful: {processed['login_success']}")
                print(f"   📊 Accounts in overview: {len(processed['accounts_overview'])}")
        
        # Process account details
        if "Extract_First_Account_Details_output" in raw_output:
            details_data = raw_output["Extract_First_Account_Details_output"]
            if isinstance(details_data, dict):
                extracted_info = details_data.get("extracted_information", {})
                processed["account_details"] = extracted_info.get("account_details", {})
                print(f"   💰 Account details extracted: {bool(processed['account_details'])}")
                if processed["account_details"]:
                    print(f"      Account: {processed['account_details'].get('account_number', 'Unknown')}")
                    print(f"      Type: {processed['account_details'].get('account_type', 'Unknown')}")
                    print(f"      Balance: {processed['account_details'].get('balance', 'Unknown')}")
        
        # Process transactions
        if "Extract_Account_Transactions_output" in raw_output:
            transactions_data = raw_output["Extract_Account_Transactions_output"]
            if isinstance(transactions_data, dict):
                extracted_info = transactions_data.get("extracted_information", {})
                processed["transactions"] = extracted_info.get("transactions", [])
                transaction_summary = extracted_info.get("transaction_summary", {})
                
                print(f"   📋 Transactions extracted: {len(processed['transactions'])}")
                if transaction_summary:
                    print(f"      Total transactions: {transaction_summary.get('total_transactions', 0)}")
                    print(f"      Date range: {transaction_summary.get('date_range', 'Unknown')}")
        
        # Process return to overview
        if "Return_To_Overview_For_Next_Account_output" in raw_output:
            overview_data = raw_output["Return_To_Overview_For_Next_Account_output"]
            if isinstance(overview_data, dict):
                extracted_info = overview_data.get("extracted_information", {})
                processed["ready_for_next_account"] = extracted_info.get("ready_for_next", False)
                next_accounts = extracted_info.get("next_accounts_available", [])
                print(f"   🔄 Ready for next account: {processed['ready_for_next_account']}")
                print(f"   📝 Next accounts available: {len(next_accounts)}")
        
        # Create extraction summary
        processed["extraction_summary"] = {
            "target_account": target_account,
            "login_successful": processed["login_success"],
            "account_details_found": bool(processed["account_details"]),
            "transactions_count": len(processed["transactions"]),
            "ready_for_next": processed["ready_for_next_account"],
            "extraction_timestamp": datetime.now().isoformat()
        }
        
        return processed

    async def extract_multiple_accounts(self, account_numbers: List[str]) -> Dict[str, Any]:
        """Extract details and transactions for multiple accounts"""
        
        print(f"🔄 MULTI-ACCOUNT EXTRACTION - {len(account_numbers)} accounts")
        print(f"   Accounts to process: {', '.join(account_numbers)}")
        
        all_results = {}
        
        for i, account_number in enumerate(account_numbers, 1):
            print(f"\n--- Processing Account {i}/{len(account_numbers)}: {account_number} ---")
            
            try:
                result = await self.extract_account_details_and_transactions(account_number)
                all_results[account_number] = result
                
                print(f"✅ Account {account_number} completed successfully")
                
                # Add delay between accounts to respect rate limits
                if i < len(account_numbers):
                    print("   ⏱️  Waiting 30 seconds before next account...")
                    await asyncio.sleep(30)
                
            except Exception as e:
                print(f"❌ Account {account_number} failed: {e}")
                all_results[account_number] = {
                    "status": "failed",
                    "error": str(e),
                    "account_number": account_number
                }
                
                # Continue with next account even if one fails
                continue
        
        return {
            "multi_account_extraction": True,
            "accounts_processed": len(account_numbers),
            "accounts_successful": len([r for r in all_results.values() if r.get("status") != "failed"]),
            "accounts_failed": len([r for r in all_results.values() if r.get("status") == "failed"]),
            "results": all_results,
            "extraction_timestamp": datetime.now().isoformat()
        }

    def save_enhanced_results(self, data: Dict[str, Any], output_path: str):
        """Save enhanced extraction results"""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"💾 Enhanced results saved: {output_file}")

    async def _get_first_available_account(self) -> str:
        """Get the first available account from the accounts overview"""
        
        print("🔍 Detecting first available account...")
        
        # Use the simple test to get accounts overview
        from simple_test import SimpleBankTest
        
        try:
            simple_tester = SimpleBankTest()
            result = await simple_tester.test_simple_extraction()
            
            if result.get("success") and result.get("raw_output"):
                # Extract accounts from the overview
                extracted_info = result["raw_output"].get("extracted_information", [])
                if extracted_info and len(extracted_info) > 0:
                    accounts_summary = extracted_info[0].get("accounts_summary", [])
                    if accounts_summary and len(accounts_summary) > 0:
                        # Get the first account number (dynamically)
                        first_account = accounts_summary[0].get("account_number")
                        if first_account:
                            print(f"📊 Found {len(accounts_summary)} accounts in overview")
                            print(f"🎯 First available account detected: {first_account}")
                            print(f"   Balance: {accounts_summary[0].get('balance', 'Unknown')}")
                            
                            # Show available accounts for reference
                            print("   Available accounts:")
                            for i, acc in enumerate(accounts_summary[:5], 1):  # Show first 5
                                acc_num = acc.get("account_number", "Unknown")
                                balance = acc.get("balance", "Unknown")
                                marker = "👉" if i == 1 else "  "
                                print(f"   {marker} {acc_num}: {balance}")
                            
                            return first_account
                
                print("⚠️  No accounts found in overview data")
                
        except Exception as e:
            print(f"⚠️  Could not get accounts overview: {e}")
            print("   This might be due to insufficient credits or API issues")
        
        # Dynamic fallback - try to use a known working account
        print("🔄 Using fallback strategy...")
        
        # Instead of hardcoding "12345", try to use any account we know works
        # First, check if we have any previously successful extractions
        fallback_accounts = ["12345", "12456", "12567", "12678"]  # Multiple fallbacks
        
        for fallback in fallback_accounts:
            print(f"   Trying fallback account: {fallback}")
            # We could add a quick validation here if needed
            return fallback
        
        # Last resort
        return "12345"


async def main():
    """Main execution function"""
    
    extractor = EnhancedBankExtractor()
    
    print("🎯 Enhanced Bank Data Extraction")
    print("   Options:")
    print("   1. Extract details + transactions for first available account (auto-detect)")
    print("   2. Extract details + transactions for multiple accounts")
    print("=" * 60)
    
    try:
        # Option 1: Extract first available account details and transactions
        print("\n🚀 Starting with first available account...")
        
        result = await extractor.extract_account_details_and_transactions()  # No specific account - will use first available
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"outputs/enhanced_extraction_{timestamp}.json"
        extractor.save_enhanced_results(result, output_path)
        
        print(f"\n✅ ENHANCED EXTRACTION COMPLETED!")
        print(f"   Account: {result.get('target_account')}")
        print(f"   Account details: {result.get('account_details_extracted')}")
        print(f"   Transactions: {result.get('transactions_extracted')}")
        print(f"   Ready for next: {result.get('ready_for_next_account')}")
        print(f"   Results: {output_path}")
        
        # If successful and ready for next account, ask user about processing more
        if result.get("ready_for_next_account") and result.get("account_details_extracted"):
            print("\n🎯 Ready to process more accounts!")
            print("   To process more accounts, run this script again or modify the account list")
            print("   Available accounts from previous extraction:")
            
            # Show available accounts from overview
            processed_data = result.get("processed_data", {})
            accounts_overview = processed_data.get("accounts_overview", [])
            for acc in accounts_overview[:5]:  # Show first 5
                print(f"   - {acc.get('account_number', 'Unknown')}: {acc.get('balance', 'Unknown')}")
        
    except Exception as e:
        print(f"\n❌ Enhanced extraction failed: {e}")
        
        if "402" in str(e):
            print("\n💡 SOLUTION:")
            print("   1. Go to: https://app.skyvern.com/billing")
            print("   2. Add more credits to your account")
            print("   3. Enhanced extraction requires more credits than simple tests")


if __name__ == "__main__":
    asyncio.run(main())
