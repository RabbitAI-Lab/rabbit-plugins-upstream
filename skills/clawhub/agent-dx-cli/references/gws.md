# GWS practice

Use GWS to verify the relationship between commands, contracts, requests, and output.
Preserve the target provider's names, headers, cursors, authentication, and file boundaries.

## 1. Read the contract

```sh
gws drive files list --help
gws schema drive.files.list
gws schema drive.File
```

Get command names and fields from current help/schema. Schema queries need no business credentials.
Check parameters, request bodies, and response types. Read referenced types as needed.

## 2. Implement the contract

| Object | Implementation and verification |
| --- | --- |
| Command tree | Generate `SERVICE RESOURCE [SUBRESOURCE] METHOD` from Discovery. Use `+` for helpers. |
| Input | Put URL/query parameters in `--params`. Put nested bodies in `--json`. Show only applicable flags. |
| Method schema | Return `httpMethod`, `path`, `description`, `parameters`, and `scopes`. Include `parameterOrder`, `requestBody`, and `response` when applicable. Body types contain `schemaRef` and `schema`. |
| Type references | Preserve nested `$ref` by default. `--resolve-refs` requests expansion. Bound cycles, depth, and size in the target CLI. |
| Descriptions | Explain the object, preconditions, direct effect, and completion boundary. Put constraints in typed contracts. |
| Output | Return raw API JSON by default. `--format json/table/yaml/csv` controls presentation. `--output PATH`/`-o` is a binary destination. |
| Files | Provide `--upload` and `--upload-content-type` only for methods that support media upload. |

A Discovery projection is not a complete JSON Schema validator. Expose accepted global parameters and preserve actual constraints.
Scopes are provider declarations. They do not prove current permissions or mean that every scope is required.
A description is documentation, not executable policy or current state. Use description when it can carry the required meaning.

## 3. Verify bounded reads

Run in an authorized environment:

```sh
gws drive files list \
  --params '{"pageSize":10,"fields":"files(id,name),nextPageToken"}' \
  --page-all --page-limit 2 --format json
```

- Use native API field masks.
- Read at most two pages. Emit one page per NDJSON line.
- Retain continuation cursors and state whether enumeration is complete.
- State whether the client or server removes unselected fields.

The pinned version defaults to 10 pages and 100 ms between pages. Set limits explicitly with `--page-limit` and `--page-delay`.

## 4. Verify previews

```sh
gws schema drive.files.create
gws drive files create \
  --json '{"name":"dx-preview.txt"}' \
  --dry-run
```

Check `dry_run`, `url`, `method`, `query_params`, `body`, and `is_multipart_upload`. Check secret masking.
The reference GWS preview can initialize authentication.
If the target declares a local-only preview, use the main skill to prove zero business HTTP, credential access, and recovery writes.
Declare metadata discovery as a separate read.

## 5. Verify adaptations

- If the target supports `@FILE` or `-`/stdin, declare these as extensions. Bound input size and parse JSON strictly. Allow one stdin consumer per call.
- Supply secrets through private files, stdin, or credential references. Keep the target provider's authentication and least privilege.
- Preserve flag meanings during migration. Compare HTTP requests and observable behavior to verify differences.
- Check structured JSON on stdout and diagnostics on stderr. Exit codes: 0 success; 1 API; 2 auth; 3 validation; 4 discovery; 5 internal.
- If MCP is required, use a compatible official SDK and a shared typed executor. Call the executor directly and test the interface separately. The pinned source has no MCP entrypoint.
- If an external response sanitizer is used, configure it explicitly first. Preserve payload and provenance. Treat sanitized results as data.

Reference: [GWS 0.22.5, commit a3768d0e82ad83cca2da97724e46bea4ff0e6dbd](https://github.com/googleworkspace/cli/tree/a3768d0e82ad83cca2da97724e46bea4ff0e6dbd/crates/google-workspace-cli/src).
Recheck behavior when changing the version.
