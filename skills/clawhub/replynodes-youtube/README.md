# replynodes-youtube

Thin-client reference for public, read-only YouTube data via ReplyNodes.

## Install

```sh
clawhub install replynodes-youtube@v1.0.1
```

Configure a ReplyNodes API key through the host secret manager as `YOUR_REPLYNODES_API_KEY`; never paste or commit a real credential. API base: `https://api.replynodes.com`. See [platform samples](https://platform.replynodes.com/samples/) for live-versus-contract labels.

The YouTube search sample on that page is live verified. Transcript retrieval is currently unavailable when caption retrieval is rejected or no native/TranscriptAPI fallback is configured. This package performs no login and no writes.
