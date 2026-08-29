## Description:

YuanXin yotta-verify is a local pre-install verifier for Agent skills and npm packages that runs deterministic static checks for prompt injection, malicious patterns, SKILL.md integrity, and permission needs, then returns a verdict, reports, and audited badges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent administrators use this skill before installing, evaluating, or publishing Agent skills and npm packages to scan a local target, produce security reports, generate audited badges, and enforce a CI pre-install gate. Its verdicts support human installation decisions but do not replace human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package installer can add a persistent skill to one or more agent skill folders, including user-level destinations.

Mitigation: Install only with a single explicit destination such as --agent or --dir, avoid global installation, and inspect existing skill folders before installation.

Risk: Existing skill files may be overwritten during installation.

Mitigation: Review the target skill directory first and install into a controlled destination where overwrites are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-verify)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-verify)
- [Prompt injection detection patterns](references/injection-patterns.md)
- [Verify report template](references/verify-report-template.md)
- [Audited badge guide](references/badges.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [CLI text, JSON, Markdown reports, SVG badges, and process exit codes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs offline static analysis; when requested, writes report and badge files to caller-selected paths.]

## Skill Version(s):

0.1.1 (source: frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
