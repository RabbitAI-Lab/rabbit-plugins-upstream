---
name: whatsapp-ultimate
version: 4.1.0
description: "You put 5 agents in a WhatsApp group. They all respond at once. Your API bill does a backflip. Protocol v2 fixes that — congestion control, conversation lifecycle, and budget-aware scheduling. Agents that know when to talk, when to shut up, and when to burn unused tokens before reset. Built for the TinkerClaw fork — github.com/globalcaos/tinkerclaw. Also ships four opt-in maintenance scripts that read your WhatsApp session credentials, enumerate group contacts, and patch your OpenClaw source tree — each refuses to run without an explicit --yes. See Permissions, Data Flow & Consent."
metadata:
  openclaw:
    emoji: "📱"
    requires:
      channels: ["whatsapp"]
      bins: ["node"]
    permissions:
      env: ["WA_AUTH_DIR", "OPENCLAW_SRC"]
      credentials:
        - path: "~/.openclaw/credentials/whatsapp/default"
          why: "Baileys multi-file auth state — the two bundled Baileys scripts need it to act as your linked device. Override with --auth-dir or WA_AUTH_DIR."
      file_read:
        - path: "~/.openclaw/credentials/whatsapp/default"
          why: "WhatsApp session credentials + LID reverse mappings (LID mappings only with --resolve-lids)"
        - path: "<openclaw-src>/src/**"
          why: "The two apply-*.sh scripts read the source files they patch"
      file_write:
        - path: "~/.openclaw/workspace/bank/whatsapp-contacts-full.json"
          why: "Contact/group export. OFF by default — only written when you pass --save. Mode 0600. Override the path with --save=PATH."
        - path: "<openclaw-src>/src/**"
          why: "The two apply-*.sh scripts edit OpenClaw source in place. Consent-gated (--yes), backed up to *.whatsapp-ultimate.bak, reversible with --revert."
      network:
        - host: "WhatsApp Web servers (via Baileys)"
          why: "The two bundled Baileys scripts connect as your linked device. No other endpoint is contacted; the skill has no telemetry."
    notes:
      security: "The documentation half of this skill is inert — it describes actions of OpenClaw's own WhatsApp channel and needs no permissions. The four bundled scripts in scripts/ are NOT inert and are OFF by default: each one prints exactly what it will touch and then EXITS unless you pass --yes. wa-fetch-contacts.ts reads your WhatsApp session credentials and enumerates every group and member (phone numbers MASKED to last-4 unless --resolve-lids; NOTHING written to disk unless --save; mode 0600 when saved). wa-create-group.ts reads the same credentials and creates a real group visible to the participants you name. apply-history-fix.sh patches OpenClaw source to store EVERY inbound message (text, sender, timestamp) in a local SQLite DB — broad, indefinite retention of other people's messages, off unless applied, reversible with --revert. apply-model-prefix.sh patches four source files so the AUTH PROFILE NAME (never a token or key) can appear in outgoing messages; reversible with --revert. Both patch scripts take a .bak before editing. No telemetry, no third-party endpoint, no privilege escalation. See the Permissions, Data Flow & Consent section for the full table."
---

# WhatsApp Ultimate

> One of dozens of skills and plugins in **[TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — a self-improving OpenClaw fork that's been running 24/7 for months.

You put 5 agents in a WhatsApp group. They all respond at once. Your API bill does a backflip.

Protocol v2 fixes that. Your agents learn group etiquette: when to talk, when to shut up, and when to spend the tokens they'd otherwise waste before the limit resets.

It adds congestion control so a busy group doesn't trigger a stampede of replies, a conversation lifecycle so a thread knows when it's actually over, and budget-aware scheduling so the cheap chatter waits and the work that matters gets the headroom. Multi-agent WhatsApp groups that stay calm, stay on-topic, and stay inside budget.

**Part of [TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — real-time token tracking, self-improving crons, persistent cognitive memory. This is one piece of that stack; the repo has dozens more.

👉 **https://github.com/globalcaos/tinkerclaw**

_Clone it. Fork it. Break it. Make it yours._

<scope>
Everything you can do in WhatsApp, your AI agent can do too. This skill documents all WhatsApp capabilities available through OpenClaw's native channel integration. No external Docker services, no CLI wrappers — direct WhatsApp Web protocol via Baileys.
</scope>

---

<prerequisites>
- OpenClaw with WhatsApp channel configured
- WhatsApp account linked via QR code (`openclaw whatsapp login`)
</prerequisites>

---

## Permissions, Data Flow & Consent

Short version: **most of this skill is documentation and needs no permissions at all.** The
action reference below describes things OpenClaw's own WhatsApp channel already does — this
package does not implement them and cannot do them on its own. What this package *does* ship
is four scripts in `scripts/`, and those are genuinely powerful. They are all **off by
default**: each one prints exactly what it is about to touch and then exits unless you pass
`--yes`.

Longer version, because you should not have to take that on trust.

**What it needs, and why.**

| Capability | Why | Scope | On by default? |
| --- | --- | --- | --- |
| Read WhatsApp credentials | The two Baileys scripts act as your linked device | `~/.openclaw/credentials/whatsapp/default`, or `--auth-dir` / `WA_AUTH_DIR` | No — `--yes` required |
| Network | Baileys → WhatsApp Web servers, as your account | WhatsApp only. **No telemetry, no analytics, no third-party endpoint** | No — `--yes` required |
| File write (export) | Contact/group inventory | `~/.openclaw/workspace/bank/whatsapp-contacts-full.json`, or `--save=PATH`; written mode `0600` | **No — requires `--save`** |
| File write (source) | The two `apply-*.sh` scripts edit your OpenClaw checkout in place | `<openclaw-src>/src/**`; `.bak` taken first, `--revert` restores | No — `--yes` required |
| Create groups / message | `wa-create-group.ts` creates a real, visible group | Only the group name + numbers you pass | No — `--yes` required |
| Read LID → phone mappings | Turn opaque WhatsApp LIDs into real phone numbers | Auth dir; **only** with `--resolve-lids` | **No — masked to last-4 otherwise** |
| Env read | `WA_AUTH_DIR`, `OPENCLAW_SRC` | Path overrides only | — |
| Secrets / tokens / API keys | **None.** Nothing reads an API key, and no token, key or secret is ever transmitted | — | — |

**The privacy-affecting things, stated plainly.**

Three of these scripts touch data about *other people*, who have not agreed to any of it.
That is a real cost and the docs should say so rather than bury it:

- **Contact enumeration** (`wa-fetch-contacts.ts`) builds a map of every group you are in and
  everyone in them. By default phone numbers are **masked to the last 4 digits** and **nothing
  is written to disk** — you get an in-memory summary. `--resolve-lids` un-masks them;
  `--save` persists them at mode `0600`. Both are deliberate, separate opt-ins.
- **Message retention** (`apply-history-fix.sh`) makes OpenClaw store *every* inbound message —
  text, sender, timestamp — in a local SQLite DB, with no retention limit and no encryption
  beyond your filesystem's. Applying it is a decision about other people's messages. In some
  jurisdictions it is also a legal obligation you are taking on. Off unless you apply it.
- **Identity metadata** (`apply-model-prefix.sh`) can print which auth profile served a reply
  into the outgoing message, where everyone in the chat sees it. It reads the profile *name*,
  never the token behind it.

**Turning it off.** Nothing here is on until you turn it on, and everything is reversible:

```bash
# The scripts do nothing without --yes. That is the off switch: don't pass it.
./scripts/apply-history-fix.sh --revert     # un-patch message retention
./scripts/apply-model-prefix.sh --revert    # un-patch the auth-mode prefix
rm ~/.openclaw/workspace/bank/whatsapp-contacts-full.json   # delete the export
```

To stop the auth-mode prefix without reverting anything, just remove `{authMode}` /
`{authProfile}` from `responsePrefix` in your config. To stop history capture without
reverting, delete the history DB — but note that new messages keep arriving until you revert.

**Read them before you run them.** All four scripts are short and are meant to be read end to
end. That is the whole security model.

---

## Capabilities Overview

| Category | Features |
|----------|----------|
| **Messaging** | Text, media, polls, stickers, voice notes, GIFs |
| **Interactions** | Reactions, replies/quotes, edit, unsend |
| **Groups** | Create, rename, icon, description, participants, admin, invite links |
| **History** | Local-DB search only (see caveat below). vCard contact extraction |

Total: 22 distinct actions.

**These 22 actions belong to OpenClaw's WhatsApp channel, not to this package.** This skill
documents them; installing it does not add them, and uninstalling it does not remove them. The
code this package actually ships is the four scripts in `scripts/` — documented below, all
consent-gated.

---

## Messaging

### Send Text
```
message action=send channel=whatsapp to="+34612345678" message="Hello!"
```

### Send Media (Image/Video/Document)
```
message action=send channel=whatsapp to="+34612345678" message="Check this out" filePath=/path/to/image.jpg
```
Supported: JPG, PNG, GIF, MP4, PDF, DOC, etc.

### Send Poll
```
message action=poll channel=whatsapp to="+34612345678" pollQuestion="What time?" pollOption=["3pm", "4pm", "5pm"]
```

### Send Sticker
```
message action=sticker channel=whatsapp to="+34612345678" filePath=/path/to/sticker.webp
```
Must be WebP format, ideally 512x512.

### Send Voice Note
```
message action=send channel=whatsapp to="+34612345678" filePath=/path/to/audio.ogg asVoice=true
```
Use OGG/Opus format for voice notes — MP3 may not play correctly.

### Send GIF
```
message action=send channel=whatsapp to="+34612345678" filePath=/path/to/animation.mp4 gifPlayback=true
```
Convert GIF to MP4 first (WhatsApp requires this):
```bash
ffmpeg -i input.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" output.mp4 -y
```

---

## Interactions

### Add Reaction
```
message action=react channel=whatsapp chatJid="34612345678@s.whatsapp.net" messageId="ABC123" emoji="🚀"
```

### Remove Reaction
```
message action=react channel=whatsapp chatJid="34612345678@s.whatsapp.net" messageId="ABC123" remove=true
```

### Reply/Quote Message
```
message action=reply channel=whatsapp to="34612345678@s.whatsapp.net" replyTo="QUOTED_MSG_ID" message="Replying to this!"
```

### Edit Message (Own Messages Only)
```
message action=edit channel=whatsapp chatJid="34612345678@s.whatsapp.net" messageId="ABC123" message="Updated text"
```

### Unsend/Delete Message
```
message action=unsend channel=whatsapp chatJid="34612345678@s.whatsapp.net" messageId="ABC123"
```
> **Irreversible and visible.** Deletion-for-everyone cannot be undone, and WhatsApp leaves a
> "This message was deleted" tombstone in the chat. Confirm with the human before an agent
> unsends anything it did not send itself.

---

## Group Management

### Create Group
```
message action=group-create channel=whatsapp name="Project Team" participants=["+34612345678", "+34687654321"]
```

### Rename Group
```
message action=renameGroup channel=whatsapp groupId="123456789@g.us" name="New Name"
```

### Set Group Icon
```
message action=setGroupIcon channel=whatsapp groupId="123456789@g.us" filePath=/path/to/icon.jpg
```

### Set Group Description
```
message action=setGroupDescription channel=whatsapp groupJid="123456789@g.us" description="Team chat for Q1 project"
```

### Add Participant
```
message action=addParticipant channel=whatsapp groupId="123456789@g.us" participant="+34612345678"
```

### Remove Participant
```
message action=removeParticipant channel=whatsapp groupId="123456789@g.us" participant="+34612345678"
```
> **Affects a real person and requires admin.** Removal is visible to the whole group and you
> cannot silently undo it. Same for `promoteParticipant` / `demoteParticipant`. Get explicit
> human confirmation before an agent changes a group's membership or admin list.

### Promote to Admin
```
message action=promoteParticipant channel=whatsapp groupJid="123456789@g.us" participants=["+34612345678"]
```

### Demote from Admin
```
message action=demoteParticipant channel=whatsapp groupJid="123456789@g.us" participants=["+34612345678"]
```

### Leave Group
```
message action=leaveGroup channel=whatsapp groupId="123456789@g.us"
```

### Get Invite Link
```
message action=getInviteCode channel=whatsapp groupJid="123456789@g.us"
```
Returns: `https://chat.whatsapp.com/XXXXX`

### Revoke Invite Link
```
message action=revokeInviteCode channel=whatsapp groupJid="123456789@g.us"
```
> **Both directions are sensitive.** `getInviteCode` returns a link that lets *anyone holding
> it* join the group — treat it as a credential and do not paste it into logs or other chats.
> `revokeInviteCode` instantly breaks every copy of the old link that is already circulating.

### Get Group Info
```
message action=getGroupInfo channel=whatsapp groupJid="123456789@g.us"
```
Returns: name, description, participants, admins, creation date.

---

## JID Formats

WhatsApp uses JIDs (Jabber IDs) internally:

| Type | Format | Example |
|------|--------|---------|
| Individual | `<number>@s.whatsapp.net` | `34612345678@s.whatsapp.net` |
| Group | `<id>@g.us` | `123456789012345678@g.us` |

When using `to=` with phone numbers, OpenClaw auto-converts to JID format.

---

## History is a local-DB search. Live fetch does not work.

**Your agent cannot pull old messages back off your phone on demand.** Anything that claims
otherwise is wrong. What actually exists:

- **Search of the local `whatsapp-history.db`** — whatever your gateway captured while it was
  running, including media captions and link previews, not just plain text.
- **On-demand historySync does not land.** The phone answers the request and the payloads are
  discarded before they reach storage. Treat a live channel plus an empty result as a gap in
  what was captured, not as a broken skill.
- **Any period your gateway was down is simply missing**, and no amount of retrying will fill
  it in. Check your own downtime before assuming a bug.
- **The backfill that does work:** use *Export chat* on your phone and drop the file into your
  workspace. Re-pairing via a fresh QR *may* bootstrap history, but it drops your existing
  linked session — that is a deliberate decision, not something an agent should do for you.

> **The history DB is off unless you turn it on.** Capturing every inbound message is a
> decision about other people's data — see [Permissions, Data Flow & Consent](#permissions-data-flow--consent)
> and `scripts/apply-history-fix.sh`.

---

## Bundled Scripts (`scripts/`)

This is the code the package actually ships. All four are **off by default** — each prints
what it will touch and exits unless you pass `--yes`. Read
[Permissions, Data Flow & Consent](#permissions-data-flow--consent) first.

The two `.ts` scripts drive Baileys directly and need Node plus `@whiskeysockets/baileys` and
`pino` resolvable — run them from inside your OpenClaw checkout, which already has both. The
two `.sh` scripts need `bash` and `python3`.

### `wa-fetch-contacts.ts` — inventory your groups and their members

```bash
npx tsx scripts/wa-fetch-contacts.ts                    # prints what it would do, then refuses
npx tsx scripts/wa-fetch-contacts.ts --yes              # in-memory only, numbers masked to last-4
npx tsx scripts/wa-fetch-contacts.ts --yes --save       # persist to bank/whatsapp-contacts-full.json (0600)
npx tsx scripts/wa-fetch-contacts.ts --yes --resolve-lids   # un-mask: full phone numbers
```

| Flag | Effect |
| --- | --- |
| `--yes` | Required. Without it the script exits 1 and touches nothing |
| `--save[=PATH]` | Opt in to writing the dataset to disk, mode `0600`. Default: nothing is written |
| `--resolve-lids` | Opt in to reading LID→phone mappings and emitting full numbers. Default: last-4 masking |
| `--auth-dir=PATH` | Use a different session directory (also `WA_AUTH_DIR`) |

**This builds a dataset about people who did not consent to it.** Delete the file when done.

### `wa-create-group.ts` — create a group

```bash
npx tsx scripts/wa-create-group.ts --yes "Project Team" "+34612345678" "+34687654321"
```

Reads your session credentials, connects as your account, and creates a real group that every
participant sees appear on their phone. Not undoable from here. Only the group name and the
numbers you pass are sent to WhatsApp. `--auth-dir=PATH` / `WA_AUTH_DIR` override the
credential path.

### `apply-history-fix.sh` — turn on full inbound message retention

```bash
./scripts/apply-history-fix.sh --yes      # patch monitor.ts (a .bak is taken first)
./scripts/apply-history-fix.sh --revert   # restore from the .bak
```

Edits `src/web/inbound/monitor.ts` in your OpenClaw checkout so every inbound message —
text, sender JID, push name, timestamp — is written to the local history DB, including
self-chat messages Baileys otherwise drops. **No retention limit, no redaction, no encryption
beyond your filesystem's.** This is a decision about other people's messages; in some
jurisdictions it is also a notice obligation you are taking on. After applying: rebuild and
restart your gateway.

### `apply-model-prefix.sh` — show model + auth mode in outgoing messages

```bash
./scripts/apply-model-prefix.sh --yes      # patch 4 files (.bak taken for each)
./scripts/apply-model-prefix.sh --revert   # restore from the .bak files
```

Adds `{authMode}` / `{authProfile}` to `responsePrefix`, e.g. `"🤖({model}|{authMode})"`. It
reads the auth profile's **name** — never a token, key or secret — but that name then appears
in your outgoing messages where everyone in the chat can see it. To stop the disclosure
without reverting, drop those variables from `responsePrefix`.

---

## Tips

### Voice Notes
Use OGG/Opus format:
```bash
ffmpeg -i input.wav -c:a libopus -b:a 64k output.ogg
```

### Stickers
Convert images to WebP stickers:
```bash
ffmpeg -i input.png -vf "scale=512:512:force_original_aspect_ratio=decrease,pad=512:512:(ow-iw)/2:(oh-ih)/2:color=0x00000000" output.webp
```

### Rate Limits
WhatsApp has anti-spam measures. Avoid:
- Bulk messaging to many contacts
- Rapid-fire messages
- Messages to contacts who haven't messaged you first

### Message IDs
To react/edit/unsend, you need the message ID. Incoming messages include this in the event payload. For your own sent messages, the send response includes the ID.

---

## Comparison with Other Skills

| Feature | whatsapp-ultimate | wacli | whatsapp-automation | gif-whatsapp |
|---------|-------------------|-------|---------------------|--------------|
| Native integration | yes | no (CLI) | no (Docker) | N/A |
| Send text | yes | yes | no | no |
| Send media | yes | yes | no | no |
| Polls | yes | no | no | no |
| Stickers | yes | no | no | no |
| Voice notes | yes | no | no | no |
| GIFs | yes | no | no | yes |
| Reactions | yes | no | no | no |
| Reply/Quote | yes | no | no | no |
| Edit | yes | no | no | no |
| Unsend | yes | no | no | no |
| Group create | yes | no | no | no |
| Group management | yes (full) | no | no | no |
| Receive messages | yes | yes | yes | no |
| Two-way chat | yes | no | no | no |
| External deps | None for the 22 actions; Node + Baileys for the bundled scripts | Go binary | Docker + WAHA | ffmpeg |

---

---

## Protocol v2: Multi-Agent Discussions

<why_this_matters>
If you put multiple AI agents in one WhatsApp group, the naive default is everyone responds to everything. Five agents replying to one message means 5x the API spend per turn, plus echo loops where agents agree with each other forever. Protocol v2 introduces congestion control, conversation lifecycle, and budget-aware scheduling so agents know when to talk, when to stay quiet, and when to wrap up.
</why_this_matters>

### Agent Identity

Each agent gets its own personality, icon, and (optionally) model:

```yaml
channels:
  whatsapp:
    agentIcon: "🤖"          # single-agent icon prefix
    turnEndMarker: "⚡"       # end-of-turn marker in 1:1 chats
    multiAgent:
      mainAgentId: "jarvis"
      agents:
        jarvis:
          id: "jarvis"
          name: "Jarvis"
          icon: "🤖"
        luna:
          id: "luna"
          name: "Luna"
          icon: "🌙"
          model: "sonnet"
        rex:
          id: "rex"
          name: "Rex"
          icon: "🦖"
          model: "haiku"
```

Agent personalities live in the workspace:
```
workspace/
├── SOUL.md                  # main agent
├── agents/
│   ├── luna/SOUL.md         # Luna's personality
│   └── rex/SOUL.md          # Rex's personality
```

### Intra-Agent Chats

Register WhatsApp groups where agents discuss freely (no trigger prefix needed):

```yaml
      intraAgentChats:
        brainstorm:
          chatId: "123456789012345678@g.us"   # your own group's JID
          participants: ["jarvis", "luna", "rex"]
          owner: "your-owner-id"
          mode: "broadcast"        # broadcast | addressed | round-robin
```

**Routing modes:**
- **broadcast** — all agents respond (with congestion control)
- **addressed** — only respond when mentioned by name ("Luna, what do you think?")
- **round-robin** — structured turn-taking

### Congestion Control (Exponential Courtesy Protocol)

Prevents N agents from all responding simultaneously:

```yaml
      congestion:
        enabled: true
        baseDelayFactor: 150     # ms × agentCount² base delay
        maxDelay: 30000          # 30s cap
        backpressureThreshold: 1.5  # slow down over-talkers
        windowMs: 60000          # 60s sliding window
```

**How it works:**
- Base delay scales quadratically with agent count (2 agents ≈ 600ms, 5 agents ≈ 3750ms)
- Random jitter prevents synchronization
- Agents talking more than their fair share get 2× delay penalty
- If another agent posts during your wait, restart the timer (yield-on-collision)

### Conversation Lifecycle

Agents detect when discussions go stale and know when to wrap up:

```yaml
      lifecycle:
        stalenessWindow: 5        # compare last N messages
        stalenessThreshold: 0.85  # cosine similarity trigger
        maxTurnsPerObjective: 30  # hard cap
        autoClose: true
```

**Features:**
- **Staleness detection** — cosine similarity of message embeddings detects circular discussions
- **Agreement loop detection** — catches "I agree" / "Good point" / "Exactly" loops
- **Topic steering** — one agent claims pivot role to redirect conversation
- **Objective tracking** — set goals, track completion, auto-close with summary
- **Closure protocol** — propose → ack → converge (all agents must agree)

### Budget-Aware Scheduling

Adjusts conversation depth based on API usage and reset timing:

```yaml
      budget:
        provider: "anthropic"
        windowDays: 7
        burnModeEnabled: true
        burnTriggerHours: 24     # hours before reset
        burnUsageThreshold: 0.20 # usage below 20%
```

**Four modes:**

| Mode | When | Congestion | Staleness | Max Turns | Tangents |
|------|------|-----------|-----------|-----------|----------|
| Conservative | >85% used | 2× slower | 0.80 | ½ | No |
| Moderate | 60-85% | Normal | 0.85 | Normal | No |
| Aggressive | <60% | 0.7× faster | 0.85 | Normal | Yes |
| **Burn** | <20% used, <24h to reset | 0.3× faster | 0.95 | 2× | Encouraged |

Burn mode philosophy: unused tokens expire at reset. Better to have emergent agent-agent discussions than waste the budget.

### DM Trigger Prefix

Protocol v2 extends `triggerPrefix` to DMs (previously groups only):

- **Owner** — always bypasses triggerPrefix
- **Authorized contacts** — must start message with prefix (e.g., "Jarvis, help me with...")
- **Intra-agent chats** — bypass triggerPrefix entirely

### Turn-End Marker

In 1:1 chats (selfChat or owner-only DM), append a visual marker to signal turn completion:

```yaml
channels:
  whatsapp:
    turnEndMarker: "⚡"
```

---

### 4.1.0

- **Added:** "Permissions, Data Flow & Consent" — full capability table, what is read, what is written, where it goes
- **Added:** Consent gate on all four bundled scripts — each prints what it will touch and exits unless you pass `--yes`
- **Added:** `--revert` off-switch and automatic `.bak` for both source-patching scripts
- **Changed:** `wa-fetch-contacts.ts` is now ephemeral by default — nothing is written to disk without `--save`, and saved files are mode `0600`
- **Changed:** `wa-fetch-contacts.ts` masks phone numbers to the last 4 digits; LID→phone resolution is opt-in via `--resolve-lids`
- **Added:** `--auth-dir` / `WA_AUTH_DIR` override so credentials are not hard-coded to one path
- **Added:** Documentation for all four bundled scripts, which were previously undisclosed
- **Added:** Safety notes on unsend, participant/admin changes, and invite links
- **Fixed:** "External deps: None" now distinguishes the channel actions from the bundled scripts
- **Fixed:** Removed operator-specific content (real group JID, owner name, internal notes) from the history section and config examples

### 4.0.0

- **Protocol v2:** Multi-agent discussions with configurable routing (broadcast/addressed/round-robin)
- **Added:** Congestion control — Exponential Courtesy Protocol prevents message explosion in multi-agent chats
- **Added:** Conversation lifecycle — staleness detection, agreement loop detection, topic steering, objective tracking, closure protocol
- **Added:** Budget-aware scheduling — four spending modes including burn mode for pre-reset token usage
- **Added:** Agent identity system — per-agent SOUL.md, icons, names, model overrides
- **Added:** DM triggerPrefix gating — non-owner contacts must use prefix in DMs
- **Added:** Turn-end marker (⚡) for 1:1 chats
- **Added:** `agentIcon` config for outbound message prefixing

### 3.7.0

- **Added:** vCard phone number extraction — contact messages now return structured `vcard` field with names and phone numbers
- **Added:** `contactsArrayMessage` support — multi-contact shares are now parsed
- **Improved:** New contact messages store phone numbers in `text_content` for full-text search (e.g. search by phone number)
- **Improved:** `raw_json` now included in search results for contact-type messages, enabling vCard extraction from historical data

### 3.4.0

- **Fixed:** Chat search now resolves LID/JID aliases — searching by chat name finds messages across both `@lid` and `@s.whatsapp.net` JID formats
- **Added:** `resolveChatJids()` cross-references chats, contacts, and messages tables to discover all JID aliases for a given chat filter
- **Improved:** Search falls back to original LIKE behaviour if no JIDs resolve, so no regressions

### 3.0.0

```
Your Agent
    ↓
OpenClaw message tool
    ↓
WhatsApp Channel Plugin
    ↓
Baileys (WhatsApp Web Protocol)
    ↓
WhatsApp Servers
```

No external services. No Docker. No CLI tools. Direct protocol integration.

---

## Included Files

| File | Purpose | Runs anything? |
| --- | --- | --- |
| `SKILL.md` | This page — the action reference and the protocol v2 config | No |
| `description.md` | ClawHub listing copy | No |
| `scripts/wa-fetch-contacts.ts` | Group/contact inventory. Consent-gated, masked + ephemeral by default | Yes — `--yes` |
| `scripts/wa-create-group.ts` | Create a group via Baileys. Consent-gated | Yes — `--yes` |
| `scripts/apply-history-fix.sh` | Patch OpenClaw for full inbound retention. Consent-gated, `--revert` | Yes — `--yes` |
| `scripts/apply-model-prefix.sh` | Patch OpenClaw for `{authMode}` prefix. Consent-gated, `--revert` | Yes — `--yes` |

There is no `bin/`, no installer, no background process and no telemetry. Everything the
documentation above describes is either in this package or is a documented action of
OpenClaw's own WhatsApp channel — and the table in
[Permissions, Data Flow & Consent](#permissions-data-flow--consent) says which is which. If you
find a claim here that the code does not do, that is a bug — open an issue on
[the repo](https://github.com/globalcaos/tinkerclaw/issues).

---

## Pairs Well With

- [smart-model-router](https://clawhub.ai/globalcaos/smart-model-router) — auto-select the right model per agent role (creative → Sonnet, analyst → Haiku, devil's advocate → GPT)
- [agent-superpowers](https://clawhub.ai/globalcaos/agent-superpowers) — verification iron law and three-agent review for when your multi-agent discussions produce code
- [subagent-overseer](https://clawhub.ai/globalcaos/subagent-overseer) — monitor agent sessions without burning tokens on polling loops

https://github.com/globalcaos/tinkerclaw

_Clone it. Fork it. Break it. Make it yours._

---

## License

MIT — Part of OpenClaw

---

## Links

- OpenClaw: https://github.com/openclaw/openclaw
- Baileys: https://github.com/WhiskeySockets/Baileys
- ClawHub: https://clawhub.com
