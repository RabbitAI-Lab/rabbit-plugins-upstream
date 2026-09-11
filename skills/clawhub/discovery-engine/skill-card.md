## Description:

Automatically discover novel, statistically validated patterns in tabular data, including feature interactions, subgroup effects, conditional relationships, hold-out validated findings, FDR-corrected p-values, academic-literature novelty checks, effect sizes, citations, and novelty scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

Developers, data scientists, analysts, and research teams use this skill to send tabular datasets to Disco, select a target outcome, and retrieve validated patterns, feature importance, novelty classifications, citations, and report links. It is useful when the user wants to discover non-obvious relationships rather than run summary statistics, visualization, filtering, or SQL-style analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected datasets may be sent to Disco's hosted service.

Mitigation: Use the skill only with data you are permitted to upload, and choose private mode for confidential, proprietary, personal, medical, financial, or regulated data.

Risk: Public analyses are published and should be treated as public disclosure.

Mitigation: Confirm visibility before running an analysis, and use private mode when the data or results should not be public.

Risk: A locally running MCP server can upload files from paths it can access.

Mitigation: Run it with narrow filesystem access, use a dedicated upload folder, and review the exact file path before upload.

Risk: The integration exposes billing-related actions such as payment methods, credit purchases, and subscription changes.

Mitigation: Require direct, explicit user confirmation for the exact charge, credit purchase, or plan change before invoking billing actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco Homepage](https://disco.leap-labs.com)
- [Disco MCP Endpoint](https://disco.leap-labs.com/mcp)
- [Python SDK Documentation](docs/python-sdk.md)
- [OpenAPI Specification](docs/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured analysis results, JSON-like tool responses, Python and shell examples, report URLs, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DISCOVERY_API_KEY. Results can include pattern descriptions, conditions, FDR-corrected p-values, effect sizes, feature importance, citations, novelty classifications, summaries, and interactive report links.]

## Skill Version(s):

0.2.178 (source: pyproject.toml, server.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
