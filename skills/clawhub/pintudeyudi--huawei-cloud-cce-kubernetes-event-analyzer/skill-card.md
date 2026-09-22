## Description:

Query and analyze Kubernetes events in Huawei Cloud CCE clusters using API or LTS logs, apply filters, identify patterns, and hand off to diagnosis skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pintudeyudi](https://clawhub.ai/user/pintudeyudi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to inspect Kubernetes event data in Huawei Cloud CCE clusters, prioritize Warning events, group repeated failure patterns, and prepare evidence for follow-up diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is advertised as read-only event analysis, but the packaged dispatcher exposes broader Huawei Cloud, Kubernetes secret, credential, and mutation capabilities.

Mitigation: Install only after narrowing execution to the documented event actions or enforce tightly scoped read-only Huawei IAM and Kubernetes RBAC; avoid broad AK/SK credentials and do not expose Secret payloads.

Risk: Event summaries can expose production pod, node, workload, namespace, or cluster identifiers.

Mitigation: Redact sensitive resource names in summaries and use fictional or generic examples for public outputs.

Risk: Unbounded or overly broad event queries can return excessive data and obscure the incident signal.

Mitigation: Use recent, time-bounded windows and narrow by namespace, reason, or event type before detailed analysis.

## Reference(s):

- [Event Query Workflow](references/workflow.md)
- [Risk Rules & Guardrails](references/risk-rules.md)
- [Output Schema](references/output-schema.md)
- [ClawHub skill page](https://clawhub.ai/pintudeyudi/skills/huawei-cloud-cce-kubernetes-event-analyzer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured event summaries and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes event counts, warning summaries, repeated patterns, affected-resource summaries, and suggested next steps.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
