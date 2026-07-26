## Description: <br>
Advanced log analysis for Docker containers using signal extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mkrdiop](https://clawhub.ai/user/mkrdiop) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to extract high-signal error context from Docker container logs and reason about likely failure causes, code errors, or resource issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A crafted container name can cause unintended local shell commands to run when the helper invokes Docker logs. <br>
Mitigation: Review before installing, validate container names, and update the helper to call Docker with an argument list and shell=False. <br>
Risk: Docker logs may contain secrets or sensitive operational data that could be exposed during analysis. <br>
Mitigation: Use only containers you control, warn users before analysis, and redact sensitive log content before sending it to an agent. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown narrative with inline shell commands, diagnostic findings, and fix suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper inspects the last 1000 Docker log lines and returns up to 50 high-signal context lines.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
