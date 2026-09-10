## Description:

Discovery helps agents use Disco to find statistically validated feature interactions, subgroup effects, and conditional relationships in tabular data, returning structured patterns with effect sizes, p-values, citations, novelty assessments, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and data practitioners use this skill to upload or reference tabular datasets, choose a target outcome, run Disco analyses, and present validated pattern results. It is intended for discovery-oriented tabular analysis rather than basic summary statistics, visualization, filtering, or SQL-style querying.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote dataset upload and public-by-default analysis can expose confidential, regulated, or proprietary data.

Mitigation: Use private visibility for sensitive datasets, confirm visibility before analysis, and share only approved datasets and metadata with Disco.

Risk: The agent-facing surface includes account creation and billing actions.

Mitigation: Require explicit user confirmation before adding payment methods, purchasing credits, or changing subscriptions.

Risk: Local MCP or file-upload workflows can read and upload local datasets.

Mitigation: Run local MCP processes from a directory containing only approved datasets and use least-privilege API keys or accounts.

## Reference(s):

- [ClawHub Discovery Skill](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco Homepage](https://disco.leap-labs.com)
- [Disco MCP Endpoint](https://disco.leap-labs.com/mcp)
- [Disco Developers / API Keys](https://disco.leap-labs.com/developers)
- [Disco Python SDK Documentation](docs/python-sdk.md)
- [Disco API OpenAPI Specification](docs/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON, Python, and shell command examples; completed analysis results may include structured JSON fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include column inspection guidance, upload and analysis commands, pattern descriptions, p-values, effect sizes, novelty classifications, citations, feature importance, and report URLs.]

## Skill Version(s):

0.2.176 (source: pyproject.toml and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
