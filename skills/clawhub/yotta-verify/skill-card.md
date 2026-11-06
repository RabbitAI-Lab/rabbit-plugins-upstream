## Description:

Yotta Verify performs deterministic static scans of agent skills and npm packages for prompt injection, suspicious patterns, skill-file integrity, and permissions, then produces a verdict and optional report or audited badge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and skill publishers use it to assess a skill or package before installation, review the resulting security verdict, and optionally create a report, badge, or CI gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner can produce safety badges without scanning and specially packaged content can bypass installation checks.

Mitigation: Treat verdicts and badges as supplementary evidence; independently review skipped content and confirm a successful scan of the exact target.

Risk: Installer analysis is partial, and external hook enforcement remains unverified.

Mitigation: Choose a specific installation destination and preview it with --dry-run; do not rely on external hook enforcement.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-verify)
- [Prompt injection detection patterns](references/injection-patterns.md)
- [Verification report template](references/verify-report-template.md)
- [Audited badge guide](references/badges.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown, SVG badge]

**Output Format:** [Text verdicts, JSON scan results, Markdown reports, and SVG badges]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional report, badge, or CI gate output; scan results require human confirmation.]

## Skill Version(s):

0.3.5 (source: server release, SKILL.md frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
