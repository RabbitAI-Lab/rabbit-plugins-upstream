## Description: <br>
Auto Monitor helps an agent proactively check system health, report normal status or alerts, and provide guidance for disk, memory, CPU, network, and process issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to have an agent monitor server health, summarize status, and flag threshold-based issues before a user asks. It is suited for operational visibility workflows where any repair action is explicitly scoped and approved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for proactive system monitoring without a clear default scope or check frequency. <br>
Mitigation: Define the monitored systems, allowed health checks, reporting destination, and check frequency before use. <br>
Risk: Automatic repair behavior could change a system without sufficient user opt-in or rollback planning. <br>
Mitigation: Require explicit approval before any repair action and document permitted commands and rollback steps. <br>
Risk: Monitoring workflows may expose local or server health data to the agent. <br>
Mitigation: Limit access to the minimum necessary status data and avoid collecting unrelated logs, secrets, or user data. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown health reports, alerts, and remediation guidance with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require local or server health data access and explicit approval for repair actions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
