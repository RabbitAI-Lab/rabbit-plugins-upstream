## Description: <br>
HeartFlow is a local rule-based cognitive preprocessor that classifies and routes text, detects emotional signals, checks reasoning and risk, and returns structured analysis for downstream agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mark-heartflow](https://clawhub.ai/user/mark-heartflow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use HeartFlow to add local deterministic text analysis, cognitive-state checks, decision routing, memory search, self-diagnosis, and MCP-accessible safety review to an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local HTTP MCP service modes can expose the engine if bound or proxied beyond localhost. <br>
Mitigation: Bind the MCP service to localhost, do not expose the port externally, and set a deployment-specific HEARTFLOW_MCP_TOKEN. <br>
Risk: Persistent local memory can retain or change local state across sessions. <br>
Mitigation: Disable memory or daemon modes when they are not required and review stored state before using the skill with sensitive data. <br>
Risk: Optional code execution can run untrusted or unintended code paths. <br>
Mitigation: Keep code execution disabled unless a separate sandboxed environment and review process are in place. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/mark-heartflow/skills/heartflow) <br>
- [NPM package](https://www.npmjs.com/package/@yun520-1/heartflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands plus structured text or JSON-style analysis from MCP tools.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs as a local Node.js/MCP workflow; code execution is disabled by default but can be enabled by configuration.] <br>

## Skill Version(s): <br>
6.3.39 (source: server release and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
