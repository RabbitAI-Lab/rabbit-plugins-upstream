## Description:

元安 audits AI skills for malicious patterns, checks Windows and Linux security baselines, and scans selected education data for student privacy risks through read-only reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security practitioners, system administrators, and education staff use it to review skills before installation, inspect system security baselines, and identify sensitive student information in selected folders before sharing. Scan only authorized targets and treat results as risk signals, not legal or compliance determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may expose sensitive student-record metadata, file paths, or credential-related findings, even when examples are masked.

Mitigation: Keep reports private and inspect them before sharing; use explicit authorized targets and least privilege.

Risk: Exclusions can let unsafe skills escape detection, so a clean scan may provide false reassurance.

Mitigation: Review exclusions and scan scope, and treat results as triage rather than proof of safety.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yottameta/skills/yotta-security-audit)
- [Project homepage](https://github.com/YottaMeta/yotta-security-audit)
- [Threat patterns](references/threat-patterns.md)
- [System baseline checks](references/system-baseline.md)
- [Student data privacy scan](references/student-data-scan.md)
- [Remediation guidance](references/remediation-guide.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Text in the terminal, or JSON and Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only findings with masked examples by default; JSON reports can still expose education headers and file paths.]

## Skill Version(s):

0.3.2 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
