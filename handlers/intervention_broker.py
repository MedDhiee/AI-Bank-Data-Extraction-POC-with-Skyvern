"""
Simple intervention broker for the POC:
- When the agent emits a 2FA request, we print it and ask user to type the code on stdin.
- For production, replace with webhook/push/email/secure UI.
"""

import json

def handle_intervention(intervention: dict) -> dict:
    # intervention is expected like {"type":"2FA","channel":"SMS","message":"Enter code"}
    print("=== HUMAN INTERVENTION REQUIRED ===")
    print(json.dumps(intervention, indent=2))
    code = input("Enter 2FA code (or 'skip' to abort): ").strip()
    return {"provided_code": code}
