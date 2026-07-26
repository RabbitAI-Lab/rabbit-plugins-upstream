## Description: <br>
Automatically discovers novel, statistically validated patterns in tabular data and returns structured conditions, effect sizes, citations, and novelty scores. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and data scientists use this skill to send tabular datasets to Disco, choose target and exclusion settings, run public or private analyses, and interpret statistically validated pattern results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Datasets may be sent to Disco's remote service, and public analyses may publish data or results. <br>
Mitigation: Use private mode for confidential data and confirm the requested visibility before starting an analysis. <br>
Risk: Private analyses and account actions can consume credits or involve paid plans. <br>
Mitigation: Estimate cost first, get explicit user confirmation, and do not attach payment methods, buy credits, or change plans unless the user requested that exact action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine) <br>
- [Disco homepage](https://disco.leap-labs.com) <br>
- [Disco MCP endpoint](https://disco.leap-labs.com/mcp) <br>
- [Python SDK documentation](docs/python-sdk.md) <br>
- [OpenAPI specification](docs/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with API and tool-call guidance, configuration snippets, and code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured pattern summaries with conditions, p-values, effect sizes, citations, novelty labels, and report links.] <br>

## Skill Version(s): <br>
0.2.152 (source: ClawHub release evidence; artifact package metadata reports 0.2.151) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
