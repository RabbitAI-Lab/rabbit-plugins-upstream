## Description:

Research TikTok Creative Center Top Ads by brand, market, industry, and objective through Crawlora for competitor-ad comparisons, creative briefs, messaging and format analysis, and inspection of public ad-performance charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers, creative strategists, and developers use this skill to query Crawlora's TikTok Top Ads endpoints and build sourced competitor-ad comparisons with material IDs, filters, performance fields, and retrieval context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can redirect the Crawlora API key and request data to an arbitrary API base through the CRAWLORA_API_BASE environment variable.

Mitigation: Run it only where CRAWLORA_API_BASE is unset or controlled, avoid sensitive request bodies, and prefer a version that pins or validates the Crawlora API host before sending the API key.

Risk: Public Top Ads samples and performance charts can be misread as complete campaign coverage or proof of conversion causality.

Mitigation: Report filters, sort order, sample bounds, retrieval time, and uncertainty; present creative tests as hypotheses rather than causal claims.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown research summary with inline shell commands and JSON response details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include material IDs, source links, filters, metric labels, returned performance fields, and retrieval time.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
