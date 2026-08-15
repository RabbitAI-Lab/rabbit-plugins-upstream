## Description:

LYGO SkillSpector is a local pre-install risk scanner for OpenClaw and ClawHub skill packages that can scan, gate, batch, and generate Markdown reports for subprocess, network, secret, dynamic-execution, remote-code, mining-signal, and permission-claim mismatch findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and release maintainers use this skill to audit ClawHub/OpenClaw skill directories before installation or publication and to enforce CI gates based on risk bands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-selected skill directories and reports snippets from flagged files, which may expose secrets already present in scanned files.

Mitigation: Scan only directories intended for audit and handle generated reports as sensitive.

Risk: Static scanner results are triage signals, not proof that a scanned skill is safe or malicious.

Mitigation: Use risk-band output to prioritize review, then inspect critical paths before installation or deployment.

Risk: The SkillHub FULL builder package is a separate artifact from the public ClawHub release.

Mitigation: Review the FULL builder package independently before using it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/deepseekoracle/skills/lygo-skill-spector)
- [Project homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-skill-spector)
- [SkillHub FULL LYGO builder package](https://chatagent.ca/lygoskillhub.html#full-lygo)
- [Security notes](references/SECURITY.md)
- [SkillSpector audit response](references/SKILLSPECTOR_AUDIT.md)
- [Quickstart](examples/quickstart.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [CLI text output, risk-band exit codes, JSON summaries, and optional Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report writes are optional and require --i-consent; gate commands use nonzero exit codes for elevated or high-risk outcomes.]

## Skill Version(s):

1.0.1 (source: server release, SKILL.md frontmatter, claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
