## Description:

Security scanner for AI agent skills (SKILL.md packs). Use before installing any skill from ClawHub, GitHub or external sources, when auditing a skill directory for malicious patterns (prompt injection, credential theft, exfiltration, destructive commands, obfuscated payloads, persistence), or when asked "is this skill safe?". Produces a SAFE/CAUTION/SUSPICIOUS/MALICIOUS verdict with evidence and CI-friendly exit codes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thiennhant95](https://clawhub.ai/user/thiennhant95)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use the scanner to inspect third-party agent skills before installation, identify common malicious patterns, and obtain evidence-backed verdicts for manual review or CI gating.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner has a confirmed flaw that can downgrade serious findings, and the scan coverage was incomplete.

Mitigation: Review and fix the downgrade flaw before relying on scanner verdicts; until then, use manual review and inspect content that was not fully analyzed before installation.

## Reference(s):

- [Threat Model & Rule Catalog](references/threat-model.md)
- [Test harness](https://github.com/thiennhant95/agent-skills/tree/main/skill-firewall)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, SARIF, Files]

**Output Format:** [Human-readable report, JSON, SARIF 2.1.0, or one-line verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes findings and CI-friendly exit codes; can write or read a baseline file.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
