## Description:

检测并修复OpenClaw工作目录嵌套问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxkandel99-arch](https://clawhub.ai/user/maxkandel99-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to diagnose OpenClaw workspace nesting problems, validate workspace paths, and prepare safe repair steps for affected workspace configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repair steps can delete directories or change workspace configuration when the referenced PowerShell scripts are run with execution enabled.

Mitigation: Run the documented dry-run first, review the exact paths that would be changed or deleted, and proceed only after confirming those paths.

Risk: The repair workflow depends on PowerShell scripts that are referenced by path but not bundled in the artifact.

Mitigation: Verify the exact source and contents of each referenced script before running it, and back up affected configuration and workspace directories.

Risk: Ambiguous relative execution paths can cause commands to run against an unintended workspace.

Mitigation: Validate the current workspace directory and configuration paths before executing detection, validation, or repair commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maxkandel99-arch/skills/workspace-health)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline PowerShell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run repair guidance and path confirmation steps before destructive workspace changes.]

## Skill Version(s):

1.0.0 (source: frontmatter, _meta.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
