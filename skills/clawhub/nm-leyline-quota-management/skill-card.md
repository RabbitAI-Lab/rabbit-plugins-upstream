## Description:

Tracks quotas, monitors thresholds, and degrades gracefully for rate-limited APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for guidance on tracking rate, token, and cost quotas before and after operations in service integrations. It helps agents propose threshold checks, usage recording, quota-aware degradation, and resource estimation patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the documentation examples as a complete quota tracker implementation.

Mitigation: Confirm that any plugin using these patterns has an actual tracker implementation and review where usage data, queued work, and cached results are stored.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-leyline-quota-management)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration]

**Output Format:** [Markdown with Python and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no commands or tools are executed by the skill itself.]

## Skill Version(s):

1.9.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
