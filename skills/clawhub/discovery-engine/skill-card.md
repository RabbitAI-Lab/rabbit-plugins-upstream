## Description: <br>
Discovery helps agents use Disco to find novel, statistically validated patterns in tabular data, including feature interactions, subgroup effects, citations, and novelty scores. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and data analysts use this skill to upload tabular datasets, choose an outcome, run Disco analyses, and report statistically validated patterns with links to interactive reports. It is intended for discovery workflows where users need help finding non-obvious subgroup effects, feature interactions, and novel relationships in structured data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Datasets or dataset URLs may be sent to Disco for analysis, and public runs can publish results. <br>
Mitigation: Use private visibility for confidential, regulated, personal, or proprietary data, and choose public runs only when publication is intended. <br>
Risk: The skill exposes billing-related actions such as attaching a payment method, buying credits, or changing subscriptions. <br>
Mitigation: Require explicit user approval before any payment method, credit purchase, or subscription change. <br>
Risk: The authoritative security review flags the release as suspicious because publication and billing actions require careful review before enabling. <br>
Mitigation: Install only after reviewing the security guidance and run with current patched dependencies. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine) <br>
- [Disco Homepage](https://disco.leap-labs.com) <br>
- [Disco MCP Endpoint](https://disco.leap-labs.com/mcp) <br>
- [Python SDK Reference](docs/python-sdk.md) <br>
- [OpenAPI Specification](docs/openapi.json) <br>
- [Python SDK on PyPI](https://pypi.org/project/discovery-engine-api/) <br>
- [Disco API Keys](https://disco.leap-labs.com/developers) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API calls, shell commands, JSON configuration, and structured analysis summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include discovered patterns, p-values, effect sizes, citations, feature importance, novelty labels, report URLs, and account or billing guidance.] <br>

## Skill Version(s): <br>
0.2.153 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
