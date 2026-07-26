---
name: google-meet
description: "Google Meet: Create and manage Google Meet meeting spaces. View conference history including participants and join/leave times. Use when an agent needs google meet, google meet connector, create meeting spaces on demand, get meeting details and active conference status, update meeting access settings, end active conferences, create space, config through AgentPMT-hosted remote tool calls. Discovery terms: google meet, google meet connector, create meeting spaces on demand."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/google-meet-connector
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/google-meet-connector"}}
---
# Google Meet

## Freshness
Last updated: `2026-06-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Schedule and manage video meetings, review past conferences, and access meeting intelligence — all without leaving your workflow. Create meeting rooms on demand, view who attended and when, retrieve recordings and full transcripts with speaker-level detail. Perfect for automating meeting follow-ups, attendance tracking, and extracting insights from conversations.

## Product Instructions
### Google Meet

Create and manage Google Meet meeting spaces, view conference history, access participants, recordings, and transcripts.

#### Overview

This tool provides access to the Google Meet REST API v2. You can create persistent meeting spaces with configurable access controls, end active conferences, browse conference history, view participant details and join/leave sessions, access meeting recordings (stored as MP4 in Google Drive), and retrieve meeting transcripts (stored as Google Docs) with individual spoken entries.

##### Key Concepts

- **Space**: A persistent meeting room with a meeting URI and code. One space can host many conferences over time.
- **Conference Record**: A single meeting session within a space. Auto-deleted 30 days after the conference ends.
- **Participant**: A person who joined a conference. Includes join/leave times and user identity (signed-in, anonymous, or phone).
- **Recording**: MP4 file stored in the organizer's Google Drive. Use the Google Drive tool to download.
- **Transcript**: Google Doc containing the full meeting transcript. Use the Google Docs tool to read the full document.

#### Actions

##### create_space

Create a new Google Meet meeting space.

**Required parameters:** None (all parameters are optional)

**Optional parameters:**
- `config` (object) -- space configuration:
  - `access_type` (string) -- `OPEN` (anyone can join), `TRUSTED` (organization members auto-join), `RESTRICTED` (invitees only)
  - `entry_point_access` (string) -- `ALL` or `CREATOR_APP_ONLY`

**Example -- create with defaults:**
```json
{"action":"create_space"}
```

**Example -- create restricted space:**
```json
{"action":"create_space","config":{"access_type":"RESTRICTED"}}
```

**Example -- create with trusted access and restricted entry points:**
```json
{"action":"create_space","config":{"access_type":"TRUSTED","entry_point_access":"CREATOR_APP_ONLY"}}
```

Returns: `name`, `meeting_uri`, `meeting_code`, `access_type`, `entry_point_access`, `active_conference`, `raw`

---

##### get_space

Get details of an existing meeting space.

**Required parameters:**
- `space_name` (string) -- space resource name (e.g. `spaces/jQCFfuBOdN5z`) or meeting code (e.g. `abc-mnop-xyz`)

**Example -- by space name:**
```json
{"action":"get_space","space_name":"spaces/jQCFfuBOdN5z"}
```

**Example -- by meeting code:**
```json
{"action":"get_space","space_name":"abc-mnop-xyz"}
```

Returns: `name`, `meeting_uri`, `meeting_code`, `access_type`, `entry_point_access`, `active_conference`, `raw`

---

##### update_space

Update configuration of an existing meeting space.

**Required parameters:**
- `space_name` (string) -- space resource name or meeting code

**Optional parameters:**
- `config` (object) -- updated configuration with `access_type` and/or `entry_point_access`

**Example:**
```json
{"action":"update_space","space_name":"spaces/abc123","config":{"access_type":"RESTRICTED"}}
```

Returns: `name`, `meeting_uri`, `meeting_code`, `access_type`, `entry_point_access`, `active_conference`, `raw`

---

##### end_conference

End the currently active conference in a space.

**Required parameters:**
- `space_name` (string) -- space resource name or meeting code

**Example:**
```json
{"action":"end_conference","space_name":"spaces/abc123"}
```

Returns: `ended` (boolean), `space_name`

---

##### list_conference_records

List conference records. Only returns conferences where the authenticated user is the organizer.

**Optional parameters:**
- `filter` (string) -- filter expression, e.g. `space.name="spaces/abc123"` or `start_time>="2024-01-01T00:00:00Z"`
- `page_size` (integer, 1-250, default 25) -- max results per page
- `page_token` (string) -- pagination token from previous response

**Example -- filter by space:**
```json
{"action":"list_conference_records","filter":"space.name=\"spaces/abc123\""}
```

**Example -- filter by time:**
```json
{"action":"list_conference_records","filter":"start_time>=\"2024-06-01T00:00:00Z\"","page_size":50}
```

Returns: `conference_records[]` (with `name`, `space`, `start_time`, `end_time`, `expire_time`), `next_page_token`

---

##### get_conference_record

Get details of a specific conference record.

**Required parameters:**
- `conference_record_name` (string) -- conference record resource name (e.g. `conferenceRecords/abc123`)

**Example:**
```json
{"action":"get_conference_record","conference_record_name":"conferenceRecords/abc123"}
```

Returns: `name`, `space`, `start_time`, `end_time`, `expire_time`

---

##### list_participants

List participants in a conference.

**Required parameters:**
- `conference_record_name` (string) -- conference record resource name

**Optional parameters:**
- `filter` (string) -- filter by `earliest_start_time` or `latest_end_time`
- `page_size` (integer, 1-250, default 25) -- max results per page
- `page_token` (string) -- pagination token

**Example:**
```json
{"action":"list_participants","conference_record_name":"conferenceRecords/abc123","page_size":100}
```

Returns: `participants[]` (with `name`, `earliest_start_time`, `latest_end_time`, `user` with `type`, `user_id`, `display_name`), `next_page_token`

---

##### get_participant

Get details of a specific participant.

**Required parameters:**
- `participant_name` (string) -- participant resource name (e.g. `conferenceRecords/abc/participants/xyz`)

**Example:**
```json
{"action":"get_participant","participant_name":"conferenceRecords/abc/participants/xyz"}
```

Returns: `name`, `earliest_start_time`, `latest_end_time`, `user` (with `type`, `user_id`, `display_name`)

---

##### list_participant_sessions

List individual join/leave sessions for a participant (one entry per device or rejoin).

**Required parameters:**
- `participant_name` (string) -- participant resource name

**Optional parameters:**
- `page_size` (integer, 1-250, default 25) -- max results per page
- `page_token` (string) -- pagination token

**Example:**
```json
{"action":"list_participant_sessions","participant_name":"conferenceRecords/abc/participants/xyz"}
```

Returns: `participant_sessions[]` (with `name`, `start_time`, `end_time`), `next_page_token`

---

##### list_recordings

List recordings for a conference.

**Required parameters:**
- `conference_record_name` (string) -- conference record resource name

**Optional parameters:**
- `page_size` (integer, 1-250, default 25) -- max results per page
- `page_token` (string) -- pagination token

**Example:**
```json
{"action":"list_recordings","conference_record_name":"conferenceRecords/abc123"}
```

Returns: `recordings[]` (with `name`, `state`, `start_time`, `end_time`, `drive_file_id`, `export_uri`), `next_page_token`

---

##### get_recording

Get details of a specific recording.

**Required parameters:**
- `recording_name` (string) -- recording resource name (e.g. `conferenceRecords/abc/recordings/xyz`)

**Example:**
```json
{"action":"get_recording","recording_name":"conferenceRecords/abc/recordings/xyz"}
```

Returns: `name`, `state`, `start_time`, `end_time`, `drive_file_id`, `export_uri`

---

##### list_transcripts

List transcripts for a conference.

**Required parameters:**
- `conference_record_name` (string) -- conference record resource name

**Optional parameters:**
- `page_size` (integer, 1-250, default 25) -- max results per page
- `page_token` (string) -- pagination token

**Example:**
```json
{"action":"list_transcripts","conference_record_name":"conferenceRecords/abc123"}
```

Returns: `transcripts[]` (with `name`, `state`, `start_time`, `end_time`, `docs_document_id`, `export_uri`), `next_page_token`

---

##### get_transcript

Get details of a specific transcript.

**Required parameters:**
- `transcript_name` (string) -- transcript resource name (e.g. `conferenceRecords/abc/transcripts/xyz`)

**Example:**
```json
{"action":"get_transcript","transcript_name":"conferenceRecords/abc/transcripts/xyz"}
```

Returns: `name`, `state`, `start_time`, `end_time`, `docs_document_id`, `export_uri`

---

##### list_transcript_entries

List individual spoken entries within a transcript, including speaker, text, language, and timestamps.

**Required parameters:**
- `transcript_name` (string) -- transcript resource name

**Optional parameters:**
- `page_size` (integer, 1-250, default 25) -- max results per page
- `page_token` (string) -- pagination token

**Example:**
```json
{"action":"list_transcript_entries","transcript_name":"conferenceRecords/abc/transcripts/xyz","page_size":100}
```

Returns: `transcript_entries[]` (with `name`, `participant`, `text`, `language_code`, `start_time`, `end_time`), `next_page_token`

---

#### Workflows

##### Meeting Review Workflow

Review what happened in a past meeting:

1. `list_conference_records` with a space filter to find the conference
2. `list_participants` to see who attended and their join/leave times
3. `list_transcripts` to find available transcripts
4. `list_transcript_entries` to read the full conversation
5. `list_recordings` to find the video recording
6. Use the Google Drive tool with `drive_file_id` to download the recording MP4

##### Create and Manage Meeting Space

1. `create_space` with desired access configuration
2. Share the `meeting_uri` or `meeting_code` with participants
3. `update_space` to change access controls as needed
4. `end_conference` to terminate an active session

#### Notes

- Conference records are automatically deleted 30 days after the conference ends
- Recording and transcript files persist in Google Drive beyond the 30-day conference record window
- `list_conference_records` only returns conferences where the authenticated user is the organizer
- To download recordings, use the Google Drive tool with the `drive_file_id` from the recording response
- Transcripts are stored as Google Docs; use the Google Docs tool to read the full document content
- The `space_name` parameter accepts either the full resource name (e.g. `spaces/abc123`) or just a meeting code (e.g. `abc-mnop-xyz`) -- the tool automatically resolves the format
- Participant user types include `signed_in` (with user ID and display name), `anonymous` (display name only), and `phone` (display name only)

## When To Use
- Use this skill for `Google Meet` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: google meet, google meet connector, create meeting spaces on demand, get meeting details and active conference status, update meeting access settings, end active conferences, create space, config.
- Supported action names: `create_space`, `end_conference`, `get_conference_record`, `get_participant`, `get_recording`, `get_space`, `get_transcript`, `list_conference_records`, `list_participant_sessions`, `list_participants`, `list_recordings`, `list_transcript_entries`, `list_transcripts`, `update_space`.

## Use Cases
- Create meeting spaces on demand
- Get meeting details and active conference status
- Update meeting access settings
- End active conferences
- List past conference records
- View participant attendance and join/leave times
- Access meeting recordings
- Retrieve meeting transcripts
- Get speaker-attributed transcript entries
- Automate meeting follow-up workflows

## Related Product Skills
- File Management: ../file-management (ClawHub: `file-management`, page: https://clawhub.ai/agentpmt/file-management; skills.sh: `npx skills add AgentPMT/agent-skills --skill file-management`) - Use this companion skill to inspect, download, upload, and manage files referenced by this product.

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `14`.
x402 availability: not enabled for this product.

- `create_space` (action slug: `create-space`): Create a new Google Meet meeting space. Price: `5` credits. Parameters: `config`.
- `end_conference` (action slug: `end-conference`): End the currently active conference in a space. Price: `5` credits. Parameters: `space_name`.
- `get_conference_record` (action slug: `get-conference-record`): Get details of a specific conference record. Price: `5` credits. Parameters: `conference_record_name`.
- `get_participant` (action slug: `get-participant`): Get details of a specific participant. Price: `5` credits. Parameters: `participant_name`.
- `get_recording` (action slug: `get-recording`): Get details of a specific recording. Price: `5` credits. Parameters: `recording_name`.
- `get_space` (action slug: `get-space`): Get details of an existing meeting space. Price: `5` credits. Parameters: `space_name`.
- `get_transcript` (action slug: `get-transcript`): Get details of a specific transcript. Price: `5` credits. Parameters: `transcript_name`.
- `list_conference_records` (action slug: `list-conference-records`): List conference records. Only returns conferences where the authenticated user is the organizer. Price: `5` credits. Parameters: `filter`, `page_size`, `page_token`.
- `list_participant_sessions` (action slug: `list-participant-sessions`): List individual join/leave sessions for a participant. Price: `5` credits. Parameters: `page_size`, `page_token`, `participant_name`.
- `list_participants` (action slug: `list-participants`): List participants in a conference. Price: `5` credits. Parameters: `conference_record_name`, `filter`, `page_size`, `page_token`.
- `list_recordings` (action slug: `list-recordings`): List recordings for a conference. Price: `5` credits. Parameters: `conference_record_name`, `page_size`, `page_token`.
- `list_transcript_entries` (action slug: `list-transcript-entries`): List individual spoken entries within a transcript with speaker, text, language, and timestamps. Price: `5` credits. Parameters: `page_size`, `page_token`, `transcript_name`.
- `list_transcripts` (action slug: `list-transcripts`): List transcripts for a conference. Price: `5` credits. Parameters: `conference_record_name`, `page_size`, `page_token`.
- `update_space` (action slug: `update-space`): Update configuration of an existing meeting space. Price: `5` credits. Parameters: `config`, `space_name`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "google-meet-connector"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "google-meet-connector"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "google-meet-connector"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "google-meet-connector"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "google-meet-connector"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "google-meet-connector"
  }
}
```

## Call This Tool
Product slug: `google-meet-connector`

Marketplace page: https://www.agentpmt.com/marketplace/google-meet-connector

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
    "name": "Google-Meet",
    "arguments": {
      "action": "create_space",
      "config": {
        "access_type": "OPEN",
        "entry_point_access": "ALL"
      }
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "google-meet-connector",
  "parameters": {
    "action": "create_space",
    "config": {
      "access_type": "OPEN",
      "entry_point_access": "ALL"
    }
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `create_space` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/google-meet-connector
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
