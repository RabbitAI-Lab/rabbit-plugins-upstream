## Description:

Scans skills and packages before installation for prompt injection, hazardous patterns, structural issues, and permission needs, then provides an advisory verdict and optional verification badge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to assess a skill or package before installation, create verification reports and badges, and apply a CI gate. Its static verdict supports, but does not replace, a human installation decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The npm and shell installers can copy this skill into multiple agent skill directories.

Mitigation: Install with an explicit --agent or --dir target; avoid -g/--global unless broad installation is intended.

Risk: A static scan verdict can miss risks and is not a final security guarantee.

Mitigation: Review scan findings and the package manually before deciding whether to install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-verify)
- [Project homepage (listed in skill metadata)](https://github.com/YottaMeta/yotta-verify)
- [Prompt injection detection patterns](references/injection-patterns.md)
- [Verification report template](references/verify-report-template.md)
- [Audited badge documentation](references/badges.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, SVG badges, Shell commands]

**Output Format:** [Plain-text verdicts, Markdown or JSON reports, and optional SVG badges]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Severity-based verdicts; CI gate can return a nonzero exit code.]

## Skill Version(s):

0.3.3 (source: skill frontmatter, package.json, changelog, and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
