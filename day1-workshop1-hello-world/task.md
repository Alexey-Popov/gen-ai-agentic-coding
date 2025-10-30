# Day 1 Workshop 1: Hello World with AI - Building Your First Web API

## Workshop Overview

Build a simple REST API web application using AI assistance. Learn the fundamentals of AI-assisted coding with Aider CLI and Claude Code using basic models.

---

## Learning Objectives

- Get hands-on experience with AI-assisted coding tools (Aider CLI and Claude Code)
- Build your first web API application with AI assistance
- Learn to interact effectively with AI coding assistants

---

## Step-by-Step Guide

### 1. Setup and First Steps

#### Using Aider CLI

**Initial Setup:**
```bash
# Setup Aider
export OPENAI_API_KEY=<your-key>
aider --model gpt-4o-mini
```

**In Aider session:**
```bash
# Ask AI to create the application
Create a simple node.js web application with a hello world endpoint
```

**Follow these steps:**
1. Create a new JavaScript file: `app.js`
2. Ask AI: *"Create a simple node.js web application with a hello world endpoint"*
3. Review the generated code
4. Ask to explain how to run it
5. Test it locally - ask how to test it:
   - Follow steps and run it
   - Check in browser

---

#### Using Claude Code

**Follow these steps:**
1. Open Claude Code interface

```bash
claude
```

2. Ask AI: *"Create a simple node.js web application with a hello world endpoint. Call it hello.js, add documentation with running instructions"*
3. Then ask: *"Add a GET endpoint that accepts parameter and adds it after hello world"*

---

### 2. Optional Additional Tasks

Enhance your application with the following features:

- ✅ Include proper error handling and HTTP status codes
- ✅ Add input validation for POST and PUT requests
- ✅ Add comprehensive documentation in `README.md` with:
  - Installation instructions
  - API endpoint documentation
  - Example curl commands for testing
  - How to run the application

---

### 3. Running and Testing

#### Installation
```bash
# Install dependencies
npm install
```

#### Run the Application
```bash
# Run the application
node app.js
```

#### Test with curl
```bash
# Test the hello endpoint
curl http://localhost:3000/hello

# Test with parameter (if implemented)
curl http://localhost:3000/hello?name=World
```

---
