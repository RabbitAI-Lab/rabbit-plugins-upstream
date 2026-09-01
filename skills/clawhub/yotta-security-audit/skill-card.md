## Description:

Yuan'an yotta-security-audit scans AI skill directories for malicious patterns and checks Windows/Linux system security baselines using read-only, zero-dependency Python tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent operators use this skill before installing or periodically auditing AI skills, and to produce local system baseline findings for Windows or Linux hosts they are authorized to inspect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad scans can inspect all discovered local skill directories, and system baseline mode can inspect local baseline files and command output.

Mitigation: Prefer running with --path for a specific skill unless broad discovery is intended; use --target system only on authorized hosts where local baseline inspection is acceptable.

Risk: Security findings are detection signals that may require context before action.

Mitigation: Review findings by severity, confirm the matched evidence, and get user authorization before isolation, deletion, credential rotation, or other remediation.

## Reference(s):

- [Threat Patterns](references/threat-patterns.md)
- [Remediation Guide](references/remediation-guide.md)
- [System Baseline](references/system-baseline.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Plain text scan summaries, optional JSON results, and optional Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analysis; reports mask secrets by default]

## Skill Version(s):

0.2.2 (source: SKILL.md frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
