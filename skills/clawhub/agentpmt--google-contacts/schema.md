# Google Contacts Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `google-contacts`

x402 availability: not enabled for this product.

## `create_contact`

Action slug: `create-contact`

Price: `5` credits

Create a new contact. At least one field must be provided in the contact object.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `contact` | `object` | yes | Contact data. At least one field is required. Also accepts Google People API format (names, emailAddresses, phoneNumbers arrays) and plural aliases (emails, phones). |

Sample parameters:

```json
{
  "contact": {
    "address": {
      "city": "example city",
      "country": "example country",
      "postal_code": "example postal code",
      "region": "example region",
      "street_address": "example street address"
    },
    "company": "example company",
    "email": "user@example.com",
    "first_name": "example first name",
    "full_name": "example full name",
    "job_title": "example job title",
    "last_name": "example last name",
    "notes": "example notes"
  }
}
```

Generated JSON parameter schema:

```json
{
  "contact": {
    "description": "Contact data. At least one field is required. Also accepts Google People API format (names, emailAddresses, phoneNumbers arrays) and plural aliases (emails, phones).",
    "properties": {
      "address": {
        "description": "Physical address",
        "properties": {
          "city": {
            "description": "City",
            "required": false,
            "type": "string"
          },
          "country": {
            "description": "Country",
            "required": false,
            "type": "string"
          },
          "postal_code": {
            "description": "Postal/ZIP code",
            "required": false,
            "type": "string"
          },
          "region": {
            "description": "State/region",
            "required": false,
            "type": "string"
          },
          "street_address": {
            "description": "Street address",
            "required": false,
            "type": "string"
          }
        },
        "required": false,
        "type": "object"
      },
      "company": {
        "description": "Organization/company name",
        "required": false,
        "type": "string"
      },
      "email": {
        "description": "Primary email address",
        "required": false,
        "type": "string"
      },
      "first_name": {
        "description": "Given/first name",
        "required": false,
        "type": "string"
      },
      "full_name": {
        "description": "Full name / display name. Used to derive first/last name if those are not provided.",
        "required": false,
        "type": "string"
      },
      "job_title": {
        "description": "Job title",
        "required": false,
        "type": "string"
      },
      "last_name": {
        "description": "Family/last name",
        "required": false,
        "type": "string"
      },
      "notes": {
        "description": "Notes / biography text",
        "required": false,
        "type": "string"
      },
      "phone": {
        "description": "Primary phone number",
        "required": false,
        "type": "string"
      }
    },
    "required": true,
    "type": "object"
  }
}
```

## `delete_contact`

Action slug: `delete-contact`

Price: `5` credits

Permanently delete a contact. This action is irreversible.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `resource_name` | `string` | yes | Contact resource name (e.g., 'people/c1234567890') |

Sample parameters:

```json
{
  "resource_name": "example resource name"
}
```

Generated JSON parameter schema:

```json
{
  "resource_name": {
    "description": "Contact resource name (e.g., 'people/c1234567890')",
    "required": true,
    "type": "string"
  }
}
```

## `get_contact`

Action slug: `get-contact`

Price: `5` credits

Retrieve a single contact by resource name.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `resource_name` | `string` | yes | Contact resource name (e.g., 'people/c1234567890'). The 'people/' prefix is optional. |

Sample parameters:

```json
{
  "resource_name": "example resource name"
}
```

Generated JSON parameter schema:

```json
{
  "resource_name": {
    "description": "Contact resource name (e.g., 'people/c1234567890'). The 'people/' prefix is optional.",
    "required": true,
    "type": "string"
  }
}
```

## `list_contacts`

Action slug: `list-contacts`

Price: `5` credits

List all contacts sorted by first name ascending.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `page_size` | `integer` | no | Max results per page (default 25, max 200) |
| `page_token` | `string` | no | Pagination token from a previous response |

Sample parameters:

```json
{
  "page_size": 25,
  "page_token": "example page token"
}
```

Generated JSON parameter schema:

```json
{
  "page_size": {
    "default": 25,
    "description": "Max results per page (default 25, max 200)",
    "maximum": 200,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token from a previous response",
    "required": false,
    "type": "string"
  }
}
```

## `search_contacts`

Action slug: `search-contacts`

Price: `5` credits

Search contacts by name, email, phone, or other text.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `page_size` | `integer` | no | Max results per page (default 25, max 200) |
| `page_token` | `string` | no | Pagination token from a previous response |
| `query` | `string` | yes | Search text to match against contact fields |

Sample parameters:

```json
{
  "page_size": 25,
  "page_token": "example page token",
  "query": "example search query"
}
```

Generated JSON parameter schema:

```json
{
  "page_size": {
    "default": 25,
    "description": "Max results per page (default 25, max 200)",
    "maximum": 200,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token from a previous response",
    "required": false,
    "type": "string"
  },
  "query": {
    "description": "Search text to match against contact fields",
    "required": true,
    "type": "string"
  }
}
```

## `update_contact`

Action slug: `update-contact`

Price: `5` credits

Update an existing contact. Only the fields included in the contact object are modified; other fields remain unchanged.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `contact` | `object` | yes | Fields to update. Same structure as create_contact. Only provided fields are changed. |
| `etag` | `string` | no | ETag for optimistic concurrency. If omitted, the tool fetches it automatically. |
| `resource_name` | `string` | yes | Contact resource name (e.g., 'people/c1234567890') |

Sample parameters:

```json
{
  "contact": {
    "address": {
      "city": "example city",
      "country": "example country",
      "postal_code": "example postal code",
      "region": "example region",
      "street_address": "example street address"
    },
    "company": "example company",
    "email": "user@example.com",
    "first_name": "example first name",
    "full_name": "example full name",
    "job_title": "example job title",
    "last_name": "example last name",
    "notes": "example notes"
  },
  "etag": "example etag",
  "resource_name": "example resource name"
}
```

Generated JSON parameter schema:

```json
{
  "contact": {
    "description": "Fields to update. Same structure as create_contact. Only provided fields are changed.",
    "properties": {
      "address": {
        "description": "Physical address",
        "properties": {
          "city": {
            "description": "City",
            "required": false,
            "type": "string"
          },
          "country": {
            "description": "Country",
            "required": false,
            "type": "string"
          },
          "postal_code": {
            "description": "Postal/ZIP code",
            "required": false,
            "type": "string"
          },
          "region": {
            "description": "State/region",
            "required": false,
            "type": "string"
          },
          "street_address": {
            "description": "Street address",
            "required": false,
            "type": "string"
          }
        },
        "required": false,
        "type": "object"
      },
      "company": {
        "description": "Organization/company name",
        "required": false,
        "type": "string"
      },
      "email": {
        "description": "Primary email address",
        "required": false,
        "type": "string"
      },
      "first_name": {
        "description": "Given/first name",
        "required": false,
        "type": "string"
      },
      "full_name": {
        "description": "Full name / display name",
        "required": false,
        "type": "string"
      },
      "job_title": {
        "description": "Job title",
        "required": false,
        "type": "string"
      },
      "last_name": {
        "description": "Family/last name",
        "required": false,
        "type": "string"
      },
      "notes": {
        "description": "Notes / biography text",
        "required": false,
        "type": "string"
      },
      "phone": {
        "description": "Primary phone number",
        "required": false,
        "type": "string"
      }
    },
    "required": true,
    "type": "object"
  },
  "etag": {
    "description": "ETag for optimistic concurrency. If omitted, the tool fetches it automatically.",
    "required": false,
    "type": "string"
  },
  "resource_name": {
    "description": "Contact resource name (e.g., 'people/c1234567890')",
    "required": true,
    "type": "string"
  }
}
```
