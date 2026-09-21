## Description:

Verify code references against the repository before trusting them. Use when writing, renaming, or reviewing code, imports, paths, or comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gonisulaimann](https://clawhub.ai/user/gonisulaimann)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to verify repository references before changing code, imports, paths, comments, or documentation claims. It helps identify stale symbols, stale imports, stale file references, number drift, and fragile anchors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full-repository scans read project files.

Mitigation: Install only where repository scanning is appropriate and prefer changed-line scans for pull request checks.

Risk: Running grounded fix without --dry-run can edit code.

Mitigation: Preview changes with grounded fix --dry-run and apply writes only after reviewing unambiguous rewrites.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gonisulaimann/skills/grounded)
- [Commands reference](references/commands.md)
- [Rules reference](references/rules.md)
- [Grounded rules documentation](https://grounded.readthedocs.io/en/latest/rules/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and reference guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to prefer JSON or SARIF for machine-readable grounded CLI results.]

## Skill Version(s):

0.12.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
