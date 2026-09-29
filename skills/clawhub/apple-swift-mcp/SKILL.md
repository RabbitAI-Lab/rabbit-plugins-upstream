---
name: apple-swift-mcp
description: This skill should be used when the user asks about Apple app data via the native Swift MCP — Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, Photos, or Apple Music playlists on macOS. Triggers on phrases like "check my calendar", "find contact", "send iMessage", "search my notes", "recent emails", "find photos of", "make a playlist", "add this song to my playlist", "sort my playlist", or any macOS-native app automation. Requires macOS 14+ on Apple Silicon; faster than the AppleScript-backed Node variant.
---

# apple-swift-mcp

Native Swift MCP server for Apple apps. Compiled binary with embedded TCC usage descriptions — Calendar, Reminders, Contacts, and Maps talk to EventKit / Contacts / MapKit directly. Mail, Messages, Notes still go through AppleScript (no public framework exists) but run in-process via `NSAppleScript` instead of spawning `osascript`. Photos combines PhotoKit (structured search, albums, favorites, export/import) with the same in-process AppleScript for title/description/keyword metadata and free-text search. Music playlists go through Music.app's scripting dictionary in an `osascript` subprocess (MusicKit cannot edit playlists on macOS).

- **GitHub:** [github.com/chrischall/apple-swift-mcp](https://github.com/chrischall/apple-swift-mcp)

## Install

Download the latest `.mcpb` from [GitHub Releases](https://github.com/chrischall/apple-swift-mcp/releases) and double-click to install in Claude Desktop. First run prompts for TCC permissions (Calendar, Reminders, Contacts, full disk if reading `chat.db`, Automation for Music on the first music call).

Requires **macOS 14+ on Apple Silicon**. Intel users can build from source (`swift build -c release`).

## Tools

Reads and writes are separate tools, so a client can allow the read-only
`*_read` tools without also allowing sends, edits or deletes. Each `*_read`
tool takes an `operation`; every write tool does exactly one thing and takes
no `operation`.

### Calendar / Reminders
- `calendar_read` — `calendars`, `list`, `search`, `get`. `list`/`search`
  only ever look inside one window: `fromDate` + `toDate`, or `fromDate` +
  `daysAhead` (pass one, not both; default 7 days for `list`, 30 for
  `search`, maximum 366). Every response names the window it searched and,
  when more matched than `limit` held, the total and the `offset` for the
  next page — so an empty answer means nothing was scheduled in that window,
  never that the calendar is clear beyond it. A window longer than the
  maximum is refused rather than quietly shortened. Each occurrence of a
  recurring event gets its own id (`<series id>#occ=<original start>`);
  `get` and the write tools act on exactly that occurrence, and a bare
  series id is refused for a recurring event rather than applied to its
  first occurrence.
- `calendar_read` `freeTime` — open slots within working hours across every
  calendar on the Mac (work Exchange/Google accounts included), or one with
  `calendarName`. `workdayStart`/`workdayEnd` (default `09:00`–`17:00`),
  `weekdaysOnly` (default true), `minDurationMinutes` (default 30); window
  default today plus 7 days, maximum 31. A day the window cuts short says
  so. Busy means not marked free, not cancelled and
  not declined by you; all-day events block only with `includeAllDay: true`.
  Nothing before now is offered. Times are wall-clock times in the Mac's
  zone, which is how `calendar_create` reads an offset-less time, so a slot
  can be booked by passing its date and time straight back.
- `calendar_create`, `calendar_update` (passing `calendarName` moves the
  event), `calendar_delete` — `update`/`delete` take `span: "futureEvents"`
  to change that occurrence and every later one.
- `reminders_read` — `lists`, `list`, `search`, `get` (paged, soonest due first)
- `reminders_create`, `reminders_update`, `reminders_complete`,
  `reminders_reopen`, `reminders_delete`

### Contacts / Maps
- `contacts_read` — `search` (default) and `get`.
- `contacts_create`, `contacts_update`, `contacts_delete`. Emails, phones and
  addresses are edited one entry at a time (`add` / `remove` / `replace`),
  so an edit never rewrites the whole list. Writes need *full* Contacts
  access. A card with anything in its Notes field cannot be written through
  the Contacts framework at all — not just its note, **every** field —
  without the `com.apple.developer.contacts.notes` entitlement. An update or
  delete on such a card is replayed automatically through Contacts.app, which
  does hold the entitlement; it needs Automation access to Contacts.app, and
  the reply says so when it happens. The replay covers name, organization, job
  title and note, and **declines** an edit touching emails/phones/addresses or
  a birthday (`contacts_create` with a note is still refused outright) — those
  cannot be expressed faithfully in AppleScript, so a declined edit writes
  nothing rather than part of itself. `contacts_delete` takes `contactId` only,
  never a name.
- `maps` — place search (default) and `directions`. Read-only.

### Mail / Messages / Notes
- `mail_read` — `accounts`, `mailboxes`, `unread`, `search`, `get`. Search
  reads Mail's Envelope Index directly (needs Full Disk Access), so it is
  fast on large accounts and returns results **newest first**.
- `mail_send` — send an email. Confirmation-gated (see below).
- `messages_read` — `chats` and `read` (history from `chat.db`, group chats).
- `messages_send` — send an iMessage / SMS, optionally with an attachment.
  Confirmation-gated (see below).
  Attachments inside hidden directories or dotfiles, `~/Library` and system
  locations are refused.
- `notes_read` — `list`, `search` (optionally with bodies inline), `get` (a
  full note, pageable), `folders`.
- `notes_create`, `notes_update`, `notes_delete`

### Photos (PhotoKit + AppleScript)
- `photos_read` — `albums`, `list`, `search`, `searchText` (free text),
  `asset` (detail), `imageData` (a JPEG rendition)
- `photos_export` (originals to a directory), `photos_import`,
  `photos_create_album`, `photos_add_to_album`, `photos_remove_from_album`,
  `photos_update` (`setFavorite` / `setTitle` / `setDescription` /
  `setKeywords`)

### Music (playlists in the local Music.app library)
- `music_read` — `playlists` (default; every playlist and folder with its
  kind, track count and folder; filter with `query` or `folderId`, `"root"`
  for the top level), `playlist` (one playlist's tracks in order, with
  positions, ids and a `revision`), `search` (library tracks matching
  `query` — find the ids to add). Ids are Music persistent IDs (16 hex
  characters, shown as `[id …]`).
- `music_create_playlist` (optionally in a folder and already holding
  `trackIds`), `music_create_folder`, `music_add_tracks` (appends; skips
  tracks already there unless `skipDuplicates: false`),
  `music_update_playlist` (rename, description, move into a folder).
- `music_remove_tracks` (`trackIds` removes every copy; `positions` removes
  exactly those rows), `music_reorder_playlist` (`mode`: `move`, `sort`,
  `reverse`, `dedupe`, `replace`), `music_delete_playlist` (a playlist, or an
  empty folder). All three are confirmation-gated.
- Local library only: a song that is only in the Apple Music catalog cannot
  be added (add it to the library in Music first). Only plain playlists have
  editable tracks — smart playlists and ones Music manages are read-only.
- Reordering rebuilds the playlist in place (Music has no reorder command):
  it keeps its id, name and folder, but each track's "date added" resets.
- Pass the `revision` from `music_read` as `expectedRevision` to have an edit
  refused if the playlist changed in between. Every write reports whether a
  re-read confirmed it; with iCloud Music Library on, Music can revert edits
  to synced playlists, so "not verified yet" means check again, not retry.
- The first call asks to let the app running the server control Music
  (Automation).

### With apple-icloud-mcp
When both servers are connected, prefer this one for Calendar, Contacts and
Mail on the Mac (it sees every account, not only iCloud) and for Reminders,
Notes, Messages, Photos and Music.app playlist edits. Use apple-icloud-mcp for
the Apple Music catalog, Apple Maps and WeatherKit. Change one thing through
one server at a time: both can edit the same iCloud event, contact or synced
playlist. To put a catalog song in a local playlist, add it with
`apple_music_add_to_library` first, wait for Music.app to sync it, then
`music_read` search and `music_add_tracks`. If the search is empty, wait
rather than adding the song again. The reorder tools name their arguments
differently: `mode`/`sortBy` here, `operation`/`by` there.

### Confirmation (sends, deletes and playlist rewrites)

`mail_send`, `messages_send`, `calendar_delete`, `contacts_delete`,
`music_remove_tracks`, `music_reorder_playlist` and `music_delete_playlist`.

These cannot be undone, so none acts on its first call. A client with MCP
elicitation prompts the user. Otherwise the first call returns
`status: "confirmation-required"` with a preview and a `confirmToken`: show
the preview to the user, and only after they approve call again with the same
arguments plus `confirmToken`. The token is single-use and bound to exactly
those arguments. `MCP_CONFIRM_MODE` (`ask-user` default / `auto` / `refuse`)
sets the fallback.

### Upgrading from the multiplexed tools (2.0)

The old `calendar`, `reminders`, `contacts`, `mail`, `messages`, `notes` and
`photos` tools are gone. Calling one returns an error naming its
replacements. The same `operation` values carry over to the `*_read` tools;
each write operation became its own tool (`messages` `send` →
`messages_send`, `contacts` `delete` → `contacts_delete`, `reminders`
`complete` → `reminders_complete`, `photos` `setTitle` → `photos_update`
with `operation: "setTitle"`, and so on).

## Environment

Optional user config (set in Claude Desktop → Settings → MCP):

- `APPLE_MCP_DEFAULT_CALENDAR` — default calendar name for event creation
- `APPLE_MCP_DEFAULT_REMINDER_LIST` — default list name for reminder creation

## Notes

- Binary is arm64-only because some transitive MCP SDK deps (swift-collections, swift-service-lifecycle) don't declare x86_64.
- EventKit / Contacts / MapKit-backed tools are orders of magnitude faster than the equivalent AppleScript path.
- `messages_read` reads `chat.db` directly for history; `messages_send` uses AppleScript.
- `mail_read` `search` takes multiple terms in one call — prefer that over one call
  per term:
  - `invoice overdue` — both (implicit AND)
  - `invoice OR receipt` — either (`OR` must be uppercase)
  - `"past due"` — quoted phrase
  - `from:` / `to:` / `subject:` — field scoping, combinable with AND
- A `mail_read` timeout comes back as an explicit error, never as an empty result
  list. If you see "the search completed and matched no messages", the search
  really did finish and find nothing. If you see "Timed out", nothing was
  retrieved and the query needs narrowing — do not report it as "no mail
  found".
