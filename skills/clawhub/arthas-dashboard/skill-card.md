## Description:

Arthas Dashboard formats Arthas MCP JVM diagnostics into visual monitoring reports with anomaly detection, severity grading, root-cause notes, and remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnnyzuo](https://clawhub.ai/user/johnnyzuo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect JVM health with Arthas MCP data, including threads, memory, GC, profiler output, method monitoring, system parameters, and classloader status. The skill presents diagnostics as dashboard-style reports and follows each view with anomaly checks and suggested next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can surface JVM environment values, runtime details, method arguments, return values, and other operational data.

Mitigation: Run it only against systems the user is authorized to inspect, and redact sensitive values before sharing diagnostic output.

Risk: System-parameter and watch flows may reveal sensitive runtime information.

Mitigation: Use those flows only when authorization is clear and the requested diagnostic value justifies the exposure.

Risk: Profiler and trace diagnostics may add runtime overhead while active.

Mitigation: Keep sampling and tracing scoped to the troubleshooting task and stop them after collecting the needed evidence.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/johnnyzuo/arthas-dashboard/tree/main/arthas-dashboard)
- [ClawHub skill page](https://clawhub.ai/johnnyzuo/skills/arthas-dashboard)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Shell commands, Guidance]

**Output Format:** [Markdown diagnostic reports with tables, ASCII charts, severity labels, root-cause notes, and suggested Arthas commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JVM metrics, anomaly summaries, health scores, and operational remediation steps.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
