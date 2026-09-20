---
name: slack
description: Read messages from Slack channels and post replies. Use when the user asks about Slack channels, channel history, posting Slack messages, or any Slack-related operation. Credentials are auto-injected when Slack is connected.
---

# Slack

A Slack workspace is connected. The bot's credentials are auto-injected
into every Bash command as `$SLACK_BOT_TOKEN`, `$SLACK_TEAM_ID`, and
`$SLACK_BOT_USER_ID`. Never hard-code these.

## Commands

```bash
# Read
python skills/slack/slack_api.py whoami
python skills/slack/slack_api.py list-channels [--include-private] [--limit N]
python skills/slack/slack_api.py channel-history --channel C0123 \
    [--oldest <ts>] [--latest <ts>] [--limit N]
python skills/slack/slack_api.py lookup-user --user U0123

# Write
python skills/slack/slack_api.py send-message --channel C0123 --text "..." \
    [--thread-ts <parent_ts>]
python skills/slack/slack_api.py reactions-add    --channel C0123 --timestamp <ts> --emoji eyes
python skills/slack/slack_api.py reactions-remove --channel C0123 --timestamp <ts> --emoji eyes
```

### `whoami`
Sanity-check that the token works. Returns team, bot user ID, workspace URL.

### `list-channels`
List public channels visible to the bot. `--include-private` adds
private channels the bot has been invited to. `--limit N` caps the
result.

### `channel-history`
Fetch messages from a channel, newest first.
- `--oldest` and `--latest` accept Slack message timestamps (e.g.
  `1714000000.123456`); use `oldest` to fetch "everything since X".
- Defaults to no limit — paginates fully. Pass `--limit N` for a quick
  preview.

### `send-message`
Post a message. Pass `--thread-ts <parent_ts>` to reply in-thread instead
of posting at the channel root.

### `lookup-user`
Resolve a user ID to a display name. Use after `channel-history` to make
messages human-readable.

### `reactions-add` / `reactions-remove`
Manage emoji reactions on a specific message. Used internally by the
agent loop to ack incoming `@Corvera` mentions with 👀.

## Channel access model

The bot can only read or post in channels it has been **invited to**.
If a command returns `not_in_channel`, or a channel is missing from
`list-channels --include-private`, ask the user to run:

```
/invite @Corvera
```

in the target channel and try again.

## Triggering the agent from Slack

Users can trigger the agent in two ways from inside Slack:

- **`@Corvera <task>`** in any channel where the bot is a member.
- **DM the bot directly.**

Both flow through the Slack Events webhook and run the agent end-to-end.
The agent's reply is posted back to the same channel, threaded under the
original mention. (You don't need to do anything to make this work — the
webhook handles dispatch automatically.)

## Output format

Every command prints a single JSON object on stdout:

- Success: `{"success": true, "data": {...}}`
- Failure: `{"success": false, "error": "<message>"}`

Parse the JSON before reasoning about the result. Never assume a command
worked from the absence of stderr alone.

## Troubleshooting

- `invalid_auth` / `token_revoked` — the customer disconnected or
  reinstalled the app. Tell them to reconnect Slack from the
  Integrations page.
- `not_in_channel` — bot needs to be invited to that channel.
- `missing_scope` — the customer connected before Phase 2 scopes
  (`app_mentions:read`, `im:history`) were added. Tell them to
  reconnect Slack to grant the new scopes.
- Empty `list-channels` results — the bot was just installed and Slack
  has not finished propagating; retry after a few seconds.
