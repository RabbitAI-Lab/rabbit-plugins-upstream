## Description:

Discovery helps agents find statistically validated patterns, feature interactions, subgroup effects, and conditional relationships in tabular data, returning structured findings with effect sizes, FDR-corrected p-values, citations, and novelty scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and data practitioners use this skill to upload or reference tabular datasets, choose a target outcome, run Disco analysis, and interpret statistically validated patterns and novelty-checked findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Datasets may be sent to Leap Laboratories/Disco for remote processing, and public runs publish results.

Mitigation: Require explicit user confirmation before uploads or public analyses, and use private runs only for confidential, personal, regulated, or proprietary data.

Risk: The skill can guide account creation, API-key issuance, payment-method attachment, credit purchases, and subscription changes.

Mitigation: Require explicit confirmation before account, payment, purchase, or subscription actions, and prefer a dedicated low-privilege API key or test account.

Risk: API keys are required for authenticated Disco operations.

Mitigation: Store the Disco API key in DISCOVERY_API_KEY or another secret manager-backed environment path, and avoid placing keys in prompts, code blocks, or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco homepage](https://disco.leap-labs.com)
- [Hosted MCP server](https://disco.leap-labs.com/mcp)
- [Python SDK documentation](docs/python-sdk.md)
- [OpenAPI specification](docs/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis results with API, MCP, and SDK usage examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include pattern descriptions, conditions, effect sizes, p-values, novelty classifications, citations, feature importance, report links, and operational guidance.]

## Skill Version(s):

0.2.164 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
