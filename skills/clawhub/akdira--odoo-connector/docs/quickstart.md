# Quick Start Guide

Get up and running with the Odoo Connector in under 5 minutes. This guide walks you through your first connection, a basic query, and creating your first record.

## Step 1: Set Up Your Connection

Create a file called `odoo_config.py` to store your connection settings:

```python
# odoo_config.py — Connection configuration
# DO NOT commit this file with real credentials

URL = "https://your-odoo-instance.com"
DB = "your_database_name"
USERNAME = "your_api_user"
PASSWORD = "your_api_key"
```

In production, replace these values with environment variable reads:

```python
import os

URL = os.environ["ODOO_URL"]
DB = os.environ["ODOO_DB"]
USERNAME = os.environ["ODOO_USERNAME"]
PASSWORD = os.environ["ODOO_PASSWORD"]
```

## Step 2: Connect and Authenticate

Create `main.py` with the following content:

```python
#!/usr/bin/env python3
"""Quick start example — connect to Odoo and list partners."""

import xmlrpc.client
from odoo_config import URL, DB, USERNAME, PASSWORD

# Step 1: Create XML-RPC proxies
common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")

# Step 2: Verify the server is reachable
version = common.version()
print(f"Connected to Odoo {version['server_version']}")

# Step 3: Authenticate
uid = common.authenticate(DB, USERNAME, PASSWORD, {})
print(f"Authenticated as user ID: {uid}")

# Step 4: Query partners
partners = models.execute_kw(
    DB, uid, PASSWORD,
    'res.partner', 'search_read',
    [[('customer_rank', '>', 0)]],
    {'fields': ['name', 'email', 'phone'], 'limit': 5}
)

print(f"\nTop 5 customers:")
for p in partners:
    print(f"  - {p['name']} | {p.get('email', 'N/A')} | {p.get('phone', 'N/A')}")
```

Run it:

```bash
python3 main.py
```

Expected output:

```
Connected to Odoo 17.0+e
Authenticated as user ID: 2

Top 5 customers:
  - Acme Corporation | contact@acme.com | +62-21-1234567
  - Global Tech | info@globaltech.io | +1-555-0100
  ...
```

If you see version info and a list of partners, congratulations — your connection is working.

## Step 3: Create a Record

Extend your script to create a new customer:

```python
# Create a new partner
new_id = models.execute_kw(
    DB, uid, PASSWORD,
    'res.partner', 'create',
    [{
        'name': 'Test Customer',
        'email': 'test@example.com',
        'customer_rank': 1
    }]
)
print(f"Created partner with ID: {new_id}")
```

## Step 4: Explore Common Operations

Here is a cheat sheet of the most frequently used operations. All operations follow the same pattern: `models.execute_kw(DB, uid, PASSWORD, model, method, args, kwargs)`.

### Search for Records

```python
# Find all draft sales orders
order_ids = models.execute_kw(
    DB, uid, PASSWORD,
    'sale.order', 'search',
    [[('state', '=', 'draft')]]
)
print(f"Found {len(order_ids)} draft orders: {order_ids}")
```

### Read Specific Fields

```python
# Get details of a specific order
orders = models.execute_kw(
    DB, uid, PASSWORD,
    'sale.order', 'read',
    [[order_ids[0]]],
    {'fields': ['name', 'partner_id', 'amount_total', 'state']}
)
print(f"Order: {orders[0]['name']}, Total: {orders[0]['amount_total']}")
```

### Update a Record

```python
# Update a partner's phone number
models.execute_kw(
    DB, uid, PASSWORD,
    'res.partner', 'write',
    [[new_id], {'phone': '+62-812-0000-0000'}]
)
print(f"Updated partner {new_id}")
```

### Delete a Record

```python
# Remove the test partner we created
models.execute_kw(
    DB, uid, PASSWORD,
    'res.partner', 'unlink',
    [[new_id]]
)
print(f"Deleted partner {new_id}")
```

## Step 5: Discover Available Fields

When working with a new model, use `fields_get` to discover what fields are available:

```python
fields = models.execute_kw(
    DB, uid, PASSWORD,
    'sale.order', 'fields_get',
    [[]],
    {'attributes': ['string', 'type', 'required']}
)

for name, meta in sorted(fields.items())[:10]:
    print(f"  {name}: {meta['type']} ({meta['string']})")
```

This is invaluable when you are unfamiliar with a model's structure.

## Next Steps

Once you are comfortable with basic operations:

- Read the [API Reference](api-reference.md) for a complete listing of supported models and operations
- Check the [Examples](../examples/README.md) directory for real-world scenarios like sales order creation and inventory synchronization
- Review [Troubleshooting](troubleshooting.md) if you run into common errors

## Tips for Success

1. **Always start with `search_count`** before large `search_read` queries to understand the scale of data you are about to fetch
2. **Request only the fields you need** — fetching all fields wastes bandwidth and slows down responses
3. **Use pagination** — always include `limit` and `offset` parameters for large datasets
4. **Test with admin first** — if queries fail, verify with an admin account to rule out permission issues before debugging field names or domains
5. **Use `fields_get` liberally** — it is the fastest way to discover the correct field names and expected value types for any model
