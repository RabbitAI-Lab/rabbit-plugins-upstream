## Description:

Agent observability, tracing, and metrics guidance for trace IDs, spans, event taxonomy, redaction, latency analysis, incident timelines, health scoring, and cross-skill diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to design and review observability practices for OpenClaw tasks, including trace structure, metrics, error classification, bottleneck analysis, and incident reporting. It helps teams understand agent behavior while minimizing sensitive data exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Observability data can expose secrets, credentials, prompts, or personal information if collected too broadly.

Mitigation: Apply secret redaction, data minimization, PII handling, and the skill's no-raw-prompt-logging default before storing traces or reports.

Risk: Trace storage can accumulate sensitive operational history without retention or access boundaries.

Mitigation: Define retention limits, access controls, and secure storage policies before production use.

Risk: Diagnostics signals could influence recovery, update, or skill-evolution workflows before evidence is sufficient.

Mitigation: Require human approval and enough supporting trace evidence before using observability findings to change production behavior.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or structured text guidance for observability events, trace summaries, metrics, diagnostics, health reports, and incident timelines.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should redact secrets, avoid raw prompt logging by default, and distinguish confirmed facts from hypotheses.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact metadata reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
