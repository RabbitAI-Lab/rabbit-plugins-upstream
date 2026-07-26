# Zoho Books Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `zoho-books`

x402 availability: not enabled for this product.

## `bank_get_matching_transactions`

Action slug: `bank-get-matching-transactions`

Price: `5` credits

Find existing transactions that could match an uncategorized bank transaction.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `query_params` | `object` | no | Additional query parameters |
| `record_id` | `string` | yes | Uncategorized bank transaction ID |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "query_params": {},
  "record_id": "example record id"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "record_id": {
    "description": "Uncategorized bank transaction ID",
    "required": true,
    "type": "string"
  }
}
```

## `bank_match_transaction`

Action slug: `bank-match-transaction`

Price: `5` credits

Match an uncategorized bank transaction to one or more existing transactions. Requires 'edit' permission.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `payload` | `object` | no | Match details: transactions_to_be_matched array with transaction_id and transaction_type |
| `query_params` | `object` | no | Additional query parameters |
| `record_id` | `string` | yes | Uncategorized bank transaction ID to match |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "payload": {},
  "query_params": {},
  "record_id": "example record id"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "payload": {
    "description": "Match details: transactions_to_be_matched array with transaction_id and transaction_type",
    "required": false,
    "type": "object"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "record_id": {
    "description": "Uncategorized bank transaction ID to match",
    "required": true,
    "type": "string"
  }
}
```

## `bank_unmatch_transaction`

Action slug: `bank-unmatch-transaction`

Price: `5` credits

Remove the match from a previously matched bank transaction. Requires 'edit' permission.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `query_params` | `object` | no | Additional query parameters |
| `record_id` | `string` | yes | Bank transaction ID to unmatch |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "query_params": {},
  "record_id": "example record id"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "record_id": {
    "description": "Bank transaction ID to unmatch",
    "required": true,
    "type": "string"
  }
}
```

## `create_record`

Action slug: `create-record`

Price: `5` credits

Create a new record for a given resource type. Requires 'add' permission. The bankstatements resource only supports this action (used to import statements).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `payload` | `object` | yes | Record data to create |
| `project_id` | `string` | no | Project ID (required when resource is 'tasks') |
| `query_params` | `object` | no | Additional query parameters |
| `resource` | `string` | yes | Zoho Books resource name |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "payload": {},
  "project_id": "example project id",
  "query_params": {},
  "resource": "contacts"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "payload": {
    "description": "Record data to create",
    "required": true,
    "type": "object"
  },
  "project_id": {
    "description": "Project ID (required when resource is 'tasks')",
    "required": false,
    "type": "string"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "resource": {
    "description": "Zoho Books resource name",
    "enum": [
      "contacts",
      "items",
      "invoices",
      "estimates",
      "creditnotes",
      "chartofaccounts",
      "journals",
      "bankaccounts",
      "banktransactions",
      "bankstatements",
      "bills",
      "expenses",
      "vendorcredits",
      "customerpayments",
      "vendorpayments",
      "projects",
      "tasks",
      "time_entries"
    ],
    "required": true,
    "type": "string"
  }
}
```

## `delete_record`

Action slug: `delete-record`

Price: `5` credits

Delete a record. Requires 'delete' permission.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `project_id` | `string` | no | Project ID (required when resource is 'tasks') |
| `query_params` | `object` | no | Additional query parameters |
| `record_id` | `string` | yes | Record ID to delete |
| `resource` | `string` | yes | Zoho Books resource name |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "project_id": "example project id",
  "query_params": {},
  "record_id": "example record id",
  "resource": "contacts"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "project_id": {
    "description": "Project ID (required when resource is 'tasks')",
    "required": false,
    "type": "string"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "record_id": {
    "description": "Record ID to delete",
    "required": true,
    "type": "string"
  },
  "resource": {
    "description": "Zoho Books resource name",
    "enum": [
      "contacts",
      "items",
      "invoices",
      "estimates",
      "creditnotes",
      "chartofaccounts",
      "journals",
      "bankaccounts",
      "banktransactions",
      "bills",
      "expenses",
      "vendorcredits",
      "customerpayments",
      "vendorpayments",
      "projects",
      "tasks",
      "time_entries"
    ],
    "required": true,
    "type": "string"
  }
}
```

## `describe_action`

Action slug: `describe-action`

Price: `5` credits

Get the detailed parameter schema for any action. Useful for discovering required and optional fields.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `action_to_describe` | `string` | no | The action name to describe. Omit to get schemas for all actions. |

Sample parameters:

```json
{
  "action_to_describe": "list_organizations"
}
```

Generated JSON parameter schema:

```json
{
  "action_to_describe": {
    "description": "The action name to describe. Omit to get schemas for all actions.",
    "enum": [
      "list_organizations",
      "list_records",
      "get_record",
      "create_record",
      "update_record",
      "delete_record",
      "invoice_mark_sent",
      "invoice_mark_void",
      "invoice_mark_draft",
      "invoice_email",
      "bank_get_matching_transactions",
      "bank_match_transaction",
      "bank_unmatch_transaction"
    ],
    "required": false,
    "type": "string"
  }
}
```

## `get_record`

Action slug: `get-record`

Price: `5` credits

Retrieve a single record by its ID.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `project_id` | `string` | no | Project ID (required when resource is 'tasks') |
| `query_params` | `object` | no | Additional query parameters |
| `record_id` | `string` | yes | The record ID to fetch |
| `resource` | `string` | yes | Zoho Books resource name |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "project_id": "example project id",
  "query_params": {},
  "record_id": "example record id",
  "resource": "contacts"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "project_id": {
    "description": "Project ID (required when resource is 'tasks')",
    "required": false,
    "type": "string"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "record_id": {
    "description": "The record ID to fetch",
    "required": true,
    "type": "string"
  },
  "resource": {
    "description": "Zoho Books resource name",
    "enum": [
      "contacts",
      "items",
      "invoices",
      "estimates",
      "creditnotes",
      "chartofaccounts",
      "journals",
      "bankaccounts",
      "banktransactions",
      "bankstatements",
      "bills",
      "expenses",
      "vendorcredits",
      "customerpayments",
      "vendorpayments",
      "projects",
      "tasks",
      "time_entries"
    ],
    "required": true,
    "type": "string"
  }
}
```

## `invoice_email`

Action slug: `invoice-email`

Price: `5` credits

Send an invoice by email. Requires 'edit' permission. Payload must include recipient email addresses, subject, and body.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `payload` | `object` | yes | Email details: to_mail_ids (array), subject (string), body (string) |
| `query_params` | `object` | no | Additional query parameters |
| `record_id` | `string` | yes | Invoice ID to email |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "payload": {},
  "query_params": {},
  "record_id": "example record id"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "payload": {
    "description": "Email details: to_mail_ids (array), subject (string), body (string)",
    "required": true,
    "type": "object"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "record_id": {
    "description": "Invoice ID to email",
    "required": true,
    "type": "string"
  }
}
```

## `invoice_mark_draft`

Action slug: `invoice-mark-draft`

Price: `5` credits

Revert an invoice to draft status. Requires 'edit' permission.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `query_params` | `object` | no | Additional query parameters |
| `record_id` | `string` | yes | Invoice ID to revert to draft |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "query_params": {},
  "record_id": "example record id"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "record_id": {
    "description": "Invoice ID to revert to draft",
    "required": true,
    "type": "string"
  }
}
```

## `invoice_mark_sent`

Action slug: `invoice-mark-sent`

Price: `5` credits

Mark an invoice as sent. Requires 'edit' permission.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `query_params` | `object` | no | Additional query parameters |
| `record_id` | `string` | yes | Invoice ID to mark as sent |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "query_params": {},
  "record_id": "example record id"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "record_id": {
    "description": "Invoice ID to mark as sent",
    "required": true,
    "type": "string"
  }
}
```

## `invoice_mark_void`

Action slug: `invoice-mark-void`

Price: `5` credits

Mark an invoice as void. Requires 'edit' permission.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `query_params` | `object` | no | Additional query parameters |
| `record_id` | `string` | yes | Invoice ID to mark as void |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "query_params": {},
  "record_id": "example record id"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "record_id": {
    "description": "Invoice ID to mark as void",
    "required": true,
    "type": "string"
  }
}
```

## `list_organizations`

Action slug: `list-organizations`

Price: `5` credits

Retrieve all Zoho Books organizations associated with your account. Use this first to obtain your organization_id.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `query_params` | `object` | no | Additional query parameters |

Sample parameters:

```json
{
  "query_params": {}
}
```

Generated JSON parameter schema:

```json
{
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  }
}
```

## `list_records`

Action slug: `list-records`

Price: `5` credits

List records for a given resource type with pagination support. Defaults to 25 records per page.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `project_id` | `string` | no | Project ID (required when resource is 'tasks') |
| `query_params` | `object` | no | Query parameters for filtering and pagination (e.g., page, per_page, status, date ranges) |
| `resource` | `string` | yes | Zoho Books resource name |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "project_id": "example project id",
  "query_params": {},
  "resource": "contacts"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "project_id": {
    "description": "Project ID (required when resource is 'tasks')",
    "required": false,
    "type": "string"
  },
  "query_params": {
    "description": "Query parameters for filtering and pagination (e.g., page, per_page, status, date ranges)",
    "required": false,
    "type": "object"
  },
  "resource": {
    "description": "Zoho Books resource name",
    "enum": [
      "contacts",
      "items",
      "invoices",
      "estimates",
      "creditnotes",
      "chartofaccounts",
      "journals",
      "bankaccounts",
      "banktransactions",
      "bankstatements",
      "bills",
      "expenses",
      "vendorcredits",
      "customerpayments",
      "vendorpayments",
      "projects",
      "tasks",
      "time_entries"
    ],
    "required": true,
    "type": "string"
  }
}
```

## `update_record`

Action slug: `update-record`

Price: `5` credits

Update an existing record. Requires 'edit' permission.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `organization_id` | `string` | yes | Zoho Books organization ID |
| `payload` | `object` | yes | Fields to update |
| `project_id` | `string` | no | Project ID (required when resource is 'tasks') |
| `query_params` | `object` | no | Additional query parameters |
| `record_id` | `string` | yes | Record ID to update |
| `resource` | `string` | yes | Zoho Books resource name |

Sample parameters:

```json
{
  "organization_id": "example organization id",
  "payload": {},
  "project_id": "example project id",
  "query_params": {},
  "record_id": "example record id",
  "resource": "contacts"
}
```

Generated JSON parameter schema:

```json
{
  "organization_id": {
    "description": "Zoho Books organization ID",
    "required": true,
    "type": "string"
  },
  "payload": {
    "description": "Fields to update",
    "required": true,
    "type": "object"
  },
  "project_id": {
    "description": "Project ID (required when resource is 'tasks')",
    "required": false,
    "type": "string"
  },
  "query_params": {
    "description": "Additional query parameters",
    "required": false,
    "type": "object"
  },
  "record_id": {
    "description": "Record ID to update",
    "required": true,
    "type": "string"
  },
  "resource": {
    "description": "Zoho Books resource name",
    "enum": [
      "contacts",
      "items",
      "invoices",
      "estimates",
      "creditnotes",
      "chartofaccounts",
      "journals",
      "bankaccounts",
      "banktransactions",
      "bills",
      "expenses",
      "vendorcredits",
      "customerpayments",
      "vendorpayments",
      "projects",
      "tasks",
      "time_entries"
    ],
    "required": true,
    "type": "string"
  }
}
```
