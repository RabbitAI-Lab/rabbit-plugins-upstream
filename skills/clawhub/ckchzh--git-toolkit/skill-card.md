## Description:

Git Toolkit provides git-extras-style repository summaries, author reports, changelogs, branch helpers, ignore-file updates, undo support, standup logs, and statistics through a Bash command wrapper.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ckchzh](https://clawhub.ai/user/ckchzh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect Git repository activity, summarize contributors and files, generate changelog text, and perform common local repository maintenance commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The stats command may handle repository filenames unsafely in crafted or untrusted repositories.

Mitigation: Avoid running stats on untrusted repositories until filename handling is hardened; review repository contents and command behavior first.

Risk: The ignore, undo, and fresh-branch commands intentionally modify local Git repository state.

Mitigation: Run state-changing commands only after confirming the target repository and expected changes, and keep recoverable history or backups available.

## Reference(s):

- [Git Toolkit ClawHub skill page](https://clawhub.ai/ckchzh/skills/git-toolkit)
- [tj/git-extras inspiration reference](https://github.com/tj/git-extras)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text and Markdown emitted by Bash git utility commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command output depends on the current Git repository state and selected subcommand.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
