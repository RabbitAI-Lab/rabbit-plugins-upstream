# Examples

Real-world scenarios demonstrating how to use the Odoo Connector for common business automation tasks. Each example includes complete, runnable code and step-by-step explanations.

## Available Examples

| Example | Description | Key Models |
|---------|-------------|------------|
| [Sales Order Creation](sales-order.md) | Create and confirm a complete sales order with line items | `sale.order`, `sale.order.line`, `res.partner` |
| [Inventory Synchronization](inventory-sync.md) | Sync inventory levels between systems using stock quants | `stock.quant`, `product.product`, `stock.picking` |

## How to Use These Examples

Each example follows the same pattern:

1. **Setup** — Connection configuration and authentication
2. **Prerequisites** — Required data that must exist before running
3. **Implementation** — Step-by-step code with explanations
4. **Verification** — How to confirm the operation succeeded

### Running the Examples

Copy the code from each example into a Python file, update the connection configuration at the top, and run:

```bash
python3 example_name.py
```

All examples use only Python's standard library (`xmlrpc.client`). No additional packages are required.

### Customizing for Your Use Case

These examples are templates. Adapt them by:

- Changing domain filters to match your data
- Adding error handling for your specific failure modes
- Adjusting field values to match your Odoo configuration
- Combining multiple operations into workflows

## Prerequisites for All Examples

Before running any example, ensure:

1. You have a working Odoo connection (verify with `scripts/test-connection.py`)
2. The relevant Odoo modules are installed (Sales, Inventory, CRM, etc.)
3. Your API user has read/write access to the models used in the example
4. You understand the domain filter syntax (see [API Reference](../docs/api-reference.md))

## Additional Patterns

### Retry Logic

For production scripts, add retry logic around XML-RPC calls to handle transient network errors:

```python
import time

def retry_rpc(func, max_retries=3, delay=2):
    """Retry an XML-RPC call on transient errors."""
    for attempt in range(max_retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            if attempt < max_retries - 1:
                time.sleep(delay * (attempt + 1))
            else:
                raise
```

### Logging

Add logging to track operations for debugging:

```python
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger('odoo-connector')

# Usage
logger.info(f"Created sales order {order_name} for partner {partner_name}")
logger.warning(f"Low stock for product {product_name}: {qty} units remaining")
logger.error(f"Failed to create record: {error}")
```

### Dry Run Mode

For destructive operations, implement a dry-run mode:

```python
DRY_RUN = True  # Set to False to actually execute

if not DRY_RUN:
    models.execute_kw(db, uid, pw, 'res.partner', 'unlink', [[partner_id]])
    logger.info(f"Deleted partner {partner_id}")
else:
    logger.info(f"[DRY RUN] Would delete partner {partner_id}")
```
