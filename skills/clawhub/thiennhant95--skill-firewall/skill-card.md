## Description:

Security scanner for AI agent skills (SKILL.md packs). Use before installing any skill from ClawHub, GitHub or external sources, when auditing a skill directory for malicious patterns (prompt injection, credential theft, exfiltration, destructive commands, obfuscated payloads, persistence), or when asked "is this skill safe?". Produces a SAFE/CAUTION/SUSPICIOUS/MALICIOUS verdict with evidence and CI-friendly exit codes. Strict by default; context-based severity reductions require an explicit opt-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thiennhant95](https://clawhub.ai/user/thiennhant95)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to statically scan third-party agent skills before installation or during audits, then review a SAFE, CAUTION, SUSPICIOUS, or MALICIOUS verdict with supporting evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skill's instructions include an external install action despite its pre-install scanning purpose.

Mitigation: Review the install command and decide whether it is appropriate before running it.

Risk: The security review reports a network capability not covered by the declared network permission, with runtime enforcement unknown.

Mitigation: Review network behavior and run the skill only in an environment whose access controls match your requirements.

Risk: Two local references were unresolved, so the security review evidence is incomplete.

Mitigation: Locate and review the missing references before relying on the scan result for a high-risk installation.

## Reference(s):

- [Threat Model & Rule Catalog](references/threat-model.md)
- [Skill Firewall on ClawHub](https://clawhub.ai/thiennhant95/skills/skill-firewall)
- [Skill Firewall verification harness](https://github.com/thiennhant95/agent-skills/tree/main/skill-firewall)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, SARIF]

**Output Format:** [Human-readable report, JSON, SARIF 2.1.0, or a one-line verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include findings and a CI-friendly exit code.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
