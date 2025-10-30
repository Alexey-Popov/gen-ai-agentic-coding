# Day 2 Workshop 3: Capstone Project - Multi-Agent Banking System

## Workshop Overview

Build a distributed banking system using interconnected AI agents that process transactions through a complete pipeline. Teams work independently to create specialized agents that communicate through standardized interfaces.

---

## Learning Objectives

- Apply all learned AI coding techniques in a real-world scenario
- Build multi-agent systems with proper interfaces
- Implement distributed system communication patterns
- Demonstrate end-to-end banking transaction processing
- Collaborate on complex system integration

---

## Step-by-Step Guide

### Step 1: Team Assignment and Agent Planning

**Team Assignments (5 Teams):**

- **Team 1: Transaction Validator Agent** - Validates transaction format, amounts, and account information
- **Team 2: Fraud Detection Agent** - Analyzes transaction patterns for suspicious activity
- **Team 3: Compliance Agent** - Checks transactions against sanctions lists and regulations
- **Team 4: Settlement Agent** - Processes approved transactions and updates account balances
- **Team 5: Reporting Agent** - Aggregates processing results and generates reports

**Task:**
- Review the communication protocol and message format
- Define agent specifications and interfaces
- Plan implementation approach using AI-assisted development

---

### Step 2: Agent Development

**Task:** Implement your team's agent following specification-driven development principles

**Requirements:**
- Create a Python script that implements the agent logic
- Use AI-assisted development (Aider, Claude Code, Cursor)
- Implement standard message format communication
- Include comprehensive error handling and logging
- Add monitoring and status reporting

**In Aider session:**
Ask AI: *"Create a [team agent name] following the communication protocol in integration-guide.md. Include error handling, logging, and file-based communication"*

**Deliverables:**
- Working agent implementation
- Unit tests for agent functionality
- Agent documentation

---

### Step 3: Integration Testing

**Task:** Test agent integration with the complete system

**Activities:**
- Test individual agents with sample transaction data
- Validate message format compliance
- Debug communication issues between agents
- Test error handling scenarios
- Verify end-to-end transaction processing

**Integration Points:**
- Test your agent's input/output with other teams' agents
- Validate file-based communication protocol
- Ensure proper error propagation and handling

---

### Step 4: System Demonstration

**Task:** Present the complete multi-agent banking system

**Presentation should include:**
- How the agent was built using AI-assisted development
- Agent capabilities and limitations
- Integration with the overall system
- Demonstration of transaction processing pipeline
- Lessons learned and improvements

**Discussion Points:**
- Key decisions made during implementation
- Challenges faced and how they were resolved
- How specification-driven development helped
- Real-world applications and extensions

---

## Communication Protocol

**Message Format:**
All agents communicate using JSON messages. See `integration-guide.md` for detailed protocol specifications.

** Communication:**
- Input: `/shared/input/` - Incoming messages
- Output: `/shared/output/` - Outgoing messages
- Processing: `/shared/processing/` - Work-in-progress
- Results: `/shared/results/` - Final results

---

## Expected Results

After completing this workshop, you should have:
- ✅ Working agent implementation following the protocol
- ✅ Successful integration with other agents
- ✅ End-to-end transaction processing pipeline
- ✅ Understanding of multi-agent system architecture
- ✅ Experience with distributed system communication

---

## Resources

- See `integration-guide.md` for detailed communication protocol
- See team folders for reference implementations
- Use specification-driven development approach from previous workshops

---

