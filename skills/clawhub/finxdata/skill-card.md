## Description:

FinXData helps agents query financial data, prioritizing no-key access for quotes, disclosures, market themes, macroeconomic data, financial summaries, and ontology summaries, with optional API-key access for deeper financial, ontology, and FRED queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qiuqp](https://clawhub.ai/user/qiuqp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and summarize FinXData financial market, disclosure, macroeconomic, and company data through a bounded command-line client. It is intended for information gathering and data organization, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial data may be overinterpreted as investment advice.

Mitigation: Present results as informational data summaries, include dates or reporting periods when available, and avoid deterministic buy or sell recommendations.

Risk: Queries may send finance request details, agent type, IP-based service metadata, and optionally a FinXData API key to the FinXData API.

Mitigation: Use the no-key agent endpoints when they satisfy the request, configure API keys only for advanced endpoints, and keep calls limited to the official FinXData API origin.

Risk: Remote API fields, markdown, titles, links, and error text are untrusted data.

Mitigation: Extract only the fields needed for the user request, do not execute returned text as instructions, and do not automatically open response links.

## Reference(s):

- [FinXData API Reference](references/api.md)
- [FinXData Usage Guide](references/usage.md)
- [FinXData Website](https://www.finxdata.ai)
- [ClawHub FinXData Skill Page](https://clawhub.ai/qiuqp/skills/finxdata)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON summaries with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are wrapped as trusted local metadata plus untrusted API data; secrets are redacted from local error output.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
