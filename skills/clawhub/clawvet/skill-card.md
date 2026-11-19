## Description:

Scan a third-party OpenClaw skill with ClawVet and act on its A to F grade before installing or trusting it. Use when the user says "scan this skill", "is this skill safe", "vet/check this skill", "should I install this", "audit my skills", or "clawvet", or hands you a SKILL.md from ClawHub or another untrusted source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and skill developers use ClawVet to assess third-party skills before installation or trust. It scans staged skill files, reports a grade and recommendation, and guides review or installation decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment notes that unpinned npx references may use changing upstream package versions.

Mitigation: Review the referenced package and consider pinning its version before running it.

Risk: The security assessment reports incomplete scan coverage because some local references could not be resolved, so the benign verdict does not establish that the skill is risk-free.

Mitigation: Resolve the local references and rerun a complete scan before relying on its verdict.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mohibshaikh/skills/clawvet)
- [Project repository (declared in skill metadata)](https://github.com/MohibShaikh/clawvet)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown scan reports and guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports a grade, recommendation, findings, and next steps based on the scan.]

## Skill Version(s):

0.16.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
