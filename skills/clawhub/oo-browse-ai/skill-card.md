## Description:

Browse AI lets an agent operate Browse AI through OOMOL's browse_ai connector to list robots and tasks, inspect task data, start robot runs, and update robot cookies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent manage Browse AI robots and robot tasks through an OOMOL-connected account. It supports read workflows for robots and task data, plus confirmed write actions for starting tasks and updating robot cookies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions execute a remote oo CLI installer directly in the shell without integrity checks.

Mitigation: Prefer a verified or manually installed oo CLI, and only run the remote installer after reviewing and trusting the OOMOL installer source.

Risk: run_robot_task can change Browse AI state by starting robot tasks.

Mitigation: Confirm the exact robot, payload, and expected effect with the user before running the action.

Risk: update_robot_cookies can overwrite stored cookies for a Browse AI robot.

Mitigation: Get explicit approval for the target robot and cookie update before executing the destructive action.

## Reference(s):

- [ClawHub Browse AI Skill](https://clawhub.ai/oomol/skills/oo-browse-ai)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Browse AI Homepage](https://www.browse.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
