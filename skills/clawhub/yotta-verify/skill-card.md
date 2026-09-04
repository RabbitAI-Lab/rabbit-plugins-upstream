## Description:

元信 yotta-verify is a local pre-install security verifier that statically scans agent skills or npm packages for prompt injection, malicious patterns, SKILL.md integrity issues, and permission needs, then reports a verdict and audited badge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill before installing or publishing skills and npm packages to get a deterministic local security scan, a human-reviewable verdict, optional Markdown or JSON reports, and an audited badge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global installation can copy the skill into more agent environments than intended.

Mitigation: Install only into the intended agent skill directory, preferably with --agent or --dir; avoid --global unless broad installation is intended.

Risk: A SAFE TO INSTALL badge or verdict can be over-trusted as a final security decision.

Mitigation: Treat generated verdicts and badges as advisory static-scan results and require human review before installation or release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-verify)
- [Prompt injection detection patterns](references/injection-patterns.md)
- [Skill verify report template](references/verify-report-template.md)
- [Audited badge guide](references/badges.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Plain text verdicts, Markdown or JSON reports, SVG badge files, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static, read-only scan results; the skill does not execute scanned code or connect to the network.]

## Skill Version(s):

0.2.3 (source: ClawHub release metadata; artifact frontmatter and package.json show 0.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
