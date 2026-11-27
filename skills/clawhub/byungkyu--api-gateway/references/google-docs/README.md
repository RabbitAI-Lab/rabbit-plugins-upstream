# Google Docs

## API Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../../SKILL.md#security--permissions) for full security policy.

**App name:** `google-docs`
**Upstream base URL:** `docs.googleapis.com`

Replace the upstream base URL with the app name. Everything after the base URL including query strings is kept as-is. Any account-specific part of the base URL and the API credentials are stored in the Maton connection, and the gateway injects both so requests never carry them. For example:

- Upstream: `docs.googleapis.com/v1/documents`
- Gateway: `api.maton.ai/google-docs/v1/documents`

### Documents API

#### List Documents

Lists the user's documents through Google Drive's `files.list`, on this connection. Takes `files.list`'s parameters (`q`, `orderBy`, `pageSize`, `pageToken`, `fields`, `corpora`, `driveId`, `includeItemsFromAllDrives`, `supportsAllDrives`) and returns Drive's response; the gateway always limits results to this app's file type and leaves out trashed files.

With the `https://www.googleapis.com/auth/drive.readonly` scope it lists all the user's documents. With only `drive.file` (included by default) it lists just the documents created or opened through Maton, and the response carries a `maton_hint` field (and an `X-Maton-Hint` header) saying so; with neither scope it returns a `403` naming `drive.readonly`. To list everything, add `drive.readonly` when creating the connection, or with `maton connection reauthorize {connection_id} --scopes` listing the connection's current scopes plus `drive.readonly`. Other Drive endpoints are refused here; use a `google-drive` connection for them.

```bash
maton api "/google-docs/drive/v3/files?q=name%20contains%20'Notes'&orderBy=modifiedTime%20desc&pageSize=20&fields=nextPageToken,files(id,name,modifiedTime)"
```

#### Get Document

```bash
maton google-docs document get {documentId}            # human-readable summary (id, title, revision)
maton google-docs document get {documentId} --json     # full document payload (body, styles, etc.)
```

Or with `maton api`:

```bash
maton api '/google-docs/v1/documents/{documentId}'
```

**Note:** `{documentId}` stands for a real value; fill it in before sending the request.

#### Create Document

```bash
maton google-docs document create --title 'New Document'
```

Or with `maton api`:

```bash
maton api -X POST '/google-docs/v1/documents' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "title": "New Document"
}
JSON
```

#### Batch Update Document

```bash
maton google-docs document write {documentId} --text 'Hello, World!'
```

Or with `maton api`:

```bash
maton api -X POST '/google-docs/v1/documents/{documentId}:batchUpdate' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "requests": [
    {
      "insertText": {
        "location": {"index": 1},
        "text": "Hello, World!"
      }
    }
  ]
}
JSON
```

**Note:** `{documentId}` stands for a real value; fill it in before sending the request.

### Common BatchUpdate Requests

#### Insert Text

```json
{
  "insertText": {
    "location": {"index": 1},
    "text": "Text to insert"
  }
}
```

#### Delete Content

```json
{
  "deleteContentRange": {
    "range": {
      "startIndex": 1,
      "endIndex": 10
    }
  }
}
```

#### Replace All Text

```json
{
  "replaceAllText": {
    "containsText": {
      "text": "{{placeholder}}",
      "matchCase": true
    },
    "replaceText": "replacement value"
  }
}
```

#### Insert Table

```json
{
  "insertTable": {
    "location": {"index": 1},
    "rows": 3,
    "columns": 3
  }
}
```

#### Insert Inline Image

```json
{
  "insertInlineImage": {
    "location": {"index": 1},
    "uri": "https://example.com/image.png",
    "objectSize": {
      "height": {"magnitude": 100, "unit": "PT"},
      "width": {"magnitude": 100, "unit": "PT"}
    }
  }
}
```

#### Update Text Style

```json
{
  "updateTextStyle": {
    "range": {
      "startIndex": 1,
      "endIndex": 10
    },
    "textStyle": {
      "bold": true,
      "fontSize": {"magnitude": 14, "unit": "PT"}
    },
    "fields": "bold,fontSize"
  }
}
```

#### Insert Page Break

```json
{
  "insertPageBreak": {
    "location": {"index": 1}
  }
}
```

### Document Structure

The document body contains:
- `content` - Array of structural elements
- `body.content[].paragraph` - Paragraph element
- `body.content[].table` - Table element
- `body.content[].sectionBreak` - Section break

### Notes

- Index positions are 1-based (document starts at index 1)
- Use `endOfSegmentLocation` to append at end
- Multiple requests in batchUpdate are applied atomically
- Get document first to find correct indices for updates
- The `fields` parameter in style updates uses field mask syntax

### Resources

- [Google Docs API Overview](https://developers.google.com/docs/api/how-tos/overview)
- [Get Document](https://developers.google.com/docs/api/reference/rest/v1/documents/get)
- [Create Document](https://developers.google.com/docs/api/reference/rest/v1/documents/create)
- [Batch Update](https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate)
- [Request Types Reference](https://developers.google.com/docs/api/reference/rest/v1/documents/request)
- [Document Structure Guide](https://developers.google.com/docs/api/concepts/structure)
- [Maton CLI Manual](https://cli.maton.ai/manual)
