## Description:

YuanXin yotta-verify is a local pre-install verifier for agent skills and npm packages that performs deterministic static scans for prompt injection, malicious patterns, SKILL.md integrity, and permission needs, then produces install verdicts, reports, and audited badges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent platform operators use this skill to scan skills, npm packages, directories, or tarballs before installation, generate Markdown or JSON verification reports, create audited badges, and enforce CI pre-install gates. Its verdicts are decision support and require human confirmation before trusting or installing a target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanner and installer behavior has broad or unsafe edge cases.

Mitigation: Review the skill before trusting it and prefer a pinned or manually verified installation.

Risk: Global multi-agent installation can affect more agent environments than intended.

Mitigation: Use global multi-agent install mode only when that scope is required.

Risk: Generated audited badges may be mistaken for proof of a completed audit.

Mitigation: Treat badges as scanner output, not as final assurance; require human review for installation decisions.

Risk: Untrusted tarballs or symlink-heavy directories may expose archive extraction and traversal issues.

Mitigation: Avoid scanning those inputs until the extraction and traversal issues identified by the security evidence are fixed.

## Reference(s):

- [Prompt injection detection patterns](references/injection-patterns.md)
- [SKILL VERIFY REPORT template](references/verify-report-template.md)
- [Audited badge guide](references/badges.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-verify)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-verify)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, files, guidance]

**Output Format:** [Plain text verdicts, Markdown reports, JSON reports, SVG badge files, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local static analysis and does not execute scanned code, install packages, or make network calls during scans.]

## Skill Version(s):

0.3.0 (source: frontmatter, package.json, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
