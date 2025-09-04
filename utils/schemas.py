from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Union
from datetime import datetime

class HumanIntervention(BaseModel):
    type: Literal["2FA","CAPTCHA","CONSENT","UNKNOWN"] = "2FA"
    channel: Optional[str] = None  # "SMS", "EMAIL", "APP", "VOICE"
    message: Optional[str] = None
    required: bool = True
    timestamp: Optional[str] = None

class Account(BaseModel):
    account_id: str
    account_type: Optional[Literal["checking", "savings", "credit", "investment", "loan", "mortgage", "other"]] = None
    currency: Optional[str] = None
    balance: Optional[float] = None
    available_balance: Optional[float] = None
    credit_limit: Optional[float] = None
    interest_rate: Optional[float] = None
    sub_accounts: List["Account"] = []
    metadata: dict = Field(default_factory=dict)

class Holding(BaseModel):
    account_id: str
    symbol: str
    name: Optional[str] = None
    quantity: Optional[float] = None
    current_value: Optional[float] = None
    market_price: Optional[float] = None
    cost_basis: Optional[float] = None
    gain_loss: Optional[float] = None
    asset_type: Optional[Literal["stock", "bond", "fund", "etf", "option", "crypto", "other"]] = None

class Transaction(BaseModel):
    account_id: str
    tx_id: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    status: Optional[Literal["posted", "pending", "cancelled"]] = "posted"
    merchant: Optional[str] = None
    transaction_type: Optional[Literal["debit", "credit", "transfer", "fee", "interest"]] = None

class Document(BaseModel):
    account_id: Optional[str] = None
    doc_id: Optional[str] = None
    title: Optional[str] = None
    document_type: Optional[Literal["statement", "notice", "tax_document", "other"]] = None
    date: Optional[str] = None
    url: Optional[str] = None
    size_bytes: Optional[int] = None
    file_format: Optional[str] = None

class PlatformMetadata(BaseModel):
    platform_name: Optional[str] = None
    platform_type: Optional[Literal["bank", "credit_union", "broker", "fintech", "other"]] = None
    login_method: Optional[str] = None
    navigation_complexity: Optional[Literal["simple", "moderate", "complex"]] = None
    supported_features: List[str] = []

class BankSnapshot(BaseModel):
    target: str
    fetched_at: str
    platform_metadata: Optional[PlatformMetadata] = None
    accounts: List[Account] = []
    holdings: List[Holding] = []
    transactions: List[Transaction] = []
    documents: List[Document] = []
    interventions: List[HumanIntervention] = []
    extraction_stats: dict = Field(default_factory=dict)

# Enable forward references
Account.model_rebuild()
