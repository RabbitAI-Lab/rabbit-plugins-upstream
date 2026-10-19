---
name: commsharbor
description: Inspect domain email setup and authorized email workspaces with CommsHarbor.
license: MIT-0
---

# CommsHarbor

Connect to `https://commsharbor.com/mcp?checkout=site` with Streamable HTTP.
Read `https://commsharbor.com/llms.txt` for the current API contract.

## MCP tools

| Tool | Use |
|---|---|
| `commsharbor_email_workspace` | Read an authorized organization's workspace. |
| `commsharbor_email_domain_setup` | Find an existing domain and the organization that you can open. |

## Use

Use the person's organization ID and an authorized organization API key for private operations.
Keep keys in the client's secret storage. Do not expose keys or mailbox passwords in answers.
Before a write, confirm the intended domain, mailbox or alias and the person's authority.
The MCP tools are free, within their free limits. If a tool answers `free_limit`, tell the person that the free
limit for that action is used up. Do not offer campaign or transactional sending tools.
