# Mentionkit MCP Tools Reference

This file documents the current public Mentionkit MCP surface from `backend/components/mcp/routes.js`.

## Workflow pairing

Mentionkit MCP is workflow-first.

- `mentionkit_opportunities_context` → `mentionkit_find_opportunities` → `mentionkit_fetch_url`
- `mentionkit_mentions_context` → `mentionkit_list_mentions_raw`

Preferred rule:

- Use the opportunities flow for lead-gen review, plug review, reply opportunities, and operator review.
- Use the raw mentions flow only for browsing, pagination, and broad inspection.

## Public read tools

### `mentionkit_opportunities_context`

Use first for shortlist-style workflows.

Returns:

- available projects
- supported platforms
- allowed tags
- the `1-5` relevance scale
- default shortlist settings
- the expected response shape

Important response fields:

- `workflow.preferredFirstTool = "mentionkit_find_opportunities"`
- `workflow.preferredSecondTool = "mentionkit_fetch_url"`
- `defaults.minRelevance = 3`
- `defaults.limit = 25`
- `defaults.maxLimit = 50`

### `mentionkit_find_opportunities`

Use after `mentionkit_opportunities_context`.

Purpose:

- shortlist the strongest mentions for review workflows
- return source URLs that can be verified with `mentionkit_fetch_url`

Notable inputs:

- `projectId` or `projectName`
- `startDate`
- `endDate`
- `minRelevance`
- `limit`
- `platforms`
- `keywordValues`
- `tags`

Practical output:

- `scoreScale`
- `project`
- `filtersUsed`
- `items`

Each item includes:

- `mentionId`
- `sourceUrl`
- `platform`
- `keywordValue`
- `authorHandle`
- `sourceCreatedAt`
- `relevance`
- `relevanceText`
- `text`
- `tags`
- `commentStatus`

### `mentionkit_mentions_context`

Use first for raw feed browsing.

Returns:

- available projects
- supported platforms
- categories
- allowed tags
- sort options
- raw feed defaults
- pagination contract

Important response fields:

- `workflow.preferredUse = "raw browsing"`
- `workflow.notPreferredFor = ["lead-gen review", "reply-opportunity review"]`
- `defaults.limit = 50`
- `defaults.maxLimit = 100`
- `pagination.cursorType = "mention_id"`
- `pagination.cursorField = "nextCursor"`

### `mentionkit_list_mentions_raw`

Use after `mentionkit_mentions_context`.

Purpose:

- browse the raw mention feed
- paginate through mentions
- inspect a broad slice of data

Notable inputs:

- `projectId` or `projectName`
- `startDate`
- `endDate`
- `minRelevance`
- `limit`
- `platforms`
- `keywordValues`
- `tags`
- `sort`
- `cursor`
- `relevance`
- `category`

Practical output:

- `items`
- `nextCursor`
- `limit`
- `sort`
- `project`

Cursor rule:

- `nextCursor` is ID-based and exclusive
- pass it back unchanged for the next page

### `mentionkit_fetch_url`

Use after shortlist review.

Purpose:

- fetch the source page for a kept mention
- return readable markdown for verification

Input:

- `url`

Practical output:

- `url`
- `fetchStatus`
- `markdown`
- `truncated`
- `error`

Fetch behavior:

- success: `fetchStatus = "fetched"`
- failure: `fetchStatus = "fetch_failed"`

Fetch failure is non-fatal. Lower confidence when the source cannot be fetched.

## Public write tool

### `mentionkit_create_keyword`

Purpose:

- create or reactivate a keyword in the active organization

Scope:

- requires `mcp:write`

Notable inputs:

- `keyword`
- `platforms`
- `category`
- `englishOnly`
- `whitelistSubreddits`
- `blacklistSubreddits`
- `bannedUsers`
- `bannedWords`
- `subprompt`
- `opts`
- `projectId`
- `projectName`

Project rules:

- `projectId` wins over `projectName`
- if neither is provided and the org has exactly one project, that project is used
- otherwise the call fails and must be retried with an explicit project

Practical output:

- `keyword`
- `project`
- `platforms`

The created keyword response includes normalized keyword metadata, project info, and enabled platform config.

## Error behavior

Successful tool calls return:

- `content[0].text` as pretty JSON text
- `structuredContent` with the same payload

Tool failures do not use top-level protocol errors. They come back as:

- `result.isError = true`
- `structuredContent.error.code`
- `structuredContent.error.message`
- optional `structuredContent.error.details`

Common tool error codes:

- `invalid_arguments`
- `not_found`
- `tool_not_allowed`

Top-level JSON-RPC errors are still used for protocol problems like malformed requests or unknown JSON-RPC methods.
