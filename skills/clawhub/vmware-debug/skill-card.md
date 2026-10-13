## Description:

Helps diagnose VMware incidents by correlating collected events, ranking possible causes, and suggesting next checks without changing VMware systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to investigate VMware/vSphere incidents, correlate collected signals, and document evidence-backed hypotheses and next checks. It recommends, but does not execute, remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved case and audit records may retain sensitive operational details.

Mitigation: Do not submit passwords, tokens, .env contents, or logs beyond your retention policy; delete closed case folders when no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zw008/skills/vmware-debug)
- [Project homepage (listed in release metadata)](https://github.com/vmware-skills/VMware-Debug)
- [Setup guide](artifact/references/setup-guide.md)
- [Event envelope](artifact/references/event-envelope.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown diagnosis and structured incident results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Investigation records are saved locally until deleted; the skill does not change VMware systems.]

## Skill Version(s):

1.13.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
