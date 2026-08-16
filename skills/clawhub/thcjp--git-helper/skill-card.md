## Description:

Git辅助 helps agents support common Git workflows such as status, pull, push, branch, and log through Chinese-language interaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to ask an agent for routine Git repository operations and workflow guidance. It is intended for code management and automation workflows where Git command execution and repository changes are acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for command and write authority while its instructions are broad and under-scoped.

Mitigation: Install only in repositories where Git command execution and repository mutation are acceptable, and review proposed actions before allowing them.

Risk: Git operations such as pull, push, branch changes, resets, or file writes can alter local work or remote repository state.

Mitigation: Require explicit confirmation for mutating Git actions and inspect repository status, diffs, and target branches before execution.

Risk: The artifact claims sandbox or whitelist protections that may not be enforced by the host platform.

Mitigation: Rely on host-enforced sandboxing, permission policy, and audit controls rather than the skill text alone.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/git-helper)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may describe or propose Git mutations that should be reviewed before execution.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
