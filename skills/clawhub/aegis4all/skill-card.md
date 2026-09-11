## Description:

Aegis4All helps OpenClaw users audit and harden security posture with scored checks, behavior guardrails, and plain-language operation guides.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaozheng-jc](https://clawhub.ai/user/xiaozheng-jc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw operators use this skill to run read-only security audits, review prioritized hardening guidance, inject approved behavioral guardrails, and follow manual operation guides for higher-risk changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact fixes may be presented with inconsistent safety labels.

Mitigation: Review the fix safety rating and exact diff before applying any change.

Risk: Automatic token rotation, communication access changes, API key movement, or persistent rule injection could disrupt access or alter agent behavior.

Mitigation: Require explicit operator approval, keep a rollback path, and avoid automatic changes to credentials, channels, or persistent rules unless the diff is understood.

Risk: The security scanner verdict is suspicious despite no individual risk findings.

Mitigation: Review the high-impact sections before installing and validate behavior in a controlled OpenClaw environment.

## Reference(s):

- [Aegis4All ClawHub listing](https://clawhub.ai/xiaozheng-jc/skills/aegis4all)
- [Zheng, Tan, and Lin (2026) arXiv preprint](https://arxiv.org/abs/2606.11007)
- [Security guide](guides/security-guide.md)
- [Rule injection guide](rules/inject.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, guide text, configuration diffs, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit output is intended as a single message; configuration changes require explicit user confirmation.]

## Skill Version(s):

4.0.1 (source: server release metadata; artifact frontmatter reports 4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
