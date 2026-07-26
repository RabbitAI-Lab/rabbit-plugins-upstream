---

spec: usk/3.0
id: mgc_database_security
version: 1.1.0
name: Database Credential Security (Zero‑Exposure Edition)
description: Secure database credential management using MGC Blackbox. Supports MySQL, PostgreSQL, SQLite, MariaDB and other databases. Store credentials locally in encrypted form, retrieve at runtime without exposing to AI models.
author: MirginCipher Team
license: MIT
tags: database, mysql, postgresql, sqlite, mariadb, security, credential-management, zero-exposure, mgc
platform_compatibility: windows, macos, linux
changelog:
  - version: 1.1.0
    changes:
      - Added complete example section with workflow templates
      - Added comprehensive troubleshooting section
      - Added FAQ section
      - Added anti‑patterns section with correct practices
      - Added when to use / when not to use sections
      - Added capability boundary explanation
      - Added advanced scenarios section
      - Added templates for SKILL.md and local scripts
  - version: 1.0.1
    changes:
      - Updated to emphasize MCP tools over CLI
  - version: 1.0.0
    changes:
      - Initial release with database zero-exposure pattern

---

# Overview

Database Credential Security is a documentation skill that teaches how to manage database credentials securely using MGC Blackbox. Supports MySQL, PostgreSQL, SQLite, MariaDB and other databases. It enables AI agents to execute database operations without ever exposing database passwords or connection strings to the AI model.

This skill contains **no executable code** and is safe for automatic approval.

---

# What This Skill Enables

After reading this documentation, an AI agent will understand how to:

- Store database credentials (MySQL, PostgreSQL, SQLite, MariaDB, etc.) securely in MGC Blackbox
- Retrieve credentials at runtime without AI seeing plaintext
- Execute database queries through local scripts
- Manage multiple database connections safely
- Rotate credentials without code changes
- Seal database scripts for multi‑node execution

---

# When to Use This Skill

## Must Use Cases

1. **Production environments**
   - Any database access in production requires secure credential management
   - Prevents credential leakage in logs, prompts, and AI context

2. **Automation tasks**
   - Scheduled scripts that need database access
   - CI/CD pipelines that connect to databases

3. **Multi‑node collaboration**
   - Node A creates a database script, Node B executes it
   - Use `mgc_seal` to encrypt the script with target node's public key

4. **AI needs database access but must not see passwords**
   - AI provides SQL statements only
   - Local scripts handle credential retrieval and execution

## Example Triggers

- "Connect to MySQL database securely"
- "Execute a SQL query without exposing the password"
- "Create a scheduled backup script for PostgreSQL"
- "Run database migrations safely"
- "Share a database script with another node securely"

---

# When NOT to Use This Skill

This skill is NOT needed in these scenarios:

1. **Public databases**
   - Databases that require no authentication
   - Read‑only public data sources

2. **Local development with no sensitive data**
   - Disposable test databases
   - Demo environments with mock data

3. **Interactive manual access**
   - When user provides credentials manually each time
   - Direct database tool usage (DBeaver, MySQL Workbench, etc.)

---

# Capability Boundary

This skill has specific boundaries that users must understand:

## What This Skill Does

- **Credential storage**: Securely store database credentials in MGC Blackbox
- **Credential retrieval**: Retrieve credentials at runtime via MCP tools
- **Pattern guidance**: Provide secure patterns for database credential management
- **Multi‑node sealing**: Encrypt database scripts for trusted nodes

## What This Skill Does NOT Do

- **NOT a database client**: Cannot connect to databases directly
- **NOT a SQL executor**: Does not run SQL queries
- **NOT a migration tool**: Does not handle schema changes
- **NOT a backup tool**: Does not perform database backups

The skill provides **credential management only**. All sensitive database operations (connect, query, migrate, backup) must be performed by local scripts.

---

# Prerequisites

1. Install MGC Blackbox: `pip install mgc-blackbox`
2. Start MGC service: `mgc` (runs at http://127.0.0.1:57219)
3. Token file: `~/.mgc/database/mgc_black_box/.mgc_token`
4. Database driver installed (mysql‑connector‑python, psycopg2, etc.)

---

# Complete Example: Full Database Credential Workflow

This section demonstrates a complete flow from credential storage to secure database operation.

## Step 1: Store Database Credentials

### MySQL Credential Storage

```
Tool: mgc_save
Parameters:
  info_type:   "config"
  info_owner:  "my_mysql_prod"
  content:     "{
    \"host\": \"db.example.com\",
    \"port\": 3306,
    \"database\": \"production_db\",
    \"user\": \"app_user\",
    \"password\": \"your_secure_password\"
  }"
```

### PostgreSQL Credential Storage

```
Tool: mgc_save
Parameters:
  info_type:   "config"
  info_owner:  "my_postgres_prod"
  content:     "{
    \"host\": \"db.example.com\",
    \"port\": 5432,
    \"database\": \"production_db\",
    \"user\": \"app_user\",
    \"password\": \"your_secure_password\",
    \"sslmode\": \"require\"
  }"
```

### SQL Server Credential Storage

```
Tool: mgc_save
Parameters:
  info_type:   "config"
  info_owner:  "my_sqlserver_prod"
  content:     "{
    \"host\": \"db.example.com\",
    \"port\": 1433,
    \"database\": \"production_db\",
    \"user\": \"app_user\",
    \"password\": \"your_secure_password\"
  }"
```

> **Note:** Replace placeholder values with actual database credentials. The `info_owner` value is your reference identifier—you'll use this same value when retrieving credentials.

## Step 2: Reference Credentials in Your Skill

```
# In your SKILL.md:

database_reference:
  info_type:  "config"
  info_owner: "my_mysql_prod"
  # The AI never sees actual credentials, only the reference
```

## Step 3: Retrieve Credentials

```
Tool: mgc_get
Parameters:
  info_type:  "config"
  info_owner: "my_mysql_prod"
```

The MCP tool returns the stored JSON content. The AI receives:
- Host and port (non‑sensitive)
- Database name (non‑sensitive)
- Username (may be non‑sensitive)
- But **never** the password

## Step 4: Execute Database Operation (Conceptual)

A local script performs the actual database operation:

```
# Conceptual script flow (NOT executable):

1. Call mgc_get with info_owner="my_mysql_prod"
2. Parse returned JSON for connection parameters
3. Use database driver to connect
4. Execute SQL query
5. Return only query results (no credentials)
6. NEVER log or expose the password
```

## Multi‑Node Example: Sealing Database Scripts

When Node A needs Node B to execute a database script:

### Node A: Seal the database script

```
Tool: mgc_seal
Parameters:
  info_type:   "script"
  info_owner:  "mysql_backup_script"
  ext01:       "python"
  ext04:       "-----BEGIN PUBLIC KEY-----\n...Node B's public key...\n-----END PUBLIC KEY-----"
```

Returns: Encrypted capsule containing the database script

### Node B: Execute the sealed script

```
Tool: mgc_get
Parameters:
  info_type:  "script"
  info_owner: "mysql_backup_script"
  action:     "run"
```

Node B uses its private key to decrypt and execute. Node A's database script is never exposed to Node B.

---

# FAQ

## MGC Related

### Q: What if MGC is not installed?
**A:** Install MGC Blackbox: `pip install mgc-blackbox`

### Q: What if MGC is not running?
**A:** Start MGC: `mgc` in a terminal. Service runs at http://127.0.0.1:57219

### Q: How do I check if MGC is running?
**A:** Open http://127.0.0.1:57219 in a browser. If you see a response, MGC is running.

### Q: Port 57219 is already in use
**A:** Stop other applications using that port, or configure MGC to use a different port.

## Credential Management

### Q: How do I update database credentials?
**A:** Call `mgc_save` again with the same `info_type` and `info_owner`. The old credentials will be replaced.

### Q: How do I manage multiple databases?
**A:** Use different `info_owner` values for each database:
- "my_mysql_prod"
- "my_postgres_dev"
- "my_mysql_reporting"

### Q: How do I rotate database credentials?
**A:**
1. Update credentials in the database
2. Call `mgc_save` with new credentials (same `info_owner`)
3. Local scripts automatically retrieve new credentials on next run

### Q: What if credentials are not found?
**A:**
1. Verify `info_owner` matches exactly (case‑sensitive)
2. Verify `info_type` matches
3. List all stored credentials: `mgc_list`

## Security

### Q: How do I ensure AI never sees database passwords?
**A:**
1. Never include credentials in SKILL.md prompts
2. Never pass credentials as parameters to AI
3. Always use MGC to store credentials
4. Local scripts retrieve credentials directly from MGC
5. AI only receives non‑sensitive query results

### Q: Can AI read credentials from MGC?
**A:** Yes, if AI calls `mgc_get`. **Never call mgc_get unless you want AI to process the result.** For zero‑exposure, use local scripts that call MGC, not AI directly.

### Q: What if AI accidentally logs credentials?
**A:** Ensure your local script:
- Never prints or logs credential values
- Only logs non‑sensitive information (query, row count, etc.)
- Uses secure logging practices

## Multi‑Node Scenarios

### Q: How do I share a database script securely?
**A:**
1. Node A creates the database script
2. Use `mgc_seal` with Node B's public key
3. Node B decrypts and executes using `mgc_get` with action="run"

### Q: Can I seal a script for multiple nodes?
**A:** Currently, `mgc_seal` targets one node at a time. For multiple nodes, seal separately with each node's public key.

---

# Anti‑Patterns

## Common Mistakes and Correct Practices

### ❌ Anti‑Pattern 1: Hardcoding Database Password in Scripts

```python
# WRONG - Never do this
def connect_to_db():
    connection = pymysql.connect(
        host="db.example.com",
        password="secret_password"  # Exposed!
    )
```

**Correct Practice:**
```python
# RIGHT - Retrieve from MGC
def connect_to_db():
    credentials = get_credentials_from_mgc("my_mysql_prod")
    connection = pymysql.connect(
        host=credentials["host"],
        password=credentials["password"]
    )
```

---

### ❌ Anti‑Pattern 2: Exposing Connection String in SKILL.md

```markdown
# WRONG - In SKILL.md
Use the following database credentials:
- Host: db.example.com
- Password: my_secret_password
```

**Correct Practice:**
```markdown
# RIGHT - In SKILL.md
Database credentials are stored securely in MGC.
Reference: info_owner="my_mysql_prod"
AI should NOT handle credentials directly.
```

---

### ❌ Anti‑Pattern 3: Putting Password in ext04

```json
// WRONG
{
  "info_owner": "my_database",
  "ext04": "password=secret123"  // This is NOT for passwords!
}
```

**Correct Practice:**
```json
// RIGHT
{
  "info_owner": "my_database",
  "info_type": "config",
  "ext04": "-----BEGIN PUBLIC KEY-----\nNodeB_Public_Key...\n-----END PUBLIC KEY-----"
}
// ext04 is ONLY for public keys when sealing
```

---

### ❌ Anti‑Pattern 4: Writing Credentials to Local Files

```bash
# WRONG
echo "password=secret" > db_credentials.txt
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
Execute SQL: SELECT * FROM users WHERE password='{user_password}'
```

**Correct Practice:**
```markdown
# RIGHT
Execute SQL using credentials stored in MGC.
Reference: info_owner="my_mysql_prod"
The local script handles credential retrieval.
```

---

### ❌ Anti‑Pattern 6: Logging Credentials in Database Scripts

```python
# WRONG
def execute_query(sql):
    creds = get_credentials_from_mgc("my_database")
    print(f"Connecting with password: {creds['password']}")  # Exposed!
    # ... execute query
```

**Correct Practice:**
```python
# RIGHT
def execute_query(sql):
    creds = get_credentials_from_mgc("my_database")
    logger.info(f"Connecting to {creds['host']}")  # No password logged
    # ... execute query
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
3. Common types: "config", "credential", "script"

---

### Error: "Database connection failed"

**Symptoms:** Cannot connect to database

**Solutions:**
1. Verify credentials are correct in MGC
2. Check database server is running
3. Verify network connectivity to database host
4. Check port is correct (MySQL: 3306, PostgreSQL: 5432, SQL Server: 1433)
5. Verify firewall allows connection

---

### Error: "Invalid credentials"

**Symptoms:** Authentication fails when connecting

**Solutions:**
1. Verify username and password in MGC storage
2. Check if password was recently changed
3. Update credentials in MGC using `mgc_save`
4. Verify user has permission to access the database

---

### Error: "MGC not running"

**Symptoms:** Cannot connect to MGC service

**Solutions:**
1. Start MGC: `mgc` in terminal
2. Check service URL: http://127.0.0.1:57219
3. Verify token file exists: `~/.mgc/database/mgc_black_box/.mgc_token`
4. Restart MGC if needed

---

### Error: "MCP tool call failed"

**Symptoms:** Tool execution error

**Solutions:**
1. Verify MGC is running
2. Check service URL
3. Verify token file is readable
4. Check MCP tool parameters are correct

---

### Error: "Permission denied"

**Symptoms:** Cannot access MGC storage

**Solutions:**
1. Check file permissions on `~/.mgc/`
2. Verify token file is readable
3. Run MGC with appropriate permissions

---

# MGC Blackbox API Reference

## Service Endpoint

- Base URL: http://127.0.0.1:57219
- Token File: ~/.mgc/database/mgc_black_box/.mgc_token
- Token: String token read from token file, required for all API calls

## Get Credentials API

**Endpoint:** /api/mgc/sensitive/get
**Method:** POST
**Headers:**
- X-MGC-Token: (string token read from token file)
- Content-Type: application/json

**Body fields:**
- info_type: "config"
- info_owner: your chosen identifier

**Response fields:**
- code: status code
- data.content: JSON string containing stored credentials

## Save Credentials API

**Endpoint:** /api/mgc/sensitive/save
**Method:** POST
**Headers:** same as above

**Body fields:**
- info_type: "config"
- info_owner: your identifier
- content: JSON string of credentials

---

# Advanced Scenarios

## Multi‑Database Credential Management

Manage credentials for multiple databases:

```
# Storage identifiers:
info_owner: "my_mysql_prod"      # MySQL production
info_owner: "my_postgres_prod"   # PostgreSQL production
info_owner: "my_mysql_dev"       # MySQL development
info_owner: "my_mysql_test"      # MySQL testing
```

## Multi‑Node Database Task Distribution

### Node A: Prepares database operation script

```
Tool: mgc_seal
Parameters:
  info_type:   "script"
  info_owner:  "mysql_migration_script"
  ext01:       "python"
  ext04:       "-----BEGIN PUBLIC KEY-----\nNodeB_Public_Key...\n-----END PUBLIC KEY-----"
```

### Node B: Executes the sealed script

```
Tool: mgc_get
Parameters:
  info_type:  "script"
  info_owner: "mysql_migration_script"
  action:     "run"
```

## Credential Rotation

Regularly rotate database credentials:

1. **Generate new credentials** in database
2. **Update MGC storage**:
   ```
   Tool: mgc_save
   Parameters:
     info_type:   "config"
     info_owner:  "my_mysql_prod"
     content:     "{new_credentials}"
   ```
3. **No code changes needed** - local scripts automatically use new credentials

## Credential Version Management

Track credential versions using info_owner suffixes:

```
info_owner: "my_mysql_prod_v1"   # Version 1
info_owner: "my_mysql_prod_v2"   # Version 2 (after rotation)
```

---

# Example Directory Structure

When creating a database skill:

```
database_skill/
  SKILL.md           # Skill definition
  README.md          # User documentation
  scripts/           # Local scripts (conceptual)
    execute_query.py
    backup.py
    migrate.py
```

---

# Security Best Practices

1. **Never embed credentials in code**
2. **Use MGC for credential storage**
3. **Retrieve credentials at runtime only**
4. **Never log or print credentials**
5. **Rotate credentials regularly**
6. **Use separate credentials per database**
7. **Use separate credentials per environment** (dev/staging/prod)
8. **Enable SSL/TLS for database connections**
9. **Limit database user permissions** to minimum required

---

# Common Patterns

## Python Database Connection (Conceptual)

```
import mysql.connector

def get_connection(credentials):
    return mysql.connector.connect(
        host=credentials["host"],
        port=credentials["port"],
        database=credentials["database"],
        user=credentials["user"],
        password=credentials["password"]
    )

def execute_query(sql):
    creds = retrieve_from_mgc("my_mysql_prod")
    conn = get_connection(creds)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
```

---

# Use Cases

- Database administration scripts
- Automated backup operations
- Data migration tools
- Application database access
- Multiple environment management (dev/staging/prod)
- Scheduled database operations
- Multi‑node database task execution

---

# Template: Zero‑Exposure Database SKILL.md

When creating a new database skill:

```markdown
---

spec: usk/3.0
id: your_skill_id
version: 1.0.0
name: Your Database Skill
description: Brief description
author: Your Name
license: MIT
tags: database, mgc, zero-exposure
platform_compatibility: windows, macos, linux

---

# Overview

What this skill does.

# Prerequisites

- Install MGC Blackbox
- Store database credentials in MGC (info_owner: "your_reference")
- Install required database driver

# Usage

How to use this skill.

# Database Credentials

- info_type: "config"
- info_owner: "your_reference"
- Required fields: host, port, database, user, password

# Security

This skill uses Zero‑Exposure design.
Credentials are stored in MGC, never exposed to AI.

---

# Entrypoint

Describe how to use this skill.
```

---

# Template: Database Local Script Structure

```python
# Template structure (documentation only)

import json
import pymysql  # or psycopg2, pymssql, etc.

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

def execute_query(credentials, sql):
    # Use credentials to connect and execute
    # NEVER log credential values
    # Return: query results only
    pass

def main():
    # 1. Get credentials from MGC
    creds = get_credentials(info_owner="your_database_reference")

    # 2. Execute query
    result = execute_query(creds, "SELECT * FROM users")

    # 3. Return result (not credentials!)
    print(result)

if __name__ == "__main__":
    main()
```

---

# License

MIT
