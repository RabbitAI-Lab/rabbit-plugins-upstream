# Inventory Synchronization Example

Complete workflow for reading current inventory levels from Odoo and generating a sync report. This example demonstrates how to work with stock quants, products, and inventory adjustments using the XML-RPC API.

## Scenario

You need to extract current inventory levels from Odoo for all stocked products, compare them against expected values, and identify discrepancies. This is useful for integrating Odoo inventory data with external systems like e-commerce platforms, warehouses, or reporting dashboards.

## Prerequisites

- Inventory module installed in Odoo
- Products with `type` set to `product` (storable products)
- Stock quants populated (inventory has been received/adjusted at least once)
- API user with read access to `stock.quant` and `product.product`

## Complete Code

```python
#!/usr/bin/env python3
"""
Inventory Synchronization Example
Reads current stock levels and identifies low-stock items.
"""

import xmlrpc.client
from datetime import datetime

# ─── Configuration ───────────────────────────────────────────
URL = "https://your-odoo-instance.com"
DB = "your_database"
USERNAME = "your_api_user"
PASSWORD = "your_api_key"

LOW_STOCK_THRESHOLD = 10  # Alert when quantity is below this

# ─── Connection ──────────────────────────────────────────────
common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")

uid = common.authenticate(DB, USERNAME, PASSWORD, {})
print(f"Connected to Odoo | User: {uid}")

# ─── Step 1: Get all storable products ───────────────────────
products = models.execute_kw(
    DB, uid, PASSWORD,
    'product.product', 'search_read',
    [[('type', '=', 'product'), ('active', '=', True)]],
    {'fields': ['name', 'default_code', 'uom_id', 'categ_id']}
)

print(f"\nFound {len(products)} storable products")

# Build a lookup map for product details
product_map = {p['id']: p for p in products}

# ─── Step 2: Get stock quants (current inventory) ────────────
# Stock quants represent the real-time inventory by product + location
quants = models.execute_kw(
    DB, uid, PASSWORD,
    'stock.quant', 'search_read',
    [[
        ('product_id', 'in', list(product_map.keys())),
        ('quantity', '>', 0)  # Only locations with stock
    ]],
    {'fields': ['product_id', 'location_id', 'quantity', 'reserved_quantity']}
)

print(f"Retrieved {len(quants)} stock quant records")

# ─── Step 3: Aggregate inventory by product ──────────────────
inventory = {}

for quant in quants:
    product_id = quant['product_id'][0]
    qty_on_hand = quant['quantity']
    qty_reserved = quant['reserved_quantity']
    qty_available = qty_on_hand - qty_reserved
    location = quant['location_id'][1]

    if product_id not in inventory:
        inventory[product_id] = {
            'on_hand': 0,
            'reserved': 0,
            'available': 0,
            'locations': []
        }

    inventory[product_id]['on_hand'] += qty_on_hand
    inventory[product_id]['reserved'] += qty_reserved
    inventory[product_id]['available'] += qty_available
    inventory[product_id]['locations'].append({
        'name': location,
        'on_hand': qty_on_hand,
        'available': qty_available
    })

# ─── Step 4: Generate report ─────────────────────────────────
print("\n" + "=" * 70)
print(f"INVENTORY REPORT — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 70)

low_stock_items = []
out_of_stock = []

for product_id, data in sorted(inventory.items(), key=lambda x: x[1]['available']):
    product = product_map.get(product_id)
    if not product:
        continue

    sku = product.get('default_code', 'N/A')
    name = product['name']
    category = product['categ_id'][1] if product.get('categ_id') else 'Uncategorized'

    print(f"\n{sku} — {name}")
    print(f"  Category: {category}")
    print(f"  On Hand: {data['on_hand']}")
    print(f"  Reserved: {data['reserved']}")
    print(f"  Available: {data['available']}")

    if len(data['locations']) > 1:
        print(f"  Locations:")
        for loc in data['locations']:
            print(f"    - {loc['name']}: {loc['available']} available")

    # Track low stock / out of stock
    if data['available'] <= 0:
        out_of_stock.append((sku, name))
    elif data['available'] < LOW_STOCK_THRESHOLD:
        low_stock_items.append((sku, name, data['available']))

# ─── Step 5: Summary ─────────────────────────────────────────
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"Total products tracked: {len(inventory)}")
print(f"Products with stock: {sum(1 for d in inventory.values() if d['available'] > 0)}")
print(f"Out of stock: {len(out_of_stock)}")
print(f"Low stock (<{LOW_STOCK_THRESHOLD}): {len(low_stock_items)}")

if out_of_stock:
    print("\n⚠️  OUT OF STOCK:")
    for sku, name in out_of_stock:
        print(f"  - {sku}: {name}")

if low_stock_items:
    print(f"\n⚡ LOW STOCK:")
    for sku, name, qty in low_stock_items:
        print(f"  - {sku}: {name} ({qty} available)")
```

## Step-by-Step Explanation

### Step 1: Get Storable Products

We filter for `type = 'product'` because Odoo has three product types:
- `consu` — Consumable (no inventory tracking)
- `product` — Storable product (inventory tracked)
- `service` — Service (no inventory)

Only storable products have stock quants.

### Step 2: Read Stock Quants

Stock quants are Odoo's way of tracking real-time inventory. Each quant represents a quantity of a specific product at a specific location. A single product may have quants across multiple locations (warehouse, shelf, virtual locations).

Key fields:
- `quantity` — Total on-hand quantity at this location
- `reserved_quantity` — Quantity reserved for outgoing operations (sales orders, delivery orders)
- Available quantity = `quantity - reserved_quantity`

### Step 3: Aggregate by Product

Since a product can have quants in multiple locations, we aggregate them to get total inventory levels. This gives us a complete picture of how much stock is available across all locations.

### Step 4: Generate Report

The report shows per-product inventory with location breakdown, and flags items that need attention (low stock or out of stock).

### Step 5: Summary

A quick overview for decision-making: reorder triggers, procurement alerts.

## Extending This Example

### Trigger Replenishment Orders

When low stock is detected, you can automatically create replenishment orders:

```python
# Create an inventory adjustment (Odoo 17+)
for sku, name, qty in low_stock_items:
    product = next(p for p in products
                   if p.get('default_code') == sku)
    # Trigger reorder rule if configured
    models.execute_kw(
        DB, uid, PASSWORD,
        'product.product', 'action_replenishment',
        [[product['id']]]
    )
```

### Export to CSV for External Systems

```python
import csv

with open('inventory_sync.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['SKU', 'Product', 'On Hand', 'Reserved', 'Available'])
    for product_id, data in inventory.items():
        product = product_map.get(product_id)
        if product:
            writer.writerow([
                product.get('default_code', ''),
                product['name'],
                data['on_hand'],
                data['reserved'],
                data['available']
            ])
```

### Sync with E-Commerce Platform

After reading inventory from Odoo, push stock levels to your e-commerce platform:

```python
# Example: update Shopify inventory via their API
def update_shopify_inventory(sku, available_qty):
    """Push inventory level to Shopify."""
    # Implementation depends on your e-commerce platform
    pass

for product_id, data in inventory.items():
    product = product_map.get(product_id)
    if product and product.get('default_code'):
        update_shopify_inventory(product['default_code'], data['available'])
```

### Scheduled Execution

Run this script on a schedule using cron:

```bash
# Run every hour during business hours
0 8-18 * * * cd /path/to/scripts && python3 inventory-sync.py >> /var/log/inventory-sync.log 2>&1
```
