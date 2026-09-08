## Description:

Defensive multi-agent SRE/SecOps red-team and purple-team resilience commander for authorized incident response, resilience fallbacks, rollback planning, evidence handling, and gated defensive exercises.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, developers, and SecOps/SRE teams use this skill to plan authorized incident response, defensive red-team or purple-team exercises, model-resilience reviews, rollback planning, and evidence-handling workflows with local validation and approval templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Safety gates can incorrectly approve unsafe commands or approval checks.

Mitigation: Keep use tightly scoped, require exact human approval, manually review commands, and do not rely on the validator or approval gate as the sole authorization control.

Risk: Local approval and feedback logs can contain operational context.

Mitigation: Protect or delete local approval and feedback logs and redact them before sharing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/shieldswarm-redteam-resilience)
- [Incident Command Playbook](references/incident.md)
- [Model Resilience and Weak-Model Fallback](references/model_resilience.md)
- [Mode Playbooks](references/modes.md)
- [Ethical Promotion, Publishing Gate, and Refusal](references/promotion.md)
- [Self-Improvement Loop](references/self_improvement.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown templates, YAML configuration, key=value shell output, and concise operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only workflows; approval and feedback logs may be written in the skill workspace.]

## Skill Version(s):

2.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
