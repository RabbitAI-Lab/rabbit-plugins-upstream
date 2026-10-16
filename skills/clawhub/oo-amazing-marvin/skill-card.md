## Description:

Helps users read and manage Amazing Marvin tasks, projects, schedules, categories, and labels through their connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People using Amazing Marvin can ask an agent to review tasks, projects, schedules, and labels, or create and complete tasks through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions suggest running remote installer scripts directly in a shell without verification.

Mitigation: Review the official installation guide and inspect downloads and available checksums or signatures before installation.

Risk: Creating or completing tasks and projects changes the user's Amazing Marvin data.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running write actions.

Risk: Experimental task completion may not reproduce all recurrence and reward behavior.

Mitigation: Check recurring tasks and rewards in Amazing Marvin after completing a task.

## Reference(s):

- [Amazing Marvin](https://amazingmarvin.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown responses based on connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results reflect the connected Amazing Marvin account; changes require confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
