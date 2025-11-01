# Integration Guide: Multi-Agent Banking System

## System Overview

The Multi-Agent Banking System processes transactions through a pipeline of specialized agents, each responsible for a specific aspect of transaction processing. This guide explains how to integrate all agents into a cohesive system.

## System Architecture

```
Input System → Transaction Validator → Fraud Detection → Compliance → Settlement → Reporting → Output System
```

### Agent Flow
1. **Transaction Validator**: Validates transaction format and basic business rules
2. **Fraud Detection**: Analyzes transactions for suspicious patterns
3. **Compliance**: Checks regulatory compliance and sanctions lists
4. **Settlement**: Processes approved transactions and updates balances
5. **Reporting**: Generates comprehensive reports and audit trails

## Communication Protocol

### Message Format
All agents communicate using standardized JSON messages:

```json
{
  "message_id": "unique_message_id",
  "timestamp": "2024-01-15T10:30:00Z",
  "source_agent": "agent_name",
  "target_agent": "agent_name",
  "message_type": "transaction|result|error",
  "data": {
    "transaction_id": "TXN001",
    "amount": 1000.00,
    "currency": "USD",
    "account_from": "ACC123456",
    "account_to": "ACC789012",
    "transaction_type": "wire",
    "description": "Payment for services",
    "status": "pending|approved|rejected",
    "metadata": {}
  }
}
```

### File-Based Communication
Agents communicate through shared directories using relative paths:
- **Input Folder**: `./shared/input/` - Contains incoming messages
- **Output Folder**: `./shared/output/` - Contains outgoing messages
- **Processing Folder**: `./shared/processing/` - Contains work-in-progress files
- **Results Folder**: `./shared/results/` - Contains final results

## Integration Steps

### 1. Environment Setup

Create the shared directory structure required by all agents. The directories should include input, output, processing, and results folders. An integrator script can automate this setup, or you can create the directories manually.

### 2. Agent Communication Flow

Each agent follows this pattern:
1. Monitors its input folder for new messages (polling every 1-2 seconds)
2. Processes messages according to its function
3. Writes output messages to the shared output folder
4. Moves processed files to the processing folder

**File Naming Convention:**
- Validator outputs: `validator_transaction_{id}.json`
- Fraud detector outputs: `fraud_transaction_{id}.json`
- Compliance checker outputs: `compliance_transaction_{id}.json`
- Settlement processor outputs: `settlement_transaction_{id}.json`
- Reporting agent outputs: `report_{transaction_id}.json` (in results folder)

### 3. Running the System

#### Using an Integrator Script
An integrator script can orchestrate the entire system:
1. Creates shared directories
2. Loads sample transactions from JSON file
3. Converts transactions to message format
4. Starts all agents as subprocesses or separate processes
5. Monitors the pipeline
6. Validates results

#### Manual Execution
1. Ensure shared directories exist
2. Start each agent as a separate process (in different terminals or as background processes)
3. Load transactions into `./shared/input/` using the message format

## Testing

### Basic Integration Test
Run the integrator script to test the complete system. The script will:
- Load sample transactions
- Start all agents
- Monitor processing
- Validate that results are generated correctly
- Show test results (PASSED/FAILED)

### Manual Testing
1. Place a transaction message in `./shared/input/`
2. Monitor files moving through the pipeline
3. Check `./shared/results/` for final reports

## Success Criteria

The system successfully integrates when:
- All agents start and run without errors
- Transactions flow through the complete pipeline
- Message format is consistent between agents
- Error handling works correctly
- Final results appear in `./shared/results/`
