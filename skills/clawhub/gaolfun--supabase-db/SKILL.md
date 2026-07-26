# Supabase Database Integration — SKILL.md

## Metadata

**name:** supabase-db  
**description:** Query, insert, update, delete, and call RPC on Supabase (PostgREST) tables directly from OpenClaw. No server-side code required.  
**version:** 1.0.0  
**author:** OpenClaw / CCD  
**tags:** supabase, postgrest, database, rest-api, backend  

---

## Trigger Phrases

1. "query Supabase"
2. "fetch data from Supabase"
3. "insert into Supabase table"
4. "update Supabase record"
5. "delete from Supabase"
6. "call Supabase RPC function"
7. "list Supabase tables"
8. "get Supabase row by ID"
9. "batch insert Supabase"
10. "Supabase database operation"
11. "Supabase REST API"
12. "Supabase filter query"
13. "Supabase join tables"
14. "Supabase pagination"
15. "check Supabase table schema"

---

## Capabilities

| # | Capability | Description |
|---|-----------|-------------|
| 1 | **Query / Select** | Fetch rows with filters, sorting, pagination, and column selection via PostgREST |
| 2 | **Insert** | Insert one or multiple rows into a table |
| 3 | **Update** | Update rows matching a filter condition |
| 4 | **Delete** | Delete rows matching a filter condition |
| 5 | **Call RPC** | Invoke a stored procedure or function via `rpc()` endpoint |
| 6 | **List Tables** | Discover all tables in a schema via `information_schema` |
| 7 | **Get Row by ID** | Fetch a single row by its primary key |
| 8 | **Batch Operations** | Bulk insert or upsert rows in one request |
| 9 | **Introspect Schema** | Get column names, types, and constraints for a table |
| 10 | **Head Request** | Check row existence or count without fetching data |

---

## Prerequisites

### Required

| Item | Where to Find |
|------|--------------|
| **Project Reference** | Supabase Dashboard → Project Settings → General |
| **API Key (anon/public)** | Supabase Dashboard → Project Settings → API → `anon` key |
| **Table name** | Known in advance or discovered via List Tables |

> ⚠️ **Security Note:** The `anon` key is safe for client-side use. It respects Row Level Security (RLS) policies defined in your Supabase project. Never expose the `service_role` or `secret` key in skill parameters.

### Environment Variables (Recommended)

```bash
SUPABASE_URL=https://<PROJECT_REF>.supabase.co
SUPABASE_ANON_KEY=<your-anon-key>
```

Store these in your OpenClaw environment config so they are injected at runtime — never hardcode them in conversations.

---

## Detailed Steps

### Base URL

```
https://<PROJECT_REF>.supabase.co/rest/v1/<TABLE_NAME>
```

### Authentication Headers

Every request requires:

```
apikey: <SUPABASE_ANON_KEY>
Authorization: Bearer <SUPABASE_ANON_KEY>
Content-Type: application/json
Prefer: return=representation   # optional; returns inserted/updated rows
```

### 1. Query / Select Data

**Basic fetch — all rows:**

```
GET https://<PROJECT_REF>.supabase.co/rest/v1/users
Headers:
  apikey: <KEY>
  Authorization: Bearer <KEY>
```

**Select specific columns:**

```
GET https://<PROJECT_REF>.supabase.co/rest/v1/users?select=id,email,name
```

**Filter with PostgREST operators:**

| Operator | Meaning | Example |
|----------|---------|---------|
| `eq` | equals | `id=eq.42` |
| `neq` | not equals | `status=neq.archived` |
| `gt` | greater than | `age=gt.18` |
| `gte` | greater or equal | `score=gte.100` |
| `lt` | less than | `price=lt.50` |
| `lte` | less or equal | `qty=lte.10` |
| `like` | SQL LIKE (case-sensitive) | `name=like.*John*` |
| `ilike` | ILIKE (case-insensitive) | `email=ilike.*@gmail.*` |
| `in` | IN list | `status=in.active,pending` |
| `is` | IS (null, true, false) | `deleted_at=is.null` |
| `cs` | contains (array) | `tags=cs.{admin,editor}` |
| `ov` | overlaps (array) | `categories=ov.{tech,science}` |
| `not.eq` | chained negation | `active=not.eq.false` |

**Example — active users over 18:**

```
GET /rest/v1/users?age=gt.18&status=eq.active&select=id,name,email
```

**Sorting:**

```
GET /rest/v1/users?order=created_at.desc&limit=20&offset=0
```

**Pagination:**

```
GET /rest/v1/users?limit=10&offset=20   # page 3 (0-indexed)
```

**Count rows without fetching:**

```
GET /rest/v1/users?limit=0&select=id
(Combined with Prefer: count=exact)
```

**Or use the `HEAD` method:**

```
HEAD /rest/v1/users?status=eq.active
```

**Foreign key (join) expansion:**

```
GET /rest/v1/posts?select=id,title,user:users(name,avatar_url)
```

**Or nested expansion:**

```
GET /rest/v1/users?select=name,posts(id,title)
```

---

### 2. Insert Data

**Single row:**

```
POST https://<PROJECT_REF>.supabase.co/rest/v1/users
Headers:
  apikey: <KEY>
  Authorization: Bearer <KEY>
  Content-Type: application/json
  Prefer: return=representation

Body:
{
  "email": "alice@example.com",
  "name": "Alice",
  "age": 28
}

Response 201 Created:
[
  {
    "id": 15,
    "email": "alice@example.com",
    "name": "Alice",
    "age": 28,
    "created_at": "2026-07-04T12:00:00.000Z"
  }
]
```

**Bulk insert (array):**

```
POST /rest/v1/users

Body:
[
  { "email": "bob@example.com", "name": "Bob" },
  { "email": "carol@example.com", "name": "Carol" },
  { "email": "dave@example.com", "name": "Dave" }
]

Response 201 Created (multiple records returned if Prefer: return=representation)
```

---

### 3. Update Data

**Update by ID (filter required to avoid mass updates):**

```
PATCH https://<PROJECT_REF>.supabase.co/rest/v1/users?id=eq.42

Body:
{ "name": "Alice Updated", "age": 29 }

Response 200 OK (with Prefer: return=representation)
```

> ⚠️ **Always include a filter on `PATCH` requests.** A filter-less PATCH updates ALL rows in the table.

**Conditional update:**

```
PATCH /rest/v1/products?category=eq.electronics&stock=lt.5

Body:
{ "reorder_needed": true }
```

---

### 4. Delete Data

**Delete by ID:**

```
DELETE /rest/v1/users?id=eq.42

Response 204 No Content (success, no body)
```

**Delete with Prefer header to get deleted row:**

```
DELETE /rest/v1/users?id=eq.42
Prefer: return=representation

Response 200 OK:
[{ "id": 42, "email": "deleted@example.com", ... }]
```

---

### 5. Call RPC Function

Invoke a stored PostgreSQL function:

```
POST https://<PROJECT_REF>.supabase.co/rest/v1/rpc/<FUNCTION_NAME>

Body:
{ "param1": "value", "param2": 123 }

Response: whatever the function returns
```

**Example — login function:**

```
POST /rest/v1/rpc/login

Body:
{
  "user_email": "alice@example.com",
  "user_password": "secret123"
}

Response:
{ "token": "eyJ...", "user_id": 42 }
```

> **Note:** RPC functions bypass RLS if defined with `SECURITY DEFINER`. Check your function definition.

---

### 6. List All Tables

Query `information_schema.tables`:

```
GET https://<PROJECT_REF>.supabase.co/rest/v1/information_schema.tables?schema=eq.public&table_type=eq.BASE TABLE&select=table_name

Response:
[
  { "table_name": "users" },
  { "table_name": "posts" },
  { "table_name": "comments" }
]
```

**List all schemas:**

```
GET /rest/v1/information_schema.schemata?schema=eq.public
```

---

### 7. Get Row by ID

```
GET /rest/v1/users?id=eq.42

Response:
[{ "id": 42, "name": "Alice", ... }]
```

Or with `select` to limit columns:

```
GET /rest/v1/users?id=eq.42&select=id,name,email
```

---

### 8. Batch Insert / Upsert

**Upsert (insert or update on conflict):**

```
POST /rest/v1/users

Headers:
  Prefer: resolution=merge-duplicates
  Content-Type: application/json

Body:
[
  { "id": 1, "email": "alice@example.com", "name": "Alice" },
  { "id": 2, "email": "bob@example.com", "name": "Bob" }
]

On Conflict: specify the conflict column
(Use query param ?on_conflict=id)
```

**Bulk update with `PATCH` + filter:**

```
PATCH /rest/v1/user_roles?role=eq.admin

Body:
{ "permissions": "[\"read\",\"write\",\"delete\"]" }
```

---

### 9. Introspect Table Schema

```
GET /rest/v1/information_schema.columns?table_name=eq.users&schema=eq.public&select=column_name,data_type,is_nullable,column_default

Response:
[
  { "column_name": "id", "data_type": "bigint", "is_nullable": false, "column_default": "nextval(...)" },
  { "column_name": "name", "data_type": "text", "is_nullable": true, "column_default": null },
  { "column_name": "email", "data_type": "text", "is_nullable": false, "column_default": null }
]
```

---

### 10. HEAD Request (Check Existence)

```
HEAD /rest/v1/users?email=eq.alice@example.com
```

Response `200 OK` if exists, `406 Not Acceptable` or no rows match.

---

## Output Format

### Success — GET / SELECT

```json
{
  "status": 200,
  "data": [ ...rows ],
  "count": 42
}
```

### Success — POST / INSERT

```json
{
  "status": 201,
  "data": [ ...inserted rows ],
  "rows_affected": 1
}
```

### Success — PATCH / UPDATE

```json
{
  "status": 200,
  "data": [ ...updated rows ],
  "rows_affected": 3
}
```

### Success — DELETE

```json
{
  "status": 204,
  "rows_affected": 1
}
```

### Success — RPC

```json
{
  "status": 200,
  "data": { ...return value }
}
```

### Error

```json
{
  "status": 400,
  "error": "Bad Request",
  "message": "JSON body requested",
  "details": null
}
```

| HTTP Status | Meaning |
|-------------|---------|
| `200` | OK |
| `201` | Created |
| `204` | No Content (success, e.g. DELETE) |
| `400` | Bad Request — invalid filter syntax or body |
| `401` | Unauthorized — missing or invalid API key |
| `404` | Not Found — table does not exist |
| `406` | Not Acceptable — query returned 0 rows (HEAD) |
| `409` | Conflict — unique constraint violation |
| `422` | Unprocessable Entity — RLS blocked |
| `429` | Too Many Requests — rate limit exceeded |
| `500` | Internal Server Error — Supabase server issue |

---

## Example Conversations

### Example 1 — Fetch Active Users

**User:** "Show me all active users older than 21 from the Supabase users table"

**CCD (this skill):**
```
Using Supabase REST API → Query users table

GET https://<REF>.supabase.co/rest/v1/users
  ?age=gt.21
  &status=eq.active
  &select=id,name,email,age

Headers:
  apikey: <ANON_KEY>
  Authorization: Bearer <ANON_KEY>

Returns: Array of active users over 21 with selected fields.
```

**Expected response:**
```json
[
  { "id": 1, "name": "Bob", "email": "bob@example.com", "age": 35 },
  { "id": 4, "name": "Carol", "email": "carol@example.com", "age": 29 }
]
```

---

### Example 2 — Insert a New Post

**User:** "Insert a new post titled 'Hello World' for user ID 5 into the posts table"

**CCD:**
```
POST https://<REF>.supabase.co/rest/v1/posts
Headers:
  apikey: <ANON_KEY>
  Authorization: Bearer <ANON_KEY>
  Content-Type: application/json
  Prefer: return=representation

Body:
{
  "title": "Hello World",
  "user_id": 5,
  "published": false,
  "created_at": "2026-07-04T12:00:00Z"
}

Response 201:
[
  {
    "id": 88,
    "title": "Hello World",
    "user_id": 5,
    "published": false,
    "created_at": "2026-07-04T12:00:00Z"
  }
]
```

---

### Example 3 — Call RPC to Search Posts

**User:** "Call the search_posts function with query='AI' and limit=10"

**CCD:**
```
POST https://<REF>.supabase.co/rest/v1/rpc/search_posts
Headers:
  apikey: <ANON_KEY>
  Authorization: Bearer <ANON_KEY>
  Content-Type: application/json

Body:
{
  "search_query": "AI",
  "result_limit": 10
}

Response:
[
  { "id": 12, "title": "AI Revolution", "score": 0.95 },
  { "id": 33, "title": "Intro to AI", "score": 0.82 }
]
```

---

## Installation Guide

### Step 1 — Get Your Supabase Project URL

1. Log in to [supabase.com](https://supabase.com)
2. Create a new project (or use existing)
3. Go to **Project Settings → General**
4. Copy the **Project Reference** (e.g. `abc123xyz`)
5. Your REST URL is: `https://abc123xyz.supabase.co/rest/v1`

### Step 2 — Get the API Key

1. Go to **Project Settings → API**
2. Find the **anon / public** key under "Project API keys"
3. Copy the key (starts with `eyJ...`)

### Step 3 — Configure in OpenClaw

Add to your OpenClaw environment configuration:

```bash
SUPABASE_URL=https://<PROJECT_REF>.supabase.co
SUPABASE_ANON_KEY=eyJhbGc...
```

Or pass them as parameters when invoking this skill.

### Step 4 — Enable RLS Policies (Important!)

Supabase has **Row Level Security (RLS) enabled by default** on all new tables.

1. Go to **Table Editor** → select your table
2. Click **Policies**
3. Create a policy for each operation you need

**Example — Allow anyone to read public posts:**

```sql
CREATE POLICY "Public read" ON posts
  FOR SELECT
  USING (published = true);
```

**Example — Allow authenticated users to insert their own posts:**

```sql
CREATE POLICY "Users insert own posts" ON posts
  FOR INSERT
  WITH CHECK (auth.uid() = user_id);
```

> 🔒 **Never disable RLS globally.** If you disable RLS, all data is exposed publicly. Instead, write precise policies.

### Step 5 — Verify Connectivity

Test with a simple fetch:

```bash
curl -s "https://<REF>.supabase.co/rest/v1/users?select=id&limit=1" \
  -H "apikey: <KEY>" \
  -H "Authorization: Bearer <KEY>"
```

Expected: `200 OK` with `[]` or real data.

---

## Caveats & Important Notes

### 🔒 Row Level Security (RLS)

- RLS is **ON by default** for all tables created through the Supabase UI.
- The `anon` key respects RLS. If a query returns empty results, check your RLS policies — not the API key.
- To bypass RLS (for admin operations), use the `service_role` key **only in server-side contexts**, never expose it to the client.
- Test RLS policies in the Supabase Dashboard → SQL Editor before relying on them in production.

### 🚦 Rate Limits

| Plan | Limit |
|------|-------|
| Free | 60 requests/minute per API key |
| Pro | 500 requests/minute per API key |
| Enterprise | Custom |

- On `429`, wait and retry with **exponential backoff** (1s, 2s, 4s, ...).
- Batch requests where possible — bulk inserts are more efficient than individual POSTs.
- Supabase applies project-level rate limits in addition to per-key limits.

### 🔄 Reconnection / Retry Logic

```
for attempt in [1, 2, 3, 4, 5]:
    response = supabase_request(...)
    if response.status in [200, 201, 204]:
        return response
    if response.status == 429:
        sleep(2 ** attempt)   # exponential backoff
        continue
    if response.status in [500, 502, 503, 504]:
        sleep(2 ** attempt)
        continue
    else:
        return error  # client error, don't retry
```

### 🔍 Prefer Header

| Prefer Value | Behavior |
|-------------|---------|
| `return=representation` | Returns full inserted/updated/deleted rows |
| `return=minimal` | Returns no body (default for DELETE) |
| `resolution=merge-duplicates` | Upsert behavior on conflict |
| `count=exact` | Include `Content-Range` header with total count |

### 📐 PostgREST Filter Gotchas

- **String values use dots**: `name=eq.John` (not `name=eq.'John'`).
- **Array values use curly braces**: `ids=in.{1,2,3}`.
- **Chained filters are ANDed**: `age=gt.18&status=eq.active`.
- **OR queries need `or`**: `or=(age.gt.18,status.eq.vip)`.
- **Date filtering**: Use ISO 8601 format: `created_at=gte.2026-01-01`.

### 🗄️ Schema Qualification

- By default, only the `public` schema is exposed via the REST API.
- Other schemas (e.g. `extensions`, `storage`) may not be accessible.
- To expose a schema, run: `GRANT USAGE ON SCHEMA <name> TO anon;`

### 📦 Large Payloads

- Request body max size: **10 MB** (Supabase platform limit).
- For file storage, use Supabase **Storage** (S3-backed) instead of base64-encoding into JSON.

---

## See Also

- [Supabase Docs](https://supabase.com/docs)
- [PostgREST API Reference](https://postgrest.org/)
- [PostgREST Filtering](https://postgrest.org/en/stable/api.html#filtering)
- [Supabase Auth](https://supabase.com/docs/guides/auth)
- [Supabase RLS Guide](https://supabase.com/docs/guides/auth/row-level-security)
