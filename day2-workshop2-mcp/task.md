# Day 2 Workshop 2: Model Context Protocol (MCP) 

## Workshop Overview

Explore and implement Model Context Protocol (MCP) integration to extend AI capabilities with external data sources, tools, and services. This workshop focuses on configuring GitHub MCP server for Claude Code and using it to interact with GitHub repositories.

---

## Learning Objectives

- Understand Model Context Protocol (MCP) and its role in AI development
- Learn to configure GitHub MCP server for Claude Code
- Build scripts to connect to GitHub MCP server

---

## Step-by-Step Guide

### Step 1: Configure GitHub MCP for Claude Code

**Task:** Install and configure GitHub MCP server for Claude Code CLI

**Installation:**
1. Follow the official GitHub MCP installation guide: [GitHub MCP Installation](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-claude.md)

---

### Step 2: Create Script to Connect to GitHub MCP Server

**Task:** Build a Python script that connects to GitHub MCP server and retrieves repository information

**Requirements:**
- Use environment variables for token storage
- Add error handling and logging
- Implement repository listing functionality
- Add documentation with usage examples

**In Aider session example:**
Ask AI: *"Create a Python script that connects to GitHub MCP server using HTTP transport and retrieves repository contents"*

---

### Step 3: Use GitHub Token to Get Repository Contents

**Task:** Use GitHub Personal Authorization Token to retrieve repository contents via MCP

**Using MCP tools via Claude Code:**

1. Open Claude Code with GitHub MCP configured
2. Ask: *"Using the GitHub MCP server, list all files in the repository [owner/repo]"*
3. Ask: *"Get the contents of [file-path] from [owner/repo] repository"*
4. Ask: *"Search for files containing [pattern] in [owner/repo]"*

**Instructor example:**
Example prompt: *"Using the GitHub MCP server, list all files in the repository [Alexey-Popov/awesome-ai-architect]"* 

**Optional Exercise:**
- Create a script that uses both direct GitHub API and MCP server
- Compare the approaches and document differences
- Implement error handling and token validation

---

## Expected Results

After completing this workshop, you should have:
- ✅ GitHub MCP server configured for Claude Code
- ✅ Working script to connect to GitHub MCP server
- ✅ Ability to retrieve repository contents via MCP

---

## Resources

**Official Documentation:**
- [GitHub MCP Server](https://github.com/github/github-mcp-server)
- [GitHub MCP Installation Guide](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-claude.md)
- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

**GitHub API Documentation:**
- [GitHub REST API](https://docs.github.com/en/rest)
- [Contents API](https://docs.github.com/en/rest/repos/contents)

---
