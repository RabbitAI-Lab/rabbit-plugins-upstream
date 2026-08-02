# Feishu Wiki API Notes

## Authentication

- App access token: `POST https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal`
  - Body: `{"app_id":"...","app_secret":"..."}`
  - Returns `tenant_access_token` (valid 2h)

## Wiki Operations

- **Create node**: `POST /open-apis/wiki/v2/spaces/{space_id}/nodes`
  - `obj_type`: `docx` (new-style document)
  - `node_type`: `origin`
  - `title`: document title
  - `parent_node_token` (optional): parent folder node

- **Get node**: `GET /open-apis/wiki/v2/spaces/{space_id}/nodes/{node_token}`

- **List nodes**: `GET /open-apis/wiki/v2/spaces/{space_id}/nodes`

## Docx Block Operations

- **List blocks**: `GET /open-apis/docx/v1/documents/{document_id}/blocks`
- **Create children**: `POST /open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/children`
  - Body: `{"children": [<block_objects>]}`
- **Batch delete**: `DELETE /open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/children/batch_delete`
  - Body: `{"start_index": N, "end_index": M}`

## Block Types

| Type | block_type |
|------|-----------|
| Text (page) | 1 |
| Text | 2 |
| Heading 1 | 3 |
| Heading 2 | 4 |
| Heading 3 | 5 |
| Heading 4 | 6 |
| Heading 5 | 7 |
| Heading 6 | 8 |
| Heading 7 | 9 |
| Heading 8 | 10 |
| Heading 9 | 11 |
| Bullet | 12 |
| Ordered | 13 |
| Code | 14 |
| Quote | 15 |
| Todo | 17 |
| Divider | 22 |

## Permissions Required

- `wiki:wiki` — Wiki read/write
- `docx:document` — Document content manipulation

## Rate Limits

- ~100 QPS for block creation
- Batch children in groups of 50 per request
