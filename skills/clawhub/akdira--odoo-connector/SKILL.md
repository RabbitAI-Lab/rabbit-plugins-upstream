---
name: odoo-connector
description: AI Agent skill for Odoo 17/18/19 XML-RPC API integration — authentication, CRUD, search operations
version: 1.2.0
author: akdira
tags: [odoo, erp, xmlrpc, api, integration, automation]
related_skills:
  - name: camofox-default-browser
    owner: akdira
    purpose: Browser automation tool for handling CAPTCHA challenges during authenticated Odoo web UI login (requires proper authorization)
    install: openclaw skills install @akdira/camofox-default-browser
---

# Odoo XML-RPC API Integration

Complete guide for AI agents to interact with Odoo instances via XML-RPC protocol. Works with Odoo 17, 18, and 19.

## What Is This

This skill enables AI agents to programmatically interact with Odoo ERP systems through its built-in XML-RPC API. Odoo exposes two XML-RPC endpoints that provide full access to all models (tables) in the database: search, read, create, update, delete, and execute any model method.

**Key capabilities:**
- Query any Odoo model (partners, products, sales orders, invoices, etc.)
- Create/update/delete records across all models
- Execute model-specific methods (approve, cancel, generate reports)
- No external dependencies — Python's `xmlrpc.client` stdlib only
- Works over HTTPS through standard reverse proxies (Traefik, nginx)

## Why XML-RPC

Odoo provides multiple API access methods:
- **REST API**: Limited, mostly for external integrations
- **JSON-RPC**: Browser-oriented, requires session management
- **XML-RPC**: Full programmatic access, stateless, language-agnostic

XML-RPC is the most reliable for AI agent automation because it's stateless (no session cookies), supports all operations, and works with any programming language that has XML-RPC client support.

## ⚡ FIRST TIME? START HERE — Authentication Setup

> **🔴 CRITICAL: You CANNOT use XML-RPC without valid API credentials.**
> Before writing ANY code, make sure you have an API key. If you don't, follow the steps below FIRST.

### Decision Flow
```
Do you have Odoo API credentials (API key)?
├── YES → Skip to "Connection Setup" section below
└── NO  → Follow Step 1 & Step 2 below, THEN continue
```

### Step 1: Login to Odoo Web UI

1. Open a browser and navigate to `{ODOO_BASE_URL}/web/login`
2. Enter your credentials:
   - Fresh install default: `admin` / `admin` — **change immediately after first login**
   - Production: use the credentials provided by your Odoo administrator
3. If you don't have credentials at all, contact the Odoo administrator

**⚠️ Encountering CAPTCHA or Cloudflare challenges?**
Many production Odoo instances use Cloudflare/WAF protection that may present CAPTCHA challenges during login. **Important: Only proceed if you have explicit authorization to access this Odoo instance.**

If you encounter CAPTCHA challenges during legitimate access:
- **Recommended:** Install and use the [camofox-default-browser](https://clawhub.ai/akdira/skills/camofox-default-browser) skill — browser automation tool that can handle CAPTCHA challenges during authenticated sessions.
- **Alternative:** Switch to a different network/IP, disable VPN, or use a browser extension like uBlock Origin to reduce CAPTCHA frequency.
- **Self-hosted/local Odoo:** No CAPTCHA — proceed normally.

> **⚠️ Legal & ToS Notice:** Bypassing security measures without authorization may violate the service's Terms of Service and applicable laws. Only use automation tools on systems you own or have explicit written permission to access. Repeated failed login attempts may result in account lockout.

### Step 2: Generate API Key (REQUIRED for XML-RPC)

> **Why API keys instead of passwords?** API keys are more secure — they can be revoked independently, don't expose your login password, and are the recommended method for programmatic access.

1. After login, navigate to: **Settings → Users & Companies → Users**
2. Click on **your user account** (the one that will be used for API access)
3. Scroll down to the **"API Keys"** section (near the bottom of the user form)
4. Click **"New API Key"**
5. Enter a description (e.g., `"AI Agent Automation - {date}"`)
6. Click **"Generate"**
7. **⚠️ CRITICAL: Copy the API key IMMEDIATELY — it's shown ONLY ONCE.** After you close the dialog, it cannot be retrieved again.
8. Store it securely (environment variable, password manager, `.env` file)

> **Can't find the API Keys section?** Make sure you're logged in as an administrator. In some Odoo versions, you may need to enable Developer Mode first: go to **Settings → scroll to bottom → click "Activate the developer mode"**.

### Step 3: Verify Credentials Work

Before proceeding, verify your credentials authenticate successfully:

```python
import xmlrpc.client

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(database, username, api_key, {})

if not uid:
    raise Exception("Auth failed — check database name, username, and API key")
print(f"Authenticated as UID: {uid}")
```

### What You Need Before Coding

| Item | Where to get it | Example |
|------|----------------|----------|
| Odoo URL | Your server admin / deployment config | `https://erp.example.com` |
| Database name | Ask admin or list via `common.db.list()` | `production_db` |
| Username | Your Odoo login email | `admin@example.com` |
| API Key | **Settings → Users → Your User → API Keys → New** | `abc123def456...` |

> 📖 **For detailed troubleshooting and best practices:** [See docs/authentication.md](docs/authentication.md)

---

## Prerequisites

**Python 3.8+** with standard library only:
```python
import xmlrpc.client  # Built-in, no pip install needed
```

**Odoo server requirements:**
- XML-RPC API enabled (default in Odoo Community/Enterprise)
- **API Key generated** (see "⚡ FIRST TIME? START HERE" section above — this is REQUIRED)
- Valid user credentials with appropriate access rights
- Network access to the Odoo instance (typically HTTPS port 443)

## Repository Structure

This skill includes comprehensive documentation and examples:

```
akdira/odoo-connector/
├── SKILL.md                          ← You are here
├── README.md                         ← Overview, installation, features
├── _meta.json                        ← Skill metadata
├── LICENSE                           ← MIT-0 license
├── .gitignore
├── docs/
│   ├── authentication.md             ← Login + API key setup guide
│   ├── installation.md               ← Installation & prerequisites
│   ├── quickstart.md                 ← Quick start tutorial
│   ├── api-reference.md              ← Full API reference (all models)
│   └── troubleshooting.md            ← Common errors & solutions
├── examples/
│   ├── README.md                     ← Examples overview
│   ├── sales-order.md                ← Sales order creation example
│   └── inventory-sync.md             ← Inventory sync scenario
├── scripts/
│   ├── test-connection.py            ← Test Odoo connection
│   └── bulk-import.py                ← Bulk data import script
├── CHANGELOG.md
├── CONTRIBUTING.md
└── SECURITY.md
```

**GitHub Repository:** https://github.com/akdira/odoo-connector
**ClawHub Skill Page:** https://clawhub.ai/akdira/odoo-connector

**Key files to read:**
- Authentication setup: [docs/authentication.md](docs/authentication.md)
- Quick start: [docs/quickstart.md](docs/quickstart.md)
- API reference: [docs/api-reference.md](docs/api-reference.md)
- Troubleshooting: [docs/troubleshooting.md](docs/troubleshooting.md)
- Examples: [examples/](examples/)

## Connection Setup

Every Odoo instance exposes two XML-RPC endpoints:

```
{BASE_URL}/xmlrpc/2/common    # Authentication + version info
{BASE_URL}/xmlrpc/2/object    # All data operations
```

### Basic Connection

```python
import xmlrpc.client

# Configuration
url = "https://your-odoo-instance.com"
database = "your_database_name"
username = "your_login"
password = "your_password"

# Create proxies
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
```

**Why ServerProxy instead of raw calls:** `ServerProxy` handles XML-RPC envelope wrapping, type conversion, and error handling automatically.

## Authentication

Authentication is a two-step process that returns a numeric user ID (UID).

### Step 1: Verify Connection

```python
version = common.version()
# Returns dict with server version info:
# {
#   'server_version': '17.0+e',
#   'server_version_info': [17, 0, 0, 'final', 0, ''],
#   'server_serie': '17.0',
#   'protocol_version': 1
# }
```

This confirms the server is reachable and responsive. Always do this first in your script.

### Step 2: Authenticate

```python
uid = common.authenticate(database, username, password, {})
```

- `database`: exact database name (case-sensitive)
- `username`: login email or username
- `password`: user's password
- `{}`: environment dict (can be empty)

**Returns:** Numeric user ID (e.g., `2` for admin), or raises `AuthenticationError` if credentials are wrong.

**Store the UID** — you need it for every subsequent operation.

### Authentication Errors

```python
try:
    uid = common.authenticate(database, username, password, {})
except Exception as e:
    print(f"Authentication failed: {e}")
    # Common causes:
    # - Wrong database name
    # - Invalid username/password
    # - User doesn't exist
    # - Database not accessible
```

## Core Operations

All data operations go through the `models` proxy using `execute_kw()`. This method has a consistent signature:

```python
models.execute_kw(
    database,      # string: database name
    uid,           # int: authenticated user ID
    password,      # string: password
    model_name,    # string: Odoo model (e.g., 'res.partner')
    method_name,   # string: method to call
    args,          # list: positional arguments
    kwargs         # dict: keyword arguments (optional)
)
```

### Search Records

Find records matching criteria. Returns list of matching IDs.

```python
# Search all partners
partner_ids = models.execute_kw(
    database, uid, password,
    'res.partner', 'search',
    [[]]  # Empty domain = match all
)
# Returns: [1, 2, 3, 5, 8, ...]

# Search with domain filter
customer_ids = models.execute_kw(
    database, uid, password,
    'res.partner', 'search',
    [[('customer_rank', '>', 0)]]  # Only customers
)

# Search with limits
recent_ids = models.execute_kw(
    database, uid, password,
    'res.partner', 'search',
    [[('create_date', '>', '2024-01-01')]],
    {'limit': 100, 'offset': 0, 'order': 'create_date DESC'}
)
```

**Domain syntax:** List of tuples `[(field, operator, value)]`

Common operators:
- `=` equals
- `!=` not equals
- `>` `<` `>=` `<=` numeric/date comparison
- `in` value in list: `[('state', 'in', ['draft', 'sent'])]`
- `not in` not in list
- `ilike` case-insensitive contains: `[('name', 'ilike', 'john')]`
- `like` case-sensitive contains
- `=like` pattern match with `%` and `_` (SQL LIKE)
- `&` AND between criteria (default)
- `|` OR between next two criteria
- `!` NOT the next criterion

**Multiple criteria are ANDed by default:**
```python
# Partners named John who are customers
domain = [
    ('name', 'ilike', 'john'),
    ('customer_rank', '>', 0)
]
```

**OR operator requires prefix:**
```python
# Partners named John OR Mary
domain = [
    '|',
    ('name', 'ilike', 'john'),
    ('name', 'ilike', 'mary')
]
```

### Read Records

Fetch field values for specific record IDs.

```python
# Read specific fields for partner ID 1
partner = models.execute_kw(
    database, uid, password,
    'res.partner', 'read',
    [[1]],  # List of IDs
    {'fields': ['name', 'email', 'phone', 'customer_rank']}
)
# Returns: [{'id': 1, 'name': 'John Doe', 'email': 'john@example.com', ...}]

# Read multiple records
partners = models.execute_kw(
    database, uid, password,
    'res.partner', 'read',
    [[1, 2, 3]],
    {'fields': ['name']}
)
```

**Important:** Fields use internal names. Common Odoo models:

| Model | Typical Fields |
|-------|---------------|
| `res.partner` | `name`, `email`, `phone`, `customer_rank`, `supplier_rank`, `company_id` |
| `res.users` | `login`, `name`, `email`, `active`, `groups_id` |
| `res.company` | `name`, `website`, `logo`, `currency_id` |
| `product.product` | `name`, `default_code`, `list_price`, `type` |
| `sale.order` | `name`, `partner_id`, `state`, `amount_total`, `date_order` |
| `account.move` | `name`, `partner_id`, `state`, `amount_total`, `invoice_date` |

### Search + Read in One Call

Combine search and read for efficiency:

```python
customers = models.execute_kw(
    database, uid, password,
    'res.partner', 'search_read',
    [[('customer_rank', '>', 0)]],  # Domain filter
    {
        'fields': ['name', 'email', 'phone'],
        'limit': 50,
        'offset': 0,
        'order': 'name ASC'
    }
)
# Returns: [{'id': 5, 'name': 'Alice', ...}, {'id': 8, 'name': 'Bob', ...}, ...]
```

This is more efficient than separate search + read calls (one round-trip instead of two).

### Create Records

> **⚠️ WARNING: Write Operations Affect Live Systems**
> Create/update/delete operations immediately modify the connected Odoo database. If connected to a production instance, these changes are real and may trigger downstream business workflows (notifications, invoices, inventory updates, etc.).
> - **Always test in a staging/development environment first**
> - **Verify you have proper authorization before writing to production**
> - **Consider using `search_read` first to check if records already exist**

Create new records:

```python
# Create a new partner
new_partner_id = models.execute_kw(
    database, uid, password,
    'res.partner', 'create',
    [{
        'name': 'Jane Smith',
        'email': 'jane@example.com',
        'phone': '+1-555-0123',
        'customer_rank': 1
    }]
)
# Returns: 42 (new record ID)
```

### Update Records

Modify existing records:

```python
# Update partner fields
result = models.execute_kw(
    database, uid, password,
    'res.partner', 'write',
    [[1], {'phone': '+1-555-9999', 'city': 'New York'}]
    #   ^ ID list  ^ fields to update
)
# Returns: True on success
```

**Note:** First argument to `write` is a list of IDs (allows batch updates).

### Delete Records

Remove records:

```python
result = models.execute_kw(
    database, uid, password,
    'res.partner', 'unlink',
    [[42]]  # List of IDs to delete
)
# Returns: True on success
```

**Warning:** Some models have constraints preventing deletion (e.g., records referenced by other transactions). Use with caution.

### Count Records

Get count without fetching data:

```python
count = models.execute_kw(
    database, uid, password,
    'res.partner', 'search_count',
    [[('customer_rank', '>', 0)]]
)
# Returns: 150
```

## Working with Fields

### Discover Model Fields

```python
fields = models.execute_kw(
    database, uid, password,
    'res.partner', 'fields_get',
    [[]],  # Empty list = all fields
    {'attributes': ['string', 'type', 'help', 'required']}
)
# Returns dict with field metadata
```

Useful for:
- Validating field names before read/write
- Understanding field types (selection lists, relation types)
- Getting help text for fields

### Field Types

Common Odoo field types:
- `char` / `text`: String fields
- `selection`: Dropdown with predefined values
- `boolean`: True/False
- `integer` / `float`: Numeric fields
- `date` / `datetime`: Date/time fields
- `many2one`: Foreign key to single record (returns dict `{'id': 1, 'name': 'Partner Name'}`)
- `one2many` / `many2many`: Reverse relations (returns list of IDs)

**Selection field values:**
```python
# Get available values for a selection field
fields = models.execute_kw(
    database, uid, password,
    'sale.order', 'fields_get',
    [[]],
    {'attributes': ['selection']}
)
state_values = fields['state']['selection']
# Returns: [('draft', 'Quotation'), ('sent', 'Quotation Sent'), ('sale', 'Sales Order'), ...]
```

## Common Real-World Examples

### Example 1: List All Active Users

```python
users = models.execute_kw(
    database, uid, password,
    'res.users', 'search_read',
    [[('active', '=', True)]],
    {'fields': ['login', 'name', 'email', 'create_date']}
)

for user in users:
    print(f"{user['name']} ({user['login']}) - {user['email']}")
```

### Example 2: Get Company Information

```python
company = models.execute_kw(
    database, uid, password,
    'res.company', 'read',
    [[1]],  # Company ID 1 is typically the main company
    {'fields': ['name', 'website', 'phone', 'email', 'city', 'country_id']}
)

print(f"Company: {company[0]['name']}")
print(f"Website: {company[0]['website']}")
```

### Example 3: Find Recent Sales Orders

```python
orders = models.execute_kw(
    database, uid, password,
    'sale.order', 'search_read',
    [[('state', 'in', ['sale', 'done'])]],
    {
        'fields': ['name', 'partner_id', 'amount_total', 'date_order'],
        'order': 'date_order DESC',
        'limit': 10
    }
)

for order in orders:
    partner_name = order['partner_id'][1]  # Many2one returns [id, name]
    print(f"{order['name']}: {partner_name} - ${order['amount_total']}")
```

### Example 4: Create a Customer with Address

> **⚠️ This creates a real record in the connected Odoo instance.** Ensure you're connected to the correct environment (staging vs production).

```python
new_customer = models.execute_kw(
    database, uid, password,
    'res.partner', 'create',
    [{
        'name': 'Acme Corporation',
        'email': 'contact@acme.com',
        'phone': '+62-21-1234567',
        'website': 'https://acme.com',
        'street': 'Jl. Sudirman No. 1',
        'city': 'Jakarta',
        'zip': '10220',
        'country_id': 102,  # Indonesia
        'customer_rank': 1
    }]
)
```

### Example 5: Execute Model-Specific Method

> **⚠️ CRITICAL: State-Changing Actions Trigger Downstream Workflows**
> Methods like `action_confirm`, `action_cancel`, or `action_post` are real business operations that may trigger:
> - Order fulfillment and shipping workflows
> - Invoice generation and payment processing
> - Inventory reservations and stock moves
> - Email notifications to customers
> - Accounting journal entries
> 
> **Always verify the order state and get explicit approval before executing state-changing actions on production systems.**

Some models have custom methods you can call:

```python
# Confirm a quotation (change state to 'sale')
# WARNING: This is a real business action - it may trigger fulfillment, invoicing, and notifications
models.execute_kw(
    database, uid, password,
    'sale.order', 'action_confirm',
    [[42]]  # Order ID 42
)

# Generate invoice from sales order
# WARNING: This creates actual invoices that affect accounting
models.execute_kw(
    database, uid, password,
    'sale.order', 'action_view_invoice',
    [[42]]
)
```

**Tip:** Check model source code or documentation for available methods.

### Example 6: Batch Update Multiple Records

```python
# Update multiple partners at once
partner_ids = [5, 8, 12, 15]
models.execute_kw(
    database, uid, password,
    'res.partner', 'write',
    [partner_ids, {'customer_rank': 0}]  # Set all to non-customers
)
```

## Error Handling

### Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `KeyError: 'ir.http'` | Database not initialized | Initialize with `odoo -i base -d dbname` |
| `ValueError: Invalid field 'xyz'` | Wrong field name | Check field name with `fields_get()` |
| `AccessError` | User lacks permissions | Use admin account or grant access rights |
| `AuthenticationError` | Wrong credentials | Verify database name, username, password |
| `500 Internal Server Error` | Module error or DB issue | Check Odoo server logs |
| `ValidationError` | Data constraint violated | Check required fields, unique constraints |

### Defensive Programming

```python
import xmlrpc.client

try:
    # Verify connection
    version = common.version()
    print(f"Connected to Odoo {version['server_version']}")
    
    # Authenticate
    uid = common.authenticate(database, username, password, {})
    if not uid:
        raise Exception("Authentication returned no UID")
    
    # Perform operations safely
    records = models.execute_kw(
        database, uid, password,
        'res.partner', 'search_read',
        [[('active', '=', True)]],
        {'fields': ['name'], 'limit': 5}
    )
    
    if not records:
        print("No records found")
    else:
        print(f"Found {len(records)} records")
    
except xmlrpc.client.Fault as e:
    print(f"Odoo error: {e.faultString}")
except Exception as e:
    print(f"Connection error: {e}")
```

## Tips and Best Practices

### Performance

- **Use `search_read` instead of separate `search` + `read`** — one call instead of two
- **Limit result sets** — don't fetch 10,000 records at once; use pagination with `limit` and `offset`
- **Request only needed fields** — don't use `fields=[]` (returns all fields) unless you actually need everything
- **Use `search_count` to check existence** — faster than `search` if you only need to know if records exist

### Security

- **Never hardcode credentials in scripts** — use environment variables or secure config files
- **Use least-privilege service accounts** — don't give your API user admin rights unless necessary
- **Validate inputs** — especially for create/write operations; Odoo will reject invalid data but it's better to prevent errors
- **Use HTTPS** — credentials travel in cleartext over HTTP

### Odoo 17/18/19 Differences

Some fields changed between versions:

| Version | Logo field | Notes |
|---------|-----------|-------|
| Odoo 17 | `logo_1920` | Standard logo field |
| Odoo 18/19 | `logo` | Simplified naming |
| Odoo 18/19 | `logo_web` | Web-specific variant |

**Always verify field names with `fields_get()`** if you encounter "Invalid field" errors.

### Debugging Tips

- **Test with admin account first** — eliminates permission issues
- **Use `fields_get` liberally** — discover exact field names and types
- **Check Odoo server logs** — XML-RPC errors often have detailed stack traces in logs
- **Start with simple queries** — verify connection works, then build complexity
- **Use search_count before search** — confirms records exist before fetching

### Working with Related Fields

**Many2one fields** return a tuple `(id, display_name)`:
```python
order = models.execute_kw(
    database, uid, password,
    'sale.order', 'read',
    [[1]],
    {'fields': ['partner_id', 'user_id']}
)
partner_name = order[0]['partner_id'][1]  # "John Doe"
partner_id = order[0]['partner_id'][0]    # 5
```

**One2many / Many2many** return list of IDs:
```python
products = models.execute_kw(
    database, uid, password,
    'sale.order', 'read',
    [[1]],
    {'fields': ['order_line']}
)
line_ids = products[0]['order_line']  # [10, 11, 12]
```

## Complete Script Template

```python
#!/usr/bin/env python3
"""
Odoo XML-RPC API Client Template
Usage: python3 odoo_client.py
"""

import xmlrpc.client
import sys

# Configuration
ODOO_URL = "https://your-odoo-instance.com"
ODOO_DB = "your_database"
ODOO_USERNAME = "your_login"
ODOO_PASSWORD = "your_password"

def connect():
    """Establish connection and authenticate"""
    try:
        common = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
        models = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/object")
        
        # Verify connection
        version = common.version()
        print(f"✓ Connected to Odoo {version['server_version']}")
        
        # Authenticate
        uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
        if not uid:
            raise Exception("Authentication failed: no UID returned")
        
        print(f"✓ Authenticated as UID {uid}")
        return common, models, uid
    except Exception as e:
        print(f"✗ Connection failed: {e}")
        sys.exit(1)

def main():
    """Main execution"""
    common, models, uid = connect()
    
    # Your operations here
    # Example: List first 5 partners
    partners = models.execute_kw(
        ODOO_DB, uid, ODOO_PASSWORD,
        'res.partner', 'search_read',
        [[('active', '=', True)]],
        {'fields': ['name', 'email'], 'limit': 5}
    )
    
    print(f"\nFound {len(partners)} partners:")
    for p in partners:
        print(f"  • {p['name']} ({p['email']})")

if __name__ == "__main__":
    main()
```

## Troubleshooting

### "Wrong login/password" but credentials are correct

Some Odoo configurations require the exact database name. Double-check:
```python
# List available databases
databases = common.db.list()
print(databases)
```

### "Access Error" despite correct credentials

Your user may lack model access. Check:
1. User is active (`active=True` in `res.users`)
2. User has read/write access to the model (check security groups in Odoo UI)
3. Record rules aren't filtering out the data

### Timeout on large queries

For large datasets:
- Use `limit` parameter (e.g., `limit=1000`)
- Process in batches with `offset`
- Increase XML-RPC client timeout:

```python
common = xmlrpc.client.ServerProxy(
    f"{ODOO_URL}/xmlrpc/2/common",
    allow_none=True,
    verbose=False
)
```

## See Also

- [Odoo External API Documentation](https://www.odoo.com/documentation/17.0/developer/reference/external_api.html)
- [Odoo ORM API Reference](https://www.odoo.com/documentation/17.0/developer/reference/backend/orm.html)
- This skill's internal notes: `/root/.openclaw/workspace/memory/odoo-xmlrpc-api-setup.md`
