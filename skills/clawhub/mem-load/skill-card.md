## Description:

Global workflow for loading memory bank files based on recent activity and context when the user invokes $mem-load or asks for this workflow by name.

This skill is ready for commercial/non-commercial use.

## Publisher:

[space-cadet](https://clawhub.ai/user/space-cadet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to restore project context by reading memory-bank files, identifying the current task and recent session, and loading relevant implementation documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can bring local memory-bank files into the agent context, which may expose project notes or implementation details during a session.

Mitigation: Use the skill only in workspaces where reading memory-bank files into context is acceptable, and review those files for sensitive content before invoking the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/mem-load)

## Skill Output:

**Output Type(s):** [guidance, shell commands]

**Output Format:** [Markdown guidance with inline shell-style read commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to select and read local memory-bank files; it does not define automatic background behavior.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
