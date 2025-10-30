# Day 1 Workshop 2: Dealing with Context, Model and Prompt

## Workshop Overview

Build a banking transaction parser that can handle multiple formats (CSV, JSON, XML) and detect potential fraud patterns. 

---

## Learning Objectives

- Understand the fundamentals of AI-assisted coding 
- Learn how to work with context 
- Master switching between different AI models for different tasks

---

## Prerequisites

### Setup Aider CLI

**Get API Keys:**
- [Aider Documentation - Models and Keys](https://aider.chat/docs/troubleshooting/models-and-keys.html)
- [OpenAI API Keys](https://platform.openai.com/api-keys)

**Initial Setup:**
```bash
# Verify Aider installation
aider -v

# Set API key (Mac/Linux)
export OPENAI_API_KEY=<your-key>

# Set API key (Windows)
setx OPENAI_API_KEY <your-key>
# Note: Restart shell after setx on Windows
```

**Start Aider:**
```bash
# Use smaller model for quick tasks
aider --model gpt-4o-mini

# Use reasoning model for complex tasks
aider --model o3-mini
# Or with high reasoning effort
aider --model o3 --reasoning-effort high
```

---

## Step-by-Step Guide

### Step 1: Initial Build Request

**Task:** Build a banking transaction parser that can handle multiple formats (CSV, JSON) and detect potential fraud patterns.

**In Aider session:**
1. Ask AI: *"Build a banking transaction parser that can handle multiple formats (CSV, JSON) and detect potential fraud patterns"*
2. Ask AI: *"Please build a CSV test file support"*

---

### Step 2: Working with Context

**Task:** Update README with installation instructions using proper context.

**In Terminal:**
```bash
aider transaction_parser.py readme.md
```

**In Aider session:**
- Ask AI: *"Update readme to add installation instructions"*

---

### Step 3: Switching Models

**Task:** Add XML support using a different model.

**In Terminal:**
```bash
# Try with reasoning model
aider --model o3-mini transaction_parser.py readme.md
```

**In Aider session:**
- Ask AI: *"Add support for XML format parsing and update the README"*

---

### Step 4: Best Practices and Testing

**Task:** Ask about best standards and implement testing.

**Discussion with Participants:**
- Ask: *"What do you see as best standards for this codebase?"*
- Ask AI: *"How should I write tests for this project?"*

**Suggested Prompts:**
1. *"Create pytest tests for the Transaction class validation"*
2. *"Add tests for CSV, JSON, and XML parsing"*
3. *"Create test cases for fraud detection scenarios"*

---

### Step 5: Currency Understanding Challenge

**Task:** Create a FraudDetector class with currency conversion awareness.

**Individual Exercise:**
1. Ask AI: *"Create a FraudDetector class that flags transactions over 10,000"*

---

## Transition to Next Workshop

**Preview:** In the next workshop, we'll explore how to use `specification.md` files to manage context more effectively. We'll revisit these same tasks using specification-driven development to show improved context handling.
