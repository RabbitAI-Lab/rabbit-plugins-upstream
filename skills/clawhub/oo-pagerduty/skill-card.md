## Description:

Operates PagerDuty through an OOMOL-connected account to list and retrieve incidents, list on-call assignments, acknowledge or resolve incidents, and update incident fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage PagerDuty incident workflows from an agent through the oo CLI, including incident lookup, on-call lookup, acknowledgement, resolution, and updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands pipe remote scripts directly into a shell.

Mitigation: Review the installer source and verify integrity before running curl|bash or irm|iex setup commands.

Risk: PagerDuty actions can change incident state by acknowledging, resolving, or updating incidents.

Mitigation: Use an account with appropriate PagerDuty permissions and confirm the exact target, payload, and effect with the user before state-changing actions.

## Reference(s):

- [ClawHub PagerDuty skill](https://clawhub.ai/oomol/skills/oo-pagerduty)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [PagerDuty homepage](https://www.pagerduty.com)

## Skill Output:

**Output Type(s):** [shell commands, guidance, configuration]

**Output Format:** [Markdown with inline bash and PowerShell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing JSON payloads; state-changing incident actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
