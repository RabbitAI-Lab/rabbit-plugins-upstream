## Description:

Yuan'an detects malicious patterns in AI skills and checks Windows/Linux system security baselines with a read-only, zero-dependency scanner.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and security reviewers use this skill to scan AI skill directories before installation, periodically audit installed skills, and inspect authorized Windows/Linux security baselines. The skill reports findings and recommended next steps without performing remediation, deletion, or quarantine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installers can make the skill available across multiple agent environments.

Mitigation: Use a single explicit --dir or --agent install target; avoid -g unless broad installation is intended.

Risk: Broad scans may cover all discovered skills or system-baseline locations.

Mitigation: Run scans with an explicit --path for a specific authorized target unless broad coverage is intentional.

## Reference(s):

- [Threat Patterns](references/threat-patterns.md)
- [Remediation Guide](references/remediation-guide.md)
- [System Baseline](references/system-baseline.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain-text audit report with optional JSON and Markdown report outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only scanner output is severity-ranked and masked by default to avoid exposing full credentials or secrets.]

## Skill Version(s):

0.1.6 (source: frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
