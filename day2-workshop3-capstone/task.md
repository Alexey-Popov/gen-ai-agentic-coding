# Day 2 Workshop 4: Capstone Project - Multi-Agent Banking System

## Project Overview

Build a complete distributed banking system using interconnected AI agents that process transactions through a full pipeline. **Each team builds all 5 agents**, with team members implementing individual agents that integrate into one cohesive system.

---

## Learning Objectives

- Apply all learned AI coding techniques in a real-world scenario
- Build multi-agent systems with proper interfaces
- Implement distributed system communication patterns
- Demonstrate end-to-end banking transaction processing
- Collaborate within a team to integrate multiple components

---

## Team Structure

Each team will:
- Build **all 5 agents** of the banking system
- Assign one agent per team member (if team has <5 members, some will implement multiple agents)
- Integrate all agents on **one team member's machine** for final testing and demonstration
- Present the complete integrated system

### The 5 Agents (Your Team Must Build All)

1. **Transaction Validator Agent** - Validates transaction format, amounts, and account information
2. **Fraud Detection Agent** - Analyzes transaction patterns for suspicious activity
3. **Compliance Agent** - Checks transactions against sanctions lists and regulations
4. **Settlement Agent** - Processes approved transactions and updates account balances
5. **Reporting Agent** - Aggregates processing results and generates reports

---

## Step-by-Step Guide

### Step 1: Team Formation and Agent Assignment

**Tasks:**
1. Form your team (typically 4-6 members)
2. Review the communication protocol and message format (see `integration-guide.md`)
3. Assign agents to team members:
   - Each member implements one agent (or two if team is smaller)
   - Identify who will host the integrated system on their machine
   - Plan how you'll share code (shared folder, Git etc.)

**Agent Assignment Template:**
- Member 1: Transaction Validator Agent
- Member 2: Fraud Detection Agent
- Member 3: Compliance Agent
- Member 4: Settlement Agent
- Member 5: Reporting Agent
- Integration Host: [Member name who will run the complete system]

---

### Step 2: Individual Agent Development

**Task for Each Team Member:** Implement your assigned agent following specification-driven development principles

**Requirements:**
- Create a script that implements your agent's logic
- Use AI-assisted development (Aider, Claude Code, Cursor)
- Implement standard message format communication
- Include comprehensive error handling and logging
- Add monitoring and status reporting
- Ensure your agent follows the protocol in `integration-guide.md`

**Deliverables Per Member:**
- Working agent implementation
- Unit tests for your agent
- Brief documentation of your agent's capabilities

---

### Step 3: Code Sharing and Integration

**Task:** Collect all agents and make integration

1. **Share Code:**

2. **Download All Agents:**
   - The integration host downloads all team members' agents
   - Organize agents in folder structure:
     ```
     team-project/
     ├── agent-validator/
     ├── agent-fraud/
     ├── agent-compliance/
     ├── agent-settlement/
     ├── agent-reporting/
     └── shared/
         ├── input/
         ├── output/
         ├── processing/
         └── results/
     ```
---

**Integration Testing Checklist:**
- ✅ All agents start successfully
- ✅ Transactions flow through complete pipeline
- ✅ Message format is consistent between agents
- ✅ Error handling works correctly
- ✅ Final results appear in `shared/results/`

---

### Step 4: System Demonstration

**Task:** Present your complete integrated multi-agent banking system

1. **System Overview:**
   - Show the complete pipeline
   - Explain the communication flow
   - Demonstrate how agents communicate

2. **Agent Implementation Details:**
   - Each member briefly explains their agent:
     - What it does
     - How it was built using AI-assisted development
     - Key challenges and solutions
     - Capabilities and limitations

3. **Live Demonstration:**
   - Process a transaction through the complete system
   - Show messages moving through each agent
   - Display final results and reports
   - Demonstrate error handling scenarios

---

## Communication Protocol

**Message Format:**
All agents communicate using standardized JSON messages. See `integration-guide.md` for detailed protocol specifications and message format examples.

**File-Based Communication:**
Agents communicate through shared directories (when integrated on one machine):
- Input: `./shared/input/` - Incoming messages
- Output: `./shared/output/` - Outgoing messages
- Processing: `./shared/processing/` - Work-in-progress files
- Results: `./shared/results/` - Final results

---

## Expected Results

After completing this capstone project, your team should have:

**Technical Deliverables:**
- ✅ All 5 agents implemented and working
- ✅ Complete integrated system running on one machine
- ✅ End-to-end transaction processing pipeline functioning
- ✅ Proper error handling and logging throughout
- ✅ Unit tests for individual agents

---
