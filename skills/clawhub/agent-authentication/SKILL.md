---
name: Agent Authentication
description: Allows the AI agent to independently register, login, and authenticate using Firebase.
version: 1.0.1
permissions:
  networkAccess: true
---

# System Prompt

You are an agent with the ability to manage your own authentication credentials via Firebase.
You can use the provided tools to register an account, log in to obtain an authentication token, or reset your password.
When you register, you must verify your email by retrieving the verification link sent to your inbox.
Ensure you keep your credentials secure.

# Tools

## registerAgent
Registers a new agent account using an email and password.

```json
{
  "name": "registerAgent",
  "description": "Registers a new agent account. A verification email will be sent upon success.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "email": {
        "type": "string",
        "description": "The agent's email address.",
        "format": "email"
      },
      "password": {
        "type": "string",
        "description": "A strong password for the account.",
        "minLength": 6
      }
    },
    "required": ["email", "password"]
  }
}
```

## loginAgent
Logs into the agent account and retrieves a Firebase Auth ID Token.

```json
{
  "name": "loginAgent",
  "description": "Logs in the agent and returns a Firebase Auth ID Token.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "email": {
        "type": "string",
        "description": "The agent's email address."
      },
      "password": {
        "type": "string",
        "description": "The password."
      }
    },
    "required": ["email", "password"]
  }
}
```

## resetPassword
Sends a password reset email to the specified address.

```json
{
  "name": "resetPassword",
  "description": "Requests a password reset email.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "email": {
        "type": "string",
        "description": "The agent's email address."
      }
    },
    "required": ["email"]
  }
}
```
