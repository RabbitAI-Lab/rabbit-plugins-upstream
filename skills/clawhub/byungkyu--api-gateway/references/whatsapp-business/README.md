# WhatsApp Business Routing Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../SKILL.md#security--permissions) for full security policy.

**App name:** `whatsapp-business`
**Base URL proxied:** `graph.facebook.com`

## API Path Pattern

```
/whatsapp-business/v21.0/{resource}
```

## Common Endpoints

### Send Text Message
```bash
maton api -X POST '/whatsapp-business/v21.0/{phone_number_id}/messages' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "messaging_product": "whatsapp",
  "to": "1234567890",
  "type": "text",
  "text": {"body": "Hello from WhatsApp!"}
}
EOF
```

### Send Template Message
```bash
maton api -X POST '/whatsapp-business/v21.0/{phone_number_id}/messages' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "messaging_product": "whatsapp",
  "to": "1234567890",
  "type": "template",
  "template": {
    "name": "hello_world",
    "language": {"code": "en_US"},
    "components": [
      {
        "type": "body",
        "parameters": [{"type": "text", "text": "John"}]
      }
    ]
  }
}
EOF
```

### Send Image Message
```bash
maton api -X POST '/whatsapp-business/v21.0/{phone_number_id}/messages' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "messaging_product": "whatsapp",
  "to": "1234567890",
  "type": "image",
  "image": {
    "link": "https://example.com/image.jpg",
    "caption": "Check out this image!"
  }
}
EOF
```

### Send Document Message
```bash
maton api -X POST '/whatsapp-business/v21.0/{phone_number_id}/messages' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "messaging_product": "whatsapp",
  "to": "1234567890",
  "type": "document",
  "document": {
    "link": "https://example.com/document.pdf",
    "filename": "report.pdf"
  }
}
EOF
```

### Send Interactive Button Message
```bash
maton api -X POST '/whatsapp-business/v21.0/{phone_number_id}/messages' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "messaging_product": "whatsapp",
  "to": "1234567890",
  "type": "interactive",
  "interactive": {
    "type": "button",
    "body": {"text": "Would you like to proceed?"},
    "action": {
      "buttons": [
        {"type": "reply", "reply": {"id": "yes", "title": "Yes"}},
        {"type": "reply", "reply": {"id": "no", "title": "No"}}
      ]
    }
  }
}
EOF
```

### Send Interactive List Message
```bash
maton api -X POST '/whatsapp-business/v21.0/{phone_number_id}/messages' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "messaging_product": "whatsapp",
  "to": "1234567890",
  "type": "interactive",
  "interactive": {
    "type": "list",
    "body": {"text": "Choose from the list below"},
    "action": {
      "button": "View Options",
      "sections": [
        {
          "title": "Products",
          "rows": [
            {"id": "prod1", "title": "Product 1"},
            {"id": "prod2", "title": "Product 2"}
          ]
        }
      ]
    }
  }
}
EOF
```

### Mark Message as Read
```bash
maton api -X POST '/whatsapp-business/v21.0/{phone_number_id}/messages' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "messaging_product": "whatsapp",
  "status": "read",
  "message_id": "wamid.xxxxx"
}
EOF
```

### Upload Media
```bash
# `maton api` sends a body verbatim but does not build a multipart envelope: assemble it
# first, then hand the result to --input. Nothing here handles a credential — the CLI injects it.
FILE=/path/to/file.jpg            # exactly the path the user gave, never a discovered one
BOUNDARY="maton-$$"
{
  printf -- '--%s\r\nContent-Disposition: form-data; name="messaging_product"\r\n\r\nwhatsapp\r\n' "$BOUNDARY"
  printf -- '--%s\r\nContent-Disposition: form-data; name="type"\r\n\r\nimage/jpeg\r\n' "$BOUNDARY"
  printf -- '--%s\r\nContent-Disposition: form-data; name="file"; filename="%s"\r\nContent-Type: image/jpeg\r\n\r\n' "$BOUNDARY" "$(basename "$FILE")"
  cat "$FILE"
  printf -- '\r\n'
  printf -- '--%s--\r\n' "$BOUNDARY"
} > /tmp/whatsapp-upload.body

maton api -X POST '/whatsapp-business/v21.0/{phone_number_id}/media' \
  -H "Content-Type: multipart/form-data; boundary=$BOUNDARY" \
  --input /tmp/whatsapp-upload.body
```

### Get Media URL
```bash
maton api '/whatsapp-business/v21.0/{media_id}'
```

### List Message Templates
```bash
maton api '/whatsapp-business/v21.0/{whatsapp_business_account_id}/message_templates'
```

### Create Message Template
```bash
maton api -X POST '/whatsapp-business/v21.0/{whatsapp_business_account_id}/message_templates' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "name": "order_confirmation",
  "language": "en_US",
  "category": "UTILITY",
  "components": [
    {"type": "BODY", "text": "Hi {{1}}, your order #{{2}} has been confirmed!"}
  ]
}
EOF
```

### Get Business Profile
```bash
maton api '/whatsapp-business/v21.0/{phone_number_id}/whatsapp_business_profile?fields=about,address,description,email,websites'
```

### Update Business Profile
```bash
maton api -X POST '/whatsapp-business/v21.0/{phone_number_id}/whatsapp_business_profile' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "messaging_product": "whatsapp",
  "about": "Your trusted partner",
  "description": "We provide excellent services"
}
EOF
```

## Notes

- Phone numbers must be in international format without `+` (e.g., `1234567890`)
- `messaging_product` must always be set to `whatsapp`
- Template messages are required for initiating conversations (24-hour messaging window)
- Media files must be publicly accessible URLs or uploaded via the Media API
- Interactive messages support up to 3 buttons or 10 list items
- Template categories: `AUTHENTICATION`, `MARKETING`, `UTILITY`

## Resources

- [WhatsApp Business API Overview](https://developers.facebook.com/docs/whatsapp/cloud-api/overview)
- [Send Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages)
- [Message Templates](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates)
- [Media](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media)
- [Business Profiles](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/business-profiles)
- [Webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks)
- [Error Codes](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes)
