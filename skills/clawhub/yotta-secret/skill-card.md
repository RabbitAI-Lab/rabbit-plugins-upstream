## Description:

Scans authorized local files, configuration, and Git history for suspected exposed credentials and produces masked findings for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to check authorized code, configuration, and Git history for possible secrets before sharing or releasing them. Findings require human confirmation; the skill does not validate or rotate credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can affect unintended agent skill directories in an untrusted repository.

Mitigation: Install only into a specific trusted skill directory; avoid running the npm installer from repositories with untrusted pre-existing agent skill directories.

Risk: Scan reports can expose credentials, including in URLs that masking may not fully protect.

Mitigation: Treat reports as sensitive and review URLs for embedded tokens before sharing, even after using mask.

Risk: CSV reports from untrusted repositories may contain spreadsheet formulas.

Mitigation: Neutralize formulas before opening CSV reports in spreadsheet software.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-secret)
- [Project homepage](https://github.com/YottaMeta/yotta-secret)
- [Detection rules](artifact/references/rules.md)
- [Entropy and verification](artifact/references/entropy-and-verification.md)
- [Integration guidance](artifact/references/integration.md)

## Skill Output:

**Output Type(s):** [Text, JSON, CSV, Guidance]

**Output Format:** [Plain text, JSON, or CSV findings; optionally masked text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are masked by default and include severity and source location; results are suspected secrets, not verified credentials.]

## Skill Version(s):

0.2.1 (source: server release metadata, skill frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
