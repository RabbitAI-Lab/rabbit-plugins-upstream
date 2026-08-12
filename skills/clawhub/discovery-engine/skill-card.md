## Description:

Automatically discover novel, statistically validated patterns in tabular data, including feature interactions, subgroup effects, conditional relationships, FDR-corrected p-values, citations, and novelty scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, researchers, and data practitioners use this skill to upload or reference tabular datasets, choose a target column, and run Disco to find statistically validated patterns that may not be apparent from ordinary exploratory analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected datasets or dataset URLs may be sent to Disco/Leap Labs for remote processing.

Mitigation: Use the skill only for data approved for remote processing, and verify the exact file path or URL before upload.

Risk: Public analysis runs publish results by default.

Mitigation: Choose private visibility for confidential, proprietary, regulated, or personal data before submitting an analysis.

Risk: Agent-callable account tools can purchase credits, subscribe to paid plans, or change payment-method state.

Mitigation: Require explicit user approval before any credit purchase, subscription, or payment-method action, and estimate private-run costs before analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco homepage](https://disco.leap-labs.com)
- [Disco MCP endpoint](https://disco.leap-labs.com/mcp)
- [Python SDK documentation](docs/python-sdk.md)
- [OpenAPI specification](docs/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured API results containing discovered patterns, conditions, effect sizes, p-values, citations, novelty classifications, feature importance, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Disco API key through DISCOVERY_API_KEY or an authenticated session; public runs publish results, while private runs require credits.]

## Skill Version(s):

0.2.156 (source: evidence release, server.json, and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
