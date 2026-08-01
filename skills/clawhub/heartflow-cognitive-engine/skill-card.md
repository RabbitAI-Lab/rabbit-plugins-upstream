## Description: <br>
HeartFlow is a local rule-based cognitive preprocessing engine that analyzes text for routing, PAD emotion signals, decision signals, and safety-oriented discrimination outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mark-heartflow](https://clawhub.ai/user/mark-heartflow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to run deterministic local text analysis, cognitive routing, emotion analysis, reasoning checks, and MCP-accessible HeartFlow diagnostics before or alongside downstream model responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is presented as a local analysis engine, but server security evidence says the artifacts show broader local authority and persistence than the user-facing description clearly scopes. <br>
Mitigation: Treat it as a broad local agent subsystem, review it before installation, and run it only in a contained project directory. <br>
Risk: The MCP server can operate through local HTTP/SSE and artifact behavior includes token loading plus automatic .env token writing when an explicit token is not set. <br>
Mitigation: Bind the service only to localhost, set the MCP token explicitly, and avoid exposing the server beyond trusted local clients. <br>
Risk: Memory, benchmark, and psychology-analysis features may require more local file access than a simple deterministic text classifier. <br>
Mitigation: Do not grant access to sensitive local files unless those features are intentionally needed for the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mark-heartflow/skills/heartflow-cognitive-engine) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/mark-heartflow) <br>
- [npm package @yun520-1/heartflow](https://www.npmjs.com/package/@yun520-1/heartflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Structured text and JSON-like MCP tool responses, with Markdown guidance and shell commands in setup instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs as a local MCP HTTP/SSE server; output details depend on the selected HeartFlow tool.] <br>

## Skill Version(s): <br>
6.3.40 (source: server release metadata; artifact VERSION and package.json report 6.3.39, SKILL.md reports 6.3.37) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
