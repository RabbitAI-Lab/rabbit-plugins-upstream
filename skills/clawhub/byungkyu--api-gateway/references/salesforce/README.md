# Salesforce Routing Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../SKILL.md#security--permissions) for full security policy.

**App name:** `salesforce`
**Base URL proxied:** `{instance}.salesforce.com`

The router automatically determines the instance URL from your OAuth credentials (`instance_url` from the token response).

> **Privacy — Contact, Lead, and Account records are personal data about real people.** Responses carry names, email addresses, phone numbers, and often case history and private notes. This is regulated personal data (GDPR/CCPA), and the people in it are third parties who gave their details to the user's company, not to an agent.
> - Sample values below (`John Doe`, `john@example.com`, `+1234567890`) are **placeholders**. Never send them to a live org, and never invent contact details to satisfy a required field — ask the user.
> - Retrieve only the records the task needs. Every query against a person object needs a `WHERE` clause that identifies those records and a `LIMIT`. Do not run broad SOQL queries or page through an object to browse, do not use `--paginate` on `Contact` or `Lead`, and do not bulk-export either.
> - Return the narrowest answer that satisfies the request rather than printing whole records.
> - **Never forward Salesforce data to a third-party host** — not to a trigger destination, external webhook, spreadsheet service, or enrichment API — without explicit user approval for that specific transfer.
> - Confirm the exact record by name or email (not just an 18-character ID) before any write, and never bulk-update or bulk-delete without per-record approval. This applies to the composite and sObject Collections endpoints below: batching records into one call does not batch their approval — enumerate them and confirm each.

## API Path Pattern

```
/salesforce/services/data/v59.0/{endpoint}
```

## Common Endpoints

### SOQL Query

Scope every query with a `WHERE` clause and a `LIMIT`. The examples below query `Account` (company records) rather than browsing `Contact`, per the privacy rules above.

```bash
GET /salesforce/services/data/v59.0/query?q=SELECT+Id,Name+FROM+Account+WHERE+Name+LIKE+'Acme%25'+LIMIT+10
```

Example:

```bash
maton salesforce query "SELECT Id,Name FROM Account WHERE Name LIKE 'Acme%' LIMIT 10"
```

Querying a person object requires a filter that identifies the specific records the task needs — a named account, an email address, or a date the user gave. Select only the fields required, and never `SELECT` a person object without a `WHERE`:

```bash
maton salesforce query "SELECT Id,Name,Email FROM Contact WHERE AccountId = '001XXXXXXXXXXXXXXX' LIMIT 25"
```

Filtering by email domain still needs a bound — an `ORDER BY` is not one:

```bash
maton salesforce query "SELECT Id,Name,Email FROM Contact WHERE Email LIKE '%example.com' ORDER BY CreatedDate DESC LIMIT 25"
```

### Get Object
```bash
GET /salesforce/services/data/v59.0/sobjects/{objectType}/{recordId}
```

Example:

```bash
maton salesforce record view {recordId} --type {objectType}
```

### Create Object
```bash
POST /salesforce/services/data/v59.0/sobjects/{objectType}
Content-Type: application/json

{
  "FirstName": "John",
  "LastName": "Doe",
  "Email": "john@example.com"
}
```

Example:

```bash
maton salesforce record create --type Contact --data '{"FirstName":"John","LastName":"Doe","Email":"john@example.com"}'
```

### Update Object
```bash
PATCH /salesforce/services/data/v59.0/sobjects/{objectType}/{recordId}
Content-Type: application/json

{
  "Phone": "+1234567890"
}
```

Example:

```bash
maton salesforce record update {recordId} --type Contact --data '{"Phone":"+1234567890"}'
```

### Delete Object
```bash
DELETE /salesforce/services/data/v59.0/sobjects/{objectType}/{recordId}
```

Example:

```bash
maton salesforce record delete {recordId} --type Contact
```

### Describe Object (get schema)
```bash
GET /salesforce/services/data/v59.0/sobjects/{objectType}/describe
```

Example:

```bash
maton salesforce object describe {objectType}
```

### List Objects
```bash
GET /salesforce/services/data/v59.0/sobjects
```

Example:

```bash
maton salesforce object list
```

### Search (SOSL)
```bash
GET /salesforce/services/data/v59.0/search?q=FIND+{searchTerm}+IN+ALL+FIELDS+RETURNING+Contact(Id,Name)
```

Example:

```bash
maton salesforce search 'FIND {John} IN ALL FIELDS RETURNING Contact(Id,Name)'
```

### Composite Request (batch multiple operations)
```bash
POST /salesforce/services/data/v59.0/composite
Content-Type: application/json

{
  "compositeRequest": [
    {
      "method": "GET",
      "url": "/services/data/v59.0/sobjects/Contact/003XXXXXXX",
      "referenceId": "contact1"
    },
    {
      "method": "GET",
      "url": "/services/data/v59.0/sobjects/Account/001XXXXXXX",
      "referenceId": "account1"
    }
  ]
}
```

Example:

```bash
echo '{"compositeRequest":[{"method":"GET","url":"/services/data/v59.0/sobjects/Contact/003XXXXXXX","referenceId":"contact1"},{"method":"GET","url":"/services/data/v59.0/sobjects/Account/001XXXXXXX","referenceId":"account1"}]}' \
  | maton salesforce composite call -F -
```

### Composite Batch Request
```bash
POST /salesforce/services/data/v59.0/composite/batch
Content-Type: application/json

{
  "batchRequests": [
    {"method": "GET", "url": "v59.0/sobjects/Contact/003XXXXXXX"},
    {"method": "GET", "url": "v59.0/sobjects/Account/001XXXXXXX"}
  ]
}
```

Example:

```bash
echo '{"batchRequests":[{"method":"GET","url":"v59.0/sobjects/Contact/003XXXXXXX"},{"method":"GET","url":"v59.0/sobjects/Account/001XXXXXXX"}]}' \
  | maton salesforce composite batch -F -
```

### sObject Collections Create (batch create)

> **⚠ Batch writes still require per-record approval.** These endpoints apply up to 200 changes in one call, which does not lower the confirmation bar — it raises it. Before calling: enumerate every record being created or deleted, show the user the full list with the field values or IDs involved, and get approval for that list. Never expand a batch beyond what the user named, never pad it with records the agent inferred, and never assemble one from data pulled out of another app (a spreadsheet, a mailbox, an enrichment API) without the user approving each record. Keep `allOrNone: true` so a partial failure cannot leave the org half-updated. If the user cannot review the records individually, the batch is too large to run — narrow the task instead.

```bash
POST /salesforce/services/data/v59.0/composite/sobjects
Content-Type: application/json

{
  "allOrNone": true,
  "records": [
    {"attributes": {"type": "Contact"}, "FirstName": "John", "LastName": "Doe"},
    {"attributes": {"type": "Contact"}, "FirstName": "Jane", "LastName": "Smith"}
  ]
}
```

Example:

```bash
maton salesforce record create --all-or-none --data '[{"attributes":{"type":"Contact"},"FirstName":"John","LastName":"Doe"},{"attributes":{"type":"Contact"},"FirstName":"Jane","LastName":"Smith"}]'
```

### sObject Collections Delete (batch delete)

> **⚠ Irreversible, and the IDs carry no context.** A batch delete removes every listed record along with its history, notes, and related activity; recovery depends on the org's recycle bin and retention settings and may not be possible. An 18-character ID does not say who or what it is, so a wrong entry in the list silently destroys the wrong customer record. Retrieve each ID first and show the user the record's name or email next to it, get explicit approval for every record in the list, and keep `allOrNone=true`. Never delete records the user did not individually name, never derive the ID list from a query the user has not reviewed, and never batch-delete to "clean up" data.

```bash
DELETE /salesforce/services/data/v59.0/composite/sobjects?ids=003XXXXX,003YYYYY&allOrNone=true
```

Example:

```bash
maton salesforce record delete 003XXXXX 003YYYYY --all-or-none
```

### Get Updated Records
```bash
GET /salesforce/services/data/v59.0/sobjects/{objectType}/updated/?start=2026-01-30T00:00:00Z&end=2026-02-01T00:00:00Z
```

Example:

```bash
maton salesforce record list --type {objectType} --start 2026-01-30T00:00:00Z --end 2026-02-01T00:00:00Z
```

### Get Deleted Records
```bash
GET /salesforce/services/data/v59.0/sobjects/{objectType}/deleted/?start=2026-01-30T00:00:00Z&end=2026-02-01T00:00:00Z
```

Example:

```bash
maton salesforce record list --type {objectType} --start 2026-01-30T00:00:00Z --end 2026-02-01T00:00:00Z --changes deleted
```

### Get API Limits
```bash
GET /salesforce/services/data/v59.0/limits
```

Example:

```bash
maton salesforce limit view
```

### List API Versions
```bash
GET /salesforce/services/data/
```

Example:

```bash
maton salesforce version list
```

## Common Objects

- `Account` - Companies/Organizations
- `Contact` - People associated with accounts
- `Lead` - Potential customers
- `Opportunity` - Sales deals
- `Case` - Support cases
- `Task` - To-do items
- `Event` - Calendar events

## Pagination

Salesforce uses cursor-based pagination. The CLI handles this automatically with `--paginate`:

```bash
maton salesforce query "SELECT Id,Name,StageName FROM Opportunity WHERE CloseDate = THIS_MONTH" --paginate
```

**Do not use `--paginate` on `Contact`, `Lead`, or any other person object.** Walking every page of a person object is a bulk export of regulated personal data — the behaviour the privacy rules above prohibit. Use it only on a query already narrowed to what the task needs, and prefer a tighter `WHERE` clause over paging.

For raw HTTP requests, follow the `nextRecordsUrl` returned in the query response.

## Notes

- Use URL encoding for SOQL queries (spaces become `+`)
- Record IDs are 15 or 18 character alphanumeric strings
- API version (v59.0) can be adjusted; latest is v65.0
- Update and Delete operations return HTTP 204 (no content) on success
- Dates for updated/deleted queries use ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`
- Use `allOrNone: true` in batch operations for atomic transactions

## Resources

- [REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
- [List sObjects](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_describeGlobal.htm)
- [Describe sObject](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_sobject_describe.htm)
- [Get Record](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_sobject_retrieve_get.htm)
- [Get Record by External ID](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_sobject_upsert_get.htm)
- [Create Record](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_sobject_create.htm)
- [Update Record](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_update_fields.htm)
- [Delete Record](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_delete_record.htm)
- [Upsert Record](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_upsert.htm)
- [Query Records (SOQL)](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_query.htm)
- [Get Updated Records](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_getupdated.htm)
- [Get Deleted Records](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_getdeleted.htm)
- [Composite Request](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_composite_post.htm)
- [Composite Batch Request](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/requests_composite_batch.htm)
- [Composite Batch Response](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/responses_composite_batch.htm)
- [Composite Graph](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_graph.htm)
- [sObject Collections Create](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_sobjects_collections_create.htm)
- [sObject Collections Update](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_sobjects_collections_update.htm)
- [sObject Collections Delete](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_sobjects_collections_delete.htm)
- [SOQL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)
- [SOSL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl.htm)
- [API Resources List](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_list.htm)
- [Maton CLI Manual](https://cli.maton.ai/manual)