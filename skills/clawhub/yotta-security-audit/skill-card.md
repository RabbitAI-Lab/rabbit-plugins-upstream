## Description:

Yuan'an (元安) detects malicious patterns in AI skills across 13 detector classes and scans Windows/Linux system security baselines with read-only, zero-dependency checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent operators use this skill before installing new skills, during periodic audits of installed skills, or when checking Windows/Linux system security baselines. It reports suspicious patterns and remediation guidance without performing fixes, deletion, or quarantine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installers can copy the skill into agent directories and make it available to agents beyond the intended scope.

Mitigation: Install only into the specific agent directories intended for use, and avoid broad/global installation unless that exposure is deliberate.

Risk: Security scans may inspect local skill folders or system baseline information outside an authorized review scope.

Mitigation: Run scans only against systems, folders, and skills the user is authorized to audit.

Risk: Audit findings are security signals and may require context before action, especially medium-severity network, entropy, URL, or pattern matches.

Mitigation: Review findings by severity and evidence location before recommending isolation, credential rotation, or other manual remediation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-security-audit)
- [Threat patterns guide](references/threat-patterns.md)
- [Remediation guide](references/remediation-guide.md)
- [System baseline guide](references/system-baseline.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-security-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text findings, optional JSON, and optional Markdown reports with recommended next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are read-only scan results; credentials and sensitive values are masked by default.]

## Skill Version(s):

0.1.7 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
