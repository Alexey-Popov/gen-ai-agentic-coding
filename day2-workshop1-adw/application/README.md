# Fraud Detection System

A fraud detection transaction processing system that analyzes transactions for fraudulent activity using risk scoring and anomaly detection.

## Features

- Concurrent transaction processing with Python asyncio
- Risk scoring based on transaction amounts (critical threshold: $10,000)
- Anomaly detection for suspicious merchants and locations
- Data validation and sanitization

## Requirements
- Python 3.12+

## Installation

No external dependencies required - uses Python standard library only.

## Usage

### Run Fraud Detection

```bash
python src/fraud_detector.py
```

### Run Tests


```bash
python src/test_runner.py
```
