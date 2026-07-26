## Description: <br>
HeartFlow is a local rule-engine cognitive preprocessor that classifies user input, routes decisions, checks emotional and reasoning signals, and returns structured analysis for downstream agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mark-heartflow](https://clawhub.ai/user/mark-heartflow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to run local pre-response classification, routing, memory lookup, emotional signal analysis, and cognitive health checks before an assistant drafts or acts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run as a local MCP service with persistent memory and logs. <br>
Mitigation: Use a strong HEARTFLOW_MCP_TOKEN, review package data and log directories, and deploy only in environments where local persistence is acceptable. <br>
Risk: The artifact includes code-execution surfaces and output-rewriting behavior. <br>
Mitigation: Keep code execution disabled unless explicitly needed, review generated or rewritten outputs before acting on them, and scan the package before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mark-heartflow/skills/mark-heartflow-skill) <br>
- [Publisher profile](https://clawhub.ai/user/mark-heartflow) <br>
- [npm package @yun520-1/heartflow](https://www.npmjs.com/package/@yun520-1/heartflow) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and structured text with optional JSON examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local MCP tool guidance, status checks, routing decisions, and risk-aware setup steps.] <br>

## Skill Version(s): <br>
6.0.66 (source: server release metadata; artifact frontmatter and package.json report 6.2.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
