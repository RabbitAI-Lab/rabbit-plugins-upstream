---
name: news-media-research
description: Researches public BBC, CNN, and Guardian news through the Crawlora API — headlines, article text, live-story updates, search, and topic archives — returning clean JSON. Use when the user wants current coverage or article content from these outlets without scraping pages directly.
---

# News media research

Search and read public news coverage from BBC, CNN, and The Guardian as
normalized JSON, with outlet-native article, headline, live-story, and topic
surfaces.

## When to use this skill

- Get the latest headlines for a section or topic.
- Search an outlet for a story or article.
- Read an article's public body and metadata.
- Inspect a CNN or BBC live-story update stream.
- Browse Guardian topic or section archives.

## Setup

- Get a Crawlora API key at [crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- Requests use `x-api-key: $CRAWLORA_API_KEY` against `https://api.crawlora.net/api/v1`.

## How it works

- BBC: use `/bbc/headlines`, `/bbc/search`, and `/bbc/article`; use
  `/bbc/live` for a canonical live page.
- CNN: use `/cnn/headlines` and `/cnn/article`; use `/cnn/live-story` for
  chronological live updates.
- Guardian: use `/guardian/headlines`, `/guardian/article`, and
  `/guardian/topic` for archives.

Use [`reference/endpoints.md`](reference/endpoints.md) for exact parameters.

## Example

```sh
scripts/crawlora.sh /bbc/headlines section=world | jq '.'
scripts/crawlora.sh /cnn/article url="https://www.cnn.com/example" | jq '.'
scripts/crawlora.sh /guardian/topic topic=technology page=1 | jq '.'
```
