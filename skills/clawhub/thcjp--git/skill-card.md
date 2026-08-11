## Description:

Helps agents perform Git commits, branch operations, rebases, merges, conflict resolution, history recovery, and team workflow tasks in repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to have an agent assist with Git repository workflows such as commits, branches, merges, rebases, conflict handling, and history recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad read, write, and command execution access can affect repository contents and working tree state.

Mitigation: Use the skill only in intended repositories, review proposed commands before execution, and keep recoverable backups or remote history.

Risk: History-changing Git operations such as rebase, reset, and force-push can discard or rewrite work.

Mitigation: Require explicit confirmation before destructive or history-rewriting actions and inspect repository status and recent history first.

Risk: Generic credential guidance in the artifact could encourage unnecessary secret exposure.

Mitigation: Avoid giving the skill unrelated API keys or credentials; provide only access needed for the repository workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/git)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets and JSON-style status examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Git operations that require repository read/write access and command execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
