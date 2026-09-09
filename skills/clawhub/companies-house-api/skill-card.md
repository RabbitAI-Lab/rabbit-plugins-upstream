## Description:

Search the UK Companies House register by name, then pull a company's full register entry, its officers, and its filing history as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up UK companies, retrieve register entries, inspect officers, and review filing histories for KYB, due diligence, compliance, and B2B data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Scavio API key, consumes API credits, and sends company names or company numbers to Scavio.

Mitigation: Confirm the user is comfortable using the configured key and spending credits before making calls; keep the key in environment or secret storage.

Risk: Officer records can include correspondence addresses and partial dates of birth from the public register.

Mitigation: Treat officer fields as personal data and avoid compiling profiles of private individuals beyond the user's requested purpose.

Risk: Broad Companies House searches are capped at 50 pages and may not be exhaustive.

Mitigation: Narrow broad search terms and avoid claiming exhaustive coverage when the query could exceed the register window.

Risk: Pagination can make an empty officers or filing-history page ambiguous.

Mitigation: Check page 1 before reporting that a company has no officers or filings, and treat later empty pages as stop signals.

## Reference(s):

- [Scavio Companies House documentation](https://scavio.dev/docs/companies-house-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=companies-house-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/companies-house-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=companies-house-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API response descriptions and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses Scavio API credits.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
