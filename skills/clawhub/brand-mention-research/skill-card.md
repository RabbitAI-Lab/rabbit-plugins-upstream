## Description:

Builds a sourced brand-mention and reputation brief from bounded Reddit, TikTok, and YouTube searches and comment samples through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Brand and reputation researchers use this skill to identify attributable mentions, compare discussion themes, and prepare a sourced brief with explicit sampling limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and selected public social-media retrieval requests are sent to Crawlora using an API key.

Mitigation: Avoid private or sensitive query text, protect the API key, and keep requests within the intended scope.

Risk: Broad queries or excessive pagination can increase API usage and obscure sampling limits.

Mitigation: Set a page and credit budget before collecting, and report the resulting coverage and denominators.

Risk: Search coverage and ambiguous mentions may skew conclusions, especially across regions or languages.

Mitigation: Set relevant language and region parameters, corroborate ambiguous matches, and qualify claims against the sampled evidence.

## Reference(s):

- [Brand Mention Research on ClawHub](https://clawhub.ai/crawlora-org/skills/brand-mention-research)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown brief with coverage ledger and evidence table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, dates when available, selection reasons, sentiment, sampling counts, and coverage limits.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
