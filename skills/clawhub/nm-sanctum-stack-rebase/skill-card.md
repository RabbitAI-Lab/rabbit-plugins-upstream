## Description:

Cascades a rebase through an entire PR stack after a base PR merges or upstream changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to rebase stacked pull request branches after a base branch changes, a root PR merges, or a middle slice is revised.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers may activate a force-push and PR-edit workflow for general git or PR requests.

Mitigation: Use the skill only for intentional stacked-PR rebases, narrow invocation triggers when possible, and confirm the stack branch glob, fetched remote state, target PR number, and every branch before force-pushing.

Risk: Rebase operations rewrite local branch history and can affect multiple stack branches.

Mitigation: Require a clean working tree, fetch remote state first, use force-with-lease rather than force, and review each branch that will be pushed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-rebase)
- [Declared homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes checklist-style progress markers, git and GitHub CLI command examples, and conflict-handling guidance.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
