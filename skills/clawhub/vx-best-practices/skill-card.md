## Description:

Provides best practices for managing tools, configuring projects, and coordinating team workflows with vx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to set up vx-managed projects, choose tool versions, maintain lockfiles, and follow team and CI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Migration examples recursively delete nvm and pyenv directories, potentially destroying tools or user data.

Mitigation: Do not execute removal commands automatically; inspect directory contents, confirm they are no longer needed, and back up important data first.

## Reference(s):

- [vx-best-practices on ClawHub](https://clawhub.ai/loonghao/skills/vx-best-practices)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with Bash, TOML, YAML, and Starlark examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover project setup, tool versions, team workflows, and provider development.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
