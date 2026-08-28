## Description:

元信 yotta-verify is a local pre-install security verifier for agent skills and npm packages that performs deterministic static scans for prompt injection, malicious patterns, SKILL.md integrity, and permission needs, then returns a verdict and audited badge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and security reviewers use this skill before installing or publishing agent skills or npm packages to get a deterministic local scan, a human-reviewable verdict, Markdown or JSON reports, audited badges, and CI gate behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled installers can persistently copy the skill into one or more agent skill directories, especially when global installation or default auto-detection is used.

Mitigation: Prefer explicit single-target installation with --agent or --dir, avoid -g and default auto-detection unless multi-agent installation is intended, and review the destination directory before and after installation.

Risk: The scanner is deterministic static analysis and its verdict does not replace human review or dynamic security testing.

Mitigation: Use the report as a pre-install screening step, manually review findings before installation decisions, and escalate medium or higher findings to deeper review.

## Reference(s):

- [Prompt Injection Detection Patterns](references/injection-patterns.md)
- [SKILL VERIFY REPORT Template](references/verify-report-template.md)
- [Audited Badge Guide](references/badges.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files]

**Output Format:** [One-line verdict text, Markdown and JSON reports, SVG badge files, and CI gate exit codes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python 3.8+ standard library and does not execute scanned code or upload scanned content.]

## Skill Version(s):

0.1.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
