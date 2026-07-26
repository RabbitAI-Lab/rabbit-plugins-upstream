# Google Tasks Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `google-tasks`

x402 availability: not enabled for this product.

## `batch_create_tasks`

Action slug: `batch-create-tasks`

Price: `5` credits

Create multiple tasks at once in a task list.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' if omitted |
| `tasks` | `array` | yes | Array of task objects to create |

Sample parameters:

```json
{
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
```

Generated JSON parameter schema:

```json
{
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' if omitted",
    "required": false,
    "type": "string"
  },
  "tasks": {
    "description": "Array of task objects to create",
    "items": {
      "properties": {
        "due": {
          "description": "Due date in ISO 8601 format",
          "type": "string"
        },
        "notes": {
          "description": "Task notes",
          "type": "string"
        },
        "parent": {
          "description": "Parent task ID",
          "type": "string"
        },
        "previous": {
          "description": "Previous task ID",
          "type": "string"
        },
        "status": {
          "description": "Task status",
          "enum": [
            "needsAction",
            "completed"
          ],
          "type": "string"
        },
        "title": {
          "description": "Task title",
          "type": "string"
        }
      },
      "type": "object"
    },
    "required": true,
    "type": "array"
  }
}
```

## `clear_completed`

Action slug: `clear-completed`

Price: `5` credits

Remove all completed tasks from a task list.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' if omitted |

Sample parameters:

```json
{
  "tasklist_id": "example tasklist id"
}
```

Generated JSON parameter schema:

```json
{
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' if omitted",
    "required": false,
    "type": "string"
  }
}
```

## `complete_task`

Action slug: `complete-task`

Price: `5` credits

Mark a task as completed.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `task_id` | `string` | yes | Task ID |
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' if omitted |

Sample parameters:

```json
{
  "task_id": "example task id",
  "tasklist_id": "example tasklist id"
}
```

Generated JSON parameter schema:

```json
{
  "task_id": {
    "description": "Task ID",
    "required": true,
    "type": "string"
  },
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' if omitted",
    "required": false,
    "type": "string"
  }
}
```

## `create_task`

Action slug: `create-task`

Price: `5` credits

Create a new task in a task list.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `due` | `string` | no | Due date in ISO 8601 format (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ) |
| `notes` | `string` | no | Task notes/description |
| `parent` | `string` | no | Parent task ID for creating subtasks |
| `previous` | `string` | no | Previous task ID for positioning |
| `status` | `string` | no | Task status |
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' if omitted |
| `title` | `string` | yes | Task title |

Sample parameters:

```json
{
  "due": "example due",
  "notes": "example notes",
  "parent": "example parent",
  "previous": "example previous",
  "status": "needsAction",
  "tasklist_id": "example tasklist id",
  "title": "example title"
}
```

Generated JSON parameter schema:

```json
{
  "due": {
    "description": "Due date in ISO 8601 format (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)",
    "required": false,
    "type": "string"
  },
  "notes": {
    "description": "Task notes/description",
    "required": false,
    "type": "string"
  },
  "parent": {
    "description": "Parent task ID for creating subtasks",
    "required": false,
    "type": "string"
  },
  "previous": {
    "description": "Previous task ID for positioning",
    "required": false,
    "type": "string"
  },
  "status": {
    "description": "Task status",
    "enum": [
      "needsAction",
      "completed"
    ],
    "required": false,
    "type": "string"
  },
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' if omitted",
    "required": false,
    "type": "string"
  },
  "title": {
    "description": "Task title",
    "required": true,
    "type": "string"
  }
}
```

## `create_tasklist`

Action slug: `create-tasklist`

Price: `5` credits

Create a new task list.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `tasklist_title` | `string` | yes | Title for the new task list. You can also use 'title' as a shorthand. |

Sample parameters:

```json
{
  "tasklist_title": "example tasklist title"
}
```

Generated JSON parameter schema:

```json
{
  "tasklist_title": {
    "description": "Title for the new task list. You can also use 'title' as a shorthand.",
    "required": true,
    "type": "string"
  }
}
```

## `delete_task`

Action slug: `delete-task`

Price: `5` credits

Delete a task.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `task_id` | `string` | yes | Task ID |
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' if omitted |

Sample parameters:

```json
{
  "task_id": "example task id",
  "tasklist_id": "example tasklist id"
}
```

Generated JSON parameter schema:

```json
{
  "task_id": {
    "description": "Task ID",
    "required": true,
    "type": "string"
  },
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' if omitted",
    "required": false,
    "type": "string"
  }
}
```

## `delete_tasklist`

Action slug: `delete-tasklist`

Price: `5` credits

Delete a task list.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `tasklist_id` | `string` | yes | Task list ID |

Sample parameters:

```json
{
  "tasklist_id": "example tasklist id"
}
```

Generated JSON parameter schema:

```json
{
  "tasklist_id": {
    "description": "Task list ID",
    "required": true,
    "type": "string"
  }
}
```

## `get_all_tasks`

Action slug: `get-all-tasks`

Price: `5` credits

Retrieve all tasks across all task lists.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `show_completed` | `boolean` | no | Whether to show completed tasks |
| `show_deleted` | `boolean` | no | Whether to show deleted tasks |
| `show_hidden` | `boolean` | no | Whether to show hidden tasks |

Sample parameters:

```json
{
  "show_completed": true,
  "show_deleted": false,
  "show_hidden": false
}
```

Generated JSON parameter schema:

```json
{
  "show_completed": {
    "default": true,
    "description": "Whether to show completed tasks",
    "required": false,
    "type": "boolean"
  },
  "show_deleted": {
    "default": false,
    "description": "Whether to show deleted tasks",
    "required": false,
    "type": "boolean"
  },
  "show_hidden": {
    "default": false,
    "description": "Whether to show hidden tasks",
    "required": false,
    "type": "boolean"
  }
}
```

## `get_task`

Action slug: `get-task`

Price: `5` credits

Get details of a specific task.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `task_id` | `string` | yes | Task ID |
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' if omitted |

Sample parameters:

```json
{
  "task_id": "example task id",
  "tasklist_id": "example tasklist id"
}
```

Generated JSON parameter schema:

```json
{
  "task_id": {
    "description": "Task ID",
    "required": true,
    "type": "string"
  },
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' if omitted",
    "required": false,
    "type": "string"
  }
}
```

## `get_tasklist`

Action slug: `get-tasklist`

Price: `5` credits

Get details of a specific task list.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `tasklist_id` | `string` | yes | Task list ID |

Sample parameters:

```json
{
  "tasklist_id": "example tasklist id"
}
```

Generated JSON parameter schema:

```json
{
  "tasklist_id": {
    "description": "Task list ID",
    "required": true,
    "type": "string"
  }
}
```

## `list_tasklists`

Action slug: `list-tasklists`

Price: `5` credits

List all task lists in the user's account.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `max_results` | `integer` | no | Maximum number of items to return (1-100) |
| `page_token` | `string` | no | Page token for pagination |

Sample parameters:

```json
{
  "max_results": 100,
  "page_token": "example page token"
}
```

Generated JSON parameter schema:

```json
{
  "max_results": {
    "default": 100,
    "description": "Maximum number of items to return (1-100)",
    "maximum": 100,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Page token for pagination",
    "required": false,
    "type": "string"
  }
}
```

## `list_tasks`

Action slug: `list-tasks`

Price: `5` credits

List tasks in a specific task list.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `completed_max` | `string` | no | Upper bound for task's completion date (RFC 3339) |
| `completed_min` | `string` | no | Lower bound for task's completion date (RFC 3339) |
| `due_max` | `string` | no | Upper bound for task's due date (RFC 3339) |
| `due_min` | `string` | no | Lower bound for task's due date (RFC 3339) |
| `max_results` | `integer` | no | Maximum number of items to return (1-100) |
| `page_token` | `string` | no | Page token for pagination |
| `show_completed` | `boolean` | no | Whether to show completed tasks |
| `show_deleted` | `boolean` | no | Whether to show deleted tasks |
| `show_hidden` | `boolean` | no | Whether to show hidden tasks |
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' (primary list) if omitted |
| `updated_min` | `string` | no | Lower bound for task's last modification time (RFC 3339) |

Sample parameters:

```json
{
  "completed_max": "example completed max",
  "completed_min": "example completed min",
  "due_max": "example due max",
  "due_min": "example due min",
  "max_results": 100,
  "page_token": "example page token",
  "show_completed": true,
  "show_deleted": false
}
```

Generated JSON parameter schema:

```json
{
  "completed_max": {
    "description": "Upper bound for task's completion date (RFC 3339)",
    "required": false,
    "type": "string"
  },
  "completed_min": {
    "description": "Lower bound for task's completion date (RFC 3339)",
    "required": false,
    "type": "string"
  },
  "due_max": {
    "description": "Upper bound for task's due date (RFC 3339)",
    "required": false,
    "type": "string"
  },
  "due_min": {
    "description": "Lower bound for task's due date (RFC 3339)",
    "required": false,
    "type": "string"
  },
  "max_results": {
    "default": 100,
    "description": "Maximum number of items to return (1-100)",
    "maximum": 100,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Page token for pagination",
    "required": false,
    "type": "string"
  },
  "show_completed": {
    "default": true,
    "description": "Whether to show completed tasks",
    "required": false,
    "type": "boolean"
  },
  "show_deleted": {
    "default": false,
    "description": "Whether to show deleted tasks",
    "required": false,
    "type": "boolean"
  },
  "show_hidden": {
    "default": false,
    "description": "Whether to show hidden tasks",
    "required": false,
    "type": "boolean"
  },
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' (primary list) if omitted",
    "required": false,
    "type": "string"
  },
  "updated_min": {
    "description": "Lower bound for task's last modification time (RFC 3339)",
    "required": false,
    "type": "string"
  }
}
```

## `move_task`

Action slug: `move-task`

Price: `5` credits

Move a task within a list (reorder or nest under a parent).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `parent` | `string` | no | Parent task ID to nest under |
| `previous` | `string` | no | Previous task ID to position after |
| `task_id` | `string` | yes | Task ID |
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' if omitted |

Sample parameters:

```json
{
  "parent": "example parent",
  "previous": "example previous",
  "task_id": "example task id",
  "tasklist_id": "example tasklist id"
}
```

Generated JSON parameter schema:

```json
{
  "parent": {
    "description": "Parent task ID to nest under",
    "required": false,
    "type": "string"
  },
  "previous": {
    "description": "Previous task ID to position after",
    "required": false,
    "type": "string"
  },
  "task_id": {
    "description": "Task ID",
    "required": true,
    "type": "string"
  },
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' if omitted",
    "required": false,
    "type": "string"
  }
}
```

## `patch_task`

Action slug: `patch-task`

Price: `5` credits

Partially update specific fields of a task.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `due` | `string` | no | Due date in ISO 8601 format |
| `notes` | `string` | no | Task notes/description |
| `status` | `string` | no | Task status |
| `task_id` | `string` | yes | Task ID |
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' if omitted |
| `title` | `string` | no | Task title |

Sample parameters:

```json
{
  "due": "example due",
  "notes": "example notes",
  "status": "needsAction",
  "task_id": "example task id",
  "tasklist_id": "example tasklist id",
  "title": "example title"
}
```

Generated JSON parameter schema:

```json
{
  "due": {
    "description": "Due date in ISO 8601 format",
    "required": false,
    "type": "string"
  },
  "notes": {
    "description": "Task notes/description",
    "required": false,
    "type": "string"
  },
  "status": {
    "description": "Task status",
    "enum": [
      "needsAction",
      "completed"
    ],
    "required": false,
    "type": "string"
  },
  "task_id": {
    "description": "Task ID",
    "required": true,
    "type": "string"
  },
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' if omitted",
    "required": false,
    "type": "string"
  },
  "title": {
    "description": "Task title",
    "required": false,
    "type": "string"
  }
}
```

## `patch_tasklist`

Action slug: `patch-tasklist`

Price: `5` credits

Partially update a task list title.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `tasklist_id` | `string` | yes | Task list ID |
| `tasklist_title` | `string` | yes | New title for the task list. You can also use 'title' as a shorthand. |

Sample parameters:

```json
{
  "tasklist_id": "example tasklist id",
  "tasklist_title": "example tasklist title"
}
```

Generated JSON parameter schema:

```json
{
  "tasklist_id": {
    "description": "Task list ID",
    "required": true,
    "type": "string"
  },
  "tasklist_title": {
    "description": "New title for the task list. You can also use 'title' as a shorthand.",
    "required": true,
    "type": "string"
  }
}
```

## `search_tasks`

Action slug: `search-tasks`

Price: `5` credits

Search for tasks by keyword across all task lists. Matches against task titles and notes.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `search_query` | `string` | yes | Search query for finding tasks |
| `show_completed` | `boolean` | no | Whether to include completed tasks in search results |

Sample parameters:

```json
{
  "search_query": "example search query",
  "show_completed": true
}
```

Generated JSON parameter schema:

```json
{
  "search_query": {
    "description": "Search query for finding tasks",
    "required": true,
    "type": "string"
  },
  "show_completed": {
    "default": true,
    "description": "Whether to include completed tasks in search results",
    "required": false,
    "type": "boolean"
  }
}
```

## `uncomplete_task`

Action slug: `uncomplete-task`

Price: `5` credits

Mark a completed task as incomplete.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `task_id` | `string` | yes | Task ID |
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' if omitted |

Sample parameters:

```json
{
  "task_id": "example task id",
  "tasklist_id": "example tasklist id"
}
```

Generated JSON parameter schema:

```json
{
  "task_id": {
    "description": "Task ID",
    "required": true,
    "type": "string"
  },
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' if omitted",
    "required": false,
    "type": "string"
  }
}
```

## `update_task`

Action slug: `update-task`

Price: `5` credits

Fully update a task (merges with existing data).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `due` | `string` | no | Due date in ISO 8601 format |
| `notes` | `string` | no | Task notes/description |
| `status` | `string` | no | Task status |
| `task_id` | `string` | yes | Task ID |
| `tasklist_id` | `string` | no | Task list ID. Defaults to '@default' if omitted |
| `title` | `string` | no | Task title |

Sample parameters:

```json
{
  "due": "example due",
  "notes": "example notes",
  "status": "needsAction",
  "task_id": "example task id",
  "tasklist_id": "example tasklist id",
  "title": "example title"
}
```

Generated JSON parameter schema:

```json
{
  "due": {
    "description": "Due date in ISO 8601 format",
    "required": false,
    "type": "string"
  },
  "notes": {
    "description": "Task notes/description",
    "required": false,
    "type": "string"
  },
  "status": {
    "description": "Task status",
    "enum": [
      "needsAction",
      "completed"
    ],
    "required": false,
    "type": "string"
  },
  "task_id": {
    "description": "Task ID",
    "required": true,
    "type": "string"
  },
  "tasklist_id": {
    "description": "Task list ID. Defaults to '@default' if omitted",
    "required": false,
    "type": "string"
  },
  "title": {
    "description": "Task title",
    "required": false,
    "type": "string"
  }
}
```

## `update_tasklist`

Action slug: `update-tasklist`

Price: `5` credits

Fully update a task list (replaces existing data).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `tasklist_id` | `string` | yes | Task list ID |
| `tasklist_title` | `string` | yes | New title for the task list. You can also use 'title' as a shorthand. |

Sample parameters:

```json
{
  "tasklist_id": "example tasklist id",
  "tasklist_title": "example tasklist title"
}
```

Generated JSON parameter schema:

```json
{
  "tasklist_id": {
    "description": "Task list ID",
    "required": true,
    "type": "string"
  },
  "tasklist_title": {
    "description": "New title for the task list. You can also use 'title' as a shorthand.",
    "required": true,
    "type": "string"
  }
}
```
