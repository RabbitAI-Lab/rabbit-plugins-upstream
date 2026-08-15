## Description:

Discovery helps agents use Disco to find statistically validated patterns in tabular datasets, including feature interactions, subgroup effects, conditional relationships, effect sizes, citations, novelty scores, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and data analysts use Discovery to upload tabular datasets, choose target columns, and receive statistically validated pattern discoveries, feature importance, citations, novelty classifications, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Datasets are sent to Disco/Leap Labs for remote processing.

Mitigation: Install only when remote processing is acceptable, and use private mode for sensitive, proprietary, personal, or regulated data.

Risk: Public analyses publish datasets, results, or reports that users may not intend to disclose.

Mitigation: Confirm the desired visibility before analysis and do not run public analysis unless publication is intended.

Risk: The integration exposes billing, credit-purchase, subscription, and payment-method actions.

Mitigation: Require explicit user confirmation before any payment-method, credit-purchase, or subscription action.

Risk: Returned disco_ API keys grant account access.

Mitigation: Protect returned API keys like passwords and avoid exposing them in logs, reports, or shared outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco Homepage](https://disco.leap-labs.com)
- [Hosted MCP Endpoint](https://disco.leap-labs.com/mcp)
- [Python SDK Documentation](docs/python-sdk.md)
- [OpenAPI Specification](docs/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON/API results, Python examples, shell commands, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DISCOVERY_API_KEY for authenticated Disco API access; results may include pattern descriptions, conditions, effect sizes, p-values, citations, novelty classifications, feature importance, and hosted report URLs.]

## Skill Version(s):

0.2.165 (source: ClawHub release evidence; artifact pyproject.toml and server.json list 0.2.164)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
