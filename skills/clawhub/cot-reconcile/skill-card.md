## Description:

Tripwire check for multi-session drift. Scans state files, recent commits, and file conflicts caused by parallel Claude Code sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to check repositories for drift after parallel Claude Code sessions, worktree merges, crashes, or other multi-session workflows. It reports branch, file, state, and single-source-of-truth inconsistencies before any fix is applied.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects git history, diffs, and local state files, which may expose repository-sensitive information to the agent session.

Mitigation: Install and run it only in repositories where agent inspection of commit history, diffs, and state files is acceptable.

Risk: Proposed fixes could be incorrect if branch intent or state-file meaning is ambiguous.

Mitigation: Review each reported issue and approve any fix individually before changes are applied.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/cot-reconcile)
- [Artifact README](artifact/README.md)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only scan output; proposed fixes require approval before changes are applied.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
