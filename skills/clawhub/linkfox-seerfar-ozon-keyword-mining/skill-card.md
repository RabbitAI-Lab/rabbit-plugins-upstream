## Description:

Mines related Ozon and Wildberries marketplace keywords around a seed keyword using Seerfar data, returning search, growth, competition, pricing, relevancy, conversion, and top-product metrics for keyword expansion and opportunity analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and e-commerce operators use this skill to expand from a seed keyword into related Ozon keywords, compare market metrics, and identify long-tail or lower-competition keyword opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox account login, SMS codes, API-key creation, billing, and payment workflows.

Mitigation: Prefer self-service API-key setup when possible, treat API keys and SMS codes as sensitive credentials, and review billing steps before running onboarding or payment commands.

Risk: Keyword mining calls consume account credits, and repeated searches or pagination can create additional cost.

Mitigation: Confirm cost expectations before repeated calls, use the built-in 24-hour cache for identical parameters, and avoid automatic retries with changed keywords, pages, or filters.

Risk: Full keyword results may be cached or persisted outside the current project if the preferred directory is not writable.

Mitigation: Run from an intended writable workspace and review generated linkfox session files before sharing, committing, or moving project data.

Risk: Environment-controlled endpoint variables can affect where API requests are sent.

Mitigation: Use trusted environment settings for LinkFox gateway variables and inspect them before execution in shared or untrusted environments.

Risk: The skill can report feedback to LinkFox when it detects mismatches, praise, dissatisfaction, or improvement opportunities.

Mitigation: Review feedback behavior in the bundled API reference and avoid including sensitive business context in feedback content.

## Reference(s):

- [Seerfar Ozon Keyword Mining API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-keyword-mining)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses to a linkfox session data directory, prints small responses inline, and summarizes large responses unless --inline is used.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
