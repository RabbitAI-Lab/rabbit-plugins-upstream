# Troubleshooting Guide

Common errors, their causes, and solutions when working with the Odoo Connector skill.

## Connection Errors

### AuthenticationError

**Error message:**
```
xmlrpc.client.Fault: <Fault cannot authenticate: ...>
```

**Causes and solutions:**

1. **Wrong database name** — Database names are case-sensitive. Verify with `common.version()` first, then check your database name in Odoo's database manager or by querying the server's database list.

2. **Invalid username** — The username must be the login field (usually email), not the display name. Check in Odoo under Settings → Users.

3. **Wrong password or expired API key** — Regenerate the API key in Odoo. API keys do not expire by default, but they can be manually revoked.

4. **User is inactive** — Inactive users cannot authenticate. Check the `active` field on the user record.

**Debug steps:**

```python
# Step 1: Is the server reachable?
common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
version = common.version()
print(version)  # If this fails, server is unreachable

# Step 2: Are credentials correct?
uid = common.authenticate(DB, USERNAME, PASSWORD, {})
# If this fails, credentials are wrong
```

### Connection Refused / Timeout

**Error message:**
```
ConnectionRefusedError: [Errno 111] Connection refused
```
or
```
TimeoutError: timed out
```

**Causes and solutions:**

1. **Odoo server is down** — Check if the Odoo service is running: `docker ps | grep odoo` or `systemctl status odoo`.

2. **Wrong URL** — Verify the URL includes the protocol (`https://`) and correct port. Default Odoo port is 8069 (HTTP) or 443 (HTTPS through reverse proxy).

3. **Firewall blocking** — Check firewall rules: `sudo ufw status` or `iptables -L`. Ensure port 8069/443 is open.

4. **DNS resolution failure** — If using a domain name, verify DNS: `dig your-odoo-domain.com`.

5. **SSL certificate issues** — For self-signed certificates in development, Python may reject the connection. For testing only:
   ```python
   import ssl
   ssl._create_default_https_context = ssl._create_unverified_context
   ```
   **Never use this in production** — obtain a proper certificate instead.

### KeyError: 'ir.http'

**Error message:**
```
KeyError: 'ir.http'
```

**Cause:** The database exists but has not been initialized with the base module.

**Solution:** Initialize the database:
```bash
odoo -i base -d your_database_name
```

Or in Docker:
```bash
docker exec odoo-container odoo -i base -d your_database_name
```

## Data Operation Errors

### ValueError: Invalid field 'xyz'

**Error message:**
```
ValueError: Invalid field 'xyz' on model 'res.partner'
```

**Causes and solutions:**

1. **Typo in field name** — Field names are case-sensitive. Use `fields_get()` to discover exact names:
   ```python
   fields = models.execute_kw(db, uid, pw, 'res.partner', 'fields_get', [[]])
   print([f for f in fields.keys() if 'name' in f.lower()])
   ```

2. **Version differences** — Some fields were renamed between Odoo versions. For example, the logo field changed from `logo_1920` (Odoo 17) to `logo` (Odoo 18+). Always verify with `fields_get()` when upgrading.

3. **Module not installed** — If the field belongs to an optional module (e.g., CRM, Inventory), that module must be installed. Check installed apps in Odoo.

### AccessError

**Error message:**
```
odoo.exceptions.AccessError: The requested operation cannot be completed due to security restrictions.
```

**Cause:** The authenticated user does not have permission for the requested operation on the target model.

**Solutions:**

1. **Check user access rights** — In Odoo, go to Settings → Users, select the user, and verify they have appropriate access (Read/Write/Create/Delete) for the model.

2. **Use a service account** — Create a dedicated API user with only the permissions needed for your integration. This is more secure than using an admin account.

3. **Record rules** — Odoo may have record rules that restrict access to specific records even if the user has model-level access. Check Settings → Security → Record Rules.

### ValidationError

**Error message:**
```
odoo.exceptions.ValidationError: The value for field '...' is not valid.
```

**Common causes:**

1. **Required field missing** — Check which fields are required:
   ```python
   fields = models.execute_kw(db, uid, pw, 'model.name', 'fields_get', [[]],
       {'attributes': ['required']})
   required = [f for f, m in fields.items() if m.get('required')]
   ```

2. **Invalid selection value** — For selection fields, check the allowed values:
   ```python
   fields = models.execute_kw(db, uid, pw, 'sale.order', 'fields_get', [[]],
       {'attributes': ['selection']})
   print(fields['state']['selection'])
   ```

3. **Unique constraint violation** — Some fields must be unique (e.g., `default_code` for products). Check if a record with the same value already exists.

4. **Data type mismatch** — Passing a string when an integer is expected, or vice versa. Check field types with `fields_get()`.

## Performance Issues

### Slow Queries

**Symptoms:** Queries take longer than 5-10 seconds.

**Solutions:**

1. **Add indexes** — Custom fields may lack database indexes. This requires server-side configuration.

2. **Reduce result set** — Use `limit` and only request needed fields:
   ```python
   # BAD: Fetches everything
   records = models.execute_kw(db, uid, pw, 'res.partner', 'search_read',
       [[]], {'fields': []})
   
   # GOOD: Fetches only what you need
   records = models.execute_kw(db, uid, pw, 'res.partner', 'search_read',
       [[('customer_rank', '>', 0)]], {
           'fields': ['name', 'email'],
           'limit': 100
       })
   ```

3. **Avoid N+1 queries** — Use `search_read` instead of separate `search` + `read` calls.

4. **Batch operations** — Use batch `write` instead of individual updates:
   ```python
   # BAD: One call per record
   for id in ids:
       models.execute_kw(db, uid, pw, 'res.partner', 'write', [[id], {'city': 'Jakarta'}])
   
   # GOOD: One call for all records
   models.execute_kw(db, uid, pw, 'res.partner', 'write', [ids, {'city': 'Jakarta'}])
   ```

### 500 Internal Server Error

**Error message:**
```
xmlrpc.client.Fault: <Fault 500: ...>
```

**Cause:** Usually a server-side error in Odoo — a module bug, corrupted data, or server misconfiguration.

**Solutions:**

1. **Check Odoo server logs** — The log will contain the full Python traceback:
   ```bash
   docker logs odoo-container --tail 100
   ```

2. **Check if a specific record triggers it** — Try the same operation on different record IDs. If only certain records fail, there may be data corruption or unusual data.

3. **Simplify the operation** — Break complex operations into smaller steps to isolate the failing part.

## XML-RPC Specific Issues

### Boolean Values in Domains

Odoo XML-RPC requires Python/Java boolean types, not strings:

```python
# WRONG
domain = [('active', '=', 'True')]

# CORRECT
domain = [('active', '=', True)]
```

### Many2one Field Writes

When creating or writing a Many2one field, pass the ID (integer), not a dict:

```python
# WRONG
{'partner_id': {'id': 5, 'name': 'John'}}

# CORRECT
{'partner_id': 5}
```

### Date and DateTime Formats

Odoo expects dates as strings in specific formats:

```python
# Date field: YYYY-MM-DD
{'invoice_date': '2024-01-15'}

# DateTime field: YYYY-MM-DD HH:MM:SS
{'date_order': '2024-01-15 10:30:00'}
```

### Empty Lists vs False

Odoo distinguishes between empty list `[]` and `False` for relational fields:

```python
# Clear a many2many field
{'tag_ids': [(5, 0, 0)]}    # Unlink all

# Check for empty many2one
if not record['partner_id']:
    # partner_id is False (not set), not an empty list
    pass
```

## Getting Help

If you cannot resolve an issue:

1. Check the [API Reference](api-reference.md) for correct method signatures
2. Use `fields_get()` to verify field names and types
3. Check Odoo server logs for detailed error messages
4. Test with admin credentials to rule out permission issues
5. Verify your Odoo version — some fields and methods differ between versions
