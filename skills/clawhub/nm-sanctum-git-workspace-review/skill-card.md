## Description:

Verifies workspace state and staged changes as a read-only preflight before commits or pull requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before commit, pull request, or release-note workflows to inspect repository status, staged changes, diff statistics, and detailed diffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is described as read-only, but the security evidence says it may alter staged files and run project formatting or lint commands.

Mitigation: Treat the skill as write-capable, review proposed staging and formatting actions before allowing changes, and avoid broad triggers when only display-only git output is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-git-workspace-review)
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and git review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to run formatting, linting, staging, unstaging, and git diff commands.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
