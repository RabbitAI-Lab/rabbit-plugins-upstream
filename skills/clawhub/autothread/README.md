# AutoThread

Add `/topic` to the start of any message in a supported group → a new topic or thread is created from it. The title is figured out from your message automatically — no need to think of one yourself.

**Supported platforms:** Telegram · Nicegram · Discord · Signal

Built from the ground up as an [OpenClaw](https://openclaw.ai) skill. No forks, no clones.

## Example

**1.** You send a message starting with `/topic`:
> /topic @your_bot I need to look into renewing my passport before March

**2.** A new topic **"Passport Renewal Before March"** is created with your message quoted inside it. You get a reply linking directly to the new topic.

## How It Works

1. You send a message starting with `/topic`
2. A new topic/thread is created — titled from your message automatically
3. Your message is quoted in the new topic with your name
4. You get a reply with a clickable link to the new topic
5. The bot responds to your message in the new topic

Works with media too — photos, videos, or documents with `/topic` in the caption get forwarded into the new topic (Telegram).

## Platform Support

| Platform | Mechanism | Prerequisites | Notes |
|----------|-----------|---------------|-------|
| **Telegram** | Forum topic via Bot API | Group has forum/topics enabled; bot admin with *Manage Topics* | Full support incl. media forwarding |
| **Nicegram** | Forum topic via Telegram Bot API | Same as Telegram (Nicegram chats *are* Telegram chats) | Optional separate bot token |
| **Discord** | Thread from message via REST API | Bot needs *Create Public Threads* + *Send Messages in Threads* | Thread names capped at 100 chars |
| **Signal** | Pseudo-topic digest | `signal-cli` with registered account | No native topics — see below |

### Signal limitation

Signal has no forum topics or threads — there is no API object equivalent to a topic. The Signal adapter runs in **pseudo-topic mode**: it posts a titled, quoted digest (`📌 <title>`) of the original message to the group and returns the sent timestamp as the `topic_id`, with `link: null`.

## Install

Clone this repo into your OpenClaw skills directory, or install directly:

```bash
clawhub install abyssbugg/autothread
```

## Adapters

```
scripts/
├── lib/
│   └── common.sh              # shared: config read, title fallback, JSON output
├── autothread-telegram.sh     # Telegram forum topics
├── autothread-nicegram.sh     # Nicegram (delegates to Telegram adapter)
├── autothread-discord.sh      # Discord threads
└── autothread-signal.sh       # Signal pseudo-topic digest
```

Every adapter takes the same shape of arguments and returns the same JSON contract on stdout:

```json
{"topic_id": 123, "title": "Used title", "link": "https://..."}
```

```
<adapter>.sh <group_or_channel_id> <message_id> "<sender>" [title] [text]
```

- `title` — if omitted, auto-generated from the first ~50 chars of the text at a word boundary
- `text` — if empty (media-only), the message is forwarded into the new topic (Telegram)

## Permissions

The scripts read your OpenClaw configuration file (`~/.openclaw/openclaw.json`) to obtain platform credentials (bot tokens / signal account). Credentials are used solely for API calls to the corresponding platform to create topics/threads and post messages. No data is sent anywhere else.

## Optional configuration (Telegram)

**Skip the @bot mention** — by default, the bot only responds when mentioned. To use `/topic` without mentioning the bot:

```json
"channels.telegram.groups.<CHAT_ID>": { "requireMention": false }
```

**Telegram autocomplete** — to get `/topic` in Telegram's command menu, add under `channels.telegram`:

```json
{
  "customCommands": [
    { "command": "topic", "description": "Create a new topic from a message" }
  ]
}
```

## License

MIT
