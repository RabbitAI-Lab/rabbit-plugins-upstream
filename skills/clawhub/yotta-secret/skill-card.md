## Description:

Yotta-secret is a local, offline secret and credential scanner that helps agents inspect source code, configuration files, .env files, logs, and git history for suspected API keys, private keys, credential assignments, URL-embedded credentials, and high-entropy tokens using regex, entropy, and format validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent operators use this skill before commits, releases, or sharing logs to find and mask suspected secrets in authorized local files, stdin content, or git history. It supports triage and remediation decisions, but its findings remain suspected secrets that require human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local files and git history to search for suspected secrets.

Mitigation: Run it only on authorized paths and prefer a specific agent or --dir installation scope when broad agent access is not intended.

Risk: Using --show-secret can expose plaintext secrets in terminal output, logs, or reports.

Mitigation: Keep the default masked output unless plaintext is intentionally required for a controlled remediation workflow.

Risk: Regex, entropy, and format checks can produce false positives or miss custom secret formats.

Mitigation: Treat findings as suspected secrets, confirm them with a human review, and rotate or revoke confirmed credentials.

## Reference(s):

- [Yotta-secret ClawHub release](https://clawhub.ai/yottameta/skills/yotta-secret)
- [Rule catalog and matching behavior](references/rules.md)
- [Entropy and format validation](references/entropy-and-verification.md)
- [Integration and usage posture](references/integration.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-secret)

## Skill Output:

**Output Type(s):** [text, json, csv, guidance]

**Output Format:** [Text, JSON, or CSV scan reports with secrets masked by default]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings may include category, severity, file path, line number, masked secret, entropy, snippet context, and git commit/path metadata when git history scanning is used.]

## Skill Version(s):

0.1.1 (source: frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
