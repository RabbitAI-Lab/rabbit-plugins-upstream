---
name: "jira-reader"
description: "Read-only Jira Cloud lookup commands for scoped API tokens."
metadata:
  version: 0.3.1
  tags: ["jira", "atlassian", "readonly", "issues", "javascript", "reader"]
  openclaw:
    primaryEnv: JIRA_ACCESS_TOKEN
allowed-tools:
  - exec
---

# Jira Reader

Use for read-only Jira Cloud lookups with scoped Atlassian API tokens: issue details, JQL searches, project metadata, recent project activity, assigned open work, and current-user context.

## Requirements

- Node.js 18+.
- Scoped Atlassian API token with Jira read scopes for the target site/project.
- Config provided through process environment variables, optionally loaded from `.env`:
  - `JIRA_BASE_URL`: Jira Cloud site URL, for example `https://example.atlassian.net`.
  - `JIRA_EMAIL`: Atlassian account email for scoped API token auth.
  - `JIRA_PROJECT`: default Jira project key, for example `ENG`.
  - `JIRA_ACCESS_TOKEN`: scoped Atlassian API token.
  - `JIRA_CLOUD_ID`: optional; discovered from `JIRA_BASE_URL/_edge/tenant_info` when absent.

The helper automatically loads `.env` from the current working directory before reading config from `process.env`. Set `JIRA_ENV_FILE` to load a different env file. Existing process environment values take precedence over values from `.env`.

Never print or commit access tokens. Do not include secrets in issue queries, JQL, summaries, comments, or error reports.

## Authentication

Only scoped Atlassian API tokens are supported. Use Basic `email:token` authentication against `https://api.atlassian.com/ex/jira/{cloudId}`.

## Workflow

1. Use `scripts/jira-reader.mjs` for Jira API calls.
2. Prefer the default project from `JIRA_PROJECT` unless the user names another project or issue key.
3. Keep all actions read-only. Do not create, update, assign, comment, transition, delete, or log work.
4. Use Jira's `/rest/api/3/search/jql` endpoint for JQL searches.
5. Treat open assigned work as `statusCategory != Done`; old Done issues may still have unresolved resolution.
6. For vague requests, start with a narrow search or recent issue list, then inspect exact issue keys.

## Commands

Run from the skill directory or pass the script path explicitly.

```bash
node scripts/jira-reader.mjs me
node scripts/jira-reader.mjs project
node scripts/jira-reader.mjs issue PROJ-123
node scripts/jira-reader.mjs search --jql 'project = PROJ ORDER BY updated DESC' --max 10
node scripts/jira-reader.mjs recent --max 10
node scripts/jira-reader.mjs my-open --max 20
```

## Output

The helper prints compact JSON summaries suitable for reading in-agent. It avoids printing credentials and trims very large text fields.

## Validation

Use harmless read-only calls:

```bash
node scripts/jira-reader.mjs me
node scripts/jira-reader.mjs project
```
