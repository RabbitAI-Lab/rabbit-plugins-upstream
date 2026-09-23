## Description:

Helper for using the Git CLI to inspect, stage, commit, branch, and synchronize code changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlang-cn](https://clawhub.ai/user/openlang-cn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to get concise Git command guidance, inspect repository state, stage and commit changes, manage branches, synchronize with remotes, troubleshoot common Git errors, and use small helper scripts or templates when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may suggest repository-changing Git commands, including destructive recovery commands in advanced workflows.

Mitigation: Review proposed commands before execution, prefer read-only inspection first, and require explicit confirmation before destructive Git operations.

Risk: The troubleshooting guidance includes advice to disable TLS certificate verification temporarily, which can weaken repository security if used persistently.

Mitigation: Prefer fixing CA or proxy configuration; if TLS verification is disabled for diagnosis, keep it narrowly scoped and restore secure verification immediately afterward.

## Reference(s):

- [Git Commands Reference](reference/commands.md)
- [Git Workflows](reference/workflows.md)
- [Git Troubleshooting](reference/troubleshooting.md)
- [Git CLI Scripts](scripts/README.md)
- [Git CLI Assets](assets/README.md)
- [ClawHub Skill Page](https://clawhub.ai/openlang-cn/skills/git-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise procedural guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference bundled Bash scripts and text templates; command execution should be reviewed before repository-changing operations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
