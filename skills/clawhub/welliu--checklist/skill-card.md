## Description:

Collaborative task checklist manager for AI agents with sequential, parallel, and looping execution. Features agent coordination, dependencies, deadlock prevention, and loop safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[welliu](https://clawhub.ai/user/welliu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent operators use Checklist to create and track coordinated workflows, assign work across agents, and manage sequential, parallel, or looping checklist execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports that the skill overstates loop limits, deadlock prevention, and validation behavior.

Mitigation: Review the skill before installing for autonomous multi-agent coordination and verify safety behavior manually before relying on it.

Risk: The release evidence reports local file-handling flaws and cautions that untrusted template names can affect local checklist files.

Mitigation: Use trusted templates and template names, and review local checklist files created by the skill.

## Reference(s):

- [Checklist ClawHub skill page](https://clawhub.ai/welliu/skills/checklist)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and local JSON checklist state]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can write local checklist state when the shell script is installed and run.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
