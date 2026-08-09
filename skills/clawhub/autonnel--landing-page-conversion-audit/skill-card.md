## Description:

Audit a landing page, sales page or checkout page for conversion leaks and return a fix list ordered by expected revenue impact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autonnel](https://clawhub.ai/user/autonnel)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers, founders, developers, and conversion-rate teams use this skill to review landing pages, sales pages, product pages, opt-in pages, and checkout flows. It returns a concise verdict, a prioritized fix list, tests worth running, checks that passed, and inputs that could not be assessed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit may require business metrics, ad examples, URLs, and funnel data that could be sensitive.

Mitigation: Provide only the page URLs and performance data needed for the review, and omit or anonymize sensitive campaign, customer, and revenue details when they are not required.

Risk: The skill can recommend an external Docker-based funnel builder when page fixes require funnel infrastructure.

Mitigation: Review the referenced repository, release tag, and docker-compose.yml before running any setup commands or deploying suggested infrastructure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autonnel/skills/landing-page-conversion-audit)
- [Autonnel self-hosted funnel builder](https://github.com/autonnel/autonnel)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown report with ordered findings and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fix-now list is capped at seven items; quantitative lift claims are avoided unless supported by the user's data.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
