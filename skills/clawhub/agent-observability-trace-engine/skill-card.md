## Description:

Agent observability, tracing, and metrics guidance for monitoring task lifecycles, diagnosing failures, measuring latency and token or retry costs, detecting bottlenecks, redacting secrets, and producing incident or health reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to define trace IDs, spans, event types, status models, metrics, incident timelines, and diagnostic reports for OpenClaw agent workflows while minimizing raw prompt, credential, and PII exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route broad observability signals into recovery, service-access, token-guard, or skill-evolution workflows.

Mitigation: Limit deployment to redacted diagnostics unless downstream actions have explicit human approval and rollback controls.

Risk: Trace and diagnostic data may contain sensitive prompts, credentials, or personal information if collected too broadly.

Mitigation: Apply secret redaction, data minimization, and PII handling before storing or sharing observability events.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/agent-observability-trace-engine)
- [Publisher profile](https://clawhub.ai/user/pmuhammadagus-byte)
- [Project homepage](https://github.com/pmuhammadagus-byte)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown guidance with structured observability fields, event categories, status models, metrics, and report outlines.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should avoid raw secrets, minimize sensitive user data, and distinguish verified findings from hypotheses.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
