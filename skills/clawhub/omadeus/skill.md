---

name: maestro
description: Interact with the Maestro task management system. Use this skill to create tasks, list recent tasks, and send messages to Maestro rooms.
metadata:
openclaw:
primaryEnv: MAESTRO_API_KEY
---------------------------

# Maestro Skill

Use this skill to interact with the Maestro API.

The skill supports the following operations:

1. Create a task
2. List tasks
3. Send a message to a room

---

## Configuration

The skill requires:

### 1. API Key

The Maestro API key is provided by OpenClaw as:

```text
MAESTRO_API_KEY
```

Use it in every API request:

```http
ApiToken: <MAESTRO_API_KEY>
```

Do not use:

```http
Authorization: Bearer <token>
```

Never hardcode, expose, print, or return the API key.

---

### 2. Environment

Read the current environment from:

```text
OMADEUS_ENV
```

The value of `OMADEUS_ENV` must be used to select the API base URL from the configured URL map.

Never hardcode the API base URL.

If `OMADEUS_ENV` is missing, do not guess the environment.

If no URL is configured for the current environment, do not make the API request.

---

### 3. API URLs

The configured URL map contains an entry for each environment.

Example:

```json
{
  "urls": {
    "dev": "https://dev-maestro.rouztech.com",
    "staging": "https://staging-maestro.rouztech.com",
    "production": "https://maestro.rouztech.com"
  }
}
```

Resolve the base URL as:

```text
urls[OMADEUS_ENV]
```

For example:

```text
OMADEUS_ENV=dev
```

resolves to:

```text
urls.dev
```

The final API URL is:

```text
<resolved-base-url><api-path>
```

---

### 4. Member Reference ID

The `memberReferenceId` must be read from the Skill configuration.

Never hardcode this value.

When creating a task, include the configured value in the request body.

If the value is missing, do not invent one and do not create the task.

---

# Authentication

Every request must include:

```http
Accept: application/json, text/plain, */*
ApiToken: <MAESTRO_API_KEY>
```

Never use a Bearer token.

Never expose the API key to the user.

---

# Operation 1: Create a Task

Use this operation when the user asks to:

* create a task
* add a task
* create a todo
* track work
* create a bug task
* create a feature task
* create an enhancement task
* create a refactoring task
* create a cleanup task
* create a performance task

## API

```text
CREATE /dolphin/apiv1/nuggets
```

The final URL is:

```text
<resolved-base-url>/dolphin/apiv1/nuggets
```

## Headers

```http
Accept: application/json, text/plain, */*
ApiToken: <MAESTRO_API_KEY>
Content-Type: application/json
```

## Request Body

```json
{
  "title": "<generated task title>",
  "description": "<generated task description>",
  "kind": "task",
  "priority": "<priority>",
  "memberReferenceId": "<configured memberReferenceId>"
}
```

## Field Rules

### `title`

Generate a concise and meaningful title based on the user's request.

The title should:

* clearly describe the work
* be concise
* use action-oriented language when appropriate
* avoid unnecessary details

### `description`

Generate a clear description of the requested work.

The description should explain:

* what needs to be done
* relevant context provided by the user
* the expected result

Do not invent technical details that the user did not provide.

### `kind`

The value MUST always be:

```text
task
```

Never ask the user to choose a kind.

Never infer a different value.

Never send another value.

### `priority`

Use the priority specified by the user.

Supported values:

```text
low
medium
high
urgent
```

If the user does not specify a priority, use:

```text
low
```

### `memberReferenceId`

Read the value from the Skill configuration.

Never hardcode it.

If it is missing, do not create the task.

### `stage`

Do not send a `stage` field.

---

## Create Task Behavior

When the user provides enough information:

1. Understand the requested work.
2. Generate a concise title.
3. Generate a clear description.
4. Determine the priority.
5. Set `kind` to `task`.
6. Read `memberReferenceId` from configuration.
7. Resolve the API base URL using `OMADEUS_ENV`.
8. Send the request.
9. Return the result to the user.

Do not ask unnecessary questions.

If the request is too vague to create a useful task, ask only for the missing information.

---

# Operation 2: List Tasks

Use this operation when the user asks to:

* show tasks
* list tasks
* show my tasks
* show recent tasks
* show open tasks
* find a task
* check the task list

## API

```text
LIST /dolphin/apiv1/global/taskviews
```

The final URL is:

```text
<resolved-base-url>/dolphin/apiv1/global/taskviews
```

## Default Query Parameters

```text
sort=-recentMessageAt
take=25
zone=tasklists-tasks
```

## Default Request

```text
LIST /dolphin/apiv1/global/taskviews?sort=-recentMessageAt&take=25&zone=tasklists-tasks
```

## Headers

```http
Accept: application/json, text/plain, */*
ApiToken: <MAESTRO_API_KEY>
```

## Query Rules

### `take`

Default:

```text
25
```

If the user asks for a specific number of tasks, use that number.

### `sort`

Always use:

```text
-recentMessageAt
```

unless the API behavior is explicitly changed.

### `zone`

Always use:

```text
tasklists-tasks
```

unless the user explicitly asks for another zone.

---

## List Task Behavior

1. Resolve the API base URL using `OMADEUS_ENV`.
2. Send the request.
3. Parse the response.
4. Present the tasks in a readable format.

When available, include:

* title
* description
* status or stage
* priority
* last activity
* task identifier

Do not expose the raw API response unless the user asks for it.

If no tasks are returned, tell the user that no tasks were found.

---

# Operation 3: Send a Message

Use this operation when the user asks to:

* send a message
* send a message to a room
* post a message
* notify a room
* send an update
* communicate with a Maestro room

## API

```text
SEND /jaguar/apiv1/rooms/{room_id}/messages
```

The final URL is:

```text
<resolved-base-url>/jaguar/apiv1/rooms/{room_id}/messages
```

Replace `{room_id}` with the target room ID.

## Headers

```http
Accept: application/json, text/plain, */*
ApiToken: <MAESTRO_API_KEY>
Content-Type: application/json;charset=UTF-8
```

Do not send:

```http
Activity: true
```

## Request Body

The body must contain only:

```json
{
  "body": "<message>"
}
```

Do not add:

* `temporaryId`
* `links`
* any other fields

## Room ID Rules

Never invent a room ID.

If the user provides a room ID, use it.

If the current conversation context provides a room ID, use it.

If no room ID is available, ask the user to provide one.

---

# Environment Resolution

Before every API request:

1. Read `OMADEUS_ENV`.
2. Read the configured URL map.
3. Find the URL matching `OMADEUS_ENV`.
4. Use that URL as the API base URL.
5. Append the operation-specific API path.

Example:

```text
OMADEUS_ENV=dev
```

Configuration:

```json
{
  "urls": {
    "dev": "https://dev-maestro.rouztech.com"
  }
}
```

Result:

```text
https://dev-maestro.rouztech.com
```

Then:

```text
https://dev-maestro.rouztech.com/dolphin/apiv1/nuggets
```

---

# Error Handling

## Missing API Key

If the API key is not available, do not make the request.

Report that Maestro authentication is not configured.

Never ask the user to provide the API key in chat if it should be configured in OpenClaw.

---

## Authentication Error

If the API returns an authentication or authorization error:

```text
Maestro authentication failed. The configured API key may be missing, expired, or invalid.
```

Never expose the API key.

---

## Missing Environment

If `OMADEUS_ENV` is missing:

```text
The OMADEUS_ENV environment is not configured.
```

Do not guess the environment.

---

## Missing URL

If no URL exists for the current environment:

```text
No Maestro API URL is configured for the current OMADEUS_ENV.
```

Do not make the request.

---

## Missing Member Reference ID

If `memberReferenceId` is missing while creating a task:

```text
The Maestro member reference ID is not configured.
```

Do not create the task.

---

## Validation Error

If the API returns a validation error:

1. Read the error response.
2. Identify the invalid or missing field.
3. Explain the problem clearly.
4. Ask only for information that is actually missing.

---

## Network Error

If the Maestro API cannot be reached:

```text
I could not connect to the Maestro API. Please try again later.
```

---

# Security Rules

Never:

* hardcode API keys
* hardcode the API base URL
* hardcode `memberReferenceId`
* print API keys
* expose API keys
* log the `ApiToken` header
* return credentials to the user
* include credentials in task descriptions
* include credentials in messages

---

# Response Guidelines

After successfully creating a task:

```text
Task created successfully.

Title: <task title>
```

Include the task identifier if the API returns one.

After successfully sending a message:

```text
Message sent successfully.
```

After listing tasks:

* use a concise readable list
* include useful task information
* do not dump the raw API response

---

# Examples

## Create a Task

User:

```text
Create a task to fix the ingress deletion issue.
```

Request body:

```json
{
  "title": "Fix ingress deletion issue",
  "description": "Investigate and fix the issue preventing ingress resources from being deleted correctly.",
  "kind": "task",
  "priority": "low",
  "memberReferenceId": 83
}
```

The `memberReferenceId` must come from configuration.

---

## Create a High Priority Task

User:

```text
Create a high priority task to fix the OpenClaw plugin authentication issue.
```

Request body:

```json
{
  "title": "Fix OpenClaw plugin authentication issue",
  "description": "Investigate and resolve the authentication issue in the OpenClaw plugin.",
  "kind": "task",
  "priority": "high",
  "memberReferenceId": 83
}
```

---

## List Recent Tasks

User:

```text
Show me my recent tasks.
```

Request:

```text
LIST /dolphin/apiv1/global/taskviews?sort=-recentMessageAt&take=25&zone=tasklists-tasks
```

---

## List 10 Tasks

User:

```text
Show my 10 most recent tasks.
```

Request:

```text
LIST /dolphin/apiv1/global/taskviews?sort=-recentMessageAt&take=10&zone=tasklists-tasks
```

---

## Send a Message

User:

```text
Send "Deployment completed successfully" to room 46.
```

Request:

```text
SEND /jaguar/apiv1/rooms/46/messages
```

Body:

```json
{
  "body": "Deployment completed successfully"
}
```

