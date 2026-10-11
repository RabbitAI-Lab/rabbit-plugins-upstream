## Description:

Scans authorized local files and Git history for suspected exposed credentials, with masked text, JSON, or CSV findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to check authorized source code, configuration, and Git history for suspected credential leaks before sharing or release, and to mask sensitive text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning or sharing findings may expose sensitive files or credentials.

Mitigation: Scan only authorized files and repositories; keep masking enabled and use --show-secret only in a controlled environment.

Risk: Installing the skill can write into agent skill directories.

Mitigation: Pin the package version and consider --dry-run before installation.

Risk: Pattern matches are suspected credentials, not proof that a key is valid or exposed.

Mitigation: Review findings before taking action; decide on rotation or cleanup with the asset owner.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-secret)
- [Project homepage](https://github.com/YottaMeta/yotta-secret)
- [Detection rules](references/rules.md)
- [Entropy and verification](references/entropy-and-verification.md)
- [Integration guidance](references/integration.md)
- [Frequently asked questions](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Guidance]

**Output Format:** [Masked text, JSON, or CSV findings; brief guidance for human review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include category, severity, location, and masked credential by default; optional explicit unmasking.]

## Skill Version(s):

0.2.2 (source: frontmatter, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
