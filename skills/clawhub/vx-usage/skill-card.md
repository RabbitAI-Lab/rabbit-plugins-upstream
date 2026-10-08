## Description:

Guides agents in using vx to manage development tools, project setup, Git and GitHub workflows, MCP integrations, and CI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill for vx-managed tool execution, project configuration, Git and GitHub tasks, MCP setup, and CI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad guidance may redirect Git, GitHub, and project setup work through vx even when it is not needed.

Mitigation: Activate the skill only for vx-specific tasks and review its guidance before installation.

Risk: Unpinned MCP servers, GitHub Actions, and container images can change after review.

Mitigation: Pin MCP server versions, GitHub Actions, and container images before use.

Risk: Global skill setup, force updates, or changes to CI, hooks, PATH, and GitHub state may affect the user's environment or repositories.

Mitigation: Require explicit user approval before running these commands or making these changes.

## Reference(s):

- [ClawHub vx-usage release](https://clawhub.ai/loonghao/skills/vx-usage)
- [vx managed command shim guide](https://github.com/loonghao/vx/blob/main/docs/guide/managed-command-shims.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
