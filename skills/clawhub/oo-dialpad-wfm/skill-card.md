## Description:

Dialpad WFM lets agents operate Dialpad Workforce Management through an OOMOL-connected oo CLI workflow for schedules and metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operations teams with connected Dialpad WFM accounts use this skill to retrieve schedule entries and activity or agent metrics through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly.

Mitigation: Install the oo CLI only through a verified, user-approved process and do not let an agent run remote installer commands automatically.

Risk: The `get_schedule` action is labeled `[write]` even though its description reads like a retrieval action, which can confuse confirmation requirements.

Mitigation: Treat all write-tagged actions as requiring explicit user confirmation until the action labeling is corrected.

## Reference(s):

- [Dialpad WFM homepage](https://www.dialpad.com/features/workforce-management-software/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dialpad-wfm)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running action payloads.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
