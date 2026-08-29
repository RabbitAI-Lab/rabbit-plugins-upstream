# Reducto Routing Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../SKILL.md#security--permissions) for full security policy.

> **⚠ Documents are sent to an external processor.** Reducto is a third-party service: every `document_url` you submit is fetched and read by Reducto, every file you upload is transmitted to and stored on its infrastructure, and the parsed text, tables, and extracted fields come back through its servers. The documents this is used on are rarely trivial — contracts, invoices, IDs, medical and financial records, HR files, signed forms — so the content, and whatever the extraction schema pulls out of it, is disclosed off-platform.
>
> - **Confirm the specific document and that the user accepts an external processor.** Say what is being uploaded and where it goes before doing it. Never submit a document the user did not name, and never batch a folder of them.
> - **A `document_url` discloses more than the file.** A signed S3 or Drive link, or any URL with a token in its query string, is a credential: handing it to Reducto lets that host fetch the object itself. Prefer an explicit upload of a file the user chose over passing a pre-signed URL.
> - **`schema` and `system_prompt` values are sent verbatim** and often describe exactly what the user is looking for — keep internal context and party names out of them where the extraction does not require it.
> - **Return the narrowest answer.** Extracted fields frequently contain personal data belonging to third parties (counterparties, patients, employees). Summarize rather than echoing whole documents, and do not forward results to another app or a trigger destination without approval for that transfer.
> - Uploaded files and job results persist in the user's Reducto account until deleted, and processing consumes paid credits.

**App name:** `reducto`
**Base URL proxied:** `platform.reducto.ai`

## API Path Pattern

```
/reducto/parse
/reducto/parse_async
/reducto/extract
/reducto/extract_async
/reducto/split
/reducto/split_async
/reducto/edit
/reducto/edit_async
/reducto/upload
/reducto/pipeline
/reducto/jobs
/reducto/job/{job_id}
/reducto/version
```

## Important Notes

- Connection uses API_KEY authentication method (not OAuth)
- Use async endpoints for large documents to avoid timeouts
- Upload presigned URLs expire quickly
- Use `reducto://` URLs from upload in subsequent requests
- Use `jobid://` to reuse parsed content from previous jobs

## Common Endpoints

### Parse Document

```bash
POST /reducto/parse
Content-Type: application/json

{
  "document_url": "https://example.com/document.pdf"
}
```

### Parse Document (Async)

```bash
POST /reducto/parse_async
Content-Type: application/json

{
  "document_url": "https://example.com/document.pdf"
}
```

### Extract Data

```bash
POST /reducto/extract
Content-Type: application/json

{
  "document_url": "https://example.com/document.pdf",
  "schema": {
    "type": "object",
    "properties": {
      "title": {"type": "string"},
      "date": {"type": "string"}
    }
  }
}
```

### Split Document

```bash
POST /reducto/split
Content-Type: application/json

{
  "document_url": "https://example.com/document.pdf",
  "split_description": [
    {"name": "section1", "description": "First section"}
  ]
}
```

### Edit Document

```bash
POST /reducto/edit
Content-Type: application/json

{
  "document_url": "https://example.com/form.pdf",
  "edit_instructions": "Fill the name field with 'John Doe'"
}
```

### Upload File

```bash
POST /reducto/upload
Content-Type: application/json

{}
```

### List Jobs

```bash
GET /reducto/jobs
```

### Get Job Status

```bash
GET /reducto/job/{job_id}
```

### Get Version

```bash
GET /reducto/version
```

## Job Status Values

- `Pending`: Job is queued or processing
- `InProgress`: Job is actively processing
- `Completed`: Job finished successfully
- `Failed`: Job failed

## Document URL Formats

- Public URL: `https://example.com/document.pdf`
- Presigned S3: `https://bucket.s3.amazonaws.com/key?...`
- Upload result: `reducto://file-id`
- Previous job: `jobid://job-id`

## Resources

- [Reducto Documentation](https://docs.reducto.ai)
- [Reducto API Reference](https://docs.reducto.ai/api-reference)
- [Reducto Studio](https://studio.reducto.ai)
