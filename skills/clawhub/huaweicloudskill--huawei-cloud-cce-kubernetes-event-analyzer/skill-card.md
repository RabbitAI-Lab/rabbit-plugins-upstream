## Description:

Query and analyze Kubernetes Events in Huawei Cloud CCE clusters. Trigger when users ask about CCE events, Kubernetes warning events, FailedScheduling, FailedMount, ImagePullBackOff, event patterns, historical events in LTS, or event-based diagnosis for a CCE cluster or namespace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to inspect current or historical Kubernetes Events in Huawei Cloud CCE clusters, group recurring warnings, check referenced resource status, and prepare evidence for diagnosis handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud keys may be exposed through local process arguments.

Mitigation: Use an approved local credential provider, avoid passing keys on command lines, and keep credentials narrowly scoped.

Risk: Crafted event resource names may broaden cluster queries.

Mitigation: Validate event resource names before automatic queries and restrict access to intended namespaces.

Risk: The external kubectl-cce plugin binary's behavior is unverified.

Mitigation: Verify the plugin's provenance and integrity before installing or using it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cce-kubernetes-event-analyzer)
- [Event query workflow](references/workflow.md)
- [Risk rules and guardrails](references/risk-rules.md)
- [Output schema](references/output-schema.md)
- [kubectl-cce usage](references/kubectl-cce.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [kubectl-cce plugin release](https://github.com/pancake0001/kubectl-cce-plugin/releases/tag/v0.1.0)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [JSON event records and aggregated analysis, with concise diagnosis handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes event counts, patterns, time ranges, and supported resource status; redact production resource identifiers when sharing summaries.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
