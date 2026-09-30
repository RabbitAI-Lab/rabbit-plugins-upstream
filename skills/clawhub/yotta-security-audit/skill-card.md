## Description:

Scans AI skill directories for malicious patterns, Windows and Linux security baselines, and student-data privacy risks, then reports findings without modifying scanned files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, system administrators, and educators use the skill to review authorized skill directories, local system settings, or student-data files for security and privacy risks before deciding what to do next. It reports findings rather than taking remedial action or making legal determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad skill discovery may read more local skill directories than intended.

Mitigation: Use --path to limit scans to authorized directories.

Risk: System and education scans can access sensitive local configuration or student-data files.

Mitigation: Run these modes only on authorized targets, keep education scans narrowly scoped, and review reports before sharing.

Risk: Global installation may write into multiple agent environments, and unpinned installs can change between runs.

Mitigation: Avoid -g unless multi-environment installation is intended; pin the npm version for reproducibility.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-security-audit)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-security-audit)
- [Threat patterns](references/threat-patterns.md)
- [System baseline checks](references/system-baseline.md)
- [Student-data scanning and redaction](references/student-data-scan.md)
- [Remediation guidance](references/remediation-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Text findings or structured JSON, with an optional Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Education-mode examples are redacted; findings require human review and are not legal conclusions.]

## Skill Version(s):

0.3.0 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
