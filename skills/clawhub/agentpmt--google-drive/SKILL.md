---
name: google-drive
description: "Google Drive file management: search, upload, download, organize folders, move/copy files, share with permissions, and export Google Docs formats. Use when an agent needs google drive, search drive files by name or content, download files to agentpmt storage for processing, upload files to drive from agentpmt storage, create folder structures and organize files, copy file, file id, new name through AgentPMT-hosted remote tool calls. Discovery terms: google drive."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/google-drive
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/google-drive"}}
---
# Google Drive

## Freshness
Last updated: `2026-06-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Give your AI agent access to Google Drive for seamless file management, organization, and collaboration. Search across your Drive to find files by name or content, download files to AgentPMT storage for processing, and upload new files back to Drive from AgentPMT storage or public URLs. Create folder structures with automatic path creation, move and copy files between folders, and manage sharing permissions to collaborate with others. Export Google Docs, Sheets, and Slides to formats like PDF, DOCX, or XLSX. This tool is essential for agents that need to work with documents stored in Drive, automate file organization, sync content between systems, or manage document workflows. All operations run securely through your connected Google OAuth account with support for both personal Drive and shared drives.

## Product Instructions
### Google Drive

#### Overview
Search, upload, download, organize, and share Google Drive files and folders. Supports My Drive and shared drives, folder path resolution, file export/conversion, and permission management.

#### Actions

##### search_files
Search for files and folders in Google Drive by text, MIME type, or folder location.

**Required fields:** None (returns all non-trashed files by default)

**Optional fields:**
- `query` (string) - Plain-text search matched against full text and file name
- `raw_query` (string) - Advanced Drive query string (used directly as the `q` parameter). If provided, overrides `query` and other filters
- `mime_type` (string) - Filter by MIME type. Accepts aliases: `folder`, `document`, `spreadsheet`, `presentation`, `drawing`, or a full MIME type string
- `folder_id` (string) - Restrict to a specific folder by ID. Use `"root"` for My Drive root
- `folder_path` (string) - Restrict to a folder by path (e.g., `"Projects/Client A"`), resolved under `folder_id` or root
- `trashed` (boolean, default: false) - If true, include trashed items
- `page_size` (integer, default: 25, max: 1000) - Results per page
- `page_token` (string) - Pagination token from a previous response's `next_page_token`
- `order_by` (string, default: `"modifiedTime desc"`) - Sort order
- `include_shared_drives` (boolean, default: true) - Include items from shared drives

```json
{
  "action": "search_files",
  "query": "quarterly report",
  "mime_type": "document",
  "page_size": 10
}
```

```json
{
  "action": "search_files",
  "folder_path": "Finance/2026",
  "mime_type": "spreadsheet"
}
```

```json
{
  "action": "search_files",
  "raw_query": "mimeType='application/pdf' and modifiedTime > '2026-01-01T00:00:00'"
}
```

##### get_file_metadata
Retrieve metadata for a specific file or folder.

**Required fields:**
- `file_id` (string) - The Drive file or folder ID

```json
{
  "action": "get_file_metadata",
  "file_id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms"
}
```

##### download_file_to_storage
Download a file from Drive and store it in temporary storage. Google Docs/Sheets/Slides are automatically exported (Docs to PDF, Sheets to XLSX, Slides to PPTX by default).

**Required fields:**
- `file_id` (string) - The Drive file ID

**Optional fields:**
- `export_format` (string, enum: `pdf`, `txt`, `html`, `docx`, `xlsx`, `pptx`, `odt`, `rtf`, `epub`, `zip`, `csv`, `tsv`) - Override the export format for Google Workspace files
- `output_filename` (string) - Override the stored filename
- `max_bytes` (integer, default: 26214400 / 25 MiB, max: 262144000 / 250 MiB) - Safety limit for download size
- `expiration_days` (integer, default: 7, range: 1-7) - Days until the stored file expires
- `acknowledge_abuse` (boolean, default: false) - Allow downloading files flagged as abusive (non-Google files only)

```json
{
  "action": "download_file_to_storage",
  "file_id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "export_format": "docx"
}
```

```json
{
  "action": "download_file_to_storage",
  "file_id": "1abc123def456",
  "output_filename": "invoice_march.pdf",
  "expiration_days": 3
}
```

##### upload_file_from_storage
Upload a file into Google Drive. Provide exactly one source. Files under 10 MiB use multipart upload; larger files use resumable upload automatically.

**Required fields (exactly one):**
- `source_content_base64` (string) - Base64-encoded file content. **Requires `filename`**
- `source_file_url` (string) - Public URL to fetch content from
- `source_file_id` (string) - File ID from AgentPMT storage (from a previous download or upload)

**Optional fields:**
- `filename` (string) - Filename for the uploaded file (required with `source_content_base64`, optional otherwise)
- `content_type` (string) - MIME type override (inferred from filename if omitted)
- `parent_folder_id` (string) - Destination folder ID (provide only one of `parent_folder_id` or `parent_folder_path`)
- `parent_folder_path` (string) - Destination folder path (e.g., `"Projects/Reports"`)
- `create_parent_folders` (boolean, default: false) - Auto-create missing folders in `parent_folder_path`
- `max_upload_bytes` (integer, default: 26214400 / 25 MiB, max: 262144000 / 250 MiB) - Safety limit for upload size

**Local file paths are NOT supported.** You cannot pass a filesystem path.

```json
{
  "action": "upload_file_from_storage",
  "source_content_base64": "SGVsbG8gV29ybGQh",
  "filename": "greeting.txt",
  "parent_folder_path": "Documents/Notes",
  "create_parent_folders": true
}
```

```json
{
  "action": "upload_file_from_storage",
  "source_file_url": "https://example.com/report.pdf",
  "filename": "annual_report_2026.pdf",
  "parent_folder_id": "1AbCdEfGhIjKlMnOpQrStUvWxYz"
}
```

```json
{
  "action": "upload_file_from_storage",
  "source_file_id": "storage_abc123",
  "parent_folder_path": "Backups"
}
```

##### create_folder
Create a new folder in Google Drive.

**Required fields:**
- `folder_name` (string) - Name of the new folder

**Optional fields:**
- `parent_folder_id` (string) - Parent folder ID (provide only one of `parent_folder_id` or `parent_folder_path`)
- `parent_folder_path` (string) - Parent folder path
- `create_parent_folders` (boolean, default: false) - Auto-create missing parent folders
- `folder_id` (string) - Root context for resolving `parent_folder_path` (defaults to My Drive root)

```json
{
  "action": "create_folder",
  "folder_name": "March Invoices",
  "parent_folder_path": "Finance/2026",
  "create_parent_folders": true
}
```

##### ensure_folder_path
Ensure a full folder path exists, creating any missing segments. Returns the final folder ID.

**Required fields:**
- `ensure_path` (string) - Folder path to ensure (e.g., `"Projects/Client A/Deliverables"`)

**Optional fields:**
- `folder_id` (string) - Root folder ID to resolve path under (defaults to My Drive root)

```json
{
  "action": "ensure_folder_path",
  "ensure_path": "Projects/Client A/Deliverables/Q1"
}
```

##### move_file
Move a file or folder to a different location.

**Required fields:**
- `file_id` (string) - The file or folder ID to move
- One of: `destination_folder_id` (string) or `destination_folder_path` (string)

**Optional fields:**
- `remove_existing_parents` (boolean, default: true) - If true, removes the file from its current parent(s). If false, the destination is added as an additional parent
- `create_parent_folders` (boolean, default: false) - Auto-create missing folders in `destination_folder_path`
- `folder_id` (string) - Root context for resolving `destination_folder_path`

```json
{
  "action": "move_file",
  "file_id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "destination_folder_path": "Archive/2025"
}
```

##### copy_file
Create a copy of a file.

**Required fields:**
- `file_id` (string) - The file ID to copy

**Optional fields:**
- `new_name` (string) - Name for the copy
- `parent_folder_id` (string) - Destination folder ID (provide only one of `parent_folder_id` or `parent_folder_path`)
- `parent_folder_path` (string) - Destination folder path
- `create_parent_folders` (boolean, default: false) - Auto-create missing folders

```json
{
  "action": "copy_file",
  "file_id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "new_name": "Budget 2026 (Copy)",
  "parent_folder_path": "Finance/Templates"
}
```

##### trash_file
Move a file or folder to the trash (recoverable).

**Required fields:**
- `file_id` (string) - The file or folder ID to trash

```json
{
  "action": "trash_file",
  "file_id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms"
}
```

##### delete_file
Permanently delete a file or folder (not recoverable).

**Required fields:**
- `file_id` (string) - The file or folder ID to delete

```json
{
  "action": "delete_file",
  "file_id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms"
}
```

##### share_file
Share a file or folder by creating a permission.

**Required fields:**
- `file_id` (string) - The file or folder ID to share
- `permission` (object) - Permission details:
  - `type` (string, enum: `user`, `group`, `domain`, `anyone`) - Permission type
  - `role` (string, enum: `reader`, `commenter`, `writer`, `organizer`, `fileOrganizer`) - Permission role
  - `email` (string) - Required for `user` or `group` types. Also accepts `emailAddress` as alias
  - `domain` (string) - Required for `domain` type
  - `allow_file_discovery` (boolean, default: false) - For `anyone`/`domain` types, allow discovery via search

**Optional fields:**
- `send_notification` (boolean, default: true) - Send email notification (only for `user`/`group` types)
- `email_message` (string) - Custom message in the notification email

```json
{
  "action": "share_file",
  "file_id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "permission": {
    "type": "user",
    "role": "writer",
    "email": "colleague@example.com"
  },
  "email_message": "Here is the project document for your review."
}
```

```json
{
  "action": "share_file",
  "file_id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "permission": {
    "type": "anyone",
    "role": "reader"
  },
  "send_notification": false
}
```

##### list_permissions
List all permissions on a file or folder.

**Required fields:**
- `file_id` (string) - The file or folder ID

```json
{
  "action": "list_permissions",
  "file_id": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms"
}
```

#### Common Workflows

##### 1. Organize uploaded content into a folder structure
1. Use `ensure_folder_path` with `ensure_path: "Projects/Client B/Assets"` to create the full path
2. Use `upload_file_from_storage` with `source_file_url` or `source_content_base64` and set `parent_folder_path: "Projects/Client B/Assets"`
3. Use `share_file` to grant the client read access

##### 2. Download a Google Doc, convert, and reshare
1. Use `search_files` with `query: "proposal draft"` and `mime_type: "document"` to find the file
2. Use `download_file_to_storage` with the `file_id` and `export_format: "docx"` to get a Word version
3. The returned storage file ID can be used with other tools or re-uploaded elsewhere

##### 3. Archive old files to a subfolder
1. Use `search_files` with `folder_path: "Active Projects"` to list files
2. Use `ensure_folder_path` with `ensure_path: "Archive/2025"` to ensure the archive folder exists
3. Use `move_file` for each file, setting `destination_folder_path: "Archive/2025"`

#### Important Notes
- **MIME type aliases:** Use `folder`, `document`, `spreadsheet`, `presentation`, or `drawing` instead of full MIME strings when filtering searches
- **Folder path resolution:** Paths use `/` separators (e.g., `"Projects/Client A/Reports"`). If a path segment matches multiple folders with the same name, the tool prefers the exact case match. If truly ambiguous, it returns candidate IDs so you can use the direct folder ID instead
- **Download size limits:** Default 25 MiB, max 250 MiB. Increase `max_bytes` for larger files
- **Upload size limits:** Default 25 MiB, max 250 MiB. Increase `max_upload_bytes` for larger files
- **Google Workspace exports:** Google Docs export to PDF by default, Sheets to XLSX, Slides to PPTX, Drawings to PDF. Override with `export_format`
- **Shared drives:** Included by default (`include_shared_drives: true`). Set to false to exclude
- **Trash vs delete:** `trash_file` is recoverable; `delete_file` is permanent
- **Upload sources:** Provide exactly one of `source_file_id`, `source_file_url`, or `source_content_base64`. Local filesystem paths are not supported
- **Downloaded files are stored temporarily** and expire after `expiration_days` (default 7, max 7)
- **Pagination:** When results exceed `page_size`, the response includes `next_page_token`. Pass it as `page_token` in the next request to get the next page

## When To Use
- Use this skill for `Google Drive` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: google drive, search drive files by name or content, download files to agentpmt storage for processing, upload files to drive from agentpmt storage, create folder structures and organize files, copy file, file id, new name.
- Supported action names: `copy_file`, `create_folder`, `delete_file`, `download_file_to_storage`, `ensure_folder_path`, `get_file_metadata`, `list_permissions`, `move_file`, `search_files`, `share_file`, `trash_file`, `upload_file_from_storage`.

## Use Cases
- Search Drive files by name or content
- Download files to AgentPMT storage for processing
- Upload files to Drive from AgentPMT storage
- Create folder structures and organize files
- Move and copy files between folders
- Share files and manage permissions
- Export Google Docs to PDF or DOCX
- Sync files between Drive and other systems
- Automate document organization workflows
- Manage shared drive content

## Related Product Skills
- File Management: ../file-management (ClawHub: `file-management`, page: https://clawhub.ai/agentpmt/file-management; skills.sh: `npx skills add AgentPMT/agent-skills --skill file-management`) - Use this companion skill to inspect, download, upload, and manage files referenced by this product.

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `12`.
x402 availability: not enabled for this product.

- `copy_file` (action slug: `copy-file`): Create a copy of a file in Google Drive. Price: `5` credits. Parameters: `create_parent_folders`, `file_id`, `folder_id`, `include_shared_drives`, `new_name`, `parent_folder_id`, `parent_folder_path`.
- `create_folder` (action slug: `create-folder`): Create a new folder in Google Drive. Price: `5` credits. Parameters: `create_parent_folders`, `folder_id`, `folder_name`, `include_shared_drives`, `parent_folder_id`, `parent_folder_path`.
- `delete_file` (action slug: `delete-file`): Permanently delete a file or folder (not recoverable). Price: `5` credits. Parameters: `file_id`, `include_shared_drives`.
- `download_file_to_storage` (action slug: `download-file-to-storage`): Download a file from Drive and store it in temporary AgentPMT storage. Google Docs/Sheets/Slides are automatically exported (Docs to PDF, Sheets to XLSX, Slides to PPTX by default). Price: `5` credits. Parameters: `acknowledge_abuse`, `expiration_days`, `export_format`, `file_id`, `include_shared_drives`, `max_bytes`, `output_filename`.
- `ensure_folder_path` (action slug: `ensure-folder-path`): Ensure a full folder path exists, creating any missing segments. Returns the final folder ID. Price: `5` credits. Parameters: `ensure_path`, `folder_id`, `include_shared_drives`.
- `get_file_metadata` (action slug: `get-file-metadata`): Retrieve metadata for a specific file or folder. Price: `5` credits. Parameters: `file_id`, `include_shared_drives`.
- `list_permissions` (action slug: `list-permissions`): List all permissions on a file or folder. Price: `5` credits. Parameters: `file_id`, `include_shared_drives`.
- `move_file` (action slug: `move-file`): Move a file or folder to a different location in Google Drive. Price: `5` credits. Parameters: `create_parent_folders`, `destination_folder_id`, `destination_folder_path`, `file_id`, `folder_id`, `include_shared_drives`, `remove_existing_parents`.
- `search_files` (action slug: `search-files`): Search for files and folders in Google Drive by text, MIME type, or folder location. Price: `5` credits. Parameters: `folder_id`, `folder_path`, `include_shared_drives`, `mime_type`, `order_by`, `page_size`, `page_token`, `query`, plus 2 more.
- `share_file` (action slug: `share-file`): Share a file or folder by creating a permission. Price: `5` credits. Parameters: `email_message`, `file_id`, `include_shared_drives`, `permission`, `send_notification`.
- `trash_file` (action slug: `trash-file`): Move a file or folder to the trash (recoverable). Price: `5` credits. Parameters: `file_id`, `include_shared_drives`.
- `upload_file_from_storage` (action slug: `upload-file-from-storage`): Upload a file into Google Drive. Provide exactly one source: source_content_base64 (requires filename), source_file_url, or source_file_id. Local file paths are NOT supported. Price: `5` credits. Parameters: `content_type`, `create_parent_folders`, `filename`, `folder_id`, `include_shared_drives`, `max_upload_bytes`, `parent_folder_id`, `parent_folder_path`, plus 3 more.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "google-drive"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "google-drive"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "google-drive"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "google-drive"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "google-drive"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "google-drive"
  }
}
```

## Call This Tool
Product slug: `google-drive`

Marketplace page: https://www.agentpmt.com/marketplace/google-drive

- AgentPMT account route: first use `../agentpmt-account-mcp-rest-api-setup` to connect the main MCP server or REST API for an Agent Group where this tool is enabled.
- x402 route: not enabled for this product.
- AgentPMT overview: use `../what-is-agentpmt` for marketplace, Agent Group, workflow, MCP, REST, and payment concepts.

If those setup skills are not installed beside this product skill, use the downloads below.

Core AgentPMT setup skills:
- What AgentPMT is: ../what-is-agentpmt
  - ClawHub page: https://clawhub.ai/agentpmt/what-is-agentpmt
  - OpenClaw install: `openclaw skills install what-is-agentpmt`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup
  - ClawHub page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup
  - OpenClaw install: `openclaw skills install agentpmt-account-mcp-rest-api-setup`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`

skills.sh install script:

```bash
npx skills add AgentPMT/agent-skills --skill what-is-agentpmt
npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup
```

MCP call shape after the main AgentPMT MCP server is connected:

```json
{
  "method": "tools/call",
  "params": {
    "name": "Google-Drive",
    "arguments": {
      "action": "copy_file",
      "create_parent_folders": false,
      "file_id": "example file id",
      "folder_id": "example folder id",
      "include_shared_drives": true,
      "new_name": "example new name",
      "parent_folder_id": "example parent folder id",
      "parent_folder_path": "example parent folder path"
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "google-drive",
  "parameters": {
    "action": "copy_file",
    "create_parent_folders": false,
    "file_id": "example file id",
    "folder_id": "example folder id",
    "include_shared_drives": true,
    "new_name": "example new name",
    "parent_folder_id": "example parent folder id",
    "parent_folder_path": "example parent folder path"
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `copy_file` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/google-drive
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
