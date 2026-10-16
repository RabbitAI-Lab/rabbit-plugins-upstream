## Description:

Analyzes public customer reviews and discussions through Crawlora to identify feedback themes and competitive gaps with cited examples and sample counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Product teams and researchers use this skill to turn bounded samples of public reviews and discussions into cited voice-of-customer briefs, feature-request themes, and product comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may disclose sensitive customer details to Crawlora.

Mitigation: Use public feedback only and omit private customer data from query terms.

Risk: An API key and a bundled shell helper are needed to collect feedback.

Mitigation: Keep the key in the environment and review the helper before running it where shell execution is restricted.

Risk: Small or filtered samples can misrepresent complaint prevalence.

Mitigation: Bound and disclose the sample, report source-specific denominators, and avoid population-level claims.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/customer-feedback-analysis)
- [Crawlora](https://crawlora.net)
- [Supported sources and endpoints](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown theme table and brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cited examples, unique-review counts and denominators, collection filters, and follow-up hypotheses.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
