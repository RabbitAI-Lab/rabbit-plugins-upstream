# SignNow Routing Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../SKILL.md#security--permissions) for full security policy.

**App name:** `signnow`
**Base URL proxied:** `api.signnow.com`

## API Path Pattern

```
/signnow/{resource}
```

## Common Endpoints

### User

```bash
maton api '/signnow/user'
maton api '/signnow/user/documents'
```

### Documents

```bash
# Upload document: multipart needs a body assembled first; see the example below.

# Get document
maton api '/signnow/document/{document_id}'

# Update document
maton api -X PUT '/signnow/document/{document_id}'

# Download document
maton api '/signnow/document/{document_id}/download?type=collapsed'

# Get document history
maton api '/signnow/document/{document_id}/historyfull'

# Move document to folder
maton api -X POST '/signnow/document/{document_id}/move'

# Merge documents (returns PDF)
maton api -X POST '/signnow/document/merge'

# Delete document
maton api '/signnow/document/{document_id}' -X DELETE
```

Upload document:

```bash
# `maton api` sends a body verbatim but does not build a multipart envelope: assemble it
# first, then hand the result to --input. Nothing here handles a credential — the CLI injects it.
FILE=/path/to/document.pdf            # exactly the path the user gave, never a discovered one
BOUNDARY="maton-$$"
{
  printf -- '--%s\r\nContent-Disposition: form-data; name="file"; filename="%s"\r\nContent-Type: application/pdf\r\n\r\n' "$BOUNDARY" "$(basename "$FILE")"
  cat "$FILE"
  printf -- '\r\n'
  printf -- '--%s--\r\n' "$BOUNDARY"
} > /tmp/signnow-upload.body

maton api -X POST '/signnow/document' \
  -H "Content-Type: multipart/form-data; boundary=$BOUNDARY" \
  --input /tmp/signnow-upload.body
```

### Templates

```bash
# Create template from document
maton api -X POST '/signnow/template'

# Create document from template
maton api -X POST '/signnow/template/{template_id}/copy'
```

### Invites

```bash
# Send freeform invite
maton api -X POST '/signnow/document/{document_id}/invite'

# Create signing link (requires document fields)
maton api -X POST '/signnow/link'
```

### Folders

```bash
maton api '/signnow/folder'
maton api '/signnow/folder/{folder_id}'
```

### Webhooks (Event Subscriptions)

```bash
maton api '/signnow/event_subscription'
maton api -X POST '/signnow/event_subscription'
maton api '/signnow/event_subscription/{subscription_id}' -X DELETE
```

## Notes

- Documents must be uploaded as multipart form data with PDF file
- Supported file types: PDF, DOC, DOCX, ODT, RTF, PNG, JPG
- System folders cannot be renamed or deleted
- Creating signing links requires documents to have signature fields
- Custom invite subject/message requires paid subscription
- Rate limit in development mode: 500 requests/hour per application

## Resources

- [SignNow API Reference](https://docs.signnow.com/docs/signnow/reference)
- [SignNow Developer Portal](https://www.signnow.com/developers)
