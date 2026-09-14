## Description:

元钥 yotta-secret helps agents run local, offline secret and credential leak checks across source code, configuration files, .env files, logs, and git history using regex, entropy, and format validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and release engineers use this skill to find suspected hardcoded API keys, passwords, private keys, tokens, and URL-embedded credentials before commits, releases, or report sharing. It is intended for authorized repositories, owned assets, and educational environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanner reports may reveal sensitive snippets or suspected secrets even when the skill is expected to mask secrets.

Mitigation: Review text, JSON, and CSV reports before sharing them, keep outputs in controlled locations, and avoid explicit secret display unless it is necessary for authorized remediation.

Risk: A clean scan result may be misleading if requested files, directories, or git history were unreadable or not scanned.

Mitigation: Confirm the requested targets were readable and included in the scan before relying on exit code 0 or a clean report.

Risk: Secret scanning can expose or process data outside the user's authorization scope.

Mitigation: Use the skill only on owned, authorized, or educational targets and keep remediation decisions under human review.

Risk: Unversioned package installation can pick up a newer release than the one reviewed.

Mitigation: Pin the npm package version for repeatable installation and review the selected release before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-secret)
- [Rules Reference](references/rules.md)
- [Entropy and Verification Reference](references/entropy-and-verification.md)
- [Integration Reference](references/integration.md)
- [FAQ](references/faq.md)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-secret)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, plus scanner reports in text, JSON, or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports mask suspected secrets by default; JSON and CSV outputs may include file, line, rule, severity, entropy, snippet, and commit metadata.]

## Skill Version(s):

0.2.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
