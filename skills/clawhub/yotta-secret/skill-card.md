## Description:

Yotta Secret is a local, zero-dependency agent skill that scans source code, configuration, .env files, logs, and git history for suspected secrets and credentials using regex, entropy, and format checks, with text, JSON, or CSV output masked by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent operators use this skill to check owned or authorized repositories, files, pasted text, or git history for suspected leaked API keys, passwords, private keys, tokens, and URL-embedded credentials before commit, release, or sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanner reports may contain masked credential material or intentionally revealed secrets.

Mitigation: Avoid --show-secret unless necessary and protect generated text, JSON, or CSV reports.

Risk: Findings are suspected secrets and may include false positives.

Mitigation: Require human review before declaring a credential real, then rotate or revoke confirmed exposed credentials.

Risk: Secret scanning can expose information from sensitive files and repositories.

Mitigation: Run the skill only on files, repositories, and git history the user owns or is authorized to inspect.

## Reference(s):

- [Rules Catalog and Matching Notes](references/rules.md)
- [Entropy and Format Verification](references/entropy-and-verification.md)
- [Integration and Usage Patterns](references/integration.md)
- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-secret)

## Skill Output:

**Output Type(s):** [Text, JSON, CSV, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and scanner reports in text, JSON, or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Secrets are masked by default; reports should be protected because they may still contain sensitive credential context.]

## Skill Version(s):

0.1.2 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
