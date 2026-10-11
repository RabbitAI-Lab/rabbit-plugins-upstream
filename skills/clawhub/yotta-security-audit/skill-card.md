## Description:

Scans AI skills for suspicious patterns, checks Windows and Linux security baselines, and flags student-data privacy risks in local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and school staff use this skill to review authorized AI skill directories, check local system baselines, and identify student-data exposure before sharing files. It reports findings and suggested next steps without making repairs or legal determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can change files, and the installer has reported filesystem boundary-safety concerns.

Mitigation: Use --dry-run first, choose one explicit --dir or --agent destination, avoid the global installer, and avoid directories prepared by others until symlinked destinations are rejected.

Risk: Local scans may read sensitive configuration, student records, and credential-adjacent files.

Mitigation: Scan only authorized, narrowly scoped paths; protect generated reports and review findings before sharing them.

Risk: Privileged system scans may access more sensitive information than needed.

Mitigation: Do not run system mode as root unless privileged baseline checks are specifically required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-security-audit)
- [Project homepage listed in ClawHub metadata](https://github.com/YottaMeta/yotta-security-audit)
- [Threat patterns](artifact/references/threat-patterns.md)
- [System baseline checks](artifact/references/system-baseline.md)
- [Student-data scan guidance](artifact/references/student-data-scan.md)
- [Remediation guidance](artifact/references/remediation-guide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Console findings and guidance, with optional JSON or Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Student-data examples are masked; findings include severity and location.]

## Skill Version(s):

0.3.1 (source: ClawHub release, skill frontmatter, package.json and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
