## Description:

LYGO Skill Gate is a local pre-install risk scanner for OpenClaw and ClawHub skill packages that checks for subprocess, network, secret, dynamic-code, webhook, destructive-operation, and permission-claim mismatch signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to statically scan ClawHub or OpenClaw skill folders before installation and review risk bands, findings, and permission-claim mismatches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Static heuristic findings are review signals rather than proof that a scanned skill is safe or unsafe.

Mitigation: Review flagged files and security notes before installation, especially for high-risk or critical paths.

Risk: The scanner reads the user-supplied skill directory and can write a JSON report when requested.

Mitigation: Scan only intended skill directories and use report writing only with explicit consent.

Risk: Permission-claim mismatches or high findings may reflect legitimate operator tooling as well as unsafe behavior.

Mitigation: Use the risk band, findings, and source context together before allowing or blocking a skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-skill-gate)
- [Publisher profile](https://clawhub.ai/user/deepseekoracle)
- [Project homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-skill-gate)
- [Security notes](references/SECURITY.md)
- [Quickstart](examples/quickstart.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands, Files]

**Output Format:** [JSON scan report with a plain-English summary, process exit code, and optional consent-based JSON report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static local analysis only; report writing is limited to the skill state directory when the user passes explicit consent.]

## Skill Version(s):

1.0.0 (source: frontmatter, claw.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
