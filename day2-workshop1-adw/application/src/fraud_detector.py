"""
Fraud Detection Transaction Processing System
Detects fraudulent transactions using risk scoring and anomaly detection

🤔 AGENT IMPLEMENTATION NOTES:
- This is a working fraud detection system with basic functionality
- Current limitations provide opportunities for agent-based improvements
- Review the code and consult with AI and the team for detailed limitations and agent opportunities
"""

import asyncio
import csv
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict
from enum import Enum


class RiskLevel(Enum):
    """Risk level classification"""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


@dataclass
class Transaction:
    """Transaction data model"""
    transaction_id: str
    user_id: str
    amount: float
    merchant: str
    location: str
    timestamp: str
    card_last4: str

    @classmethod
    def from_dict(cls, data: Dict) -> 'Transaction':
        """
        Create transaction from dictionary with validation
        
        🤔 CURRENT LIMITATIONS:
        - Basic validation only (amount > 0)
        - No schema validation (required fields, data types)
        - No range validation (amount too high, timestamp format)
        - No sanitization of malicious input (SQL injection, XSS)
        - No handling of missing or extra fields
        
        💡 AGENT OPPORTUNITIES:
        - Build a Schema Validator Agent to enforce JSON schema validation
        - Build a Sanitization Agent to clean and normalize input data
        - Build a Rich Validation Agent for complex business rules
        """
        # Data validation and sanitization
        try:
            amount = float(data['amount'])
            if amount < 0:
                raise ValueError("Amount cannot be negative")

            return cls(
                transaction_id=str(data['transaction_id']).strip(),
                user_id=str(data['user_id']).strip(),
                amount=amount,
                merchant=str(data['merchant']).strip(),
                location=str(data['location']).strip(),
                timestamp=str(data['timestamp']).strip(),
                card_last4=str(data['card_last4']).strip()
            )
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid transaction data: {e}")


@dataclass
class FraudDetectionResult:
    """Fraud detection result"""
    transaction: Transaction
    risk_level: RiskLevel
    risk_score: float
    is_fraudulent: bool
    reasons: List[str]


class FraudDetector:
    """Core fraud detection system"""

    # Risk score thresholds
    # 💡 AGENT OPPORTUNITY: These hard-coded thresholds should be configurable
    #    Build a Configuration Agent to load from YAML/JSON config files
    CRITICAL_THRESHOLD = 10000.0  # $10,000 threshold
    HIGH_RISK_THRESHOLD = 5000.0
    MEDIUM_RISK_THRESHOLD = 1000.0

    # Suspicious keywords
    # 💡 AGENT OPPORTUNITY: These should be maintainable lists, perhaps in a database
    #    Build a Knowledge Manager Agent to maintain and update blacklists
    SUSPICIOUS_MERCHANTS = ["Casino", "Crypto", "Wire Transfer", "Luxury"]
    SUSPICIOUS_LOCATIONS = ["Nigeria", "Russia", "Unknown"]

    async def analyze_transaction(self, transaction: Transaction) -> FraudDetectionResult:
        """
        Analyze a single transaction for fraud
        Pattern Recognition: Detects high-value transactions over $10,000
        
        🤔 CURRENT LIMITATIONS:
        - Only analyzes one transaction at a time (no velocity checking)
        - No user history or behavioral analysis
        - No time-of-day or day-of-week patterns
        - No cross-merchant or cross-location analysis
        
        💡 AGENT OPPORTUNITIES:
        - Build a Velocity Check Agent to detect rapid-fire transactions from same user
        - Build a Behavioral Analysis Agent to learn user spending patterns
        - Build a Pattern Recognition Agent for more sophisticated fraud detection
        """
        risk_score = 0.0
        reasons = []

        # Core fraud detection logic - Amount-based risk scoring
        if transaction.amount >= self.CRITICAL_THRESHOLD:
            risk_score += 100.0
            reasons.append(f"Critical: Transaction amount ${transaction.amount:,.2f} exceeds $10,000 threshold")
        elif transaction.amount >= self.HIGH_RISK_THRESHOLD:
            risk_score += 60.0
            reasons.append(f"High amount: ${transaction.amount:,.2f}")
        elif transaction.amount >= self.MEDIUM_RISK_THRESHOLD:
            risk_score += 30.0
            reasons.append(f"Medium amount: ${transaction.amount:,.2f}")

        # Anomaly detection - Suspicious merchant patterns
        if any(keyword in transaction.merchant for keyword in self.SUSPICIOUS_MERCHANTS):
            risk_score += 25.0
            reasons.append(f"Suspicious merchant: {transaction.merchant}")

        # Anomaly detection - Suspicious location patterns
        if any(keyword in transaction.location for keyword in self.SUSPICIOUS_LOCATIONS):
            risk_score += 15.0
            reasons.append(f"Suspicious location: {transaction.location}")

        # Determine risk level
        if risk_score >= 100:
            risk_level = RiskLevel.CRITICAL
            is_fraudulent = True
        elif risk_score >= 60:
            risk_level = RiskLevel.HIGH
            is_fraudulent = True
        elif risk_score >= 30:
            risk_level = RiskLevel.MEDIUM
            is_fraudulent = False
        else:
            risk_level = RiskLevel.LOW
            is_fraudulent = False

        return FraudDetectionResult(
            transaction=transaction,
            risk_level=risk_level,
            risk_score=risk_score,
            is_fraudulent=is_fraudulent,
            reasons=reasons if reasons else ["Normal transaction"]
        )

    async def process_transactions(self, transactions: List[Transaction]) -> List[FraudDetectionResult]:
        """Process multiple transactions concurrently using asyncio"""
        tasks = [self.analyze_transaction(txn) for txn in transactions]
        results = await asyncio.gather(*tasks)
        return results

    def load_transactions_from_csv(self, filename: str) -> List[Transaction]:
        """
        Load and validate transactions from CSV file
        
        🤔 CURRENT LIMITATIONS:
        - Only reads from CSV (no database, no real-time streaming)
        - Synchronous file I/O (not async)
        - Silently skips invalid transactions (no logging/reporting)
        - No progress tracking for large files
        - No data quality metrics
        
        💡 AGENT OPPORTUNITIES:
        - Build a Data Ingestion Agent for multiple source formats (CSV, JSON, API)
        - Build a Data Quality Validator Agent to report on skipped transactions
        - Build a Progress Monitor Agent to show loading progress for large datasets
        """
        transactions = []
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    transaction = Transaction.from_dict(row)
                    transactions.append(transaction)
                except ValueError as e:
                    # 💡 AGENT OPPORTUNITY: Log invalid transactions for data quality reporting
                    # Skip invalid transactions
                    continue
        return transactions

    def print_results(self, results: List[FraudDetectionResult]):
        """
        Print results in a beautiful demo-friendly format
        
        🤔 CURRENT LIMITATIONS:
        - Results only printed to console (not saved to file/database)
        - No alert notifications for critical fraud
        - No audit trail or compliance logging
        - No integration with external systems (email, Slack, webhooks)
        - No persistent storage of results
        
        💡 AGENT OPPORTUNITIES:
        - Build an Alert Notification Agent to send emails/Slack for critical fraud
        - Build a Results Archiver Agent to save results to database/CSV
        - Build an Audit Logger Agent for compliance and regulatory requirements
        - Build an Integration Agent to connect with external fraud detection systems
        """
        print("\n" + "="*80)
        print(" "*20 + "FRAUD DETECTION SYSTEM RESULTS")
        print("="*80 + "\n")

        # Statistics
        total = len(results)
        fraudulent = sum(1 for r in results if r.is_fraudulent)
        critical = sum(1 for r in results if r.risk_level == RiskLevel.CRITICAL)
        high = sum(1 for r in results if r.risk_level == RiskLevel.HIGH)
        medium = sum(1 for r in results if r.risk_level == RiskLevel.MEDIUM)
        low = sum(1 for r in results if r.risk_level == RiskLevel.LOW)

        print(f"📊 SUMMARY STATISTICS")
        print(f"   Total Transactions Processed: {total:,}")
        print(f"   Fraudulent Transactions: {fraudulent:,} ({fraudulent/total*100:.1f}%)")
        print(f"   Clean Transactions: {total-fraudulent:,} ({(total-fraudulent)/total*100:.1f}%)")
        print(f"\n   Risk Level Breakdown:")
        print(f"   • CRITICAL: {critical:,}")
        print(f"   • HIGH:     {high:,}")
        print(f"   • MEDIUM:   {medium:,}")
        print(f"   • LOW:      {low:,}")
        print("\n" + "-"*80 + "\n")

        # Show flagged transactions
        flagged = [r for r in results if r.is_fraudulent]
        print(f"🚨 FLAGGED TRANSACTIONS ({len(flagged)} found)\n")

        for i, result in enumerate(flagged[:10], 1):  # Show first 10
            txn = result.transaction
            print(f"   [{i}] Transaction: {txn.transaction_id}")
            print(f"       Amount: ${txn.amount:,.2f}")
            print(f"       Risk Level: {result.risk_level.value}")
            print(f"       Risk Score: {result.risk_score:.1f}")
            print(f"       Merchant: {txn.merchant}")
            print(f"       Location: {txn.location}")
            print(f"       User: {txn.user_id}")
            print(f"       Reasons: {', '.join(result.reasons)}")
            print()

        if len(flagged) > 10:
            print(f"   ... and {len(flagged) - 10} more flagged transactions\n")

        print("="*80 + "\n")


async def main():
    """
    Main entry point for fraud detection system
    
    🤔 CURRENT LIMITATIONS:
    - No command-line argument parsing (hardcoded filename)
    - No configuration file support
    - No error handling or retry logic for I/O failures
    - No performance metrics or timing information
    - Linear execution (load → analyze → print) - no modularity
    
    💡 AGENT OPPORTUNITIES:
    - Build a CLI Parser Agent to handle command-line arguments
    - Build a Performance Monitor Agent to track execution time and memory
    - Build a Error Handler Agent to manage failures gracefully with retries
    - Build a Pipeline Orchestrator Agent to coordinate multi-step workflows
    """
    detector = FraudDetector()

    print("\n🔍 Loading transactions...")
    transactions = detector.load_transactions_from_csv('transactions.csv')
    print(f"✓ Loaded {len(transactions):,} transactions\n")

    print("🔍 Analyzing transactions for fraud...")
    results = await detector.process_transactions(transactions)
    print(f"✓ Analysis complete\n")

    detector.print_results(results)


if __name__ == "__main__":
    asyncio.run(main())
