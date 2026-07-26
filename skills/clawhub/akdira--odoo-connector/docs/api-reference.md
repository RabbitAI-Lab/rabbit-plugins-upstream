# API Reference

Complete reference for all Odoo models and operations supported by the Odoo Connector skill. Each section covers the model name, common fields, and typical operations.

## Core API Pattern

Every operation follows the same calling convention:

```python
models.execute_kw(
    database,    # str: database name
    uid,         # int: authenticated user ID
    password,    # str: password or API key
    model,       # str: Odoo model name (e.g., 'res.partner')
    method,      # str: method name (e.g., 'search_read')
    args,        # list: positional arguments
    kwargs       # dict: keyword arguments (optional)
)
```

## Universal Methods

These methods are available on every Odoo model:

| Method | Description | Returns |
|--------|-------------|---------|
| `search` | Find record IDs matching a domain | `list[int]` |
| `search_count` | Count records matching a domain | `int` |
| `read` | Fetch field values for given IDs | `list[dict]` |
| `search_read` | Combined search + read | `list[dict]` |
| `create` | Create a new record | `int` (new ID) |
| `write` | Update existing records | `bool` |
| `unlink` | Delete records | `bool` |
| `fields_get` | Get model field metadata | `dict` |
| `name_get` | Get display names for IDs | `list[tuple]` |

## Domain Filter Syntax

Domains are lists of criteria that filter which records are returned. Each criterion is a tuple of `(field, operator, value)`.

### Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Equals | `('state', '=', 'draft')` |
| `!=` | Not equals | `('state', '!=', 'cancel')` |
| `>` | Greater than | ('amount_total', '>', 1000) |
| `>=` | Greater than or equal | `('quantity', '>=', 10)` |
| `<` | Less than | `('priority', '<', 3)` |
| `<=` | Less than or equal | `('create_date', '<=', '2024-12-31')` |
| `in` | Value in list | `('state', 'in', ['draft', 'sent'])` |
| `not in` | Value not in list | `('state', 'not in', ['done', 'cancel'])` |
| `ilike` | Case-insensitive contains | `('name', 'ilike', 'acme')` |
| `like` | Case-sensitive contains | `('name', 'like', 'Acme')` |
| `=like` | SQL LIKE pattern | `('name', '=like', 'Acme%')` |
| `=ilike` | Case-insensitive SQL LIKE | `('name', '=ilike', 'acme%')` |

### Logical Operators

| Operator | Description | Usage |
|----------|-------------|-------|
| `&` | AND (default) | Implicit between criteria |
| `\|` | OR | Prefix before two criteria |
| `!` | NOT | Prefix before one criterion |

### Example Domains

```python
# AND (default): partners in Jakarta who are customers
[
    ('city', '=', 'Jakarta'),
    ('customer_rank', '>', 0)
]

# OR: partners named John or Mary
[
    '|',
    ('name', 'ilike', 'john'),
    ('name', 'ilike', 'mary')
]

# NOT: active partners who are NOT suppliers
[
    ('active', '=', True),
    ('!', ('supplier_rank', '>', 0))
]

# Complex: (city = Jakarta OR city = Bandung) AND is customer
[
    '&',
    '|',
    ('city', '=', 'Jakarta'),
    ('city', '=', 'Bandung'),
    ('customer_rank', '>', 0)
]
```

## Model Reference

### res.partner — Contacts / Partners

The most fundamental model in Odoo. Represents customers, vendors, employees, and any other contact.

**Key Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `name` | char | Contact display name |
| `email` | char | Email address |
| `phone` | char | Phone number |
| `mobile` | char | Mobile number |
| `website` | char | Website URL |
| `street`, `street2` | char | Address lines |
| `city` | char | City |
| `zip` | char | Postal code |
| `state_id` | many2one | State/Province |
| `country_id` | many2one | Country |
| `customer_rank` | float | Customer ranking (>0 = customer) |
| `supplier_rank` | float | Supplier ranking (>0 = supplier) |
| `company_id` | many2one | Associated company |
| `parent_id` | many2one | Parent partner |
| `active` | boolean | Active flag |
| `image_1920` | binary | Profile image (Odoo 17) |
| `category_id` | many2many | Contact tags |

**Common Operations:**

```python
# Search customers
models.execute_kw(db, uid, pw, 'res.partner', 'search',
    [[('customer_rank', '>', 0)]])

# Create a contact
models.execute_kw(db, uid, pw, 'res.partner', 'create',
    [{'name': 'New Customer', 'email': 'new@example.com', 'customer_rank': 1}])
```

### res.users — Users

Internal system users with login access.

**Key Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `login` | char | Login username (usually email) |
| `name` | char | Full name |
| `email` | char | Email address |
| `active` | boolean | Active status |
| `groups_id` | many2many | Security groups |
| `company_id` | many2one | Primary company |
| `company_ids` | many2many | Allowed companies |

### res.company — Companies

Multi-company support model.

**Key Fields:** `name`, `website`, `phone`, `email`, `logo`, `currency_id`, `country_id`.

### product.product — Products

Individual product variants.

**Key Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `name` | char | Product name |
| `default_code` | char | Internal reference / SKU |
| `barcode` | char | Barcode (EAN, UPC) |
| `list_price` | float | Sales price |
| `standard_price` | float | Cost price |
| `type` | selection | Product type: `consu`, `service`, `product` |
| `categ_id` | many2one | Product category |
| `active` | boolean | Active flag |
| `uom_id` | many2one | Unit of measure |
| `description` | text | Internal notes |

### sale.order — Sales Orders

Sales order records including quotations and confirmed orders.

**Key Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `name` | char | Order reference (e.g., S00001) |
| `partner_id` | many2one | Customer |
| `state` | selection | Status: draft, sent, sale, done, cancel |
| `amount_total` | float | Total amount |
| `amount_untaxed` | float | Subtotal (before tax) |
| `date_order` | datetime | Order date |
| `user_id` | many2one | Salesperson |
| `order_line` | one2many | Order line IDs |
| `currency_id` | many2one | Currency |
| `payment_term_id` | many2one | Payment terms |

**Key Methods:**

| Method | Description |
|--------|-------------|
| `action_confirm` | Confirm quotation → sales order |
| `action_cancel` | Cancel the order |
| `action_draft` | Reset to quotation |
| `action_done` | Mark as done (lock) |
| `action_view_invoice` | View/create invoices |

### sale.order.line — Sales Order Lines

Individual line items within a sales order.

**Key Fields:** `order_id`, `product_id`, `name` (description), `product_uom_qty` (quantity), `price_unit`, `price_subtotal`, `tax_id`.

### purchase.order — Purchase Orders

**Key Fields:** `name`, `partner_id` (vendor), `state` (draft, sent, to approve, purchase, done, cancel), `amount_total`, `date_order`, `user_id`, `order_line`.

### stock.picking — Inventory Transfers / Pickings

**Key Fields:** `name`, `partner_id`, `state` (draft, waiting, confirmed, assigned, done, cancel), `picking_type_id`, `location_id`, `location_dest_id`, `move_ids`, `scheduled_date`.

### stock.move — Stock Moves

Individual product movements within a picking.

**Key Fields:** `name`, `product_id`, `product_uom_qty`, `location_id`, `location_dest_id`, `state`, `picking_id`.

### stock.quant — Stock Quants (Current Inventory)

Real-time inventory levels by product and location.

**Key Fields:** `product_id`, `location_id`, `quantity`, `reserved_quantity`, `available_quantity` (computed).

### account.move — Invoices / Journal Entries

**Key Fields:** `name`, `partner_id`, `state` (draft, posted, cancel), `move_type` (entry, out_invoice, in_invoice, etc.), `amount_total`, `invoice_date`, `invoice_date_due`, `line_ids`.

### account.payment — Payments

**Key Fields:** `name`, `partner_id`, `amount`, `payment_type` (inbound/outbound), `state`, `date`, `journal_id`.

### crm.lead — CRM Leads / Opportunities

**Key Fields:** `name`, `partner_id`, `type` (lead/opportunity), `stage_id`, `priority`, `expected_revenue`, `probability`, `user_id`, `team_id`, `description`.

### hr.employee — Employees

**Key Fields:** `name`, `work_email`, `work_phone`, `department_id`, `job_id`, `company_id`, `parent_id`, `active`.

### project.project — Projects

**Key Fields:** `name`, `user_id` (project manager), `partner_id`, `date_start`, `date`, `active`, `task_ids`.

### project.task — Tasks

**Key Fields:** `name`, `project_id`, `user_ids`, `stage_id`, `priority`, `date_deadline`, `description`, `parent_id`.

### mrp.production — Manufacturing Orders

**Key Fields:** `name`, `product_id`, `product_qty`, `bom_id`, `state` (draft, confirmed, progress, done, cancel), `date_start`, `date_finished`.

### mrp.bom — Bills of Materials

**Key Fields:** `name`, `product_id`, `product_qty`, `bom_line_ids`, `type` (manufacture/kit), `company_id`.

## Pagination Parameters

For `search`, `search_read`, and similar methods, use these keyword arguments:

```python
{
    'limit': 100,      # Max records to return
    'offset': 0,       # Skip first N records
    'order': 'name ASC'  # Sort order (field ASC/DESC)
}
```

**Best practice:** Always include `limit` to avoid accidentally fetching thousands of records.

## Return Value Types

Understanding what Odoo returns for different field types:

| Field Type | Read Returns | Write Expects |
|-----------|-------------|---------------|
| `char` | `"string"` | `"string"` |
| `integer` | `42` | `42` |
| `float` | `3.14` | `3.14` |
| `boolean` | `True` / `False` | `True` / `False` |
| `date` | `"2024-01-15"` | `"2024-01-15"` |
| `datetime` | `"2024-01-15 10:30:00"` | `"2024-01-15 10:30:00"` |
| `many2one` | `[1, "Name"]` or `False` | `1` (ID only) |
| `one2many` / `many2many` | `[1, 2, 3]` | Command list (see below) |

### Many2many / One2many Write Commands

When writing to relational fields, use these command tuples:

```python
(0, 0, {values})    # Create new related record
(1, id, {values})   # Update existing related record
(2, id, 0)          # Delete related record
(3, id, 0)          # Unlink (remove relation, don't delete)
(4, id, 0)          # Link to existing record
(5, 0, 0)           # Unlink all
(6, 0, [ids])       # Replace all with given IDs
```

Example:

```python
# Add tags to a partner
models.execute_kw(db, uid, pw, 'res.partner', 'write',
    [[partner_id], {'category_id': [(4, tag_id, 0)]}])
```
