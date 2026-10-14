# Connecting Remember Me

Read this when no Remember Me tools are available, or when signing in fails.

## Which server

- **Personal server, `https://auth.remem.me/mcp`.** All tools. The user signs in with their Remember Me account. It admits only the assistants it knows: Claude (also Claude Code), ChatGPT (also Codex) and Grok on grok.com. Other agents, such as OpenClaw, Grok Build, Hermes or VS Code, can't sign in to it.
- **Public server, `https://mcp.remem.me/mcp`.** No sign-in, read-only: browse_collections, get_collection_detail and get_collection_metrics. It works in any MCP client.

Both use the streamable HTTP transport.

## Setting it up

Tell the user what to do; you can't add a connector yourself.

- **Claude:** on claude.ai, Settings → Connectors → Add custom connector, address `https://auth.remem.me/mcp`. Once added on the web, it also works in the mobile app and in voice mode.
- **ChatGPT:** Settings → Security and login → turn on Developer mode, then Settings → Plugins → +, address `https://auth.remem.me/mcp`. Leave the client ID and secret empty.
- **Grok:** grok.com/connectors → New Connector → Custom, address `https://auth.remem.me/mcp`.
- **Claude Code:** install the plugin, which brings the server along:
  ```
  /plugin marketplace add remem-me/bible-memory
  /plugin install bible-memory@remem-me
  ```
  Then run `/mcp`, choose `remember-me` and sign in. Without the plugin: `claude mcp add --transport http remember-me https://auth.remem.me/mcp`.
- **Codex:** `codex mcp add remember-me --url https://auth.remem.me/mcp`, then `codex mcp login remember-me` to sign in.
- **OpenClaw:** `openclaw mcp add remember-me --url https://mcp.remem.me/mcp --transport streamable-http` (public server).
- **Grok Build:** `grok mcp add --transport http remember-me https://mcp.remem.me/mcp` (public server).
- **Any other MCP client:** add `https://mcp.remem.me/mcp` as a remote server (streamable HTTP) for the public collections.

Step by step: https://www.remem.me/docs/mcp/

## Signing in

- The assistant opens a sign-in page on remem.me. The user signs in there with the email and password they use in the app and chooses **Authorize**. Never ask for the password in the chat.
- No account yet: the sign-in page links to a free sign-up. After confirming their email address, the user starts the connection again.
- The page is valid for ten minutes. After that it says the session expired, and the user starts the connection again.

## When it fails

- **"Unknown application" in Claude, ChatGPT, Codex or Grok:** check that the address is exactly `https://auth.remem.me/mcp`, with nothing added. If it is, try again later; if it keeps failing, write to support@remem.me.
- **"Unknown application" in any other assistant:** the personal server doesn't admit it. It can still use the public server for collections. To add and review verses, the user can switch to Claude, ChatGPT or Grok, or use the Remember Me app on iOS, Android or https://web.remem.me.
- **"Invalid email or password":** the same email and password as in the app. A forgotten password is reset in the app or on https://web.remem.me.
- **Asked which account:** a user can have several accounts. Tools take the account *name*, not the email; list_accounts shows the names.
- **"Write limit reached":** 30 changes within five minutes, 300 per day. Wait and continue later.

More help: the forum at https://forum.remem.me/ or support@remem.me.
