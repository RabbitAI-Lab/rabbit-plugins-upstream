## Description:

YuanXin yotta-verify is a local, deterministic pre-install verifier that scans agent skills or npm packages for prompt injection, malicious patterns, SKILL.md integrity issues, and permission needs before reporting a verdict and optional audited badge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and security reviewers use this skill before installing or publishing agent skills and npm packages to get a deterministic static scan verdict, Markdown or JSON report, audited badge, and CI gate guidance. It is decision support for authorized review, not a replacement for human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can persistently copy the skill into multiple agent directories, including a broad global mode.

Mitigation: Review the install path first, prefer one explicit --agent or --dir install, avoid -g/--global unless broad installation is intended, and remove unwanted copies from agent skill directories.

Risk: Static scan verdicts can support installation decisions but do not replace human confirmation.

Mitigation: Treat reports as review evidence, confirm findings manually, and escalate medium or higher findings to a deeper review process before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-verify)
- [Prompt injection detection patterns](references/injection-patterns.md)
- [Skill verify report template](references/verify-report-template.md)
- [Audited badge reference](references/badges.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Verdict text, Markdown reports, JSON reports, shell command exit codes, and optional local SVG badge files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated from local static analysis and should be reviewed by a human before installation decisions.]

## Skill Version(s):

0.2.2 (source: frontmatter, package.json, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
