# Day 1 Workshop 3: Spec-Driven Development with Plans & Tests

## Workshop Overview

Build a comprehensive KYC API that validates customer information and performs compliance checks. This exercise demonstrates specification-driven development, where the API specification drives the implementation.

---

## Learning Objectives

- Master specification-driven development workflow
- Understand the outcome difference of specification-driven development
- Learn to write effective specifications for AI coding
- Build a KYC (Know Your Customer) API using specifications

---

## Step-by-Step Guide

### Step 1: Basic KYC Validation API 

**Task:** Create a basic customer validation API following specification-driven development principles

#### Agent Configuration Setup

Before starting development, each group should create their AI agent configuration file:
- Generate `agents.md` or `aider.md` or `claude.md` for your project
- Define coding standards, project structure, and workflow expectations
- Include banking industry standards and security requirements
- Present results

### Step 2: Implement API application using the specification

**Suggested Prompt:**
```
Follow SPECIFICATION.md and agents.md.
- Strictly apply coding standards and project structure from agents.md.
- Implement and validate all endpoints and models as specified.
- Add comprehensive error handling, authentication, audit logging, and tests as required.
```

**Optional: Experiment with Different Models**
- Try small vs. large models
- Test reasoning models
- Compare outputs and quality

### Step 3: Presentation

Present your solution, focusing on:
- How they used the specification to guide development
- Key decisions made during implementation
- Challenges faced and how they were resolved
- Demonstration of the working API


### Optional Exercise - Full KYC Workflow 

**Task:** Extend API with document verification and compliance checks

**Suggested Aider Setup:**
```bash
aider specs/kyc-api.yaml src/models.py src/api.py src/compliance_checker.py src/document_verifier.py
```

**Suggested Prompts:**
1. *"Extend the OpenAPI spec to include document verification endpoints"*
2. *"Add compliance checking endpoints for sanctions lists and AML"*
3. *"Implement document verification logic with mock services"*
4. *"Add comprehensive error handling and validation"*

---

