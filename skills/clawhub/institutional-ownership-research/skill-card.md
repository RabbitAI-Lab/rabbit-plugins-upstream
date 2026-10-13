## Description:

Compares reported institutional-manager 13F holdings through Crawlora's live SEC and stored position tools for concentration, overlap, and issuer-holder research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers compare reported institutional positions for selected managers or issuers, with filing dates, position classes, coverage, and value-unit uncertainty made explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends a Crawlora API key with requests and may consume paid credits.

Mitigation: Confirm the API-key use before installation, protect the key, and keep searches within the requested scope and credit budget.

Risk: Delayed, incomplete, or mismatched 13F filings can misrepresent current holdings or comparisons.

Mitigation: Report filing dates and completeness; verify issuer identity, security class, and value units before comparing positions.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/institutional-ownership-research)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Markdown research summary with comparable position rows and disclosed calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes manager and filing identity, reporting coverage, source dates, units, and unresolved joins.]

## Skill Version(s):

1.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
