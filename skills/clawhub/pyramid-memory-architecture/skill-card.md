## Description:

A general AI-agent memory architecture skill that organizes rules into a layered pyramid across always-loaded rules, workspace memory/personality files, and on-demand technical guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[popo67ll](https://clawhub.ai/user/popo67ll)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to initialize and maintain workspace memory structures for AI agents, including rule placement, markdown redundancy checks, anchor hygiene, trigger ownership, and cron complexity handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide broad workspace scans and propose rewriting or deleting memory files.

Mitigation: Require a diff or dry run and a separate explicit confirmation before any cleanup, rewrite, or deletion is performed.

Risk: Cron setup and sync workflows can create scheduled tasks or run git commit, tag, and push steps.

Mitigation: Review the generated cron payloads and git commands, then confirm scheduled task creation and repository changes separately.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with tables, code blocks, JSON examples, shell or PowerShell commands, and configuration templates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose workspace file changes, cleanup steps, cron payloads, git commands, and synchronization steps that should be reviewed before execution.]

## Skill Version(s):

3.6.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
