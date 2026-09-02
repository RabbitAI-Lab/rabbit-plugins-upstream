## Description:

Discovery helps agents find novel, statistically validated patterns in tabular datasets, including subgroup effects, feature interactions, effect sizes, citations, and novelty scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and research teams use this skill to run Disco analyses on tabular datasets, choose target and excluded columns, estimate costs for private runs, and present validated patterns with statistical and literature context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public analyses may publish uploaded analyses or results.

Mitigation: Use private visibility for confidential, regulated, customer, medical, financial, or proprietary data, and confirm visibility before submitting an analysis.

Risk: Private runs and account tools can spend credits or change billing state.

Mitigation: Show the estimate before private runs and require explicit user approval before adding payment methods, buying credits, or changing subscriptions.

Risk: The skill can produce misleading results if tautological, leakage, identifier, or derived columns are analyzed as normal features.

Mitigation: Review detected columns with the user and exclude identifiers, target leakage, tautological columns, and derived columns before running Disco.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco homepage](https://disco.leap-labs.com)
- [Disco MCP server](https://disco.leap-labs.com/mcp)
- [Python SDK documentation](docs/python-sdk.md)
- [OpenAPI specification](docs/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with structured analysis results, tool parameters, and inline code or shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, pattern descriptions, p-values, effect sizes, citations, novelty labels, cost estimates, and account or upload workflow guidance.]

## Skill Version(s):

0.2.170 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
