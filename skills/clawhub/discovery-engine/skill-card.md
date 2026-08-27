## Description:

Automatically discover novel, statistically validated patterns in tabular data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

Developers, data analysts, and researchers use Discovery to run Disco analyses over tabular datasets, inspect detected columns, choose target and exclusion fields, estimate costs, submit analyses, and present validated patterns with effect sizes, p-values, citations, novelty labels, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload datasets to Leap Laboratories' service, and public analyses publish data and reports.

Mitigation: Use private visibility for confidential, regulated, or proprietary data, and review datasets before upload.

Risk: Account and billing tools can attach payment methods, purchase credits, change subscriptions, or delete API keys.

Mitigation: Require explicit human confirmation before any billing, subscription, payment-method, credit-purchase, or API-key deletion action.

Risk: Analysis output can be misleading when identifiers, target leakage, tautological columns, or derived target fields are included.

Mitigation: Inspect detected columns and exclude identifiers, leakage fields, tautological fields, and derived columns before submitting an analysis.

Risk: The required DISCOVERY_API_KEY grants access to the external Disco service.

Mitigation: Store DISCOVERY_API_KEY as a secret, avoid pasting it into prompts or logs, and rotate it if exposure is suspected.

## Reference(s):

- [Discovery ClawHub Skill Page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco Homepage](https://disco.leap-labs.com)
- [Hosted MCP Server](https://disco.leap-labs.com/mcp)
- [Python SDK Documentation](docs/python-sdk.md)
- [OpenAPI Specification](docs/openapi.json)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration, Text, Markdown]

**Output Format:** [Markdown guidance with structured API results and optional shell, Python, or JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns analysis workflow guidance, upload and status results, statistically validated pattern summaries, citations, novelty classifications, feature importance, and report links.]

## Skill Version(s):

0.2.167 (source: ClawHub server release evidence; artifact pyproject.toml and server.json report 0.2.166)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
