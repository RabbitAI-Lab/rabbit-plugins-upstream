## Description:

Maps podcast topics across bounded public show and episode samples using Crawlora's Apple Podcasts and Spotify tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Editors, researchers, and podcast creators compare how selected shows cover a topic and assemble an evidence-linked listening shortlist from public episode metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Podcast queries and route parameters are sent to Crawlora.

Mitigation: Avoid sensitive research terms unless sharing them with Crawlora is acceptable.

Risk: API credentials and credit usage require care.

Mitigation: Use a service-scoped API key, bound requests to the research scope, and monitor credit usage.

Risk: Public descriptions and discovery samples may not represent spoken content or the full podcast market.

Mitigation: Label metadata-only findings, retain episode evidence and sampling limits, and avoid unsupported audience or market-demand claims.

## Reference(s):

- [Podcast Topic Landscape skill listing](https://clawhub.ai/crawlora-org/skills/podcast-topic-landscape)
- [Podcast endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown show-by-topic matrix, episode evidence ledger, and listening shortlist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links and dates, coding basis, sampling limits, and explicit episode denominators.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
