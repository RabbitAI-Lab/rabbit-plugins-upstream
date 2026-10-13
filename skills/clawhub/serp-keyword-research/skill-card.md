## Description:

Runs search-engine results, keyword suggestions, and Google Trends research through the Crawlora API, returning structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners, marketers, and developers use this skill to compare public search rankings, discover related keywords, and examine search trends across engines and regions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and trend keywords are sent to Crawlora and related search providers.

Mitigation: Use only public, non-sensitive queries; do not submit secrets, private identifiers, or regulated data.

Risk: An exposed Crawlora API key could allow unauthorized use.

Mitigation: Keep CRAWLORA_API_KEY in the environment; never hardcode or commit it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/serp-keyword-research)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or Markdown summaries with structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results reflect public search and trends data; coverage and availability vary by engine.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
