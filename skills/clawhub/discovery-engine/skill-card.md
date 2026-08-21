## Description:

Discovery helps agents run Disco analyses to find statistically validated patterns, feature interactions, subgroup effects, citations, and novelty scores in tabular data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and researchers use this skill to upload tabular datasets, choose a target column, estimate and run Disco analyses, and present validated patterns, feature importance, citations, and report links. It is intended for agent-assisted exploratory discovery, not for summary statistics, visualization, filtering, or SQL-style querying.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send datasets to Disco, and public analysis runs may expose confidential, personal, regulated, or business-sensitive data.

Mitigation: Use private visibility for confidential datasets and do not upload sensitive personal, regulated, or business data to public runs.

Risk: The integration uses an API key and exposes account login, payment-method, purchase, and subscription actions.

Mitigation: Store DISCOVERY_API_KEY in a secret store and require explicit human approval before OTP entry, attaching payment methods, buying credits, or changing subscriptions.

Risk: Pattern discovery can produce misleading findings when identifiers, target leakage, tautological columns, or derived target fields are included.

Mitigation: Review the dataset columns before analysis and exclude identifiers, leakage, tautological columns, and derived target fields.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco Homepage](https://disco.leap-labs.com)
- [Disco MCP Endpoint](https://disco.leap-labs.com/mcp)
- [Python SDK Documentation](docs/python-sdk.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON/API responses and inline shell or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report URLs, pattern descriptions, conditions, effect sizes, p-values, citations, novelty classifications, feature importance, and account or credit status.]

## Skill Version(s):

0.2.166 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
