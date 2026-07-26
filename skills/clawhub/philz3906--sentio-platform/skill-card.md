## Description: <br>
Build, modify, or troubleshoot Sentio projects across processors, Sentio SQL in Data Studio, alerting, and dashboards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[philz3906](https://clawhub.ai/user/philz3906) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Sentio projects, query project data, configure alerts, work with dashboards, inspect processors, and run simulations through the Sentio CLI and API schema. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad authority over real Sentio account resources. <br>
Mitigation: Install only when the agent is expected to manage Sentio resources, use the least-privileged API key available, and review planned actions before execution. <br>
Risk: Credential handling could expose long-lived Sentio API keys or bearer tokens. <br>
Mitigation: Avoid pasting long-lived secrets into chat or shell arguments; prefer short-lived or scoped credentials when possible. <br>
Risk: Project deletes, processor pause or stop actions, dashboard imports, public sharing, and simulations can have material account or project impact. <br>
Mitigation: Require explicit confirmation before destructive or externally visible operations. <br>
Risk: Generated SQL queries and dashboard JSON can be incorrect or operationally misleading. <br>
Mitigation: Review generated SQL and dashboard JSON before running commands or importing dashboards. <br>


## Reference(s): <br>
- [Sentio API OpenAPI schema](artifact/references/openapi.swagger.json) <br>
- [ClawHub skill page](https://clawhub.ai/philz3906/skills/sentio-platform) <br>
- [Publisher profile](https://clawhub.ai/user/philz3906) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Code, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Sentio CLI commands, SQL queries, alert definitions, dashboard JSON, processor-management steps, and review guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
