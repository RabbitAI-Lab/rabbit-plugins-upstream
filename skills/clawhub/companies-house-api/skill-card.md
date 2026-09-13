## Description:

Search the UK Companies House register by name, then pull a company's full register entry, its officers, and its filing history as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to find UK company identifiers and retrieve structured registry, officer, and filing-history data for KYB, due diligence, compliance checks, and B2B data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and retrieved company data are sent through Scavio using SCAVIO_API_KEY.

Mitigation: Use the skill only when that data flow is acceptable, keep the API key out of source control, and store it in an environment variable or secret manager.

Risk: API calls consume Scavio credits and broad searches can generate avoidable cost.

Mitigation: Use narrow search terms, respect pagination limits, and monitor credit usage before running large workflows.

Risk: Optional SDK installation can add package supply-chain exposure.

Mitigation: Install SDKs in an isolated virtual environment or container and verify the package source where practical.

Risk: Officer records may include public personal data such as correspondence address and partial date of birth.

Mitigation: Return only data relevant to the user's request and avoid compiling unnecessary profiles of individuals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/companies-house-api)
- [Scavio Companies House API documentation](https://scavio.dev/docs/companies-house-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=companies-house-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=companies-house-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell, Python, JavaScript, and JSON-oriented API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls consume Scavio credits and return Companies House data through Scavio endpoints.]

## Skill Version(s):

1.0.4 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
