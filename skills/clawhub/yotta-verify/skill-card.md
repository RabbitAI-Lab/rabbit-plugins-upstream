## Description:

Scans agent skills and packages before installation for prompt injection, risky patterns, structural issues, and permissions, then provides an advisory verdict and optional audited badge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to assess authorized agent skills or npm packages before installation, generate scan reports and badges, and gate installations in CI. Scan verdicts are advisory and require human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation adds a persistent agent skill and pre-install hook to the skill directory.

Mitigation: Review the installation destination and hook behavior before enabling them; install only if this access is acceptable.

Risk: Scan exclusions can miss runtime code in skipped directories, large source files, or copied scanner rule data; verdicts and audited badges may overstate safety.

Mitigation: Treat verdicts and badges as advisory; review excluded and oversized files independently before installation.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-verify)
- [Prompt injection detection patterns](references/injection-patterns.md)
- [Verify report template](references/verify-report-template.md)
- [Audited badge guide](references/badges.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, SVG badges]

**Output Format:** [Text verdicts, Markdown or JSON scan reports, and optional SVG badges]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes severity findings and advisory installation verdicts; CI gate can return a nonzero exit status.]

## Skill Version(s):

0.3.4 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
