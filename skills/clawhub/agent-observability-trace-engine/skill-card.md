## Description:

Agent observability, tracing, and metrics engine for trace IDs, spans, event taxonomies, secret redaction, latency and bottleneck analysis, incident timelines, health scoring, and cross-skill diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to have an agent design and report observability traces, metrics, root-cause analysis, incident timelines, and safe recovery guidance for OpenClaw-style agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Observability records may contain task summaries, failures, timing, component health, or other sensitive operational details.

Mitigation: Use the skill only where diagnostic logging is appropriate and enforce data minimization, secret redaction, and access controls before storing or sharing traces.

Risk: Raw prompt, credential, token, cookie, or authorization data could be exposed if observability output is copied without redaction.

Mitigation: Follow the skill's required redaction behavior and avoid raw prompt logging by default; store only task summaries, trace IDs, results, errors, and metrics needed for diagnostics.

Risk: Root-cause, health, anomaly, or success claims can be misleading if based on insufficient evidence.

Mitigation: Require verification before reporting success, label confidence clearly, and avoid causal claims from a single failure or change event.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/agent-observability-trace-engine)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown diagnostic summaries, trace structures, event taxonomies, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes redacted, minimized observability data and avoids raw prompt or secret logging by default.]

## Skill Version(s):

1.1.0 (source: server release metadata, artifact _meta.json, SKILL.md metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
