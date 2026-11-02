## Description:

Scans source code, configuration, and Git history locally for suspected leaked secrets, then reports findings in text, JSON, or CSV with masking enabled by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use the skill to check authorized source repositories, configuration, and Git history before committing or releasing code. Treat matches as suspected secrets that need manual review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may expose complete credentials even when default masking is enabled.

Mitigation: Treat generated reports as sensitive and fully redact their context before sharing them in tickets, chats, or CI logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-secret)
- [Project homepage](https://github.com/YottaMeta/yotta-secret)
- [Detection rules](references/rules.md)
- [Entropy and verification guide](references/entropy-and-verification.md)
- [Frequently asked questions](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, JSON, CSV, Guidance]

**Output Format:** [Text, JSON, or CSV scan reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are masked by default and are suspected secrets requiring manual verification.]

## Skill Version(s):

0.2.3 (source: frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
