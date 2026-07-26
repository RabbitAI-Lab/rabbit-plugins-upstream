---
name: google-tasks
description: "Google Tasks: create, read, update, delete tasks and lists. Due dates, notes, subtasks, completion tracking. Batch operations and filtering. Use when an agent needs google tasks, task management automation, todo list synchronization, project task tracking, deadline monitoring, batch create tasks, tasks, tasklist id through AgentPMT-hosted remote tool calls. Discovery terms: google tasks, task management automation, todo list synchronization, project task tracking, deadline monitoring."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/google-tasks
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/google-tasks"}}
---
# Google Tasks

## Freshness
Last updated: `2026-06-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Complete Google Tasks management tool enabling AI agents to create read update and delete tasks and task lists. Supports task organization with due dates notes subtasks and completion tracking. Includes batch operations for efficient task management and advanced filtering options for retrieving tasks by date ranges and completion status. Perfect for task automation todo list synchronization project tracking and productivity workflow integration.

## Product Instructions
### Google Tasks

Manage task lists and tasks in Google Tasks. Create, update, complete, search, and organize tasks across multiple lists.

#### Task List Actions

##### list_tasklists
List all task lists in the user's account.

- **Optional:** `max_results` (integer, 1-100, default 100), `page_token` (string)

```json
{"action": "list_tasklists"}
```

##### get_tasklist
Get details of a specific task list.

- **Required:** `tasklist_id` (string)

```json
{"action": "get_tasklist", "tasklist_id": "MDk3NTEwMjQ2MzM"}
```

##### create_tasklist
Create a new task list.

- **Required:** `tasklist_title` (string) — also accepts `title`

```json
{"action": "create_tasklist", "tasklist_title": "Shopping List"}
```

##### update_tasklist
Fully update a task list (replaces existing data).

- **Required:** `tasklist_id` (string), `tasklist_title` (string) — also accepts `title`

```json
{"action": "update_tasklist", "tasklist_id": "MDk3NTEwMjQ2MzM", "tasklist_title": "Grocery List"}
```

##### patch_tasklist
Partially update a task list title.

- **Required:** `tasklist_id` (string), `tasklist_title` (string) — also accepts `title`

```json
{"action": "patch_tasklist", "tasklist_id": "MDk3NTEwMjQ2MzM", "tasklist_title": "Renamed List"}
```

##### delete_tasklist
Delete a task list.

- **Required:** `tasklist_id` (string)

```json
{"action": "delete_tasklist", "tasklist_id": "MDk3NTEwMjQ2MzM"}
```

#### Task Actions

##### list_tasks
List tasks in a specific task list.

- **Optional:** `tasklist_id` (string, defaults to primary list `@default`), `max_results` (integer, 1-100, default 100), `page_token` (string), `show_completed` (boolean, default true), `show_deleted` (boolean, default false), `show_hidden` (boolean, default false), `updated_min` (RFC 3339 timestamp), `completed_min` (RFC 3339 timestamp), `completed_max` (RFC 3339 timestamp), `due_min` (RFC 3339 timestamp), `due_max` (RFC 3339 timestamp)

```json
{"action": "list_tasks", "tasklist_id": "@default", "show_completed": false}
```

##### get_task
Get details of a specific task.

- **Required:** `task_id` (string)
- **Optional:** `tasklist_id` (string, defaults to `@default`)

```json
{"action": "get_task", "task_id": "abc123", "tasklist_id": "@default"}
```

##### create_task
Create a new task.

- **Required:** `title` (string)
- **Optional:** `tasklist_id` (string, defaults to `@default`), `notes` (string), `due` (ISO 8601 date: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ), `status` ("needsAction" or "completed"), `parent` (task ID to create as subtask), `previous` (task ID for positioning)

```json
{"action": "create_task", "title": "Buy groceries", "notes": "Milk, eggs, bread", "due": "2026-03-15"}
```

Creating a subtask:
```json
{"action": "create_task", "title": "Buy milk", "parent": "parentTaskId123"}
```

##### update_task
Fully update a task (merges with existing data).

- **Required:** `task_id` (string)
- **Optional:** `tasklist_id` (string, defaults to `@default`), `title` (string), `notes` (string), `due` (ISO 8601 date), `status` ("needsAction" or "completed")

```json
{"action": "update_task", "task_id": "abc123", "title": "Updated title", "notes": "New notes", "due": "2026-03-20"}
```

##### patch_task
Partially update specific fields of a task.

- **Required:** `task_id` (string)
- **Optional:** `tasklist_id` (string, defaults to `@default`), `title` (string), `notes` (string), `due` (ISO 8601 date), `status` ("needsAction" or "completed")

```json
{"action": "patch_task", "task_id": "abc123", "notes": "Updated notes only"}
```

##### delete_task
Delete a task.

- **Required:** `task_id` (string)
- **Optional:** `tasklist_id` (string, defaults to `@default`)

```json
{"action": "delete_task", "task_id": "abc123"}
```

##### move_task
Move a task within a list (reorder or nest under a parent).

- **Required:** `task_id` (string)
- **Optional:** `tasklist_id` (string, defaults to `@default`), `parent` (task ID to nest under), `previous` (task ID to position after)

```json
{"action": "move_task", "task_id": "abc123", "parent": "parentTaskId456"}
```

##### complete_task
Mark a task as completed.

- **Required:** `task_id` (string)
- **Optional:** `tasklist_id` (string, defaults to `@default`)

```json
{"action": "complete_task", "task_id": "abc123"}
```

##### uncomplete_task
Mark a completed task as incomplete.

- **Required:** `task_id` (string)
- **Optional:** `tasklist_id` (string, defaults to `@default`)

```json
{"action": "uncomplete_task", "task_id": "abc123"}
```

##### clear_completed
Remove all completed tasks from a list.

- **Optional:** `tasklist_id` (string, defaults to `@default`)

```json
{"action": "clear_completed", "tasklist_id": "@default"}
```

#### Bulk and Search Actions

##### batch_create_tasks
Create multiple tasks at once.

- **Required:** `tasks` (array of task objects, each with `title`; optional `notes`, `due`, `status`, `parent`, `previous`)
- **Optional:** `tasklist_id` (string, defaults to `@default`)

```json
{
  "action": "batch_create_tasks",
  "tasklist_id": "@default",
  "tasks": [
    {"title": "Task 1", "due": "2026-03-15"},
    {"title": "Task 2", "notes": "Details here"},
    {"title": "Task 3", "due": "2026-03-20", "status": "needsAction"}
  ]
}
```

##### get_all_tasks
Retrieve all tasks across all task lists.

- **Optional:** `show_completed` (boolean, default true), `show_deleted` (boolean, default false), `show_hidden` (boolean, default false)

```json
{"action": "get_all_tasks", "show_completed": false}
```

##### search_tasks
Search for tasks by keyword across all task lists. Matches against task titles and notes.

- **Required:** `search_query` (string)
- **Optional:** `show_completed` (boolean, default true)

```json
{"action": "search_tasks", "search_query": "groceries"}
```

#### Common Workflows

1. **Quick task creation:** Use `create_task` with just `title` to add to the default list.
2. **Project setup:** Use `create_tasklist` then `batch_create_tasks` to set up a project with multiple tasks.
3. **Daily review:** Use `list_tasks` with `show_completed: false` to see pending items, or `get_all_tasks` for a full overview.
4. **Find a task:** Use `search_tasks` to locate tasks by keyword across all lists.
5. **Task completion:** Use `complete_task` / `uncomplete_task` for simple status toggling.
6. **Cleanup:** Use `clear_completed` to remove finished tasks from a list.

#### Important Notes

- Use `@default` for `tasklist_id` to target the user's primary task list. If omitted, most task actions default to `@default`.
- Due dates accept `YYYY-MM-DD` or full ISO 8601 format (`YYYY-MM-DDTHH:MM:SSZ`).
- Filter timestamps (`updated_min`, `completed_min`, `completed_max`, `due_min`, `due_max`) use RFC 3339 format.
- Task status values are `needsAction` (incomplete) or `completed`.
- Use `patch_task` to update only specific fields without affecting others. Use `update_task` for full replacements.
- The `parent` parameter creates subtasks; `previous` controls ordering within the list.
- Pagination: use `page_token` from the response's `next_page_token` to fetch additional pages.

## When To Use
- Use this skill for `Google Tasks` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: google tasks, task management automation, todo list synchronization, project task tracking, deadline monitoring, batch create tasks, tasks, tasklist id.
- Supported action names: `batch_create_tasks`, `clear_completed`, `complete_task`, `create_task`, `create_tasklist`, `delete_task`, `delete_tasklist`, `get_all_tasks`, `get_task`, `get_tasklist`, `list_tasklists`, `list_tasks`, `move_task`, `patch_task`, `patch_tasklist`, `search_tasks`, `uncomplete_task`, `update_task`, `update_tasklist`.

## Use Cases
- task management automation
- todo list synchronization
- project task tracking
- deadline monitoring
- task completion reporting
- productivity workflow integration
- calendar task integration
- team task distribution
- recurring task management
- task prioritization

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `19`.
x402 availability: not enabled for this product.

- `batch_create_tasks` (action slug: `batch-create-tasks`): Create multiple tasks at once in a task list. Price: `5` credits. Parameters: `tasklist_id`, `tasks`.
- `clear_completed` (action slug: `clear-completed`): Remove all completed tasks from a task list. Price: `5` credits. Parameters: `tasklist_id`.
- `complete_task` (action slug: `complete-task`): Mark a task as completed. Price: `5` credits. Parameters: `task_id`, `tasklist_id`.
- `create_task` (action slug: `create-task`): Create a new task in a task list. Price: `5` credits. Parameters: `due`, `notes`, `parent`, `previous`, `status`, `tasklist_id`, `title`.
- `create_tasklist` (action slug: `create-tasklist`): Create a new task list. Price: `5` credits. Parameters: `tasklist_title`.
- `delete_task` (action slug: `delete-task`): Delete a task. Price: `5` credits. Parameters: `task_id`, `tasklist_id`.
- `delete_tasklist` (action slug: `delete-tasklist`): Delete a task list. Price: `5` credits. Parameters: `tasklist_id`.
- `get_all_tasks` (action slug: `get-all-tasks`): Retrieve all tasks across all task lists. Price: `5` credits. Parameters: `show_completed`, `show_deleted`, `show_hidden`.
- `get_task` (action slug: `get-task`): Get details of a specific task. Price: `5` credits. Parameters: `task_id`, `tasklist_id`.
- `get_tasklist` (action slug: `get-tasklist`): Get details of a specific task list. Price: `5` credits. Parameters: `tasklist_id`.
- `list_tasklists` (action slug: `list-tasklists`): List all task lists in the user's account. Price: `5` credits. Parameters: `max_results`, `page_token`.
- `list_tasks` (action slug: `list-tasks`): List tasks in a specific task list. Price: `5` credits. Parameters: `completed_max`, `completed_min`, `due_max`, `due_min`, `max_results`, `page_token`, `show_completed`, `show_deleted`, plus 3 more.
- `move_task` (action slug: `move-task`): Move a task within a list (reorder or nest under a parent). Price: `5` credits. Parameters: `parent`, `previous`, `task_id`, `tasklist_id`.
- `patch_task` (action slug: `patch-task`): Partially update specific fields of a task. Price: `5` credits. Parameters: `due`, `notes`, `status`, `task_id`, `tasklist_id`, `title`.
- `patch_tasklist` (action slug: `patch-tasklist`): Partially update a task list title. Price: `5` credits. Parameters: `tasklist_id`, `tasklist_title`.
- `search_tasks` (action slug: `search-tasks`): Search for tasks by keyword across all task lists. Matches against task titles and notes. Price: `5` credits. Parameters: `search_query`, `show_completed`.
- `uncomplete_task` (action slug: `uncomplete-task`): Mark a completed task as incomplete. Price: `5` credits. Parameters: `task_id`, `tasklist_id`.
- `update_task` (action slug: `update-task`): Fully update a task (merges with existing data). Price: `5` credits. Parameters: `due`, `notes`, `status`, `task_id`, `tasklist_id`, `title`.
- `update_tasklist` (action slug: `update-tasklist`): Fully update a task list (replaces existing data). Price: `5` credits. Parameters: `tasklist_id`, `tasklist_title`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "google-tasks"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "google-tasks"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "google-tasks"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "google-tasks"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "google-tasks"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "google-tasks"
  }
}
```

## Call This Tool
Product slug: `google-tasks`

Marketplace page: https://www.agentpmt.com/marketplace/google-tasks

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
    "name": "Google-Tasks",
    "arguments": {
      "action": "batch_create_tasks",
      "tasklist_id": "example tasklist id",
      "tasks": [
        {
          "due": "example due",
          "notes": "example notes",
          "parent": "example parent",
          "previous": "example previous",
          "status": "needsAction",
          "title": "example title"
        }
      ]
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "google-tasks",
  "parameters": {
    "action": "batch_create_tasks",
    "tasklist_id": "example tasklist id",
    "tasks": [
      {
        "due": "example due",
        "notes": "example notes",
        "parent": "example parent",
        "previous": "example previous",
        "status": "needsAction",
        "title": "example title"
      }
    ]
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `batch_create_tasks` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/google-tasks
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
