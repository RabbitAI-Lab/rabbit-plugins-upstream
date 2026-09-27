## Description:

Helps OpenClaw agents initialize a user-approved workspace directory structure and persistent workspace guidance without overwriting existing governance files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and agent operators use this skill to initialize or repair an explicitly designated workspace root, with approval before creating folders or changing persistent workspace guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace governance files can shape future agent behavior.

Mitigation: Review the proposed WORKSPACE.md and exact AGENTS.md diff, and approve them before any persistent changes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-initializer)
- [Workspace guidance template](templates/WORKSPACE.md)
- [Agent configuration safety template](templates/AGENTS-config-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions]

**Output Format:** [Markdown guidance and proposed workspace file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposes a change list and requests approval before persistent file changes.]

## Skill Version(s):

1.0.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
