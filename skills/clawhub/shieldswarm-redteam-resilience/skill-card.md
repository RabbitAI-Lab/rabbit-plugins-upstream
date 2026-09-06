## Description:

Defensive multi-agent SRE/SecOps red-team and purple-team resilience commander with working mode selection, command validation, approval gates, and a machine-readable model quality-floor matrix.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Security, SRE, and SecOps practitioners use this skill to plan authorized incident response, defensive red-team and purple-team exercises, model-resilience fallbacks, rollback planning, and evidence handling. It is intended for defensive, authorization-gated workflows that require explicit command validation, approval records, and redaction discipline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags weak command and approval gates and weak install provenance.

Mitigation: Pin and verify the exact package, review proposed actions manually, and do not rely on the bundled validation or approval scripts as authoritative controls until the cited issues are fixed.

Risk: Approval and feedback logs can contain sensitive operational context.

Mitigation: Protect approval.jsonl and feedback.jsonl with restricted file permissions, redact before sharing, and delete or rotate them when no longer needed.

Risk: Defensive red-team workflows can cause harm if used without authorization or a defined scope.

Mitigation: Require written authorization, a completed rules-of-engagement file, human approval for risky actions, and explicit refusal of attack traffic, login bypass, or credential collection.

## Reference(s):

- [Skill page](https://clawhub.ai/orionshaowswmw/skills/shieldswarm-redteam-resilience)
- [Agent discovery card](AGENT_DISCOVERY.md)
- [Modes playbook](references/modes.md)
- [Incident commander playbook](references/incident.md)
- [Model resilience playbook](references/model_resilience.md)
- [Ethical promotion guidance](references/promotion.md)
- [Self-improvement protocol](references/self_improvement.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, YAML templates, and key=value or JSONL command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline local scripts emit deterministic stdout; approval and feedback workflows may append local JSONL logs.]

## Skill Version(s):

2.1.1 (source: frontmatter and CHANGELOG, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
