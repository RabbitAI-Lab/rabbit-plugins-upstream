## Description:

Helps developers add or improve observability and instrumentation workflows, including logging, metrics, tracing, alerting, structured outputs, and troubleshooting guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to plan and automate observability work such as adding logs, metrics, traces, alerts, data processing, and diagnostic guidance for software systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to read workspace files and run shell commands without clear limits in the artifact documentation.

Mitigation: Use it only in workspaces where code inspection and command execution are acceptable, and require explicit confirmation before file changes, installs, shell commands, or credential use.

Risk: Observability changes can expose sensitive application data through logs, metrics, traces, or alerts.

Mitigation: Review proposed instrumentation for secrets, personal data, and access boundaries before deployment.

Risk: Generated troubleshooting or instrumentation guidance may be incomplete or incorrect for a specific runtime environment.

Mitigation: Validate recommendations against the target system, test in a non-production environment first, and review diffs before applying changes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/observability-and-instrumentation)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or structured JSON-style results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include implementation guidance, troubleshooting steps, execution status, and proposed command or configuration changes.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
