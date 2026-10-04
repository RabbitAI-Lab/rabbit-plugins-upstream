## Description:

Initializes an approved OpenClaw workspace with standard directories, workspace rules, and guidance for safe multi-agent configuration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and agent developers use this skill to organize a user-approved workspace, add persistent directory conventions, and propose safe configuration rules without overwriting existing governance files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to WORKSPACE.md or AGENTS.md can steer future agent behavior in the workspace.

Mitigation: Review the dry-run and exact file diffs before approval; do not change existing governance files without explicit consent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-initializer)
- [Workspace rules template](templates/WORKSPACE.md)
- [Agent configuration safety template](templates/AGENTS-config-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown guidance, proposed diffs, and approved local workspace files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Presents a dry-run before changes and requires explicit approval for workspace rules or agent startup instructions.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
