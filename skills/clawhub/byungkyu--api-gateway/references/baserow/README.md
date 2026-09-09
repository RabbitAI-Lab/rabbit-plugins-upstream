# Baserow Routing Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../SKILL.md#security--permissions) for full security policy.

**App name:** `baserow`
**Base URL proxied:** `api.baserow.io`

## API Path Pattern

```
/baserow/api/database/rows/table/{table_id}/
/baserow/api/database/fields/table/{table_id}/
/baserow/api/database/tables/all-tables/
/baserow/api/user-files/upload-file/
/baserow/api/user-files/upload-via-url/
```

## Important Notes

- Connection uses API_KEY authentication (database token), not OAuth
- By default, fields return as `field_{id}`; use `user_field_names=true` for readable names
- Database tokens grant access only to database row endpoints
- Cloud has a limit of 10 concurrent API requests

## Common Endpoints

### List Rows
```bash
maton api '/baserow/api/database/rows/table/{table_id}/?user_field_names=true'
```

### Get Row
```bash
maton api '/baserow/api/database/rows/table/{table_id}/{row_id}/'
```

### Create Row
```bash
maton api -X POST '/baserow/api/database/rows/table/{table_id}/' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "field_123": "value"
}
EOF
```

### Update Row
```bash
maton api -X PATCH '/baserow/api/database/rows/table/{table_id}/{row_id}/' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "field_123": "updated value"
}
EOF
```

### Delete Row
```bash
maton api '/baserow/api/database/rows/table/{table_id}/{row_id}/' -X DELETE
```

### Batch Create Rows
```bash
maton api -X POST '/baserow/api/database/rows/table/{table_id}/batch/' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "items": [
    {"field_123": "value1"},
    {"field_123": "value2"}
  ]
}
EOF
```

### Batch Update Rows
```bash
maton api -X PATCH '/baserow/api/database/rows/table/{table_id}/batch/' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "items": [
    {"id": 1, "field_123": "updated1"},
    {"id": 2, "field_123": "updated2"}
  ]
}
EOF
```

### Batch Delete Rows
```bash
maton api -X POST '/baserow/api/database/rows/table/{table_id}/batch-delete/' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "items": [1, 2, 3]
}
EOF
```

### List Fields
```bash
maton api '/baserow/api/database/fields/table/{table_id}/'
```

### List All Tables
```bash
maton api '/baserow/api/database/tables/all-tables/'
```

### Move Row
```bash
maton api -X PATCH '/baserow/api/database/rows/table/{table_id}/{row_id}/move/?before_id={row_id}'
```

### Upload File via URL
```bash
maton api -X POST '/baserow/api/user-files/upload-via-url/' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "url": "https://example.com/image.png"
}
EOF
```

### Upload File (Multipart)
```bash
# `maton api` sends a body verbatim but does not build a multipart envelope: assemble it
# first, then hand the result to --input. Nothing here handles a credential — the CLI injects it.
FILE=/path/to/file.png            # exactly the path the user gave, never a discovered one
BOUNDARY="maton-$$"
{
  printf -- '--%s\r\nContent-Disposition: form-data; name="file"; filename="%s"\r\nContent-Type: application/octet-stream\r\n\r\n' "$BOUNDARY" "$(basename "$FILE")"
  cat "$FILE"
  printf -- '\r\n'
  printf -- '--%s--\r\n' "$BOUNDARY"
} > /tmp/baserow-upload.body

maton api -X POST '/baserow/api/user-files/upload-file/' \
  -H "Content-Type: multipart/form-data; boundary=$BOUNDARY" \
  --input /tmp/baserow-upload.body
```

## Query Parameters

- `user_field_names=true` - Use human-readable field names
- `size` - Rows per page (default: 100)
- `page` - Page number (1-indexed)
- `order_by` - Field to sort by (prefix `-` for descending)
- `filter__{field}__{operator}` - Filter rows
- `search` - Search across all fields
- `include` - Fields to include
- `exclude` - Fields to exclude

## Filter Operators

**Text:** `equal`, `not_equal`, `contains`, `contains_not`, `contains_word`, `doesnt_contain_word`, `length_is_lower_than`

**Numeric:** `higher_than`, `higher_than_or_equal`, `lower_than`, `lower_than_or_equal`, `is_even_and_whole`

**Date:** `date_is`, `date_is_not`, `date_is_before`, `date_is_on_or_before`, `date_is_after`, `date_is_on_or_after`, `date_is_within`, `date_equals_today`, `date_within_days`, `date_within_weeks`, `date_within_months`

**Boolean:** `boolean`

**Link Row:** `link_row_has`, `link_row_has_not`, `link_row_contains`, `link_row_not_contains`

**Select:** `single_select_equal`, `single_select_not_equal`, `single_select_is_any_of`, `single_select_is_none_of`, `multiple_select_has`, `multiple_select_has_not`

**File:** `filename_contains`, `has_file_type`, `files_lower_than`

**General:** `empty`, `not_empty`

## Resources

- [Baserow API Documentation](https://baserow.io/api-docs)
- [Baserow API Spec](https://api.baserow.io/api/redoc/)
- [Database Tokens](https://baserow.io/user-docs/personal-api-tokens)
