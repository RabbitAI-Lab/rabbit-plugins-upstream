# Autentique

## API Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../../SKILL.md#security--permissions) for full security policy.

> **Signature requests reach real people and carry legal weight.** Autentique is a Brazilian e-signature platform: a document created with signers who have an `email` (or a `phone` with SMS/WhatsApp delivery) sends each of them a signature request at once, from the account's name, and a completed signature is legally meaningful. Signing (`signDocument`), rejecting (`rejectDocument`), resending (`resendSignatures`), and deleting (`deleteDocument`) cannot be undone.
> - **Every GraphQL mutation is a write**, even though every request is a `POST`. Queries (`{ me … }`, `{ documents … }`) are reads; anything starting with `mutation` needs the user's explicit approval for that exact call.
> - **Use `sandbox: true` for any test document.** Sandbox documents consume no credits and Autentique deletes them after a few days. Without `sandbox: true`, a test is a real document.
> - **Never add a signer the user did not name.** Before creating a document or adding a signer, show the user the document name, the file, each signer's name, email or phone, delivery method, and action (`SIGN`, `APPROVE`, `SIGN_AS_A_WITNESS`, …), and get approval for that exact list. A signer given only a `name` gets no email; the signature link comes back in `link.short_link` for the user to deliver.
> - **Never sign on the user's behalf.** `signDocument` signs as the owner of the API key. Run it only when the user, being that signer, asks to sign that exact document by ID.
> - Documents, signer names, emails, phone numbers, and CPF/CNPJ numbers are personal data. Select only the fields the task needs, and do not copy them into logs, files, or trigger destinations.

**App name:** `autentique`
**Upstream base URL:** `api.autentique.com.br`

Replace the upstream base URL with the app name. Everything after the base URL including query strings is kept as-is. Any account-specific part of the base URL and the API credentials are stored in the Maton connection, and the gateway injects both so requests never carry them. For example:

- Upstream: `api.autentique.com.br/v2/graphql`
- Gateway: `api.maton.ai/autentique/v2/graphql`

**Important:** Autentique uses a GraphQL API. Every operation is a POST to `/v2/graphql` with a JSON body holding `query` (and optionally `variables`). File uploads use the [GraphQL multipart request spec](https://github.com/jaydenseric/graphql-multipart-request-spec) instead of JSON. GraphQL errors come back with HTTP `200` and an `errors` array, so check `errors` on every response, not just the status code.

### Account

#### Get Current User

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "{ me { id name email created_at } }"}
JSON
```

`{ me { id } }` is the cheapest check that the connection's key works.

#### Get Organization

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "{ organization { id uuid name created_at } }"}
JSON
```

#### List Groups

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "{ organizationGroups(limit: 20, page: 1) { total has_more_pages data { id uuid name members_count is_default } } }"}
JSON
```

### Documents

#### List Documents

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "{ documents(limit: 10, page: 1) { total current_page last_page has_more_pages data { id name sandbox created_at signatures_count signed_count rejected_count } } }"}
JSON
```

`limit` and `page` are required. Optional filters: `status` (`PENDING`, `SIGNED`, `NOT_SIGNED`, `REJECTED`, `DELETED`), `name`, `signer`, `search`, `start_date` / `end_date`, `folder_id`, `include_archived`, `include_deleted`, `context` (`USER`, `ORGANIZATION`, `GROUP`), and `orderBy: {field: "created_at", direction: DESC}`.

Sandbox documents are hidden by default. Add `showSandbox: true` to include them or `onlySandbox: true` to list only them:

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "{ documents(limit: 10, page: 1, onlySandbox: true) { total data { id name sandbox created_at } } }"}
JSON
```

**Response (trimmed):**

```json
{
  "data": {
    "documents": {
      "total": 1,
      "has_more_pages": false,
      "data": [
        {"id": "52fe02cbe5ad6afcb4c7b54c8eed10e61901633f000b3f886", "name": "Contract", "sandbox": true, "created_at": "2026-11-26T23:08:42.000000Z"}
      ]
    }
  }
}
```

#### Get a Document

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "query ($id: UUID!) { document(id: $id) { id name sandbox created_at deadline_at signatures_count signed_count files { original signed } signatures { public_id name email action { name } link { short_link } viewed { created_at } signed { created_at } rejected { created_at } } } }", "variables": {"id": "{document_id}"}}
JSON
```

**Note:** `{document_id}` stands for a real value; fill it in before sending the request.

Document IDs are 49-character hex strings even though the schema types them as `UUID`. `signatures` lists one entry per signer plus the document's author (the entry with a null `action`). A signer's `signed` / `rejected` / `viewed` event is `null` until it happens. `files.original` and `files.signed` are download URLs for the PDF. An unknown ID returns `"message": "document_not_found"` in `errors`.

#### Create a Document

> **Requires explicit user approval.** Signers with an `email` (or a `phone` with SMS/WhatsApp delivery) receive a signature request as soon as the document is created, and a real document consumes a credit. Confirm the file, the document name, and every signer first. Use `sandbox: true` unless the user wants a real signature request.

Uploads are `multipart/form-data` following the GraphQL multipart request spec: an `operations` part (the query, with `"file": null` in `variables`), a `map` part linking the file part to `variables.file`, and the file itself. `maton api` does not build a multipart envelope, so assemble the body first and hand it to `--input`:

```bash
# Read only the path the user approved. The assembled body is a copy of the file's bytes,
# so it is written under /tmp and deleted as soon as the upload returns.
FILE="$USER_SUPPLIED_PATH"            # exactly the path the user approved, never a discovered one
umask 077
BODY="$(mktemp "${TMPDIR:-/tmp}/autentique-upload.XXXXXX")" || exit 1
trap 'rm -f -- "$BODY"' EXIT HUP INT TERM
BOUNDARY="maton-$$"
OPERATIONS='{"query": "mutation ($document: DocumentInput!, $signers: [SignerInput!]!, $file: Upload!) { createDocument(sandbox: true, document: $document, signers: $signers, file: $file) { id name sandbox created_at signatures { public_id name action { name } link { short_link } } } }", "variables": {"document": {"name": "Contract"}, "signers": [{"name": "Signer Name", "action": "SIGN"}], "file": null}}'
{
  printf -- '--%s\r\nContent-Disposition: form-data; name="operations"\r\n\r\n%s\r\n' "$BOUNDARY" "$OPERATIONS"
  printf -- '--%s\r\nContent-Disposition: form-data; name="map"\r\n\r\n%s\r\n' "$BOUNDARY" '{"file": ["variables.file"]}'
  printf -- '--%s\r\nContent-Disposition: form-data; name="file"; filename="%s"\r\nContent-Type: application/pdf\r\n\r\n' "$BOUNDARY" "$(basename "$FILE")"
  cat "$FILE"
  printf -- '\r\n--%s--\r\n' "$BOUNDARY"
} > "$BODY"

maton api -X POST '/autentique/v2/graphql' \
  -H "Content-Type: multipart/form-data; boundary=$BOUNDARY" \
  --input "$BODY"
```

The example signer has only a `name`, so no email is sent and the signature link comes back in `link.short_link`. Other signer shapes:

- `{"email": "signer@example.com", "action": "SIGN"}`: Autentique emails the signature request.
- `{"name": "…", "phone": "+5511999999999", "delivery_method": "DELIVERY_METHOD_WHATSAPP", "action": "SIGN"}`: sent by WhatsApp (`DELIVERY_METHOD_SMS` for SMS).

`action` is one of `SIGN`, `APPROVE`, `RECOGNIZE`, `SIGN_AS_A_WITNESS`, `ACKNOWLEDGE_RECEIPT`, `ENDORSE_IN_BLACK`, `ENDORSE_IN_WHITE`. Useful `document` fields: `message`, `refusable`, `sortable` (sign in order), `deadline_at`, `reminder`, `stop_on_rejected`. `folder_id` (a mutation argument) files the document into a folder. Maximum file size is 5 MB on the free plan and 20 MB on paid plans.

**Response (trimmed):**

```json
{
  "data": {
    "createDocument": {
      "id": "52fe02cbe5ad6afcb4c7b54c8eed10e61901633f000b3f886",
      "name": "Contract",
      "sandbox": true,
      "signatures": [
        {"public_id": "529e2e7fe9ee11f1818d42010a2b6021", "name": null, "action": null, "link": null},
        {"public_id": "52a2a936e9ee11f1818d42010a2b6021", "name": "Signer Name", "action": {"name": "SIGN"}, "link": {"short_link": "https://..."}}
      ]
    }
  }
}
```

#### Update a Document

> **Requires explicit user approval.**

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "mutation ($id: UUID!, $document: UpdateDocumentInput!) { updateDocument(id: $id, document: $document) { id name } }", "variables": {"id": "{document_id}", "document": {"name": "Contract (v2)"}}}
JSON
```

**Note:** `{document_id}` stands for a real value; fill it in before sending the request.

`UpdateDocumentInput` takes the same settings as creation (`name`, `message`, `deadline_at`, `reminder`, `refusable`, …); the file and signers are not changed here.

#### Move a Document to a Folder

> **Requires explicit user approval.**

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "mutation ($document_id: UUID!, $folder_id: UUID) { moveDocumentToFolder(document_id: $document_id, folder_id: $folder_id) }", "variables": {"document_id": "{document_id}", "folder_id": "{folder_id}"}}
JSON
```

**Note:** `{document_id}` and `{folder_id}` stand for real values; fill them in before sending the request. Returns `true` on success.

#### Delete a Document

> **Irreversible — requires explicit approval naming the exact document ID.** Get the document first and show the user its name, status, and signers.

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "mutation ($id: UUID!) { deleteDocument(id: $id) }", "variables": {"id": "{document_id}"}}
JSON
```

**Note:** `{document_id}` stands for a real value; fill it in before sending the request. Returns `true` on success.

#### Sign a Document

> **Legally binding and irreversible — never on the agent's own initiative.** `signDocument` signs as the owner of the API key on the connection. Run it only when the user, who is that signer, asks to sign that exact document by ID.

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "mutation ($id: UUID!) { signDocument(id: $id) }", "variables": {"id": "{document_id}"}}
JSON
```

**Note:** `{document_id}` stands for a real value; fill it in before sending the request.

### Signers

#### Add a Signer

> **Requires explicit user approval.** A signer with an `email` or a `phone` is contacted immediately. Confirm the document and the signer's details first.

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "mutation ($document_id: UUID!, $signer: SignerInput!) { createSigner(document_id: $document_id, signer: $signer) { public_id name action { name } link { short_link } } }", "variables": {"document_id": "{document_id}", "signer": {"name": "Signer Name", "action": "SIGN"}}}
JSON
```

**Note:** `{document_id}` stands for a real value; fill it in before sending the request. `signer` takes the same shapes as in Create a Document.

#### Remove a Signer

> **Requires explicit user approval.**

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "mutation ($public_id: UUID!, $document_id: UUID!) { deleteSigner(public_id: $public_id, document_id: $document_id) }", "variables": {"public_id": "{signer_public_id}", "document_id": "{document_id}"}}
JSON
```

**Note:** `{signer_public_id}` and `{document_id}` stand for real values; fill them in before sending the request. `public_id` is the signer's `signatures[].public_id`.

#### Resend Signature Requests

> **Sends email/SMS/WhatsApp to real people — requires explicit approval naming each signer.**

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "mutation ($public_ids: [UUID]) { resendSignatures(public_ids: $public_ids) }", "variables": {"public_ids": ["{signer_public_id}"]}}
JSON
```

**Note:** `{signer_public_id}` stands for a real value; fill it in before sending the request.

### Folders

#### List Folders

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "{ folders(display_children: false, limit: 20, page: 1) { total has_more_pages data { id name slug context path children_counter created_at } } }"}
JSON
```

`display_children`, `limit`, and `page` are required. Optional: `type` (`DEFAULT`, `ORGANIZATION`, `GROUP`), `search`. `total` is `null` when there are no folders.

#### Get a Folder

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "query ($id: UUID!) { folder(id: $id) { id name path subfolders { id name } } }", "variables": {"id": "{folder_id}"}}
JSON
```

**Note:** `{folder_id}` stands for a real value; fill it in before sending the request.

#### List Documents in a Folder

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "query ($folder_id: UUID) { documentsByFolder(folder_id: $folder_id, limit: 10, page: 1) { total has_more_pages data { id name created_at } } }", "variables": {"folder_id": "{folder_id}"}}
JSON
```

**Note:** `{folder_id}` stands for a real value; fill it in before sending the request. `documentsByFolder` may not list a sandbox document moved into the folder; `documents(folder_id: "{folder_id}", limit: 10, page: 1, showSandbox: true)` is the fallback.

#### Create a Folder

> **Requires explicit user approval.**

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "mutation ($folder: FolderInput!) { createFolder(folder: $folder) { id name } }", "variables": {"folder": {"name": "Contracts 2026"}}}
JSON
```

Pass `parent_id` to create a subfolder.

### Email Templates

#### List Email Templates

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "{ emailTemplates(limit: 20, page: 1) { total data { id name type } } }"}
JSON
```

Use a template's `id` as `email_template_id` when creating a document.

### Pagination

List queries take `limit` and `page` (page numbers start at 1) and return `total`, `current_page`, `last_page`, and `has_more_pages`. Request the next `page` while `has_more_pages` is `true`:

```bash
maton api -X POST '/autentique/v2/graphql' -H 'Content-Type: application/json' --input - <<'JSON'
{"query": "{ documents(limit: 50, page: 2) { current_page last_page has_more_pages data { id name } } }"}
JSON
```

Each page is one request against the 60-per-minute limit.

### Notes

- **Rate limit:** 60 requests per minute per user. Responses carry `x-ratelimit-limit` and `x-ratelimit-remaining`; a `429` (`"Too Many Attempts."`) means wait before retrying.
- **Errors:** an invalid or revoked key returns HTTP `401` with `{"message": "unauthorized"}`. Every other error, including not-found and validation failures, returns HTTP `200` with an `errors` array (`message` such as `document_not_found`, `folder_not_found`, `validation` with details under `extensions.validation`, `unavailable_credits`). Always check `errors` before using `data`.
- **Sandbox:** `createDocument(sandbox: true, …)` creates a test document that uses no credits and is deleted automatically after a few days. `documents` hides sandbox documents unless `showSandbox: true` or `onlySandbox: true` is set.
- Document IDs are 49-character hex strings; signer `public_id` values are 32-character hex strings. Both are typed `UUID` in the schema.
- Timestamps are ISO 8601 strings in UTC (`2026-11-26T23:08:42.000000Z`).
- The schema is introspectable (`{ __schema { … } }`, `{ __type(name: "DocumentInput") { inputFields { name } } }`); use it to check argument names rather than guessing.
- Folder sharing, document transfer, biometric approval, and multi-file documents exist in the API but are out of scope for this reference.
- Authentication is handled by the gateway. Upstream, Autentique uses a Bearer API key rather than OAuth, but that key belongs to the Maton connection and is injected server-side: do not build an `Authorization` header for Autentique, never request an Autentique key, and never place one in a request, a script, or a trigger destination. Requests carry the Maton credential only, exactly like every other app in this gateway.

### Resources

- [Autentique API Introduction](https://docs.autentique.com.br/api)
- [Sandbox/tests](https://docs.autentique.com.br/api/integration-basics/sandbox-testes)
- [Creating a document](https://docs.autentique.com.br/api/mutations/criando-um-documento)
- [Retrieving documents](https://docs.autentique.com.br/api/queries/resgatando-documentos)
- [Error messages](https://docs.autentique.com.br/api/integration-basics/mensagens-de-erro)
- [GraphQL multipart request spec](https://github.com/jaydenseric/graphql-multipart-request-spec)
- [Maton CLI Manual](https://cli.maton.ai/manual)
