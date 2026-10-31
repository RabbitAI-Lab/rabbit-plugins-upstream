## Description:

Provides staged Git workflows for branch management, normalized commits, remote sync, conflict guidance, and smart commit splitting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to manage branches, create normalized commits, synchronize with remotes, and get conflict resolution suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery steps may discard local changes or overwrite shared branch history.

Mitigation: Back up local work and require explicit approval before hard resets or remote history rewrites. Verify the target branch, commit, and successful cherry-pick before removing commits; prefer reverting shared commits and use verified lease protection when a rewrite is necessary.

## Reference(s):

- [Git Workflow Specification](references/git-workflow.md)
- [git-workflow on ClawHub](https://clawhub.ai/fize/skills/git-workflow)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance, Git command suggestions, and commit messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Git actions depend on repository state and configuration. Smart commit splitting is enabled by default and can be disabled with GIT_FLOW_AUTO_SPLIT=false.]

## Skill Version(s):

2.0.0 (source: frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
