## Description:

Build a sourced brand-mention and reputation brief from bounded Reddit, TikTok, and YouTube searches and comment samples through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Brand and communications teams use this skill to compile an attributable brief of public brand, product, or campaign mentions, compare discussion themes, and investigate product issues within an explicit search and sampling budget.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand, product, campaign, and selected public post or video identifiers are sent to Crawlora using a Crawlora API key.

Mitigation: Use only if this data sharing is acceptable; do not put secrets, confidential incident details, or private customer data in queries.

Risk: Broad searches or small comment samples can produce false matches or misleading conclusions about mention volume and sentiment.

Mitigation: Bound searches and page budgets, confirm aliases and source context, and report exclusions, sample sizes, and denominators.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/brand-mention-research)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown brief with coverage ledger and evidence table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source IDs and URLs, query scope, dates where available, sampling counts, and denominators.]

## Skill Version(s):

1.0.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
