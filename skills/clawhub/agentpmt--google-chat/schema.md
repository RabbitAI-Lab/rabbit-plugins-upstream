# Google Chat Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `google-chat`

x402 availability: not enabled for this product.

## `add_reaction`

Action slug: `add-reaction`

Price: `5` credits

Add a reaction.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `emoji_unicode` | `string` | yes | Unicode emoji. |
| `message_name` | `string` | yes | Message name or ID. |
| `space` | `string` | no | Space for short IDs. |

Sample parameters:

```json
{
  "emoji_unicode": "example emoji unicode",
  "message_name": "example message name",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "emoji_unicode": {
    "description": "Unicode emoji.",
    "required": true,
    "type": "string"
  },
  "message_name": {
    "description": "Message name or ID.",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space for short IDs.",
    "required": false,
    "type": "string"
  }
}
```

## `create_message`

Action slug: `create-message`

Price: `5` credits

Create a message, optionally with files.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `cards_v2` | `array` | no | Cards v2 payload. |
| `file_ids` | `array` | no | File Manager IDs to attach. |
| `max_upload_bytes` | `integer` | no | Max upload bytes. |
| `message_id` | `string` | no | Client message ID. |
| `message_reply_option` | `string` | no | Reply option. |
| `message_request_id` | `string` | no | Idempotency requestId. |
| `notification_type` | `string` | no | Notification type. |
| `space` | `string` | yes | Target space. |
| `text` | `string` | no | Message text. |
| `thread_key` | `string` | no | Thread key. |
| `thread_name` | `string` | no | Thread name. |

Sample parameters:

```json
{
  "cards_v2": [
    {}
  ],
  "file_ids": [
    "example file id"
  ],
  "max_upload_bytes": 1,
  "message_id": "example message id",
  "message_reply_option": "REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD",
  "message_request_id": "example message request id",
  "notification_type": "NOTIFICATION_TYPE_NONE",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "cards_v2": {
    "description": "Cards v2 payload.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "file_ids": {
    "description": "File Manager IDs to attach.",
    "items": {
      "type": "string"
    },
    "required": false,
    "type": "array"
  },
  "max_upload_bytes": {
    "description": "Max upload bytes.",
    "required": false,
    "type": "integer"
  },
  "message_id": {
    "description": "Client message ID.",
    "required": false,
    "type": "string"
  },
  "message_reply_option": {
    "description": "Reply option.",
    "enum": [
      "REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD",
      "REPLY_MESSAGE_OR_FAIL"
    ],
    "required": false,
    "type": "string"
  },
  "message_request_id": {
    "description": "Idempotency requestId.",
    "required": false,
    "type": "string"
  },
  "notification_type": {
    "description": "Notification type.",
    "enum": [
      "NOTIFICATION_TYPE_NONE",
      "NOTIFICATION_TYPE_FORCE_NOTIFY",
      "NOTIFICATION_TYPE_SILENT"
    ],
    "required": false,
    "type": "string"
  },
  "space": {
    "description": "Target space.",
    "required": true,
    "type": "string"
  },
  "text": {
    "description": "Message text.",
    "required": false,
    "type": "string"
  },
  "thread_key": {
    "description": "Thread key.",
    "required": false,
    "type": "string"
  },
  "thread_name": {
    "description": "Thread name.",
    "required": false,
    "type": "string"
  }
}
```

## `delete_message`

Action slug: `delete-message`

Price: `5` credits

Delete a message.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `force` | `boolean` | no | Delete replies too. |
| `message_name` | `string` | yes | Message name or ID. |
| `space` | `string` | no | Space for short IDs. |

Sample parameters:

```json
{
  "force": true,
  "message_name": "example message name",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "force": {
    "description": "Delete replies too.",
    "required": false,
    "type": "boolean"
  },
  "message_name": {
    "description": "Message name or ID.",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space for short IDs.",
    "required": false,
    "type": "string"
  }
}
```

## `delete_reaction`

Action slug: `delete-reaction`

Price: `5` credits

Delete a reaction.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `message_name` | `string` | no | Message for short IDs. |
| `reaction_name` | `string` | yes | Reaction name or ID. |
| `space` | `string` | no | Space for short IDs. |

Sample parameters:

```json
{
  "message_name": "example message name",
  "reaction_name": "example reaction name",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "message_name": {
    "description": "Message for short IDs.",
    "required": false,
    "type": "string"
  },
  "reaction_name": {
    "description": "Reaction name or ID.",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space for short IDs.",
    "required": false,
    "type": "string"
  }
}
```

## `download_attachment_to_storage`

Action slug: `download-attachment-to-storage`

Price: `5` credits

Download Chat media to File Manager.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `attachment_name` | `string` | no | Attachment name, ID, or contentName. |
| `expiration_days` | `integer` | no | Expiration days. |
| `max_bytes` | `integer` | no | Max download bytes. |
| `media_resource_name` | `string` | no | attachmentDataRef.resourceName. |
| `message_name` | `string` | no | Parent message. |
| `output_filename` | `string` | no | Stored filename. |
| `space` | `string` | no | Space for short IDs. |

Sample parameters:

```json
{
  "attachment_name": "example attachment name",
  "expiration_days": 1,
  "max_bytes": 1,
  "media_resource_name": "example media resource name",
  "message_name": "example message name",
  "output_filename": "example output filename",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "attachment_name": {
    "description": "Attachment name, ID, or contentName.",
    "required": false,
    "type": "string"
  },
  "expiration_days": {
    "description": "Expiration days.",
    "required": false,
    "type": "integer"
  },
  "max_bytes": {
    "description": "Max download bytes.",
    "required": false,
    "type": "integer"
  },
  "media_resource_name": {
    "description": "attachmentDataRef.resourceName.",
    "required": false,
    "type": "string"
  },
  "message_name": {
    "description": "Parent message.",
    "required": false,
    "type": "string"
  },
  "output_filename": {
    "description": "Stored filename.",
    "required": false,
    "type": "string"
  },
  "space": {
    "description": "Space for short IDs.",
    "required": false,
    "type": "string"
  }
}
```

## `find_direct_message`

Action slug: `find-direct-message`

Price: `5` credits

Find a DM space.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `user_name` | `string` | yes | User name, e.g. users/123. |

Sample parameters:

```json
{
  "user_name": "example user name"
}
```

Generated JSON parameter schema:

```json
{
  "user_name": {
    "description": "User name, e.g. users/123.",
    "required": true,
    "type": "string"
  }
}
```

## `get_attachment`

Action slug: `get-attachment`

Price: `5` credits

Get attachment metadata from its message.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `attachment_name` | `string` | yes | Attachment name, ID, or contentName. |
| `message_name` | `string` | no | Parent message. |
| `space` | `string` | no | Space for short IDs. |

Sample parameters:

```json
{
  "attachment_name": "example attachment name",
  "message_name": "example message name",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "attachment_name": {
    "description": "Attachment name, ID, or contentName.",
    "required": true,
    "type": "string"
  },
  "message_name": {
    "description": "Parent message.",
    "required": false,
    "type": "string"
  },
  "space": {
    "description": "Space for short IDs.",
    "required": false,
    "type": "string"
  }
}
```

## `get_message`

Action slug: `get-message`

Price: `5` credits

Get a message.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `message_name` | `string` | yes | Message name or ID. |
| `space` | `string` | no | Space for short IDs. |

Sample parameters:

```json
{
  "message_name": "example message name",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "message_name": {
    "description": "Message name or ID.",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space for short IDs.",
    "required": false,
    "type": "string"
  }
}
```

## `get_space`

Action slug: `get-space`

Price: `5` credits

Get a space.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `space` | `string` | yes | Space name or ID. |

Sample parameters:

```json
{
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "space": {
    "description": "Space name or ID.",
    "required": true,
    "type": "string"
  }
}
```

## `list_message_attachments`

Action slug: `list-message-attachments`

Price: `5` credits

List message attachments.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `message_name` | `string` | yes | Message name or ID. |
| `space` | `string` | no | Space for short IDs. |

Sample parameters:

```json
{
  "message_name": "example message name",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "message_name": {
    "description": "Message name or ID.",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space for short IDs.",
    "required": false,
    "type": "string"
  }
}
```

## `list_messages`

Action slug: `list-messages`

Price: `5` credits

List messages; newest first by default.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `filter` | `string` | no | Message filter. |
| `order_by` | `string` | no | Message sort order. |
| `page_size` | `integer` | no | Page size. |
| `page_token` | `string` | no | Next page token. |
| `show_deleted` | `boolean` | no | Include deleted messages. |
| `space` | `string` | yes | Space name or ID. |

Sample parameters:

```json
{
  "filter": "example filter",
  "order_by": "create_time DESC",
  "page_size": 1,
  "page_token": "example page token",
  "show_deleted": true,
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "filter": {
    "description": "Message filter.",
    "required": false,
    "type": "string"
  },
  "order_by": {
    "description": "Message sort order.",
    "enum": [
      "create_time DESC",
      "create_time ASC",
      "createTime DESC",
      "createTime ASC"
    ],
    "required": false,
    "type": "string"
  },
  "page_size": {
    "description": "Page size.",
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Next page token.",
    "required": false,
    "type": "string"
  },
  "show_deleted": {
    "description": "Include deleted messages.",
    "required": false,
    "type": "boolean"
  },
  "space": {
    "description": "Space name or ID.",
    "required": true,
    "type": "string"
  }
}
```

## `list_reactions`

Action slug: `list-reactions`

Price: `5` credits

List message reactions.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `filter` | `string` | no | Reaction filter. |
| `message_name` | `string` | yes | Message name or ID. |
| `page_size` | `integer` | no | Page size. |
| `page_token` | `string` | no | Next page token. |
| `space` | `string` | no | Space for short IDs. |

Sample parameters:

```json
{
  "filter": "example filter",
  "message_name": "example message name",
  "page_size": 1,
  "page_token": "example page token",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "filter": {
    "description": "Reaction filter.",
    "required": false,
    "type": "string"
  },
  "message_name": {
    "description": "Message name or ID.",
    "required": true,
    "type": "string"
  },
  "page_size": {
    "description": "Page size.",
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Next page token.",
    "required": false,
    "type": "string"
  },
  "space": {
    "description": "Space for short IDs.",
    "required": false,
    "type": "string"
  }
}
```

## `list_spaces`

Action slug: `list-spaces`

Price: `5` credits

List accessible spaces.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `filter` | `string` | no | spaces.list filter. |
| `page_size` | `integer` | no | Page size. |
| `page_token` | `string` | no | Next page token. |

Sample parameters:

```json
{
  "filter": "example filter",
  "page_size": 1,
  "page_token": "example page token"
}
```

Generated JSON parameter schema:

```json
{
  "filter": {
    "description": "spaces.list filter.",
    "required": false,
    "type": "string"
  },
  "page_size": {
    "description": "Page size.",
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Next page token.",
    "required": false,
    "type": "string"
  }
}
```

## `reply_message`

Action slug: `reply-message`

Price: `5` credits

Reply to a message, optionally with files.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `cards_v2` | `array` | no | Cards v2 payload. |
| `file_ids` | `array` | no | File Manager IDs to attach. |
| `max_upload_bytes` | `integer` | no | Max upload bytes. |
| `message_id` | `string` | no | Client message ID. |
| `message_name` | `string` | yes | Message name or ID. |
| `message_reply_option` | `string` | no | Reply option. |
| `message_request_id` | `string` | no | Idempotency requestId. |
| `notification_type` | `string` | no | Notification type. |
| `space` | `string` | no | Space for short IDs. |
| `text` | `string` | no | Reply text. |

Sample parameters:

```json
{
  "cards_v2": [
    {}
  ],
  "file_ids": [
    "example file id"
  ],
  "max_upload_bytes": 1,
  "message_id": "example message id",
  "message_name": "example message name",
  "message_reply_option": "REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD",
  "message_request_id": "example message request id",
  "notification_type": "NOTIFICATION_TYPE_NONE"
}
```

Generated JSON parameter schema:

```json
{
  "cards_v2": {
    "description": "Cards v2 payload.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "file_ids": {
    "description": "File Manager IDs to attach.",
    "items": {
      "type": "string"
    },
    "required": false,
    "type": "array"
  },
  "max_upload_bytes": {
    "description": "Max upload bytes.",
    "required": false,
    "type": "integer"
  },
  "message_id": {
    "description": "Client message ID.",
    "required": false,
    "type": "string"
  },
  "message_name": {
    "description": "Message name or ID.",
    "required": true,
    "type": "string"
  },
  "message_reply_option": {
    "description": "Reply option.",
    "enum": [
      "REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD",
      "REPLY_MESSAGE_OR_FAIL"
    ],
    "required": false,
    "type": "string"
  },
  "message_request_id": {
    "description": "Idempotency requestId.",
    "required": false,
    "type": "string"
  },
  "notification_type": {
    "description": "Notification type.",
    "enum": [
      "NOTIFICATION_TYPE_NONE",
      "NOTIFICATION_TYPE_FORCE_NOTIFY",
      "NOTIFICATION_TYPE_SILENT"
    ],
    "required": false,
    "type": "string"
  },
  "space": {
    "description": "Space for short IDs.",
    "required": false,
    "type": "string"
  },
  "text": {
    "description": "Reply text.",
    "required": false,
    "type": "string"
  }
}
```

## `search_attachments`

Action slug: `search-attachments`

Price: `5` credits

Bounded attachment search in one space.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `case_sensitive` | `boolean` | no | Case-sensitive match. |
| `filter` | `string` | no | Optional list filter. |
| `max_results` | `integer` | no | Max matches. |
| `order_by` | `string` | no | Scan sort order. |
| `page_size` | `integer` | no | Scan page size. |
| `query` | `string` | yes | Search text. |
| `scan_limit` | `integer` | no | Max messages scanned. |
| `space` | `string` | yes | Space name or ID. |

Sample parameters:

```json
{
  "case_sensitive": true,
  "filter": "example filter",
  "max_results": 1,
  "order_by": "create_time DESC",
  "page_size": 1,
  "query": "example search query",
  "scan_limit": 1,
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "case_sensitive": {
    "description": "Case-sensitive match.",
    "required": false,
    "type": "boolean"
  },
  "filter": {
    "description": "Optional list filter.",
    "required": false,
    "type": "string"
  },
  "max_results": {
    "description": "Max matches.",
    "required": false,
    "type": "integer"
  },
  "order_by": {
    "description": "Scan sort order.",
    "enum": [
      "create_time DESC",
      "create_time ASC",
      "createTime DESC",
      "createTime ASC"
    ],
    "required": false,
    "type": "string"
  },
  "page_size": {
    "description": "Scan page size.",
    "required": false,
    "type": "integer"
  },
  "query": {
    "description": "Search text.",
    "required": true,
    "type": "string"
  },
  "scan_limit": {
    "description": "Max messages scanned.",
    "required": false,
    "type": "integer"
  },
  "space": {
    "description": "Space name or ID.",
    "required": true,
    "type": "string"
  }
}
```

## `search_messages`

Action slug: `search-messages`

Price: `5` credits

Bounded message search in one space.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `case_sensitive` | `boolean` | no | Case-sensitive match. |
| `filter` | `string` | no | Optional list filter. |
| `max_results` | `integer` | no | Max matches. |
| `order_by` | `string` | no | Scan sort order. |
| `page_size` | `integer` | no | Scan page size. |
| `query` | `string` | yes | Search text. |
| `scan_limit` | `integer` | no | Max messages scanned. |
| `search_fields` | `array` | no | Fields to search. |
| `show_deleted` | `boolean` | no | Include deleted messages. |
| `space` | `string` | yes | Space name or ID. |

Sample parameters:

```json
{
  "case_sensitive": true,
  "filter": "example filter",
  "max_results": 1,
  "order_by": "create_time DESC",
  "page_size": 1,
  "query": "example search query",
  "scan_limit": 1,
  "search_fields": [
    "text"
  ]
}
```

Generated JSON parameter schema:

```json
{
  "case_sensitive": {
    "description": "Case-sensitive match.",
    "required": false,
    "type": "boolean"
  },
  "filter": {
    "description": "Optional list filter.",
    "required": false,
    "type": "string"
  },
  "max_results": {
    "description": "Max matches.",
    "required": false,
    "type": "integer"
  },
  "order_by": {
    "description": "Scan sort order.",
    "enum": [
      "create_time DESC",
      "create_time ASC",
      "createTime DESC",
      "createTime ASC"
    ],
    "required": false,
    "type": "string"
  },
  "page_size": {
    "description": "Scan page size.",
    "required": false,
    "type": "integer"
  },
  "query": {
    "description": "Search text.",
    "required": true,
    "type": "string"
  },
  "scan_limit": {
    "description": "Max messages scanned.",
    "required": false,
    "type": "integer"
  },
  "search_fields": {
    "description": "Fields to search.",
    "items": {
      "enum": [
        "text",
        "formatted_text",
        "argument_text",
        "sender",
        "attachment_name"
      ],
      "type": "string"
    },
    "required": false,
    "type": "array"
  },
  "show_deleted": {
    "description": "Include deleted messages.",
    "required": false,
    "type": "boolean"
  },
  "space": {
    "description": "Space name or ID.",
    "required": true,
    "type": "string"
  }
}
```

## `search_spaces`

Action slug: `search-spaces`

Price: `5` credits

Search accessible spaces.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `order_by` | `string` | no | Space sort order. |
| `page_size` | `integer` | no | Page size. |
| `page_token` | `string` | no | Next page token. |
| `query` | `string` | yes | Space search query. |

Sample parameters:

```json
{
  "order_by": "create_time DESC",
  "page_size": 1,
  "page_token": "example page token",
  "query": "example search query"
}
```

Generated JSON parameter schema:

```json
{
  "order_by": {
    "description": "Space sort order.",
    "enum": [
      "create_time DESC",
      "relevance DESC"
    ],
    "required": false,
    "type": "string"
  },
  "page_size": {
    "description": "Page size.",
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Next page token.",
    "required": false,
    "type": "string"
  },
  "query": {
    "description": "Space search query.",
    "required": true,
    "type": "string"
  }
}
```

## `update_message`

Action slug: `update-message`

Price: `5` credits

Update message text/cards.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `cards_v2` | `array` | no | Updated cards v2. |
| `message_name` | `string` | yes | Message name or ID. |
| `space` | `string` | no | Space for short IDs. |
| `text` | `string` | no | Updated text. |

Sample parameters:

```json
{
  "cards_v2": [
    {}
  ],
  "message_name": "example message name",
  "space": "example space",
  "text": "example text"
}
```

Generated JSON parameter schema:

```json
{
  "cards_v2": {
    "description": "Updated cards v2.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "message_name": {
    "description": "Message name or ID.",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space for short IDs.",
    "required": false,
    "type": "string"
  },
  "text": {
    "description": "Updated text.",
    "required": false,
    "type": "string"
  }
}
```

## `upload_attachment`

Action slug: `upload-attachment`

Price: `5` credits

Upload a File Manager file to Chat.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `content_type` | `string` | no | MIME type override. |
| `filename` | `string` | no | Filename override. |
| `max_upload_bytes` | `integer` | no | Max upload bytes. |
| `source_file_id` | `string` | yes | File Manager source ID. |
| `space` | `string` | yes | Target space. |

Sample parameters:

```json
{
  "content_type": "Draft marketing copy to check for banned phrases.",
  "filename": "example filename",
  "max_upload_bytes": 1,
  "source_file_id": "example source file id",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "content_type": {
    "description": "MIME type override.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename override.",
    "required": false,
    "type": "string"
  },
  "max_upload_bytes": {
    "description": "Max upload bytes.",
    "required": false,
    "type": "integer"
  },
  "source_file_id": {
    "description": "File Manager source ID.",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Target space.",
    "required": true,
    "type": "string"
  }
}
```
