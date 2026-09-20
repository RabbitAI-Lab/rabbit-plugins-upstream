## Description:

Create SubAgent helps users create and manage task-specific SubAgents for development, research, writing, and data analysis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aning35](https://clawhub.ai/user/aning35)

### License/Terms of Use:


## Use Case:

Developers and agent users use this skill to choose a SubAgent template, define its task and label, select run or session mode, and manage the resulting SubAgent lifecycle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Created SubAgents may be given read, write, web, or command execution abilities.

Mitigation: Review and limit each SubAgent's task and tools before letting it work on sensitive data.

Risk: Session mode can preserve a SubAgent beyond a short one-off task.

Mitigation: Use run mode for short tasks and reserve session mode for work that clearly requires persistence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aning35/skills/create-subagent)
- [Publisher profile](https://clawhub.ai/user/aning35)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with command examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suggested SubAgent labels, task prompts, run or session mode, cleanup posture, and management commands.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
