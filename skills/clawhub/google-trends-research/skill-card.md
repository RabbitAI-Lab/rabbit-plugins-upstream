## Description:

Compare search interest, regional patterns, seasonality, and rising queries through Crawlora's Google Trends endpoints for topic-demand briefs, keyword comparisons, and trending-topic research with correctly interpreted relative indices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare Google Trends interest across terms, regions, time ranges, and search properties, then report normalized indices with interpretation caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to a redirected API base.

Mitigation: Run from a clean environment, pin the API base to https://api.crawlora.net/api/v1, allowlist /google/trends paths, and rotate the Crawlora key if it may have been used with an unexpected base URL.

Risk: Google Trends scores can be misread as absolute demand, sales, population opinion, or comparable values across separately scaled requests.

Mitigation: Label outputs as relative indices, compare terms in the same request when possible, preserve missing-data flags, and describe sampling or anchor-method limitations.

Risk: Rapid repeated calls can worsen throttling or produce incomplete results.

Mitigation: Honor Retry-After on 429 or 503 responses, use bounded retries, avoid concurrent widget fan-out, and report missing results rather than fabricating a completed comparison.

## Reference(s):

- [Google Trends endpoint reference](reference/endpoints.md)
- [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown brief or table with optional shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; reports Google Trends values as relative 0-100 indices.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
