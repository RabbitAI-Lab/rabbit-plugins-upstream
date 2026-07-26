# @akdira/odoo-connector

OpenClaw AI Agent skill for Odoo 17/18/19 XML-RPC API integration.

## Features

- Authentication (Common + Object endpoints)
- CRUD operations (read, create, write, unlink)
- Domain filters (conditional queries)
- Error handling (80+ Odoo operations covered)
- Compatible with Odoo 17, 18, 19

## Installation

```bash
openclaw skills install @akdira/odoo-connector
```

## Usage

```bash
openclaw odoo connect --host https://your-odoo.com --db yourdb --user admin --password ****
openclaw odoo call --model res.partner --method search_read --fields '["name","email"]' --domain '[["active","=",true]]'
openclaw odoo call --model sale.order --method create --values '{"partner_id": 1, "order_line": [...]}'
```

## Supported Operations

80+ Odoo XML-RPC operations including:

| Category | Operations |
|----------|-----------|
| Authentication | `connect`, `test_connection` |
| Models | CRUD (read, create, write, unlink), `search`, `search_read` |
| Sales | `sale.order`, `sale.order.line` |
| Purchase | `purchase.order`, `purchase.order.line` |
| Inventory | `stock.picking`, `stock.move`, `stock.quant` |
| CRM | `crm.lead`, `crm.opportunity` |
| Accounting | `account.move`, `account.payment` |
| HR | `hr.employee`, `hr.contract` |
| Projects | `project.project`, `project.task` |
| Manufacturing | `mrp.production`, `mrp.bom` |

## Requirements

- OpenClaw CLI
- Python 3.10+
- Accessible Odoo instance (17, 18, or 19)

## License

MIT-0 © Akmal Dirgantara
