## Description:

Monitors server health by periodically checking disk, memory, CPU, network, and process status, then reports health and alerts on threshold breaches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xaiohuangningde](https://clawhub.ai/user/xaiohuangningde)

### License/Terms of Use:


## Use Case:

Developers and operators use this skill to have an agent monitor server health, produce concise status reports, and alert when disk, memory, or CPU thresholds are exceeded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt an agent to apply automatic fixes without clear approval boundaries.

Mitigation: Require explicit approval for automatic fixes unless a narrow allowlist of safe actions, targets, logging, and rollback steps is defined.

Risk: System health reports and alerts can expose operational details about disk, memory, CPU, network, or process state.

Mitigation: Run the agent with least privilege and restrict report recipients, logs, and retained outputs to intended operators.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xaiohuangningde/skills/auto-monitor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown health reports, alerts, and remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include threshold-based alerts for disk usage above 80%, memory usage above 85%, and CPU load above cores multiplied by 0.8.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
