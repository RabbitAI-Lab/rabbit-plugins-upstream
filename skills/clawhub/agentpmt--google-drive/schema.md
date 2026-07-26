# Google Drive Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `google-drive`

x402 availability: not enabled for this product.

## `copy_file`

Action slug: `copy-file`

Price: `5` credits

Create a copy of a file in Google Drive.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `create_parent_folders` | `boolean` | no | Auto-create missing folders (default false) |
| `file_id` | `string` | yes | The file ID to copy |
| `folder_id` | `string` | no | Root context for resolving parent_folder_path |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |
| `new_name` | `string` | no | Name for the copy |
| `parent_folder_id` | `string` | no | Destination folder ID (provide only one of parent_folder_id or parent_folder_path) |
| `parent_folder_path` | `string` | no | Destination folder path |

Sample parameters:

```json
{
  "create_parent_folders": false,
  "file_id": "example file id",
  "folder_id": "example folder id",
  "include_shared_drives": true,
  "new_name": "example new name",
  "parent_folder_id": "example parent folder id",
  "parent_folder_path": "example parent folder path"
}
```

Generated JSON parameter schema:

```json
{
  "create_parent_folders": {
    "default": false,
    "description": "Auto-create missing folders (default false)",
    "required": false,
    "type": "boolean"
  },
  "file_id": {
    "description": "The file ID to copy",
    "required": true,
    "type": "string"
  },
  "folder_id": {
    "description": "Root context for resolving parent_folder_path",
    "required": false,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  },
  "new_name": {
    "description": "Name for the copy",
    "required": false,
    "type": "string"
  },
  "parent_folder_id": {
    "description": "Destination folder ID (provide only one of parent_folder_id or parent_folder_path)",
    "required": false,
    "type": "string"
  },
  "parent_folder_path": {
    "description": "Destination folder path",
    "required": false,
    "type": "string"
  }
}
```

## `create_folder`

Action slug: `create-folder`

Price: `5` credits

Create a new folder in Google Drive.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `create_parent_folders` | `boolean` | no | Auto-create missing parent folders (default false) |
| `folder_id` | `string` | no | Root context for resolving parent_folder_path (defaults to My Drive root) |
| `folder_name` | `string` | yes | Name of the new folder |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |
| `parent_folder_id` | `string` | no | Parent folder ID (provide only one of parent_folder_id or parent_folder_path) |
| `parent_folder_path` | `string` | no | Parent folder path |

Sample parameters:

```json
{
  "create_parent_folders": false,
  "folder_id": "example folder id",
  "folder_name": "example folder name",
  "include_shared_drives": true,
  "parent_folder_id": "example parent folder id",
  "parent_folder_path": "example parent folder path"
}
```

Generated JSON parameter schema:

```json
{
  "create_parent_folders": {
    "default": false,
    "description": "Auto-create missing parent folders (default false)",
    "required": false,
    "type": "boolean"
  },
  "folder_id": {
    "description": "Root context for resolving parent_folder_path (defaults to My Drive root)",
    "required": false,
    "type": "string"
  },
  "folder_name": {
    "description": "Name of the new folder",
    "required": true,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  },
  "parent_folder_id": {
    "description": "Parent folder ID (provide only one of parent_folder_id or parent_folder_path)",
    "required": false,
    "type": "string"
  },
  "parent_folder_path": {
    "description": "Parent folder path",
    "required": false,
    "type": "string"
  }
}
```

## `delete_file`

Action slug: `delete-file`

Price: `5` credits

Permanently delete a file or folder (not recoverable).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | yes | The file or folder ID to permanently delete |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |

Sample parameters:

```json
{
  "file_id": "example file id",
  "include_shared_drives": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "The file or folder ID to permanently delete",
    "required": true,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  }
}
```

## `download_file_to_storage`

Action slug: `download-file-to-storage`

Price: `5` credits

Download a file from Drive and store it in temporary AgentPMT storage. Google Docs/Sheets/Slides are automatically exported (Docs to PDF, Sheets to XLSX, Slides to PPTX by default).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `acknowledge_abuse` | `boolean` | no | Allow downloading files flagged as abusive (non-Google files only, default false) |
| `expiration_days` | `integer` | no | Days until the stored file expires (default 7, range 1-7) |
| `export_format` | `string` | no | Override export format for Google Workspace files |
| `file_id` | `string` | yes | Drive file ID to download |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |
| `max_bytes` | `integer` | no | Safety limit for download size in bytes (default 25 MiB, max 250 MiB) |
| `output_filename` | `string` | no | Override the stored filename |

Sample parameters:

```json
{
  "acknowledge_abuse": false,
  "expiration_days": 7,
  "export_format": "pdf",
  "file_id": "example file id",
  "include_shared_drives": true,
  "max_bytes": 26214400,
  "output_filename": "example output filename"
}
```

Generated JSON parameter schema:

```json
{
  "acknowledge_abuse": {
    "default": false,
    "description": "Allow downloading files flagged as abusive (non-Google files only, default false)",
    "required": false,
    "type": "boolean"
  },
  "expiration_days": {
    "default": 7,
    "description": "Days until the stored file expires (default 7, range 1-7)",
    "maximum": 7,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "export_format": {
    "description": "Override export format for Google Workspace files",
    "enum": [
      "pdf",
      "txt",
      "html",
      "docx",
      "xlsx",
      "pptx",
      "odt",
      "rtf",
      "epub",
      "zip",
      "csv",
      "tsv"
    ],
    "required": false,
    "type": "string"
  },
  "file_id": {
    "description": "Drive file ID to download",
    "required": true,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  },
  "max_bytes": {
    "default": 26214400,
    "description": "Safety limit for download size in bytes (default 25 MiB, max 250 MiB)",
    "maximum": 262144000,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "output_filename": {
    "description": "Override the stored filename",
    "required": false,
    "type": "string"
  }
}
```

## `ensure_folder_path`

Action slug: `ensure-folder-path`

Price: `5` credits

Ensure a full folder path exists, creating any missing segments. Returns the final folder ID.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `ensure_path` | `string` | yes | Folder path to ensure (e.g., 'Projects/Client A/Deliverables') |
| `folder_id` | `string` | no | Root folder ID to resolve path under (defaults to My Drive root) |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |

Sample parameters:

```json
{
  "ensure_path": "example ensure path",
  "folder_id": "example folder id",
  "include_shared_drives": true
}
```

Generated JSON parameter schema:

```json
{
  "ensure_path": {
    "description": "Folder path to ensure (e.g., 'Projects/Client A/Deliverables')",
    "required": true,
    "type": "string"
  },
  "folder_id": {
    "description": "Root folder ID to resolve path under (defaults to My Drive root)",
    "required": false,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  }
}
```

## `get_file_metadata`

Action slug: `get-file-metadata`

Price: `5` credits

Retrieve metadata for a specific file or folder.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | yes | Drive file or folder ID |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |

Sample parameters:

```json
{
  "file_id": "example file id",
  "include_shared_drives": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "Drive file or folder ID",
    "required": true,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  }
}
```

## `list_permissions`

Action slug: `list-permissions`

Price: `5` credits

List all permissions on a file or folder.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | yes | The file or folder ID |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |

Sample parameters:

```json
{
  "file_id": "example file id",
  "include_shared_drives": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "The file or folder ID",
    "required": true,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  }
}
```

## `move_file`

Action slug: `move-file`

Price: `5` credits

Move a file or folder to a different location in Google Drive.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `create_parent_folders` | `boolean` | no | Auto-create missing folders in destination_folder_path (default false) |
| `destination_folder_id` | `string` | no | Destination folder ID (provide only one of destination_folder_id or destination_folder_path) |
| `destination_folder_path` | `string` | no | Destination folder path |
| `file_id` | `string` | yes | The file or folder ID to move |
| `folder_id` | `string` | no | Root context for resolving destination_folder_path |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |
| `remove_existing_parents` | `boolean` | no | Remove the file from its current parent(s) (default true). If false, destination is added as an additional parent. |

Sample parameters:

```json
{
  "create_parent_folders": false,
  "destination_folder_id": "example destination folder id",
  "destination_folder_path": "example destination folder path",
  "file_id": "example file id",
  "folder_id": "example folder id",
  "include_shared_drives": true,
  "remove_existing_parents": true
}
```

Generated JSON parameter schema:

```json
{
  "create_parent_folders": {
    "default": false,
    "description": "Auto-create missing folders in destination_folder_path (default false)",
    "required": false,
    "type": "boolean"
  },
  "destination_folder_id": {
    "description": "Destination folder ID (provide only one of destination_folder_id or destination_folder_path)",
    "required": false,
    "type": "string"
  },
  "destination_folder_path": {
    "description": "Destination folder path",
    "required": false,
    "type": "string"
  },
  "file_id": {
    "description": "The file or folder ID to move",
    "required": true,
    "type": "string"
  },
  "folder_id": {
    "description": "Root context for resolving destination_folder_path",
    "required": false,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  },
  "remove_existing_parents": {
    "default": true,
    "description": "Remove the file from its current parent(s) (default true). If false, destination is added as an additional parent.",
    "required": false,
    "type": "boolean"
  }
}
```

## `search_files`

Action slug: `search-files`

Price: `5` credits

Search for files and folders in Google Drive by text, MIME type, or folder location.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `folder_id` | `string` | no | Restrict to a specific folder by ID. Use 'root' for My Drive root. |
| `folder_path` | `string` | no | Restrict to a folder by path (e.g., 'Projects/Client A'), resolved under folder_id or root. |
| `include_shared_drives` | `boolean` | no | Include items from shared drives (default true) |
| `mime_type` | `string` | no | Filter by MIME type. Accepts aliases: folder, document, spreadsheet, presentation, drawing. Or a full MIME type string. |
| `order_by` | `string` | no | Drive orderBy string (default 'modifiedTime desc') |
| `page_size` | `integer` | no | Max results per page (default 25, max 1000) |
| `page_token` | `string` | no | Pagination token from a previous response |
| `query` | `string` | no | Plain-text search matched against full text and file name |
| `raw_query` | `string` | no | Advanced Drive query string (q=...). If provided, overrides query and other filters. |
| `trashed` | `boolean` | no | If true, include trashed items (default false) |

Sample parameters:

```json
{
  "folder_id": "example folder id",
  "folder_path": "example folder path",
  "include_shared_drives": true,
  "mime_type": "example mime type",
  "order_by": "modifiedTime desc",
  "page_size": 25,
  "page_token": "example page token",
  "query": "example search query"
}
```

Generated JSON parameter schema:

```json
{
  "folder_id": {
    "description": "Restrict to a specific folder by ID. Use 'root' for My Drive root.",
    "required": false,
    "type": "string"
  },
  "folder_path": {
    "description": "Restrict to a folder by path (e.g., 'Projects/Client A'), resolved under folder_id or root.",
    "required": false,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include items from shared drives (default true)",
    "required": false,
    "type": "boolean"
  },
  "mime_type": {
    "description": "Filter by MIME type. Accepts aliases: folder, document, spreadsheet, presentation, drawing. Or a full MIME type string.",
    "required": false,
    "type": "string"
  },
  "order_by": {
    "default": "modifiedTime desc",
    "description": "Drive orderBy string (default 'modifiedTime desc')",
    "required": false,
    "type": "string"
  },
  "page_size": {
    "default": 25,
    "description": "Max results per page (default 25, max 1000)",
    "maximum": 1000,
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
    "description": "Plain-text search matched against full text and file name",
    "required": false,
    "type": "string"
  },
  "raw_query": {
    "description": "Advanced Drive query string (q=...). If provided, overrides query and other filters.",
    "required": false,
    "type": "string"
  },
  "trashed": {
    "default": false,
    "description": "If true, include trashed items (default false)",
    "required": false,
    "type": "boolean"
  }
}
```

## `share_file`

Action slug: `share-file`

Price: `5` credits

Share a file or folder by creating a permission.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `email_message` | `string` | no | Custom message in the notification email |
| `file_id` | `string` | yes | The file or folder ID to share |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |
| `permission` | `object` | yes | Permission details |
| `send_notification` | `boolean` | no | Send email notification for user/group shares (default true) |

Sample parameters:

```json
{
  "email_message": "user@example.com",
  "file_id": "example file id",
  "include_shared_drives": true,
  "permission": {
    "allow_file_discovery": false,
    "domain": "example domain",
    "email": "user@example.com",
    "permission_type": "user",
    "role": "reader"
  },
  "send_notification": true
}
```

Generated JSON parameter schema:

```json
{
  "email_message": {
    "description": "Custom message in the notification email",
    "required": false,
    "type": "string"
  },
  "file_id": {
    "description": "The file or folder ID to share",
    "required": true,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  },
  "permission": {
    "description": "Permission details",
    "properties": {
      "allow_file_discovery": {
        "default": false,
        "description": "For anyone/domain types, allow discovery via search (default false)",
        "required": false,
        "type": "boolean"
      },
      "domain": {
        "description": "Domain for domain-type permissions",
        "required": false,
        "type": "string"
      },
      "email": {
        "description": "Email for user/group permissions. Also accepts emailAddress as alias.",
        "required": false,
        "type": "string"
      },
      "permission_type": {
        "description": "Permission type",
        "enum": [
          "user",
          "group",
          "domain",
          "anyone"
        ],
        "required": true,
        "type": "string"
      },
      "role": {
        "description": "Permission role",
        "enum": [
          "reader",
          "commenter",
          "writer",
          "organizer",
          "fileOrganizer"
        ],
        "required": true,
        "type": "string"
      }
    },
    "required": true,
    "type": "object"
  },
  "send_notification": {
    "default": true,
    "description": "Send email notification for user/group shares (default true)",
    "required": false,
    "type": "boolean"
  }
}
```

## `trash_file`

Action slug: `trash-file`

Price: `5` credits

Move a file or folder to the trash (recoverable).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | yes | The file or folder ID to trash |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |

Sample parameters:

```json
{
  "file_id": "example file id",
  "include_shared_drives": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "The file or folder ID to trash",
    "required": true,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  }
}
```

## `upload_file_from_storage`

Action slug: `upload-file-from-storage`

Price: `5` credits

Upload a file into Google Drive. Provide exactly one source: source_content_base64 (requires filename), source_file_url, or source_file_id. Local file paths are NOT supported.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `content_type` | `string` | no | MIME type override for upload (inferred from filename if omitted) |
| `create_parent_folders` | `boolean` | no | Auto-create missing folders in parent_folder_path (default false) |
| `filename` | `string` | no | Filename for the uploaded file (required with source_content_base64, optional otherwise) |
| `folder_id` | `string` | no | Root context for resolving parent_folder_path (defaults to My Drive root) |
| `include_shared_drives` | `boolean` | no | Include shared drives (default true) |
| `max_upload_bytes` | `integer` | no | Safety limit for upload size in bytes (default 25 MiB, max 250 MiB) |
| `parent_folder_id` | `string` | no | Destination folder ID (provide only one of parent_folder_id or parent_folder_path) |
| `parent_folder_path` | `string` | no | Destination folder path (e.g., 'Projects/Reports') |
| `source_content_base64` | `string` | no | Base64-encoded content to upload into Drive |
| `source_file_id` | `string` | no | AgentPMT storage file_id to upload into Drive |
| `source_file_url` | `string` | no | Public URL to fetch and upload into Drive |

Sample parameters:

```json
{
  "content_type": "Draft marketing copy to check for banned phrases.",
  "create_parent_folders": false,
  "filename": "example filename",
  "folder_id": "example folder id",
  "include_shared_drives": true,
  "max_upload_bytes": 26214400,
  "parent_folder_id": "example parent folder id",
  "parent_folder_path": "example parent folder path"
}
```

Generated JSON parameter schema:

```json
{
  "content_type": {
    "description": "MIME type override for upload (inferred from filename if omitted)",
    "required": false,
    "type": "string"
  },
  "create_parent_folders": {
    "default": false,
    "description": "Auto-create missing folders in parent_folder_path (default false)",
    "required": false,
    "type": "boolean"
  },
  "filename": {
    "description": "Filename for the uploaded file (required with source_content_base64, optional otherwise)",
    "required": false,
    "type": "string"
  },
  "folder_id": {
    "description": "Root context for resolving parent_folder_path (defaults to My Drive root)",
    "required": false,
    "type": "string"
  },
  "include_shared_drives": {
    "default": true,
    "description": "Include shared drives (default true)",
    "required": false,
    "type": "boolean"
  },
  "max_upload_bytes": {
    "default": 26214400,
    "description": "Safety limit for upload size in bytes (default 25 MiB, max 250 MiB)",
    "maximum": 262144000,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "parent_folder_id": {
    "description": "Destination folder ID (provide only one of parent_folder_id or parent_folder_path)",
    "required": false,
    "type": "string"
  },
  "parent_folder_path": {
    "description": "Destination folder path (e.g., 'Projects/Reports')",
    "required": false,
    "type": "string"
  },
  "source_content_base64": {
    "description": "Base64-encoded content to upload into Drive",
    "required": false,
    "type": "string"
  },
  "source_file_id": {
    "description": "AgentPMT storage file_id to upload into Drive",
    "required": false,
    "type": "string"
  },
  "source_file_url": {
    "description": "Public URL to fetch and upload into Drive",
    "required": false,
    "type": "string"
  }
}
```
