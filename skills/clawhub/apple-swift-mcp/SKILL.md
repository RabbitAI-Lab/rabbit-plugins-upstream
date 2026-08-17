---
name: apple-swift-mcp
description: This skill should be used when the user asks about Apple app data via the native Swift MCP — Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, or Photos on macOS. Triggers on phrases like "check my calendar", "find contact", "send iMessage", "search my notes", "recent emails", "find photos of", or any macOS-native app automation. Requires macOS 14+ on Apple Silicon; faster than the AppleScript-backed Node variant.
---

# apple-swift-mcp

Native Swift MCP server for Apple apps. Compiled binary with embedded TCC usage descriptions — Calendar, Reminders, Contacts, and Maps talk to EventKit / Contacts / MapKit directly. Mail, Messages, Notes still go through AppleScript (no public framework exists) but run in-process via `NSAppleScript` instead of spawning `osascript`. Photos combines PhotoKit (structured search, albums, favorites, export/import) with the same in-process AppleScript for title/description/keyword metadata and free-text search.

- **GitHub:** [github.com/chrischall/apple-swift-mcp](https://github.com/chrischall/apple-swift-mcp)

## Install

Download the latest `.mcpb` from [GitHub Releases](https://github.com/chrischall/apple-swift-mcp/releases) and double-click to install in Claude Desktop. First run prompts for TCC permissions (Calendar, Reminders, Contacts, full disk if reading `chat.db`).

Requires **macOS 14+ on Apple Silicon**. Intel users can build from source (`swift build -c release`).

## Tools

### Calendar / Reminders
- `calendar` — list, search, create, update, delete events
- `reminders` — list reminder lists and items; create, complete, delete

### Contacts / Maps
- `contacts` — search by name, phone, or email
- `maps` — directions, search nearby places

### Mail / Messages / Notes
- `mail` — search, read, send; discover accounts/mailboxes. Search reads
  Mail's Envelope Index directly (needs Full Disk Access), so it is fast
  on large accounts and returns results **newest first**.
- `messages` — send iMessage / SMS, query `chat.db` for history, group chats
- `notes` — list, search (optionally with bodies inline), get a full note (pageable), folders, create, update, delete

### Photos (PhotoKit + AppleScript)
- `photos` — list/search assets and albums, get asset detail, favorite/organize/import/export, get a JPEG rendition, set title/description/keywords, free-text search

## Environment

Optional user config (set in Claude Desktop → Settings → MCP):

- `APPLE_MCP_DEFAULT_CALENDAR` — default calendar name for event creation
- `APPLE_MCP_DEFAULT_REMINDER_LIST` — default list name for reminder creation

## Notes

- Binary is arm64-only because some transitive MCP SDK deps (swift-collections, swift-service-lifecycle) don't declare x86_64.
- EventKit / Contacts / MapKit-backed tools are orders of magnitude faster than the equivalent AppleScript path.
- Messages tool reads `chat.db` directly for history; sending uses AppleScript.
- `mail search` takes multiple terms in one call — prefer that over one call
  per term:
  - `invoice overdue` — both (implicit AND)
  - `invoice OR receipt` — either (`OR` must be uppercase)
  - `"past due"` — quoted phrase
  - `from:` / `to:` / `subject:` — field scoping, combinable with AND
- A `mail` timeout comes back as an explicit error, never as an empty result
  list. If you see "the search completed and matched no messages", the search
  really did finish and find nothing. If you see "Timed out", nothing was
  retrieved and the query needs narrowing — do not report it as "no mail
  found".
