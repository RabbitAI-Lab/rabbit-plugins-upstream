## Description:

Fetch YouTube transcripts via the Apify API from cloud IPs, with local caching and batch mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve YouTube video transcripts through Apify when direct transcript access is blocked from cloud infrastructure. It supports single-video and batch transcript retrieval for downstream summarization, analysis, and documentation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested YouTube URLs and request metadata are sent to Apify for transcript retrieval.

Mitigation: Use the skill only for videos where third-party processing by Apify is acceptable, and avoid sensitive private video requests.

Risk: Apify actor runs can incur usage costs.

Mitigation: Review Apify pricing and billing before use, rely on local caching for repeat requests, and disable fresh fetches unless needed.

Risk: Transcript content is cached locally by default.

Mitigation: Set an appropriate YT_TRANSCRIPT_CACHE_DIR, clear cached transcripts when no longer needed, or run with --no-cache for sensitive workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/robbyczgw-cla/skills/youtube-apify-transcript)
- [Apify YouTube Transcripts Actor](https://apify.com/topaz_sharingan/youtube-transcript-scraper-1)
- [Apify Pricing](https://apify.com/pricing)
- [Apify API Token Setup](https://console.apify.com/account/integrations)
- [Apify Billing](https://console.apify.com/billing)

## Skill Output:

**Output Type(s):** [text, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Plain text or JSON transcript data, with optional file output and Markdown usage guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires APIFY_API_TOKEN, uses Apify network calls, and caches transcript data locally unless caching is disabled.]

## Skill Version(s):

1.4.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
