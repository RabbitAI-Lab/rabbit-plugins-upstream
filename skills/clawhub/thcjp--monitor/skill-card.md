## Description:

Create monitors for user-defined checks, with agent-assisted scheduling, alerting, system monitoring, log analysis, operations alerts, and deployment management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, independent creators, and enterprise teams use this skill to define monitoring checks for systems, logs, operational alerts, deployment status, and automated workflows. It is not intended for physical hardware repair or complex decisions that require human judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad command and file authority can affect local or monitored systems when the monitoring task is unclear.

Mitigation: Use the skill only for clearly defined monitoring tasks, run it in a constrained environment, and require explicit confirmation before command execution, file modification, API calls, credential use, or scheduled activity.

Risk: Giving the skill broad production-system or secret access could increase the impact of mistakes or data exposure.

Mitigation: Apply least-privilege access and add local controls for allowed commands and permitted data exposure before using it with production systems or secrets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/monitor)
- [Publisher Profile](https://clawhub.ai/user/thcjp)
- [Skill Homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style status results with command, configuration, and troubleshooting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose monitoring checks, thresholds, schedules, alerts, API integration steps, and operational diagnostics.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
