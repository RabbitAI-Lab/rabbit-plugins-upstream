---

spec: usk/3.0
id: key_safe_skill_generator
version: 1.2.0
name: Key‑Safe Skill Generator
description: A documentation‑only meta‑skill that teaches AI agents how to generate secure, zero‑exposure skills using MGC Blackbox for credential management. Contains no executable code.
author: MirginCipher Team
license: MIT
tags: zero-exposure, mgc, security, credential-management, skill-generator, meta-skill
platform_compatibility: windows, macos, linux
changelog:
  - version: 1.2.0
    changes:
      - Added mgc_run tool documentation
      - Added node_pub acquisition method (WebUI recommended)
      - Updated mgc_save to support seal package storage (ext01, ext03)
  - version: 1.1.0
    changes:
      - Added complete example section with copy‑and‑paste templates
      - Added comprehensive FAQ section
      - Added anti‑patterns section with correct practices
      - Added troubleshooting section
      - Added when to use / when not to use sections
      - Restructured to recommended format
  - version: 1.0.1
    changes:
      - Updated to emphasize MCP tools over CLI
  - version: 1.0.0
    changes:
      - Initial release with conceptual workflow and USK v3 structure

---

# Overview

Key‑Safe Skill Generator is a **meta‑skill** that teaches AI agents how to generate secure skills that interact with external services requiring credentials (email, APIs, tokens, SSH keys, etc.).
It provides a **design pattern**, **structural templates**, and **conceptual workflows** for building skills that never expose secrets to AI models.

This skill contains **no executable code** and is safe for automatic approval.

---

# What This Skill Enables

After reading this documentation, an AI agent will understand how to:

- Build new skills that interact with external services **without exposing credentials**
- Use **MGC Blackbox** as the secure storage and runtime provider
- Structure a Zero‑Exposure skill using **USK v3 conventions**
- Guide users to prepare and store credentials safely
- Generate a complete skill package (SKILL.md + README + local script)
- Ensure all sensitive operations happen **outside the AI model**

---

# When to Use Key‑Safe

Use Key‑Safe in the following scenarios:

## Must Use Cases

1. **AI needs credentials but must not see them**
   - Example: AI needs to send emails via SMTP but should never see the password
   - Solution: Store credentials in MGC, retrieve via local script

2. **Multi‑node collaboration**
   - Example: Node A creates a script, Node B executes it
   - Solution: Use `mgc_seal` to encrypt the script with Node B's public key

3. **Automation tasks requiring credentials**
   - Example: Scheduled tasks that need API keys
   - Solution: Credentials stored in MGC, accessed by local scripts

4. **Sensitive script execution**
   - Example: Scripts that perform privileged operations
   - Solution: Credentials never passed through AI, retrieved directly by scripts

## Example Triggers

- "I need to send an email using my SMTP server"
- "Call a GitHub API with my personal access token"
- "Push code to my repository"
- "Execute a script that needs database credentials"
- "Create a skill that uses external APIs securely"

---

# When NOT to Use Key‑Safe

Key‑Safe is not needed in these scenarios:

1. **Public APIs without authentication**
   - Example: Calling public REST APIs that require no API key

2. **Demo / testing environments**
   - Example: Using mock credentials for testing purposes

3. **Skills that only read public data**
   - Example: Fetching weather data from public APIs

4. **Manual operations where user provides credentials each time**
   - Example: Interactive scripts that prompt for password each run

---

# Prerequisites for Zero‑Exposure Skills

To build a Zero‑Exposure skill, users must:

1. Install MGC Blackbox: `pip install mgc-blackbox`
2. Start the MGC service: `mgc` (runs at http://127.0.0.1:57219)
3. Use **MCP tools** (`mgc_save`, `mgc_get`) for credential management
4. Store credentials in MGC under a chosen identifier
5. Use a local script to retrieve credentials and perform sensitive operations

> **Important:** For AI agents, use **MCP tools** (`mgc_save`, `mgc_get`). CLI may have port conflicts in some environments.

---

# Full Example: Complete Zero‑Exposure Workflow

This section demonstrates a complete flow from credential creation to usage.

## Step 1: Store Credentials in MGC

Using the `mgc_save` MCP tool:

```
Tool: mgc_save
Parameters:
  info_type:   "config"           # Type of stored data (user‑defined)
  info_owner:  "smtp_server"      # Identifier for this credential set
  content:     "{                 # Actual credential content
    \"host\": \"smtp.example.com\",
    \"port\": 587,
    \"username\": \"your_email@example.com\",
    \"password\": \"your_app_password\",
    \"use_tls\": true
  }"
```

> **Note:** Replace the placeholder values with actual credentials. The `info_owner` value is your reference name—you'll use this same value when retrieving credentials.

## Step 2: Retrieve Credentials in Your Skill

When building a skill that needs credentials, reference the stored identifier:

```
# In your SKILL.md or local script template:

credential_reference:
  info_type:  "config"
  info_owner: "smtp_server"

# The AI never sees the actual credentials, only the reference
```

## Step 3: Use MCP Tool to Retrieve Credentials

```
Tool: mgc_get
Parameters:
  info_type:  "config"
  info_owner: "smtp_server"
```

The MCP tool returns the stored JSON content. The AI receives:
- Connection details (host, port)
- Username (if non‑sensitive)
- But **never** the password

## Step 4: Execute Sensitive Operation

A local script performs the actual operation:

```
# Conceptual script flow (NOT executable):

1. Call mgc_get with info_owner="smtp_server"
2. Parse returned JSON for host, port, username, password
3. Use smtplib to send email
4. Return only: "Email sent successfully" or error message
5. NEVER log or expose the password
```

## Multi‑Node Example: Sealing Scripts for Other Nodes

When Node A needs Node B to execute a script:

### Node A: Seal the script

```
Tool: mgc_seal
Parameters:
  info_type:   "script"
  info_owner:  "send_email_via_mgc"
  ext04:       "-----BEGIN PUBLIC KEY-----\n...Node B's public key...\n-----END PUBLIC KEY-----"
```

Returns: Encrypted capsule containing the script

### Node B: Execute the sealed script

```
Tool: mgc_get
Parameters:
  info_type:  "script"
  info_owner: "send_email_via_mgc"
  action:     "run"
```

Node B uses its private key to decrypt and execute. Node A's script content is never exposed to Node B.

---

# FAQ

## MGC Related

### Q: What if MGC is not installed?
**A:** Install MGC Blackbox by running: `pip install mgc-blackbox`

### Q: What if MGC is not running?
**A:** Start MGC by running: `mgc` in a terminal. The service runs at http://127.0.0.1:57219

### Q: How do I check if MGC is running?
**A:** Open http://127.0.0.1:57219 in a browser. If you see a response, MGC is running.

### Q: What if MGC version is too old?
**A:** Update MGC: `pip install mgc-blackbox --upgrade`

### Q: Port 57219 is already in use
**A:** Stop other applications using that port, or configure MGC to use a different port in its configuration file.

### Q: How do I get the node public key (node_pub)?
**A:** Two ways:
1. **WebUI (Recommended):** Open WebUI → Go to Skill page → Click Setting button → Get node_pub
2. **MCP:** Call `mgc_get` with `info_type="__NODE_PUB__"` and `info_owner="__NODE_PUB__"`

The node_pub is needed when using `mgc_seal` to encrypt scripts for other nodes.

## Credential Management

### Q: What if credentials are not found?
**A:**
1. Verify the `info_owner` value matches exactly (case‑sensitive)
2. Verify `info_type` matches
3. List all stored credentials using `mgc_list` to check what exists

### Q: How should I name info_type and info_owner?
**A:**
- `info_type`: Category of data (e.g., "config", "credential", "script", "api_key")
- `info_owner`: Unique identifier that describes the purpose
  - Good: "smtp_gmail", "github_token", "slack_bot"
  - Bad: "test", "foo", "abc123"

### Q: How do I update stored credentials?
**A:** Call `mgc_save` again with the same `info_type` and `info_owner`. The old value will be replaced.

### Q: How do I delete stored credentials?
**A:** Use the `mgc_delete` MCP tool (if available) or overwrite with empty content.

## ext01 / ext02 Fields

### Q: What should I put in ext01?
**A:** The programming language or script type:
- `"python"` for Python scripts
- `"bash"` for shell scripts
- `"javascript"` for Node.js

### Q: What should I put in ext02?
**A:** Optional metadata. Common uses:
- Version string (e.g., "1.0.0")
- Description
- Empty string if not needed

### Q: What is ext04 used for?
**A:** Target node's public key when using `mgc_seal`. **Never put your credentials here.**

## Security

### Q: How do I ensure AI never exposes keys?
**A:**
1. Never include credentials in SKILL.md prompts
2. Never pass credentials as parameters to AI
3. Always use MGC to store credentials
4. Local scripts retrieve credentials directly from MGC
5. AI only receives non‑sensitive results

### Q: Can AI read credentials from MGC?
**A:** Yes, if AI calls `mgc_get`. **Never call mgc_get unless you want AI to process the result.** For zero‑exposure, use local scripts that call MGC, not AI directly.

### Q: What if AI accidentally logs credentials?
**A:** Ensure your local script:
- Never prints or logs credential values
- Only logs non‑sensitive information
- Uses secure logging practices

## Multi‑Node Scenarios

### Q: How do I use Key‑Safe for multi‑node collaboration?
**A:**
1. Each node generates an RSA key pair
2. Nodes exchange public keys
3. Use `mgc_seal` with the target node's public key
4. Target node uses private key to decrypt and execute

### Q: Can I seal a script for multiple nodes?
**A:** Currently, `mgc_seal` targets one node at a time. For multiple nodes, seal separately with each node's public key.

### Q: What if a node's private key is compromised?
**A:** Regenerate the key pair and redistribute the new public key to collaborators. Any previously sealed scripts will need to be re‑sealed.

---

# Anti‑Patterns

## Common Mistakes and Correct Practices

### ❌ Anti‑Pattern 1: Embedding Keys in Scripts

```python
# WRONG - Never do this
def send_email():
    password = "my_secret_password"  # Exposed!
    smtp.login("user@example.com", password)
```

**Correct Practice:**
```python
# RIGHT - Retrieve from MGC
def send_email():
    # Local script calls mgc_get, not AI
    credentials = get_credentials_from_mgc("smtp_server")
    smtp.login(credentials["username"], credentials["password"])
```

---

### ❌ Anti‑Pattern 2: AI Directly Reading Keys

```markdown
# WRONG - In SKILL.md
Use the following credentials:
- Username: user@example.com
- Password: secret123
```

**Correct Practice:**
```markdown
# RIGHT - In SKILL.md
Credentials are stored securely in MGC.
Reference: info_owner="smtp_server"
AI should NOT handle credentials directly.
```

---

### ❌ Anti‑Pattern 3: Putting Keys in ext04

```json
// WRONG
{
  "info_owner": "my_api",
  "ext04": "api_key=secret123"  // This is NOT for credentials!
}
```

**Correct Practice:**
```json
// RIGHT
{
  "info_owner": "my_api",
  "info_type": "config",
  "ext04": "-----BEGIN PUBLIC KEY-----\nNodeB_Public_Key...\n-----END PUBLIC KEY-----"
}
// ext04 is ONLY for public keys when sealing
```

---

### ❌ Anti‑Pattern 4: Storing Keys in Plain Text Files

```bash
# WRONG
echo "password=secret" > credentials.txt
```

**Correct Practice:**
```bash
# RIGHT
# Store in MGC using mgc_save
# Never write credentials to disk files
```

---

### ❌ Anti‑Pattern 5: Passing Credentials as Prompt Parameters

```markdown
# WRONG
Send an email using password: {user_password}
```

**Correct Practice:**
```markdown
# RIGHT
Send an email using credentials stored in MGC.
Reference: info_owner="smtp_gmail"
The local script handles credential retrieval.
```

---

### ❌ Anti‑Pattern 6: Logging Credentials

```python
# WRONG
def send_email(credentials):
    print(f"Using password: {credentials['password']}")  # Exposed!
    smtp.sendmail(...)
```

**Correct Practice:**
```python
# RIGHT
def send_email(credentials):
    logger.info("Connecting to SMTP server...")  # No credentials logged
    smtp.sendmail(...)
```

---

# Troubleshooting

## Common Errors and Solutions

### Error: "Credential not found"

**Symptoms:** `mgc_get` returns empty or error

**Solutions:**
1. Verify `info_owner` matches exactly (case‑sensitive)
2. Verify `info_type` matches
3. List all credentials: `mgc_list`
4. Re‑store credentials if needed

---

### Error: "info_type mismatch"

**Symptoms:** API returns wrong data or error

**Solutions:**
1. Check the `info_type` used when saving
2. Use the same `info_type` when retrieving
3. Common types: "config", "credential", "script", "api_key"

---

### Error: "info_owner not found"

**Symptoms:** Specific identifier not found

**Solutions:**
1. List all stored items: `mgc_list`
2. Check for typos in `info_owner`
3. Remember: "smtp_server" and "SMTP_SERVER" are different

---

### Error: "Invalid key format"

**Symptoms:** RSA key parsing errors

**Solutions:**
1. Ensure public key includes proper headers/footers:
   ```
   -----BEGIN PUBLIC KEY-----
   ...
   -----END PUBLIC KEY-----
   ```
2. Ensure key is on a single line (escape newlines)
3. Verify key is valid RSA public key

---

### Error: "MGC version too old"

**Symptoms:** API incompatibility errors

**Solutions:**
1. Check version: `pip show mgc-blackbox`
2. Update: `pip install mgc-blackbox --upgrade`
3. Restart MGC service after update

---

### Error: "MCP tool call failed"

**Symptoms:** Tool execution error

**Solutions:**
1. Verify MGC is running: `mgc` in terminal
2. Check service URL: http://127.0.0.1:57219
3. Verify token file exists: `~/.mgc/database/mgc_black_box/.mgc_token`
4. Restart MGC if needed

---

### Error: "Connection refused"

**Symptoms:** Cannot connect to MGC

**Solutions:**
1. Start MGC: `mgc`
2. Check if port 57219 is available
3. Check firewall settings
4. Verify localhost resolution

---

### Error: "Permission denied"

**Symptoms:** Cannot access MGC storage

**Solutions:**
1. Check file permissions on `~/.mgc/`
2. Verify token file is readable
3. Run MGC with appropriate permissions

---

# MCP Tools Reference

This section documents the MCP tools available for Key‑Safe implementation.

## mgc_save

Store credentials securely. When persisting a sealed package from mgc_seal, pass the JSON fields as-is: content (AES-encrypted body) -> content, ext01 -> ext01, ext03 -> ext03; keep ext02 if provided. Do not modify content; it is already encrypted.

```
Tool: mgc_save
Parameters:
  info_type:   string   # Type category (e.g., "config", "credential", "script")
  info_owner:  string   # Unique identifier
  content:     string   # JSON string of credential data
  ext01:       string   # Startup command for scripts (e.g., "python", "bash")
  ext02:       string   # Runtime parameters (optional)

Returns:
  success: true/false
  msg: status message
```

> **Seal Package:** When storing output from `mgc_seal`, include ext01 (empty), ext03 (RSA-encrypted AES key) as-is.

---

## mgc_get

Retrieve stored credentials.

```
Tool: mgc_get
Parameters:
  info_type:   string   # Must match saved type
  info_owner:  string   # Must match saved identifier
  action:      string   # Optional: "run" for script execution

Returns:
  content: stored data
  ext_01: language type (for scripts)
  ext_03: signature
```

---

## mgc_run

Execute a stored script (info_type='script'). Returns execution status only, not the script content. This is the recommended tool for running scripts; `mgc_get` with action='run' is kept for backward compatibility.

```
Tool: mgc_run
Parameters:
  info_type:   string   # Must be "script"
  info_owner:  string   # Script identifier
  diff_1:      string   # First differentiation field
  diff_2:      string   # Second differentiation field (optional)
  diff_3:      string   # Third differentiation field (optional)
  ext02:       string   # Runtime parameters override (optional)

Returns:
  execution status (success/failed, output, error)
```

> **Note:** Use `mgc_run` instead of `mgc_get` with action='run' for new skills.

---

## mgc_list

List all stored credentials.

```
Tool: mgc_list
Parameters: (none required)

Returns:
  items: array of stored credential references
```

---

## mgc_seal

Create encrypted capsule for trusted nodes.

```
Tool: mgc_seal
Parameters:
  info_type:   string   # "script"
  info_owner:  string   # Script identifier
  ext04:       string   # Target node's public key (PEM format)

Returns:
  content: encrypted capsule
  ext_01: script language
  ext_03: signature
```

---

# Zero‑Exposure Workflow (Conceptual)

A Zero‑Exposure skill follows this pattern:

1. **User stores credentials in MGC**
   Example identifiers: smtp_config, slack_bot_token, github_token.

2. **Skill references the identifier**
   The AI never sees the actual credentials.

3. **Local script retrieves credentials from MGC**
   The script communicates with the local MGC service to fetch encrypted content.

4. **Local script performs the sensitive operation**
   Examples: sending email, calling an API, pushing to Git.

5. **AI receives only the result**
   No secrets are ever exposed.

---

# Common Zero‑Exposure Patterns

## Email Sender

- User stores SMTP credentials in MGC
- Local script retrieves them
- Script sends email
- AI provides only subject/body/recipient

## API Client

- User stores API key in MGC
- Local script retrieves it
- Script performs authenticated request
- AI provides endpoint and payload

## Git Automation

- User stores GitHub token in MGC
- Local script retrieves it
- Script performs push/pull/commit
- AI provides commit message

---

# Security Notes

## What This Skill Guarantees

- **No credentials in prompts**: AI never receives credential values
- **No credentials in code**: Scripts retrieve from MGC, not hardcoded
- **No credentials in logs**: Only non‑sensitive information logged
- **No credentials in memory**: Credentials stay in MGC, not AI context
- **Encrypted storage**: All credentials encrypted at rest

## Critical Rules

1. **Never** include actual credentials in SKILL.md
2. **Never** pass credentials as prompt parameters
3. **Always** use MGC for credential storage
4. **Always** use local scripts for credential retrieval
5. **Never** log credential values
6. **Always** validate credential references, not values

---

# Entrypoint

This skill has **no runtime entrypoint**.
It is a documentation‑only instructional skill.

---

# Template: Zero‑Exposure SKILL.md Structure

When creating a new skill using Key‑Safe patterns, use this structure:

```markdown
---

spec: usk/3.0
id: your_skill_id
version: 1.0.0
name: Your Skill Name
description: Brief description of what this skill does
author: Your Name
license: MIT
tags: zero-exposure, mgc, your_tags
platform_compatibility: windows, macos, linux

---

# Overview

What this skill does.

# Prerequisites

- Install MGC Blackbox
- Store credentials in MGC (info_owner: "your_reference")

# Usage

How to use this skill.

# Credentials

- info_type: "config"
- info_owner: "your_reference"
- Required fields: [list]

# Security

This skill uses Zero‑Exposure design.
Credentials are stored in MGC, never exposed to AI.

---

# Entrypoint

Describe how to use this skill.
```

---

# Template: Zero‑Exposure Local Script Structure

When creating a local script for your skill:

```python
# Template structure (documentation only)

import json
import requests  # or appropriate library

# MGC Configuration
MGC_BASE_URL = "http://127.0.0.1:57219"
TOKEN_FILE = "~/.mgc/database/mgc_black_box/.mgc_token"

def get_mgc_token():
    # Read token from file
    pass

def get_credentials(info_owner, info_type="config"):
    # Call MGC API to retrieve credentials
    # Return: dict of credential data
    pass

def perform_sensitive_operation(credentials, operation_params):
    # Use credentials to perform operation
    # NEVER log credential values
    # Return: non‑sensitive result only
    pass

def main():
    # 1. Get credentials from MGC
    creds = get_credentials(info_owner="your_reference")

    # 2. Perform operation
    result = perform_sensitive_operation(creds, params)

    # 3. Return result (not credentials!)
    print(result)

if __name__ == "__main__":
    main()
```

---
