# Specification Template for Banking Transaction Parser

> Ingest the information from this file, implement the Low-Level Tasks, and generate the code that will satisfy the High and Mid-Level Objectives.

## High-Level Objective
- Build a robust banking transaction parser that can handle multiple file formats (CSV, JSON, XML) and detect potential fraud patterns

## Mid-Level Objectives
- Create a flexible transaction data model that can represent various banking transaction types
- Implement multi-format parsing with proper error handling and validation
- Build fraud detection capabilities for common suspicious patterns
- Ensure code follows banking industry standards for data handling and security

## Implementation Notes
- Use Python 3.12+ with type hints for better code clarity
- Follow PEP 8 coding standards
- Implement comprehensive error handling for malformed data
- Use dataclasses or Pydantic for data validation
- Include logging for audit trails (important for banking)
- Handle different currencies and international transactions
- Implement proper exception handling for file I/O operations
- Use Decimal for all monetary calculations (never float)
- Support ISO 4217 currency codes
- Include data privacy compliance for PII handling

## Context

### Beginning context
- `README_2_contxt,model,prompt.md` - Workshop introduction and learning objectives
- `reference-solution/src/fraud_detector.py` - Reference implementation of fraud detection logic
- `reference-solution/src/transaction_parser.py` - Reference implementation of transaction parser
- `sample-data/transactions.csv` - Sample CSV transaction data
- `sample-data/transactions.json` - Sample JSON transaction data
- `sample-data/transactions.xml` - Sample XML transaction data
- `SPECIFICATION.md` - This specification document

### Ending context
- `src/transaction_parser.py` - Main parser with multi-format support
- `src/models.py` - Transaction and fraud detection data models
- `src/fraud_detector.py` - Fraud detection logic and patterns
- `tests/test_transaction_parser.py` - Comprehensive test suite
- `sample-data/` - Sample transaction files in different formats
- `requirements.txt` - Project dependencies
- `README.md` - Installation and usage instructions

## Low-Level Tasks

### 1. Create Transaction Data Model
- **File**: `src/models.py`
- **Component**: Transaction class with fields: id (str), amount (Decimal), currency (str), timestamp (datetime), account_from (str), account_to (str), transaction_type (str), description (str)
- **Requirements**:
  - Use dataclasses for clean data representation
  - Include proper type hints
  - Add validation for amount (must be positive)
  - Handle currency codes (ISO 4217 format)
  - Include transaction metadata
  - Use Decimal for monetary precision
  - Add data privacy considerations for PII fields

### 2. Implement CSV Parser
- **File**: `src/transaction_parser.py`
- **Component**: `parse_csv_transactions(file_path: str) -> List[Transaction]`
- **Requirements**:
  - Handle CSV headers and data rows
  - Parse amounts as Decimal for precision
  - Convert timestamp strings to datetime objects
  - Validate required fields are present
  - Handle missing or malformed data gracefully
  - Add audit logging for parsing operations
  - Support different CSV formats and encodings

### 3. Add JSON and XML Support
- **File**: `src/transaction_parser.py`
- **Components**: `parse_json_transactions(file_path: str) -> List[Transaction]`, `parse_xml_transactions(file_path: str) -> List[Transaction]`
- **Requirements**:
  - Use json and xml.etree.ElementTree modules
  - Handle nested JSON structures
  - Parse XML with proper namespace handling
  - Maintain consistent Transaction object creation
  - Add format detection based on file extension
  - Include error handling for malformed files
  - Add audit logging for all parsing operations

### 4. Implement Fraud Detection
- **File**: `src/fraud_detector.py`
- **Component**: FraudDetector class with methods: detect_high_value(), detect_velocity(), detect_patterns()
- **Requirements**:
  - Flag transactions over $10,000 USD (with currency conversion)
  - Detect rapid successive transactions (velocity checks)
  - Identify unusual timing patterns
  - Create fraud risk scoring system
  - Generate fraud alerts with confidence levels
  - Handle currency conversion for international transactions
  - Add audit logging for all fraud detection events
  - Include configurable thresholds for different risk levels

### 5. Create Test Suite
- **File**: `tests/test_transaction_parser.py`
- **Components**: Test classes: TestTransactionModel, TestCSVParser, TestJSONParser, TestXMLParser, TestFraudDetector
- **Requirements**:
  - Test valid and invalid transaction data
  - Test all three file formats (CSV, JSON, XML)
  - Test fraud detection scenarios
  - Use pytest fixtures for sample data
  - Include edge cases and error conditions
  - Test performance with large files
  - Test currency conversion accuracy
  - Include security tests for input validation
  - Achieve >90% test coverage

### 6. Create Sample Data and Documentation
- **Files**: `sample-data/transactions.csv`, `sample-data/transactions.json`, `sample-data/transactions.xml`, `README.md`
- **Components**: Sample transaction files in all three formats and comprehensive documentation
- **Requirements**:
  - Create realistic banking transaction data
  - Include various transaction types and amounts
  - Add examples of potential fraud patterns
  - Include different currencies and international transactions
  - Create comprehensive README with installation instructions
  - Add usage examples and API documentation
  - Include troubleshooting guide
  - Add security considerations and best practices