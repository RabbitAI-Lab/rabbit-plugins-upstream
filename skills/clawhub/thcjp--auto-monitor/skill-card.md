## Description: <br>
Auto Monitor helps agents monitor system status, check server health on a schedule, analyze operations signals, and report findings without waiting for repeated prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations users and developers use Auto Monitor to monitor server health, analyze logs, surface operations alerts, and manage deployment-related checks. It is not suited for complex decisions that require human judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose or rely on command execution against monitored systems. <br>
Mitigation: Require explicit user approval for every shell command and limit execution to named systems and read-only checks unless a deployment action is separately approved. <br>
Risk: The skill describes proactive or scheduled monitoring without clear trigger and scope boundaries. <br>
Mitigation: Define the monitored hosts, check frequency, alert thresholds, and stop conditions before enabling scheduled or proactive operation. <br>
Risk: The skill may involve HTTP requests or deployment actions during operations workflows. <br>
Mitigation: Require approval for each HTTP request or deployment action and review the target endpoint, payload, and expected effect before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/auto-monitor) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include monitoring status, health summaries, configuration guidance, and proposed commands that require explicit approval.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
