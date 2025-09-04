#!/usr/bin/env python3
"""
Simple Bank Test - Test extraction with minimal credits
Tests basic login and account overview extraction without infinite loops
"""

import asyncio
import json
import os
from pathlib import Path
from datetime import datetime

# Import Skyvern
try:
    from skyvern import Skyvern
    print("✅ Skyvern imported successfully")
except ImportError as e:
    print(f"❌ Error importing Skyvern: {e}")
    exit(1)


class SimpleBankTest:
    """Simple test to verify API works with limited credits"""
    
    def __init__(self):
        self.api_key = self._load_api_key()
        
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

    async def test_simple_extraction(self):
        """Test simple extraction to verify API works"""
        
        print("🧪 SIMPLE BANK TEST - Minimal Credit Usage")
        print("   Will only extract account overview without clicking individual accounts")
        print("=" * 60)
        
        # Load simple YAML workflow
        yaml_path = "recipes/simple_bank_test.yaml"
        yaml_file = Path(yaml_path)
        
        if not yaml_file.exists():
            raise FileNotFoundError(f"Simple test YAML not found: {yaml_path}")
        
        yaml_definition = yaml_file.read_text(encoding='utf-8')
        print(f"✅ Simple YAML loaded ({len(yaml_definition)} chars)")
        
        # Parameters
        variables = {
            "TARGET_URL": "https://parabank.parasoft.com/parabank/index.htm",
            "USERNAME": "MedDhia",
            "PASSWORD": "MedDhia123"
        }
        
        try:
            # Initialize client
            client = Skyvern(api_key=self.api_key, base_url="https://api.skyvern.com")
            print("✅ Skyvern client initialized")
            
            # Create workflow
            print("📝 Creating simple test workflow...")
            workflow = await client.create_workflow(yaml_definition=yaml_definition)
            workflow_id = getattr(workflow, 'workflow_permanent_id', workflow.workflow_id)
            print(f"✅ Simple workflow created: {workflow_id}")
            
            # Execute simple test
            print("🚀 Executing simple test (should use minimal credits)...")
            result = await client.run_workflow(
                workflow_id=workflow_id,
                parameters=variables,
                wait_for_completion=True,
                timeout=300  # 5 minutes timeout
            )
            
            print(f"✅ SIMPLE TEST COMPLETED!")
            print(f"   Status: {result.status}")
            print(f"   Has output: {bool(result.output)}")
            
            if result.output:
                print(f"   Output keys: {list(result.output.keys())}")
                
                # Show extracted data
                for key, value in result.output.items():
                    print(f"   {key}: {value}")
            
            # Save results
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"outputs/simple_test_{timestamp}.json"
            
            test_result = {
                "test_type": "SIMPLE_BANK_TEST",
                "timestamp": timestamp,
                "status": result.status,
                "workflow_id": workflow_id,
                "raw_output": result.output,
                "success": result.status == "completed",
                "credits_used": "minimal (single workflow execution)"
            }
            
            # Save to file
            Path("outputs").mkdir(exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(test_result, f, indent=2, ensure_ascii=False, default=str)
            
            print(f"💾 Test results saved: {output_path}")
            
            return test_result
            
        except Exception as e:
            print(f"❌ SIMPLE TEST FAILED: {e}")
            print(f"   Error type: {type(e)}")
            
            if "402" in str(e) or "Insufficient credit" in str(e):
                print("\n💳 CREDIT BALANCE ISSUE:")
                print("   Your Skyvern account doesn't have enough credits")
                print("   Visit: https://app.skyvern.com/billing to add credits")
                print("   Even simple tests require some credits")
            
            raise


async def main():
    """Main test function"""
    
    tester = SimpleBankTest()
    
    try:
        result = await tester.test_simple_extraction()
        
        if result["success"]:
            print("\n🎉 SUCCESS! Simple extraction worked!")
            print("   Your API key and setup are correct")
            print("   You can now add more credits for full extraction")
        else:
            print(f"\n⚠️  Test completed but with status: {result['status']}")
    
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        
        if "402" in str(e):
            print("\n💡 SOLUTION:")
            print("   1. Go to: https://app.skyvern.com/billing")
            print("   2. Add credits to your account")
            print("   3. Try again with the simple test")
            print("   4. Once working, use the full extraction workflow")


if __name__ == "__main__":
    asyncio.run(main())
