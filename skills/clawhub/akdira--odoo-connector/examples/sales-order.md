# Sales Order Creation Example

Complete walkthrough of creating, confirming, and managing a sales order through the Odoo XML-RPC API. This example covers the full sales order lifecycle from quotation to confirmed order.

## Scenario

You need to programmatically create a sales order for an existing customer with multiple product line items, confirm it, and verify the order was created correctly.

## Prerequisites

- An existing customer (res.partner) in Odoo
- Products (product.product) already created with known IDs
- Sales module installed in Odoo
- API user with access to `sale.order` and `sale.order.line`

## Complete Code

```python
#!/usr/bin/env python3
"""
Sales Order Creation Example
Creates a quotation, adds line items, and confirms it.
"""

import xmlrpc.client

# ─── Configuration ───────────────────────────────────────────
URL = "https://your-odoo-instance.com"
DB = "your_database"
USERNAME = "your_api_user"
PASSWORD = "your_api_key"

# ─── Connection ──────────────────────────────────────────────
common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")

uid = common.authenticate(DB, USERNAME, PASSWORD, {})
print(f"Authenticated as user {uid}")

# ─── Step 1: Find or verify the customer ─────────────────────
CUSTOMER_EMAIL = "customer@example.com"

customers = models.execute_kw(
    DB, uid, PASSWORD,
    'res.partner', 'search_read',
    [[('email', '=', CUSTOMER_EMAIL)]],
    {'fields': ['name', 'email', 'customer_rank']}
)

if not customers:
    raise Exception(f"Customer {CUSTOMER_EMAIL} not found")

customer = customers[0]
print(f"Customer: {customer['name']} (ID: {customer['id']})")

# ─── Step 2: Find products ───────────────────────────────────
PRODUCT_CODES = ["PROD-001", "PROD-002"]

products = models.execute_kw(
    DB, uid, PASSWORD,
    'product.product', 'search_read',
    [[('default_code', 'in', PRODUCT_CODES)]],
    {'fields': ['name', 'default_code', 'list_price']}
)

product_map = {p['default_code']: p for p in products}
print(f"Found {len(products)} products")

for code, prod in product_map.items():
    print(f"  - {prod['name']} ({code}): ${prod['list_price']}")

# ─── Step 3: Create the sales order ──────────────────────────
order_values = {
    'partner_id': customer['id'],
    'note': 'Created via XML-RPC API',
}

order_id = models.execute_kw(
    DB, uid, PASSWORD,
    'sale.order', 'create',
    [order_values]
)
print(f"\nCreated quotation ID: {order_id}")

# ─── Step 4: Add line items ──────────────────────────────────
order_lines = [
    {'product_id': product_map['PROD-001']['id'], 'product_uom_qty': 5},
    {'product_id': product_map['PROD-002']['id'], 'product_uom_qty': 10},
]

for line in order_lines:
    line['order_id'] = order_id
    models.execute_kw(
        DB, uid, PASSWORD,
        'sale.order.line', 'create',
        [line]
    )
    print(f"  Added product {line['product_id']} x{line['product_uom_qty']}")

# ─── Step 5: Verify order contents ───────────────────────────
order = models.execute_kw(
    DB, uid, PASSWORD,
    'sale.order', 'read',
    [[order_id]],
    {'fields': ['name', 'state', 'amount_total', 'amount_untaxed', 'order_line']}
)[0]

print(f"\nOrder summary:")
print(f"  Reference: {order['name']}")
print(f"  State: {order['state']}")
print(f"  Untaxed: ${order['amount_untaxed']}")
print(f"  Total: ${order['amount_total']}")
print(f"  Lines: {len(order['order_line'])}")

# ─── Step 6: Confirm the order ───────────────────────────────
models.execute_kw(
    DB, uid, PASSWORD,
    'sale.order', 'action_confirm',
    [[order_id]]
)

# Verify state changed
order_after = models.execute_kw(
    DB, uid, PASSWORD,
    'sale.order', 'read',
    [[order_id]],
    {'fields': ['name', 'state']}
)[0]

print(f"\nOrder confirmed! State: {order_after['state']}")
# State should now be 'sale' (confirmed sales order)
```

## Step-by-Step Explanation

### Step 1: Find the Customer

We search for the customer by email. The `customer_rank > 0` check confirms they are flagged as a customer. If the customer does not exist, the script raises an error rather than creating a new one (to avoid duplicate creation).

### Step 2: Find Products

We look up products by their internal reference code (`default_code`). This is more reliable than using names because codes are unique. We build a map for easy reference when creating line items.

### Step 3: Create the Sales Order

Creating a sales order requires only the `partner_id`. The order starts in `draft` state (quotation). Additional optional fields include `payment_term_id`, `pricelist_id`, and `user_id` (salesperson).

### Step 4: Add Line Items

Each line item requires `order_id`, `product_id`, and `product_uom_qty` (quantity). The unit price is automatically populated from the product's pricelist when the line is created. You can override it by adding `price_unit` to the line values.

### Step 5: Verify

Always read back the order after creation to confirm totals are correct and all line items were added. This catches issues like missing products or incorrect quantities.

### Step 6: Confirm

`action_confirm` transitions the order from `draft` (quotation) to `sale` (confirmed order). After confirmation, the order is locked for editing unless you use `action_draft` to reset it.

## Common Variations

### Setting Custom Prices

```python
# Override the unit price on a line item
models.execute_kw(
    DB, uid, PASSWORD,
    'sale.order.line', 'create',
    [{
        'order_id': order_id,
        'product_id': product_id,
        'product_uom_qty': 10,
        'price_unit': 99.99  # Custom price
    }]
)
```

### Adding a Discount

```python
# If discounts are enabled in Odoo settings
models.execute_kw(
    DB, uid, PASSWORD,
    'sale.order.line', 'create',
    [{
        'order_id': order_id,
        'product_id': product_id,
        'product_uom_qty': 5,
        'discount': 10  # 10% discount
    }]
)
```

### Creating a Rush Order

```python
# Set a specific deadline and priority
order_values = {
    'partner_id': customer_id,
    'date_order': '2024-06-15 09:00:00',
    'priority': '1',  # Urgent
}
```

## Error Handling for Production

```python
try:
    order_id = models.execute_kw(
        DB, uid, PASSWORD,
        'sale.order', 'create',
        [order_values]
    )
except xmlrpc.client.Fault as e:
    if 'Required' in e.faultString:
        print(f"Missing required field: {e.faultString}")
    elif 'access' in e.faultString.lower():
        print(f"Permission denied: {e.faultString}")
    else:
        print(f"Odoo error: {e.faultString}")
```
