---
name: twitter-video-downloader
description: X(Twitter) Video Downloader — paste an X(Twitter) video link and get a watermark-free video download URL instantly. Use when you need to download X(Twitter) videos, save Twitter videos, or get X video direct links. Triggers: X video download, Twitter video download, download Twitter video, X video parser, Twitter video parser.
---

# X(Twitter) Video Downloader

Parse X(Twitter) video links via the [redfox.hk](https://redfox.hk/settings/api-keys?source=clawhub) API and return watermark-free video download URLs.

---

## Overview

- **Platform Support**: X (Twitter)
- **Content Type**: Video (MP4 direct download link)
- **Input**: Paste an X(Twitter) video tweet link (one link per request; batch upload not supported)
- **Output**: Returns the video download URL directly — copy it into your browser or download tool to save

---

## Usage

### Example Command

Download an X(Twitter) video:

```bash
python3 "$SKILL_PATH/scripts/downloader.py" "https://x.com/user/status/xxxxx"
```

### First-Time Setup

Configure your API Key first, then run:

```bash
# Set environment variable
export REDFOX_API_KEY=ak_your_key

# Parse the video and get the download link
python3 "$SKILL_PATH/scripts/downloader.py" "https://x.com/user/status/xxxxx"
```

> Visit [redfox.hk](https://redfox.hk/settings/api-keys?source=clawhub) to register and get your API Key.

### Ongoing Usage

Configuration options (choose one):

| Method | Command |
|------|------|
| **Environment Variable** (recommended) | `export REDFOX_API_KEY=ark_your_key` |
| **CLI Argument** | `python3 "$SKILL_PATH/scripts/downloader.py" "<link>" --api-key ark_your_key` |
| **Config File** | `echo '{"api_key":"ark_your_key"}' > ~/.qoder/apis/redfox.json` |

---

## Key Features

| Feature | Description |
|------|------|
| **Watermark-Free Direct Link** | API automatically returns a watermark-free video download URL |
| **Paste & Parse** | Just paste the tweet link — no extra steps needed |
| **Adaptive URL Recognition** | Supports both x.com and twitter.com domains |
| **Instant Results** | Parsing completes and returns the download URL immediately — copy and use |

---

## Common Use Cases

| Scenario | Example Link | Description |
|------|----------|------|
| Save X videos | `https://x.com/user/status/xxxxx` | Get a watermark-free video download URL |
| Offline Twitter video collection | `https://twitter.com/user/status/xxxxx` | Parse and copy the link to download and save |
| Content remixing | Any X video link | Download clips for editing and creative use |
| Asset backup | Any X video link | Back up your favorite videos locally |

### Supported Link Formats

| Platform | Link Format | Example |
|------|----------|------|
| X (Twitter) | `https://x.com/<username>/status/<tweetId>` | PC web link / mobile share link |
| X (Twitter) | `https://twitter.com/<username>/status/<tweetId>` | Legacy domain link |

---

## FAQ

**Q: How do I get my API Key?**
A: Visit [redfox.hk](https://redfox.hk/settings/api-keys?source=clawhub) to register and obtain your token.

**Q: Does the downloaded video have a watermark?**
A: No. The API returns a watermark-free video direct URL.

**Q: Can I upload multiple links at once?**
A: No. Only one link can be parsed per request. Batch upload will cause parsing failure.

**Q: What if parsing fails?**
A: Make sure the link is complete, the tweet still exists, and the account is public. Private accounts or deleted tweets cannot be parsed.

---

## Learn More

This tool is built on the [redfox.hk](https://redfox.hk/settings/api-keys?source=clawhub) `parseWork/videoDownload/x` API. Visit the official website for more API capabilities and documentation.
