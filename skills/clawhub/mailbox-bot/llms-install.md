# mailbox.bot — Install Guide for AI Coding Agents

> For MCP-capable AI clients such as Cline, Cursor, Claude Code, Claude Desktop, and other development tools.

## MCP Server (Remote — no local install needed)

mailbox.bot is a remote MCP server. For clients that support remote HTTP MCP servers, no npm install, Docker, or local process is required. Add this config and you're connected to 30 tools for two live workflows: outbound physical mail plus inbound forwarded document context. Real mailbox.bot-issued mailing addresses with street address + mailbox number, scan/photo intake, and agent notifications remain a separate reservation/private-beta surface.

### Generic remote HTTP config

Add to your MCP client config:

```json
{
  "mcpServers": {
    "mailbox-bot": {
      "url": "https://mailbox.bot/api/mcp",
      "headers": { "Authorization": "Bearer sk_agent_..." }
    }
  }
}
```

### Command bridge config

For clients that expect a local command, bridge the same remote server with `mcp-remote`:

```json
{
  "mcpServers": {
    "mailbox-bot": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mailbox.bot/api/mcp",
        "--header",
        "Authorization: Bearer sk_agent_..."
      ]
    }
  }
}
```

### Cursor

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "mailbox-bot": {
      "url": "https://mailbox.bot/api/mcp",
      "headers": { "Authorization": "Bearer sk_agent_..." }
    }
  }
}
```

### Cline

Add to Cline MCP settings:

```json
{
  "mcpServers": {
    "mailbox-bot": {
      "url": "https://mailbox.bot/api/mcp",
      "headers": { "Authorization": "Bearer sk_agent_..." }
    }
  }
}
```

## Get an API Key

1. Sign up at https://mailbox.bot/signup
2. Create an agent in the dashboard
3. Generate an agent-scoped API key (`sk_agent_...`)
4. Use a test key (`sk_agent_test_...`) for sandbox — no charges, same endpoints

## What You Get

30 MCP tools for outbound mail and inbound document context:

- **send_outbound_mail** — print and mail a PDF, DOCX, image, TXT, or CSV
- **get_outbound_mail_document** — retrieve the original outbound source document as base64 with `document.read` scope
- **list_inbound_forwarding_addresses** — retrieve the operator's private intake aliases
- **list_inbound_mail** — list forwarded inbound captures
- **get_inbound_mail** — fetch extracted context and `draft_context`
- **list_postal_threads** — list linked inbound/outbound physical-mail threads
- **get_mailbox_md** — fetch standing instructions
- And 23 more (managed mailing mailbox address beta tools, packages, scan/photo intake, tags, notes, rules, usage, facility messaging, webhooks, and sandbox mail lifecycle tools)

Stored outbound-mail submissions can include `document_preview_url` for human visual verification. Support conversations and attachments are REST/OpenAPI/dashboard features, not MCP tools.

Full tool catalog: https://mailbox.bot/api/mcp/tools-public

## Links

- Install guide: https://mailbox.bot/mcp-install
- API docs: https://mailbox.bot/api-docs
- Full API reference: https://mailbox.bot/llms-full.txt
- Sandbox: https://mailbox.bot/api-docs#sandbox
