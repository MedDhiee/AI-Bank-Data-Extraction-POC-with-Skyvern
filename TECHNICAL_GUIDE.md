# 🔧 Detailed Technical Guide

## 🏗️ System Architecture

### 📋 Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    AI Banking POC                           │
├─────────────────────────────────────────────────────────────┤
│  Frontend (Python Scripts)                                 │
│  ├── simple_test.py           (Quick tests)               │
│  ├── enhanced_extractor.py    (Main extraction)           │
│  └── test_dynamic_detection.py (Automatic tests)          │
├─────────────────────────────────────────────────────────────┤
│  Business Logic                                            │
│  ├── EnhancedBankExtractor    (Business logic)            │
│  ├── Account Detection        (Dynamic detection)         │
│  └── Data Processing          (Data processing)           │
├─────────────────────────────────────────────────────────────┤
│  Data Layer                                               │
│  ├── Pydantic Schemas        (Validation)                 │
│  ├── JSON Outputs            (Persistence)                │
│  └── YAML Workflows          (Configuration)              │
├─────────────────────────────────────────────────────────────┤
│  External Services                                         │
│  ├── Skyvern API             (AI Automation)              │
│  ├── ParaBank Website        (Data source)                │
│  └── OpenAI API              (LLM for Skyvern)            │
└─────────────────────────────────────────────────────────────┘
```

### 🔄 Data Flow

```mermaid
graph TD
    A[User] --> B[enhanced_extractor.py]
    B --> C[Load .env]
    C --> D[Create Skyvern client]
    D --> E[Dynamic account detection]
    E --> F[Load YAML workflow]
    F --> G[Execute Skyvern]
    G --> H[Navigate ParaBank]
    H --> I[Extract data]
    I --> J[Pydantic validation]
    J --> K[Save JSON]
    K --> L[User result]
```

## 🧠 Technical Components

### 1. **EnhancedBankExtractor** (Main Component)

```python
class EnhancedBankExtractor:
    """
    Main banking extraction component
    
    Responsibilities:
    - Skyvern API management
    - Dynamic account detection
    - Results processing
    - Error handling
    """
    
    # Main methods
    async def extract_account_details_and_transactions(target_account=None)
    async def _get_first_available_account()
    async def _process_enhanced_results()
    async def extract_multiple_accounts()
```

### 2. **YAML Workflow** (Skyvern Configuration)

```yaml
# Structure of enhanced_bank_extraction.yaml workflow
title: Enhanced Bank Data Extraction
workflow_definition:
  parameters:           # Input parameters
    - TARGET_URL
    - USERNAME  
    - PASSWORD
    - TARGET_ACCOUNT   # Optional - auto-detection if empty
  
  blocks:              # Execution steps
    - Login_To_Bank                    # Login
    - Extract_First_Account_Details    # Account details
    - Extract_Account_Transactions     # Transactions
    - Return_To_Overview_For_Next_Account  # Return navigation
```

### 3. **Pydantic Schemas** (Validation)

```python
# utils/schemas.py
class Account(BaseModel):
    account_id: str
    account_type: Optional[str]
    balance: Optional[float]
    # ... other fields

class Transaction(BaseModel):
    account_id: str
    date: Optional[str]
    amount: Optional[float]
    # ... other fields
```

## 🔍 Key Algorithms

### 1. **Dynamic Account Detection**

```python
async def _get_first_available_account(self) -> str:
    """
    Dynamic detection algorithm:
    
    1. Try quick extraction via simple_test
    2. Parse results to get account list
    3. Return first account found
    4. On failure: fallback with predefined list
    5. Detailed logging at each step
    """
    
    # Step 1: API attempt
    try:
        result = await simple_tester.test_simple_extraction()
        accounts = parse_accounts_from_result(result)
        return accounts[0] if accounts else fallback()
    
    # Step 2: Intelligent fallback
    except Exception:
        return fallback_strategy()
```

### 2. **Error Handling with Fallback**

```python
# Multi-level fallback strategy
FALLBACK_ACCOUNTS = ["12345", "12456", "12567", "12678"]

def get_fallback_account():
    """
    Intelligent fallback:
    - Try several known accounts
    - Logs for traceability
    - Return first that could work
    """
    for account in FALLBACK_ACCOUNTS:
        log.info(f"Trying fallback account: {account}")
        return account  # Premier dans la liste
```

### 3. **Traitement Asynchrone**

```python
# Pattern d'exécution asynchrone
async def extract_multiple_accounts(accounts: List[str]):
    """
    Traitement parallèle avec contrôle:
    - Limite de concurrence
    - Délais entre requêtes
    - Gestion erreurs individuelles
    - Agrégation des résultats
    """
    
    results = {}
    for account in accounts:
        try:
            result = await extract_single_account(account)
            results[account] = result
            await asyncio.sleep(30)  # Respect des limites API
        except Exception as e:
            results[account] = {"error": str(e)}
    
    return aggregate_results(results)
```

## 🚀 Optimisations Techniques

### 1. **Gestion Mémoire**

```python
# Utilisation de générateurs pour gros volumes
def process_transactions_stream(transactions):
    """Traitement en streaming pour éviter surcharge mémoire"""
    for transaction in transactions:
        yield normalize_transaction(transaction)

# Cleanup automatique
async def __aenter__(self):
    return self

async def __aexit__(self, exc_type, exc_val, exc_tb):
    await self.cleanup_resources()
```

### 2. **Cache et Performance**

```python
# Cache des résultats d'API
from functools import lru_cache

@lru_cache(maxsize=100)
def get_account_schema():
    """Cache des schémas pour éviter recompilation"""
    return load_pydantic_schema()

# Timeout adaptatifs
TIMEOUTS = {
    "simple_test": 300,      # 5 minutes
    "enhanced": 600,         # 10 minutes  
    "multi_account": 1200    # 20 minutes
}
```

### 3. **Monitoring et Logging**

```python
import logging
from datetime import datetime

# Configuration logging structuré
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('banking_extraction.log'),
        logging.StreamHandler()
    ]
)

# Métriques de performance
class PerformanceMonitor:
    def __init__(self):
        self.start_time = datetime.now()
        self.metrics = {}
    
    def track_operation(self, operation_name):
        """Tracking temps d'exécution par opération"""
        start = datetime.now()
        # ... opération ...
        duration = datetime.now() - start
        self.metrics[operation_name] = duration
```

## 🔐 Sécurité et Bonnes Pratiques

### 1. **Gestion des Secrets**

```python
# .env - Variables sensibles
SKYVERN_API_KEY='...'  # Jamais dans le code source
OPENAI_API_KEY='...'   # Chargement via python-dotenv

# Validation des clés
def validate_api_key(api_key: str) -> bool:
    """Validation format JWT"""
    return api_key.startswith('eyJ') and len(api_key) > 100
```

### 2. **Validation des Données**

```python
# Validation stricte avec Pydantic
class TransactionSchema(BaseModel):
    amount: confloat(gt=-1000000, lt=1000000)  # Limites réalistes
    date: constr(regex=r'\d{2}-\d{2}-\d{4}')   # Format date strict
    account_id: constr(min_length=5, max_length=10)  # Longueur compte
    
    @validator('amount')
    def validate_amount(cls, v):
        """Validation métier des montants"""
        if v == 0:
            raise ValueError('Amount cannot be zero')
        return v
```

### 3. **Gestion des Limites d'API**

```python
# Rate limiting
from asyncio import Semaphore

class APIRateLimiter:
    def __init__(self, max_concurrent=3):
        self.semaphore = Semaphore(max_concurrent)
    
    async def __aenter__(self):
        await self.semaphore.acquire()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.semaphore.release()

# Usage
async with APIRateLimiter():
    result = await skyvern_api_call()
```

## 📊 Monitoring and Metrics

### 1. **Technical KPIs**

```python
# Key metrics to monitor
METRICS = {
    'extraction_success_rate': 0.95,    # 95% success rate
    'avg_extraction_time': 300,         # 5 minutes average
    'api_error_rate': 0.05,             # 5% max errors
    'data_quality_score': 0.98          # 98% valid data
}

class MetricsCollector:
    def __init__(self):
        self.metrics = defaultdict(list)
    
    def record_extraction(self, duration, success, errors):
        """Record metrics per extraction"""
        self.metrics['durations'].append(duration)
        self.metrics['successes'].append(success)
        self.metrics['errors'].extend(errors)
    
    def get_summary(self):
        """Calculate aggregated KPIs"""
        return {
            'avg_duration': mean(self.metrics['durations']),
            'success_rate': sum(self.metrics['successes']) / len(self.metrics['successes']),
            'error_count': len(self.metrics['errors'])
        }
```

### 2. **Health Checks**

```python
# System health checks
async def health_check():
    """
    Automatic checks:
    - Skyvern API connectivity
    - ParaBank availability
    - Credentials validity
    - Disk space for outputs
    """
    
    checks = {
        'skyvern_api': await check_skyvern_connectivity(),
        'parabank_site': await check_parabank_availability(),
        'disk_space': check_disk_space('outputs/'),
        'env_config': validate_environment_config()
    }
    
    return all(checks.values()), checks
```

## 🧪 Tests and Validation

### 1. **Testing Strategy**

```python
# Unit tests
class TestAccountDetection(unittest.TestCase):
    async def test_dynamic_account_detection(self):
        """Test automatic account detection"""
        extractor = EnhancedBankExtractor()
        account = await extractor._get_first_available_account()
        self.assertIsInstance(account, str)
        self.assertTrue(len(account) >= 5)

# Integration tests
class TestFullWorkflow(unittest.TestCase):
    async def test_complete_extraction_flow(self):
        """Test complete end-to-end workflow"""
        # Setup
        extractor = EnhancedBankExtractor()
        
        # Execution
        result = await extractor.extract_account_details_and_transactions()
        
        # Validations
        self.assertEqual(result['status'], 'completed')
        self.assertTrue(result['account_details_extracted'])
        self.assertGreater(result['transactions_extracted'], 0)
```

### 2. **Performance Tests**

```python
# Benchmarking
import time
import asyncio

async def benchmark_extraction():
    """Measure extraction performance"""
    start_time = time.time()
    
    extractor = EnhancedBankExtractor()
    result = await extractor.extract_account_details_and_transactions()
    
    duration = time.time() - start_time
    
    # Metrics
    print(f"Duration: {duration:.2f}s")
    print(f"Accounts: {result.get('accounts_found', 0)}")
    print(f"Transactions: {result.get('transactions_extracted', 0)}")
    print(f"Performance: {result.get('transactions_extracted', 0) / duration:.2f} tx/s")
```

## 🚀 Deployment and Production

### 1. **Production Configuration**

```python
# config/production.py
PRODUCTION_CONFIG = {
    'timeout_multiplier': 2,        # Longer timeouts
    'retry_attempts': 3,            # More retry attempts
    'logging_level': 'INFO',        # Less verbose
    'enable_monitoring': True,      # Monitoring enabled
    'rate_limit_requests': 2,       # Requests/second limit
    'max_concurrent_extractions': 1 # One extraction at a time
}
```

### 2. **Production Monitoring**

```python
# Automatic alerts
class ProductionMonitor:
    async def monitor_extraction(self, extraction_func):
        """Monitoring with alerts"""
        try:
            start = datetime.now()
            result = await extraction_func()
            duration = datetime.now() - start
            
            # Alerts if performance degraded
            if duration > timedelta(minutes=15):
                await self.send_alert("Extraction taking too long")
            
            if not result.get('success'):
                await self.send_alert("Extraction failed")
                
            return result
            
        except Exception as e:
            await self.send_alert(f"Extraction error: {e}")
            raise
```

## 📈 Future Optimizations

### 1. **Architecture Improvements**

- **Microservices**: Split into specialized services
- **Queue system**: Redis/RabbitMQ for asynchronous processing
- **Database**: PostgreSQL for persistence
- **Distributed cache**: Redis for multi-instance cache

### 2. **Artificial Intelligence**

- **ML Pipeline**: Transaction anomaly prediction
- **Advanced NLP**: Automatic transaction classification
- **Computer Vision**: OCR for financial documents
- **Reinforcement Learning**: Web navigation optimization

### 3. **Scalability**

```python
# Future distributed architecture
class DistributedExtractor:
    def __init__(self):
        self.task_queue = RedisQueue()
        self.result_store = PostgreSQLStore()
        self.cache = RedisCache()
    
    async def submit_extraction_task(self, account_id):
        """Submit task to queue"""
        task_id = uuid.uuid4()
        await self.task_queue.put({
            'task_id': task_id,
            'account_id': account_id,
            'timestamp': datetime.now()
        })
        return task_id
    
    async def get_extraction_result(self, task_id):
        """Get async result"""
        return await self.result_store.get(task_id)
```

---

*Technical documentation updated - September 2025*
