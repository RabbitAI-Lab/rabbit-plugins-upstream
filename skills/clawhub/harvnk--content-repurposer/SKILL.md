# Content Repurposer

Transform any content source (YouTube video, article, podcast) into 6 platform-ready formats in one command.

Use when: you have a piece of content and need it adapted for multiple platforms (X/Twitter, LinkedIn, Instagram, newsletter, YouTube Shorts, blog).

## What it does

Give the agent a URL or text, and it produces:

1. **X/Twitter Thread** (8-12 tweets) — Hook-driven, viral format, numbered
2. **LinkedIn Post** — Professional tone, hook + bullets + CTA, 150-300 words
3. **Instagram Caption** — Storytelling + takeaways + 20-30 hashtags
4. **Newsletter Excerpt** — Subject line (A/B), preview text, 3 key takeaways
5. **YouTube Shorts / Reels Script** — 30-second script with hook, setup, payoff, CTA
6. **SEO Blog Post** — Title, meta description, H2/H3 structure, 800-1200 words, FAQ

## Usage

```
Repurpose this video into all platforms: https://youtube.com/watch?v=XXXXX
```

```
Transform this article into a Twitter thread and LinkedIn post: https://example.com/article
```

```
Take the wheel — I want to create a content campaign for my product launch
```

## Features

- **Auto-transcription**: YouTube/podcast URLs are transcribed automatically via Supadata API
- **Article extraction**: Web articles are fetched and parsed to markdown
- **Platform-adapted tone**: Each output matches the platform's style (punchy for X, professional for LinkedIn, casual for IG)
- **Dual hooks**: Generates 2 hook options for X and LinkedIn
- **Take The Wheel mode**: Say "take the wheel" and the agent guides you through content creation step by step

## Requirements

- Supadata API key (for video/podcast transcription) — set as `SUPADATA_API_KEY` env var
- Brave Search API key (optional, for research enrichment) — set as `BRAVE_API_KEY` env var

## Pricing (as a service)

If you're offering this as a service to clients:
- 1 platform: $500-800/month
- Multi-platform (3-5): $1,200-2,000/month
- Full service: $3,000-5,000/month
- Cost per client: ~$40-80/month (APIs)
- Margin: 85-95%

## Tags
content, repurposing, social-media, twitter, linkedin, instagram, newsletter, blog, seo, automation
