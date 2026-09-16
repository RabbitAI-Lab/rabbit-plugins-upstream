## Description:

Research TikTok Creative Center Top Ads by brand, market, industry, and objective through Crawlora for competitor-ad comparisons, creative briefs, messaging analysis, format analysis, and public performance-chart inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and creative strategists use this skill to collect and compare public TikTok Top Ads by brand, market, industry, objective, and lookback window. It supports sourced creative research, messaging and format analysis, and cautious interpretation of returned public performance signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora API keys and TikTok ad research queries are sent to Crawlora over HTTPS.

Mitigation: Use a scoped, revocable API key and avoid sensitive internal campaign plans or unreleased product details in query parameters or request bodies.

Risk: Public TikTok Top Ads samples can be mistaken for exhaustive competitor activity or causal proof of performance.

Mitigation: State filters, sample limits, sort order, and retrieval time; verify advertiser identity where available and present creative-test recommendations as hypotheses.

Risk: Media access may be incomplete when only metadata is available or signed media URLs expire.

Mitigation: Limit observations to accessible fields when media cannot be inspected, preserve material IDs and source links, and mark missing observations in partial comparisons.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/tiktok-ad-research)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown research comparison with JSON API responses and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include material IDs, source links, retrieval time, market and objective filters, lookback windows, returned performance fields, and clearly marked limitations.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
