## Description:

Builds sourced brand-mention and reputation briefs from bounded Reddit, TikTok, and YouTube searches and comment samples through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and research teams use this skill to investigate brand, product, or campaign discussion across selected social platforms and produce an attributable, sampled reputation brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand queries, selected post or video IDs, and the API key are sent to Crawlora.

Mitigation: Use the service only for authorized research; avoid confidential targets and protect the API key.

Risk: Unbounded searches can consume API credits, while sampled results can misrepresent overall discussion.

Mitigation: Set page and credit budgets, retain coverage and denominators, and avoid treating sampled counts as total volume or reach.

## Reference(s):

- [Brand mention research on ClawHub](https://clawhub.ai/crawlora-org/skills/brand-mention-research)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown brief with coverage ledger and evidence table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, sampling limits, classifications, and denominators for reported proportions.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
